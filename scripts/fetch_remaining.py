#!/usr/bin/env python3
"""
针对缺失的 Unit 7 + Words to use 再跑一次
清 IndexedDB + reload 让 smartedu 必须重新 fetch
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


async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            viewport={"width": 1920, "height": 1080},
            locale="zh-CN",
            args=["--no-sandbox"],
        )
        page = context.pages[0] if context.pages else await context.new_page()

        # 收集 list
        captured: list = []
        cap_lock = asyncio.Lock()

        async def handle_route(route, request):
            try:
                response = await route.fetch()
                body = await response.body()
                await route.fulfill(response=response)
                async with cap_lock:
                    captured.append({"url": request.url, "body": body, "size": len(body)})
                    print(f"   📥 {len(captured):2d}  {request.url.split('/')[-1][:30]}  ({len(body)/1024/1024:.1f} MB)", flush=True)
            except Exception as e:
                print(f"   ⚠️  {e}", flush=True)
                await route.continue_()

        await context.route("**/r2-ndr-private.ykt.cbern.com.cn/**/*.mp3", handle_route)

        # 加载
        print("🌐 打开教材页...", flush=True)
        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(8000)

        try:
            await page.locator("text=音频资源").wait_for(state="visible", timeout=15000)
        except Exception:
            pass
        await page.wait_for_timeout(2000)

        # 多次 reload + 清 IndexedDB,触发 smartedu 重新 fetch 默认 audio(可能是 WtU)
        for i in range(5):
            print(f"\n🔄 Reload 轮次 {i+1}/5...", flush=True)
            # 清 IndexedDB
            try:
                await page.evaluate("""async () => {
                    if (indexedDB.databases) {
                        const dbs = await indexedDB.databases();
                        for (const db of dbs) {
                            if (db.name) {
                                await new Promise(resolve => {
                                    const req = indexedDB.deleteDatabase(db.name);
                                    req.onsuccess = req.onerror = req.onblocked = resolve;
                                });
                            }
                        }
                    }
                }""")
            except Exception:
                pass
            await page.wait_for_timeout(500)
            await page.reload(wait_until="domcontentloaded")
            await page.wait_for_timeout(10000)

        # 现在 captured 应该有很多。直接保存所有
        all_caps = list(captured)
        print(f"\n📊 总捕获 {len(all_caps)} 个 URL", flush=True)
        for i, c in enumerate(all_caps):
            print(f"   [{i}] {c['url'].split('/')[-1]}  ({c['size']/1024/1024:.1f} MB)", flush=True)

        await context.close()

    # 写盘(去重 by URL)
    seen_urls = set()
    unique = []
    for c in all_caps:
        if c["url"] not in seen_urls:
            seen_urls.add(c["url"])
            unique.append(c)

    print(f"\n去重后: {len(unique)} 个", flush=True)
    print("\n💾 写盘...", flush=True)
    for i, c in enumerate(unique):
        # 用 URL hash 做名(避免覆盖已知)
        from hashlib import md5
        h = md5(c["url"].encode()).hexdigest()[:8]
        dst = OUT_DIR / f"audio_{h}.mp3"
        dst.write_bytes(c["body"])
        print(f"   ✓ {dst.name}  ({c['size']/1024/1024:.1f} MB)", flush=True)

    print(f"\n📁 路径: {OUT_DIR}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
