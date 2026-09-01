#!/usr/bin/env python3
"""
诊断: 找 smartedu 教材页的 audio 列表数据
- 看 Vue 组件的 data / props
- 看 window 上的 audio 相关变量
- 看 audio 元素 src + duration 序列
- 验证 audio_00.mp3 是不是合集
"""
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

        # 找 window 上的 audio list 数据
        # smartedu 是 Vue,看 __VUE__ / __pinia / app 等
        result = await page.evaluate("""() => {
            const out = {};
            // 1. 找 Vue 实例
            const appEl = document.querySelector('#app') || document.querySelector('[data-v-app]');
            if (appEl && appEl.__vue_app__) {
                out.vue_app = 'YES';
                const app = appEl.__vue_app__.config.globalProperties;
                out.vue_global_keys = Object.keys(app).slice(0, 20);
            }

            // 2. 找所有有 __vueParentComponent 的元素(通常 audio 列表在那里)
            const allEls = document.querySelectorAll('*');
            const seen = new Set();
            const candidates = [];
            for (const el of allEls) {
                if (el.__vueParentComponent && !seen.has(el.__vueParentComponent)) {
                    seen.add(el.__vueParentComponent);
                    const comp = el.__vueParentComponent;
                    const data = comp.props || {};
                    const keys = Object.keys(data);
                    if (keys.some(k => k.toLowerCase().includes('audio'))) {
                        candidates.push({
                            tag: el.tagName,
                            text: (el.textContent || '').slice(0, 100),
                            prop_keys: keys,
                        });
                    }
                }
            }
            out.candidates = candidates.slice(0, 20);

            // 3. 找 window 上的 audio list
            const audioKeys = Object.keys(window).filter(k => {
                const v = window[k];
                if (!v || typeof v !== 'object') return false;
                if (Array.isArray(v) && v.length > 0) {
                    return v.some(item => item && typeof item === 'object' &&
                        ('url' in item || 'src' in item || 'audioUrl' in item));
                }
                return false;
            });
            out.audio_keys = audioKeys;

            // 4. 找所有带 audio 数据的全局变量
            const propKeys = Object.keys(window).filter(k => {
                if (k.startsWith('webkit') || k.startsWith('on')) return false;
                try {
                    const v = window[k];
                    if (v && typeof v === 'object' && !Array.isArray(v)) {
                        const str = JSON.stringify(v).slice(0, 1000);
                        return str.includes('r2-ndr-private') || str.includes('listening') || str.includes('.mp3');
                    }
                } catch(e) {}
                return false;
            });
            out.audio_url_globals = propKeys;

            return out;
        }""")

        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))

        # 单独试一下:点每个 unit 后,看 audio 元素的 duration 变化
        print("\n📊 点击每个 unit 后 audio 元素的 duration:")
        for name in ["Starter", "Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5",
                     "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10", "Words to use"]:
            try:
                await page.locator(f"text={name}").first.click(timeout=3000)
                await page.wait_for_timeout(2500)
                info = await page.evaluate("""() => {
                    const audios = document.querySelectorAll('audio');
                    const out = [];
                    for (const a of audios) {
                        if (a.src && a.src.startsWith('blob:')) {
                            out.push({
                                src: a.src.slice(0, 60),
                                duration: a.duration,
                                currentTime: a.currentTime,
                            });
                        }
                    }
                    return out;
                }""")
                if info:
                    d = info[0]['duration']
                    if d and d > 0 and d != float('inf'):
                        m, s = divmod(int(d), 60)
                        print(f"  {name:15} duration = {m}:{s:02d} ({d:.0f}s)")
                    else:
                        print(f"  {name:15} duration = {d}")
                else:
                    print(f"  {name:15} no audio element")
            except Exception as e:
                print(f"  {name:15} click fail: {e}")

        await context.close()

asyncio.run(main())
