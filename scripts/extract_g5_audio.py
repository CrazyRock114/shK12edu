#!/usr/bin/env python3
"""
抓取 G5A smartedu 12 个 unit 音频（按点击顺序精确配对）
- 与 extract_audio.py 区别:不依赖 duration 查表,直接用 click name
- 多次跑补漏
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

URL = (
    "https://basic.smartedu.cn/tchMaterial/detail"
    "?contentType=assets_document"
    "&contentId=48dadfac-0bda-3a13-38a3-f3d072aff528"
    "&catalogType=tchMaterial"
    "&subCatalog=tchMaterial"
)
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "raw" / "audio"
USER_DATA_DIR = Path.home() / ".cache" / "smartedu-browser"

NAMES = ["Starter", "Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5",
         "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10", "Words to use"]

# 期望 duration(秒),只做 sanity check(显示用,不参与 name 配对)
EXPECTED_DURATIONS = {
    "Starter": 351, "Unit 1": 335, "Unit 2": 321, "Unit 3": 351,
    "Unit 4": 362, "Unit 5": 376, "Unit 6": 333, "Unit 7": 341,
    "Unit 8": 335, "Unit 9": 361, "Unit 10": 374, "Words to use": 483,
}


def url_to_filename(label: str) -> str:
    return f"{label.lower().replace(' ', '_')}.mp3"


async def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    captured: dict = {}  # {name: {url, body, size}}
    lock = asyncio.Lock()

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            viewport={"width": 1920, "height": 1080},
            locale="zh-CN",
            args=["--no-sandbox"],
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        cur_name_holder = {"name": None}

        async def handle_route(route, request):
            try:
                response = await route.fetch()
                body = await response.body()
                await route.fulfill(response=response)
                cur = cur_name_holder["name"]
                if cur:
                    async with lock:
                        if cur not in captured:
                            captured[cur] = {"url": request.url, "body": body, "size": len(body)}
                            print(f"   📥 {cur:15}  {len(body)/1024/1024:.1f} MB", flush=True)
            except Exception as e:
                print(f"   ⚠️  {e}", flush=True)
                await route.continue_()

        await ctx.route("**/r2-ndr-private.ykt.cbern.com.cn/**/*.mp3", handle_route)

        # 多轮跑直到 12 个全
        max_runs = 5
        for run_idx in range(max_runs):
            missing = [n for n in NAMES if n not in captured]
            if not missing:
                print(f"\n✅ 12 个全抓到了!", flush=True)
                break
            print(f"\n{'='*60}\n🔄 Run {run_idx+1}/{max_runs}  缺 {len(missing)} 个: {missing}\n", flush=True)

            await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(8000)
            try:
                await page.locator("text=音频资源").wait_for(state="visible", timeout=15000)
            except Exception:
                pass
            await page.wait_for_timeout(2000)

            for name in missing:
                if name in captured:
                    continue
                try:
                    cur_name_holder["name"] = name
                    await page.locator(f"text={name}").first.click(timeout=5000, force=True)
                    await page.wait_for_timeout(3500)
                    # sanity check:读 duration 跟 EXPECTED 比
                    dur = await page.evaluate("""() => {
                        for (const a of document.querySelectorAll('audio')) {
                            if (a.src && a.src.startsWith('blob:') && a.duration > 0 && a.duration !== Infinity) {
                                return Math.round(a.duration);
                            }
                        }
                        return 0;
                    }""")
                    expected = EXPECTED_DURATIONS.get(name, 0)
                    if dur and abs(dur - expected) > 5:
                        print(f"   ⚠️  {name}: got {dur}s expected {expected}s (差 > 5s,可能要重抓)", flush=True)
                    else:
                        print(f"   ✓ {name}: {dur}s", flush=True)
                except Exception as e:
                    print(f"   ✗ {name}: {e}", flush=True)

            cur_name_holder["name"] = None
            await page.wait_for_timeout(3000)

        await ctx.close()

    # 写盘
    print(f"\n{'='*60}\n💾 写盘到 {OUT_DIR}/\n", flush=True)
    for name in NAMES:
        if name not in captured:
            print(f"   ❌ {name}: 未抓到", flush=True)
            continue
        c = captured[name]
        dst = OUT_DIR / url_to_filename(name)
        dst.write_bytes(c["body"])
        print(f"   ✓ {dst.name:25} ({c['size']/1024/1024:.1f} MB)", flush=True)

    print(f"\n✅ 完成: {len(captured)} / {len(NAMES)}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
