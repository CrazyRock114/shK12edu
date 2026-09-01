#!/usr/bin/env python3
"""
将 raw/trimmed/ 下的 98 张图合并为一个 PDF 文档
"""
import sys
from pathlib import Path
from PIL import Image

SRC_DIR = Path(__file__).resolve().parent.parent / "raw" / "trimmed"
DST = Path(__file__).resolve().parent.parent / "raw" / "textbook.pdf"


def main():
    if not SRC_DIR.exists():
        print(f"❌  源目录不存在: {SRC_DIR}")
        sys.exit(1)

    files = sorted(SRC_DIR.glob("page*.jpg"))
    if not files:
        print(f"❌  没找到截图: {SRC_DIR}")
        sys.exit(1)

    print(f"📁 源目录: {SRC_DIR}")
    print(f"📁 输出:   {DST}")
    print(f"📊 文件数: {len(files)}")
    print()

    # 预读取所有图（第一张用 save，后续用 append_images）
    print("⏳  加载图片...")
    images = []
    for f in files:
        try:
            img = Image.open(f).convert("RGB")
            images.append(img)
            print(f"  ✓ {f.name}  {img.size[0]}x{img.size[1]}", end="\r")
        except Exception as e:
            print(f"\n  ❌ {f.name}: {e}")
            return

    print(f"\n⏳  正在生成 PDF（{len(images)} 页，可能要几十秒）...")

    try:
        # PIL 的 PDF 保存支持多页
        images[0].save(
            DST,
            "PDF",
            resolution=150.0,  # PDF 渲染 DPI
            save_all=True,
            append_images=images[1:],
            quality=85,  # JPEG 质量（PDF 内嵌 JPEG）
            optimize=True,
        )
    except Exception as e:
        print(f"❌  PDF 生成失败: {e}")
        return

    size_mb = DST.stat().st_size / 1024 / 1024
    print(f"\n✅  PDF 生成完成")
    print(f"📁  路径: {DST}")
    print(f"💾  大小: {size_mb:.1f} MB")
    print(f"📄  页数: {len(images)}")


if __name__ == "__main__":
    main()
