#!/usr/bin/env python3
"""
提取 G5A_English(OCR).pdf 的所有文字
输出：raw/text/all_pages.txt
"""
import sys
from pathlib import Path
import fitz

PDF = Path(__file__).resolve().parent.parent / "raw" / "G5A_English(OCR).pdf"
OUT_DIR = Path(__file__).resolve().parent.parent / "raw" / "text"
OUT_TXT = OUT_DIR / "all_pages.txt"


def main():
    if not PDF.exists():
        print(f"❌  找不到: {PDF}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"📁 打开: {PDF}")
    doc = fitz.open(PDF)
    print(f"📄 总页数: {len(doc)}")

    all_text = []
    for i, page in enumerate(doc, 1):
        text = page.get_text("text")
        all_text.append(f"=== Page {i} ===")
        all_text.append(text)
        all_text.append("")
        print(f"  [{i:3d}/{len(doc)}] {len(text):5d} 字")

    OUT_TXT.write_text("\n".join(all_text), encoding="utf-8")

    total_chars = sum(len(t) for t in all_text)
    print()
    print(f"✅ 完成")
    print(f"📝 总字数: {total_chars}")
    print(f"📁 输出: {OUT_TXT}")


if __name__ == "__main__":
    main()
