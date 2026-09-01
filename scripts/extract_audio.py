#!/usr/bin/env python3
"""
抓取 smartedu 12 个教材音频(duration 配对 + 多次跑合并版)

策略:
- route handler 强制重新 fetch + body 存盘
- click 后查 audio.duration, 用 duration 查表得到 unit name(精确配对)
- 多次跑合并,直到 12 个全
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

URL = (
    "https://basic.smartedu.cn/tchMaterial/detail"
    "?contentType=assets_document"
    "&contentId=319f0cb8-03af-70e7-7c8e-5a2241688ade"
    "&catalogType=tchMaterial"
    "&subCatalog=tchMaterial"
)
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "raw" / "audio"
USER_DATA_DIR = Path.home() / ".cache" / "smartedu-browser"

# 预期时长(秒)→ unit name
DURATION_TO_NAME = {
    319: "Starter",       # 5:19
    271: "Unit 1",        # 4:31
    266: "Unit 2",        # 4:26
    265: "Unit 3",        # 4:25
    274: "Unit 4",        # 4:34
    282: "Unit 5",        # 4:42
    286: "Unit 6",        # 4:46
    252: "Unit 7",        # 4:12
    264: "Unit 8",        # 4:24
    275: "Unit 9",        # 4:35
    296: "Unit 10",       # 4:56
    678: "Words to use",  # 11:18
}

AUDIO_NAMES = list(DURATION_TO_NAME.values())


def fmt_duration(d):
    try:
        if d is None or d != d or d == float('inf'):
            return "?"
        d = int(d)
        return f"{d//60}:{d%60:02d}"
    except Exception:
        return "?"


def url_to_filename(label: str) -> str:
    safe = label.lower().replace(" ", "_")
    return f"{safe}.mp3"


def duration_to_name(d_sec: int) -> str | None:
    """duration 查表得到 unit name(允许 ±3s 误差)"""
    if not d_sec:
        return None
    for exp, name in DURATION_TO_NAME.items():
        if abs(d_sec - exp) < 3:
            return name
    return None


async def get_audio_duration(page) -> int:
    """读当前 audio 元素 duration (秒)"""
    return await page.evaluate("""() => {
        const audios = document.querySelectorAll('audio');
        for (const a of audios) {
            if (a.src && a.src.startsWith('blob:') && a.duration > 0 && a.duration !== Infinity) {
                return Math.round(a.duration);
            }
        }
        return 0;
    }""")


async def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # 收集: list of {url, body, name}
    all_audios: dict = {}  # {name: {url, body}}
    audios_lock = asyncio.Lock()

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            viewport={"width": 1920, "height": 1080},
            locale="zh-CN",
            args=["--no-sandbox"],
        )
        page = context.pages[0] if context.pages else await context.new_page()

        async def handle_route(route, request):
            try:
                response = await route.fetch()
                body = await response.body()
                await route.fulfill(response=response)
                # 存到 all_audios[clicked_name] = body
                # 但 route handler 不知道当前 click 是什么名字
                # 解决:用 ctx_vars['current_name'] 传过来
                cur_name = ctx_vars.get("current_name")
                if cur_name:
                    async with audios_lock:
                        if cur_name not in all_audios:
                            all_audios[cur_name] = {"url": request.url, "body": body, "size": len(body)}
                            print(f"   📥 {cur_name:15} {len(body)/1024/1024:.1f} MB", flush=True)
            except Exception as e:
                print(f"   ⚠️  route error: {e}", flush=True)
                await route.continue_()

        await context.route("**/r2-ndr-private.ykt.cbern.com.cn/**/*.mp3", handle_route)

        # 用 dict 跨 task 共享当前 click 的 name
        ctx_vars = {}

        # 跑 N 次,直到 12 个全
        max_runs = 5
        for run_idx in range(max_runs):
            missing = [n for n in AUDIO_NAMES if n not in all_audios]
            if not missing:
                print(f"\n✅ 12 个全抓到了!", flush=True)
                break

            print(f"\n{'='*60}\n🔄 Run {run_idx+1}/{max_runs} (缺 {len(missing)} 个: {missing})\n", flush=True)

            # 加载页
            await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(8000)
            try:
                await page.locator("text=音频资源").wait_for(state="visible", timeout=15000)
            except Exception:
                pass
            await page.wait_for_timeout(2000)

            # 点击 missing 的
            for name in missing:
                if name in all_audios:
                    continue
                try:
                    # 标记当前 click 的 name,给 route handler 用
                    ctx_vars["current_name"] = name
                    await page.locator(f"text={name}").first.click(timeout=5000, force=True)
                    # 等 audio 切歌(等 src 变 + duration 变)
                    await page.wait_for_timeout(3500)

                    # 兜底:用 audio duration 校准
                    actual_dur = await get_audio_duration(page)
                    expected_name = duration_to_name(actual_dur)
                    if expected_name and expected_name != name:
                        # smartedu 切到不同 audio 了(可能 click 命中错位置)
                        print(f"   ⚠️  click {name} 但 audio 切到 {expected_name} ({actual_dur}s)", flush=True)
                        ctx_vars["current_name"] = expected_name
                    else:
                        print(f"   ✓ click {name} ({actual_dur}s)", flush=True)
                except Exception as e:
                    print(f"   ✗ {name}: {e}", flush=True)

            ctx_vars["current_name"] = None
            await page.wait_for_timeout(3000)

        await context.close()

    # 写盘
    print(f"\n{'='*60}\n💾 写盘...\n", flush=True)
    for name in AUDIO_NAMES:
        if name not in all_audios:
            print(f"   ❌ {name}: 未抓到", flush=True)
            continue
        a = all_audios[name]
        dst = OUT_DIR / url_to_filename(name)
        dst.write_bytes(a["body"])
        exp_dur = next(k for k, v in DURATION_TO_NAME.items() if v == name)
        match = "✓" if abs(a["size"]/1024 - exp_dur * 16) < 1000 else "?"
        print(f"   {match} {dst.name:25} ({a['size']/1024/1024:.1f} MB, ~{fmt_duration(exp_dur)})", flush=True)

    print(f"\n{'='*60}", flush=True)
    saved = len(all_audios)
    print(f"✅ 完成: {saved} / {len(AUDIO_NAMES)} 个音频已保存", flush=True)
    print(f"📁 路径: {OUT_DIR}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
