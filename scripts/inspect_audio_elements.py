#!/usr/bin/env python3
"""诊断: 看 smartedu 页面里 audio 元素实际有几个 src"""
import asyncio
from playwright.async_api import async_playwright

URL = (
    "https://basic.smartedu.cn/tchMaterial/detail"
    "?contentType=assets_document"
    "&contentId=319f0cb8-03af-70e7-7c8e-5a2241688ade"
    "&catalogType=tchMaterial"
    "&subCatalog=tchMaterial"
)

async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir="/Users/paulshi/.cache/smartedu-browser",
            headless=False,
            viewport={"width": 1920, "height": 1080},
            args=["--no-sandbox"],
        )
        page = context.pages[0]

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(8000)

        # 查 audio 元素
        result = await page.evaluate("""() => {
            const audios = Array.from(document.querySelectorAll('audio'));
            return audios.map(a => ({
                src: a.src,
                currentSrc: a.currentSrc,
                duration: a.duration,
                readyState: a.readyState,
                paused: a.paused,
            }));
        }""")
        print(f"📊 页面 audio 元素数: {len(result)}")
        for i, a in enumerate(result):
            print(f"   [{i}] src={a['src'][:80] if a['src'] else 'None'}")
            print(f"       currentSrc={a['currentSrc'][:80] if a['currentSrc'] else 'None'}")
            print(f"       duration={a['duration']:.1f}s, readyState={a['readyState']}, paused={a['paused']}")

        # 查 window 上的相关变量
        keys = await page.evaluate("""() => {
            return Object.keys(window).filter(k =>
                k.includes('audio') ||
                k.includes('Audio') ||
                k.includes('player') ||
                k.includes('Player') ||
                k.includes('vue') ||
                k.includes('VUE') ||
                k.includes('store') ||
                k.includes('Store') ||
                k.includes('__') ||
                k.includes('NUXT')
            ).slice(0, 50);
        }""")
        print(f"\n📊 window 全局变量 (audio/vue/store/player/NUXT): {len(keys)}")
        for k in keys:
            print(f"   - {k}")

        # 点击 Unit 6 触发预加载
        print("\n🖱️  点击 Unit 6...")
        await page.locator("text=Unit 6").first.click()
        await page.wait_for_timeout(3000)

        result2 = await page.evaluate("""() => {
            const audios = Array.from(document.querySelectorAll('audio'));
            return audios.map(a => ({
                src: a.src,
                duration: a.duration,
            }));
        }""")
        print(f"📊 点击 Unit 6 后 audio 元素数: {len(result2)}")
        for i, a in enumerate(result2):
            print(f"   [{i}] {a['src'][:100] if a['src'] else 'None'}")

        await context.close()

asyncio.run(main())
