#!/usr/bin/env python3
"""
检查 G3A_English.pdf 和 G3A_English(OCR).pdf 的嵌入资源
"""
import sys
from pathlib import Path
import fitz

RAW = Path(__file__).resolve().parent.parent / "raw"


def inspect(pdf_path: Path):
    print(f"\n{'=' * 60}")
    print(f"📁 {pdf_path.name}")
    if not pdf_path.exists():
        print(f"❌  不存在")
        return

    doc = fitz.open(pdf_path)
    print(f"📄 页数: {len(doc)}")

    # 1. 嵌入文件
    emb_count = doc.embfile_count()
    print(f"📎 嵌入文件: {emb_count} 个")
    if emb_count > 0:
        for name in doc.embfile_names():
            info = doc.embfile_info(name)
            print(f"   - {name}  ({info.get('size', '?')} bytes)")

    # 2. annotations
    total_annots = 0
    annot_types = {}
    for i, page in enumerate(doc, 1):
        for annot in page.annots() or []:
            total_annots += 1
            t = annot.type
            annot_types[t] = annot_types.get(t, 0) + 1

    print(f"📝 annotations: {total_annots} 个")
    for t, c in annot_types.items():
        print(f"   - {t}: {c}")

    # 3. links
    total_links = 0
    for page in doc:
        for link in page.get_links() or []:
            total_links += 1
    print(f"🔗 links: {total_links} 个")

    doc.close()


def main():
    inspect(RAW / "G3A_English.pdf")
    inspect(RAW / "G3A_English(OCR).pdf")


if __name__ == "__main__":
    main()
