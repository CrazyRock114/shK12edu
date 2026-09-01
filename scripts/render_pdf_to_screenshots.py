#!/usr/bin/env python3
"""
从 G3A_English(OCR).pdf / G5A_English(OCR).pdf 渲染全部页为 jpg
- 覆盖 raw/screenshots/pageNNN.jpg
- 让 screenshots 跟 PDF 物理页码完全一致
- 备份原 screenshots 到 raw/screenshots.bak.<时间>/
"""
import sys
import shutil
from pathlib import Path
from datetime import datetime
import fitz

PDF = Path("/Users/paulshi/Documents/MiniMax/shK12edu/raw/G3A_English(OCR).pdf")
SCREENSHOTS = Path("/Users/paulshi/Documents/MiniMax/shK12edu/raw/screenshots")
DPI = 144  # 高清

# 可选：只渲染某范围
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=1)
parser.add_argument("--end", type=int, default=None)
args = parser.parse_args()


def main():
    if not PDF.exists():
        print(f"❌  PDF 不存在: {PDF}")
        sys.exit(1)

    doc = fitz.open(PDF)
    total = len(doc)
    end = args.end or total
    print(f"📄 PDF: {PDF.name} ({total} 页)")
    print(f"📁 输出: {SCREENSHOTS}")
    print(f"🔍 渲染范围: p{args.start:03d} - p{end:03d}")
    print(f"📐 DPI: {DPI}")

    # 第一次跑才备份
    bak_dir = SCREENSHOTS.parent / f"screenshots.bak.{datetime.now().strftime('%H%M%S')}"
    existing = list(SCREENSHOTS.glob("page*.jpg"))
    if existing and not bak_dir.exists():
        print(f"\n💾 备份原 screenshots → {bak_dir.name}/")
        shutil.copytree(SCREENSHOTS, bak_dir)
    elif bak_dir.exists():
        print(f"💾 备份已存在: {bak_dir.name}/")

    SCREENSHOTS.mkdir(parents=True, exist_ok=True)

    print()
    for i in range(args.start, end + 1):
        page = doc[i-1]
        pix = page.get_pixmap(dpi=DPI)
        out = SCREENSHOTS / f"page{i:03d}.jpg"
        pix.save(str(out))
        pct = (i - args.start + 1) / (end - args.start + 1) * 100
        print(f"  [{pct:5.1f}%] page{i:03d}.jpg  ({pix.width}x{pix.height})", end="\r")
    print()

    print(f"\n✅ 完成: {end - args.start + 1} 页")


if __name__ == "__main__":
    main()
