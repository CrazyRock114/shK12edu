#!/usr/bin/env python3
"""
国家中小学智慧教育平台 - 教材批量截图脚本
================================================
用法：
  1. 装依赖: pip install -r requirements.txt
  2. 装浏览器: python -m playwright install chromium
  3. 运行:   python capture.py
  4. 第一次跑会让你手动登录；之后复用登录态
"""
import asyncio
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌  playwright 未安装，请先执行:")
    print("    pip install playwright")
    print("    python -m playwright install chromium")
    sys.exit(1)

# ============== 配置 ==============
# URL 由运行时的用户输入提供
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "raw" / "screenshots"
USER_DATA_DIR = Path.home() / ".cache" / "smartedu-browser"  # 浏览器数据目录（保留登录）
DELAY_MS = 10000  # 每页等待 PDF 翻页+渲染（毫秒），10s 兜底慢网络
# ================================


def banner(text: str):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


async def is_login_required(page) -> bool:
    """检查当前页是否需要登录（用首页导航看是否有登录按钮 + 头像）"""
    # 如果页面右上角有用户头像（已登录），返回 False
    has_avatar = await page.locator("img[src*='avatar_url']").count() > 0
    # 如果有显式"登录"按钮（未登录），返回 True
    has_login_btn = await page.locator("a:has-text('登录')").count() > 0
    return has_login_btn and not has_avatar


async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # ===== 用户输入 =====
    print()
    print("=" * 60)
    print("  📚  教材批量截图工具")
    print("=" * 60)
    print()
    url = input("  请输入课程 URL\n  (示例: https://basic.smartedu.cn/tchMaterial/detail?...): ").strip()
    if not url:
        print("\n❌  URL 不能为空")
        return
    print()
    start_input = input("  起始页 (直接回车 = 1): ").strip()
    start_page = int(start_input) if start_input else 1
    end_input = input("  结束页 (直接回车 = 98): ").strip()
    end_page = int(end_input) if end_input else 98
    if end_page < start_page:
        print(f"\n❌  结束页 ({end_page}) 不能小于起始页 ({start_page})")
        return
    total_pages = end_page - start_page + 1

    banner(f"📁 输出目录: {OUTPUT_DIR}")
    banner(f"💾 浏览器数据: {USER_DATA_DIR}")
    print()
    print(f"  📖 课程 URL: {url[:90]}{'...' if len(url) > 90 else ''}")
    print(f"  📄 抓取范围: 第 {start_page} 页 → 第 {end_page} 页（共 {total_pages} 页）")
    print()

    async with async_playwright() as p:
        # 持久化 context - 保留登录态
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,  # 必须非 headless（你要看到浏览器）
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,  # HiDPI/Retina 模拟，截图分辨率 ×2
            locale="zh-CN",
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--high-dpi-support=1",
                "--force-device-scale-factor=2",
            ],
            slow_mo=0,  # 不减速
        )

        # 关闭默认空白页，导航到目标 URL
        page = context.pages[0] if context.pages else await context.new_page()
        print(f"\n🌐 打开教材页...")
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(5000)

        # 检查登录态
        if await is_login_required(page):
            banner("⚠️  检测到未登录！请手动登录")
            print("操作步骤：")
            print("  1. 在打开的浏览器中点击右上角「登录」")
            print("  2. 用教育账号/手机号/扫码完成登录")
            print("  3. 登录后回到本终端按回车")
            print()
            input("📌 登录完成后按回车继续...")
            await page.wait_for_timeout(3000)
            if await is_login_required(page):
                print("❌ 仍检测到未登录，退出")
                await context.close()
                return

        # 找到 PDF iframe
        iframe_handle = await page.wait_for_selector("iframe", state="visible", timeout=30000)
        iframe = await iframe_handle.content_frame()
        if not iframe:
            print("❌ 找不到 PDF iframe")
            await context.close()
            return

        # 等待 PDF.js viewer canvas 真的渲染出来
        print("⏳  等待 PDF viewer 加载...")
        try:
            await iframe.locator("canvas").first.wait_for(state="visible", timeout=30000)
            print("✅  PDF canvas 已就绪")
        except Exception:
            print("⚠️  PDF canvas 没出现，尝试用其他选择器...")
            try:
                await iframe.locator("#viewer, .pdfViewer").first.wait_for(state="visible", timeout=10000)
            except Exception:
                print("⚠️  仍没检测到，强行继续")

        # 点击 iframe 让 PDF viewer 拿到键盘焦点
        try:
            await iframe.locator("body").click(position={"x": 500, "y": 500})
        except Exception:
            pass

        # 额外等几秒让第一页完全渲染（关键：保证 page 抓得对）
        await page.wait_for_timeout(8000)
        print(f"✅  PDF 已加载完，请确认浏览器里看到的是第 {start_page} 页")
        print("   （如果不对，请现在手动翻到正确的页）")
        input("📌 准备好后按回车开始批量截图（脚本将连续跑，期间不要操作浏览器）...")
        print("🚀  开始截图循环\n")

        banner(f"🚀 开始批量截图，共 {total_pages} 页")
        print(f"⏱️  每页约 {DELAY_MS/1000}s，预计 {(total_pages * DELAY_MS / 60000):.1f} 分钟")
        print("📌  不要操作浏览器窗口，脚本会全权接管")
        print()

        for page_num in range(start_page, end_page + 1):
            output_path = OUTPUT_DIR / f"page{page_num:03d}.jpg"

            # 1) 先等 10s（PDF 翻页 + 渲染）
            if page_num == start_page:
                # 起始页之前已经 wait 过，少等
                await page.wait_for_timeout(3000)
            else:
                await page.wait_for_timeout(DELAY_MS)

            # 2) 截图
            try:
                await page.screenshot(path=str(output_path), full_page=True, timeout=15000)
            except Exception as e:
                print(f"\n  ⚠️  page{page_num:03d} 截图失败: {e}")

            # 强制等待防止出现小转圈
            await page.wait_for_timeout(3000)

            # 进度
            done = page_num - start_page + 1
            pct = done / total_pages * 100
            print(f"  [{pct:5.1f}%] page{page_num:03d}.jpg  ({done}/{total_pages})", end="\r")

            # 3) 翻页（最后一页不翻）
            if page_num < end_page:
                try:
                    # 点击 PDF iframe 中心
                    await iframe.locator("body").click(
                        position={"x": 500, "y": 500},
                        timeout=3000,
                    )
                except Exception:
                    # 备用：键盘 PageDown
                    try:
                        await page.keyboard.press("PageDown")
                    except Exception:
                        pass

        banner("✅ 全部完成！")
        print(f"📁  共 {total_pages} 张截图保存到:")
        print(f"   {OUTPUT_DIR}")
        print()
        # 简单统计（只统计本次抓的范围）
        target_files = [OUTPUT_DIR / f"page{i:03d}.jpg" for i in range(start_page, end_page + 1)]
        valid = [f for f in target_files if f.exists() and f.stat().st_size > 30_000]
        blanks = [f for f in target_files if f.exists() and f.stat().st_size <= 30_000]
        missing = [f for f in target_files if not f.exists()]
        print(f"📊 本次统计: 有效 {len(valid)} 张，黑屏 {len(blanks)} 张，缺失 {len(missing)} 张")
        if blanks:
            print(f"⚠️  黑屏文件: {[f.name for f in blanks]}")
        if missing:
            print(f"⚠️  缺失文件: {[f.name for f in missing]}")
        if blanks or missing:
            print(f"   可补抓：起始页={start_page}, 结束页={end_page} 重跑")

        await context.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  用户中断，已抓的图保留在 " + str(OUTPUT_DIR))
        sys.exit(0)
