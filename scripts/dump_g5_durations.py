#!/usr/bin/env python3
"""
诊断 G5A smartedu 教材页的 12 个 unit 音频 duration
- 只点不存 body,只看 audio.duration
- 输出 G5A 的 DURATION_TO_NAME 表
"""
import asyncio
from playwright.async_api import async_playwright

URL = (
    "https://basic.smartedu.cn/tchMaterial/detail"
    "?contentType=assets_document"
    "&contentId=48dadfac-0bda-3a13-38a3-f3d072aff528"
    "&catalogType=tchMaterial"
    "&subCatalog=tchMaterial"
)
USER_DATA_DIR = "/Users/paulshi/.cache/smartedu-browser"

NAMES = ["Starter", "Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5",
         "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10", "Words to use"]


async def main():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            locale="zh-CN",
            args=["--no-sandbox"],
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(8000)
        try:
            await page.locator("text=音频资源").wait_for(state="visible", timeout=15000)
        except Exception:
            pass
        await page.wait_for_timeout(2000)

        print("\n=== G5A 12 个 unit duration ===\n")
        results = []
        for name in NAMES:
            try:
                await page.locator(f"text={name}").first.click(timeout=5000, force=True)
                await page.wait_for_timeout(2800)
                dur = await page.evaluate("""() => {
                    for (const a of document.querySelectorAll('audio')) {
                        if (a.src && a.src.startsWith('blob:') && a.duration > 0 && a.duration !== Infinity) {
                            return Math.round(a.duration);
                        }
                    }
                    return 0;
                }""")
                if dur > 0:
                    m, s = divmod(dur, 60)
                    print(f"  {name:15}  {m}:{s:02d}  ({dur}s)")
                    results.append((dur, name))
                else:
                    print(f"  {name:15}  ❌ no audio")
            except Exception as e:
                print(f"  {name:15}  ❌ click fail: {e}")

        await ctx.close()

        print("\n\n=== 给 extract_audio.py 用的 DURATION_TO_NAME ===\n")
        print("DURATION_TO_NAME = {")
        for dur, name in results:
            label = name.lower().replace(" ", "_")
            print(f"    {dur}: \"{name}\",  # {label}.mp3")
        print("}")


asyncio.run(main())
