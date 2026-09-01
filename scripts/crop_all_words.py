#!/usr/bin/env python3
"""
对 unit2-10 批量从教材页裁切单词对应图
基于 PyMuPDF search_for 找文字位置,扩展 200x200 px 区域
"""
import json
import re
from pathlib import Path
import fitz
from PIL import Image

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
PDF = ROOT / "raw" / "G3A_English(OCR).pdf"
TRIMMED = ROOT / "raw" / "trimmed"


def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower()).strip()


def crop_unit_words(unit_id, book_start, topic_words, img_w=1552, img_h=2165):
    """对单个 unit 裁切单词图"""
    pdf_page = book_start + 7  # 教材 p.1 = PDF p.8
    img_path = TRIMMED / f"page{pdf_page:03d}.jpg"
    if not img_path.exists():
        print(f"   ❌ {unit_id}: {img_path.name} 不存在")
        return 0

    pdf = fitz.open(str(PDF))
    page = pdf[pdf_page - 1]
    PW, PH = page.rect.width, page.rect.height
    SX, SY = img_w / PW, img_h / PH

    im = Image.open(img_path)
    out_dir = ROOT / f"site/assets/img/{unit_id}"
    out_dir.mkdir(parents=True, exist_ok=True)

    cropped = 0
    used_boxes = []  # 已用区域,避免重叠

    for word in topic_words:
        w_safe = word.replace(" ", "_")
        # 找第一个匹配位置(在 PDF 文字中)
        rects = page.search_for(word)
        if not rects:
            # 试 normalize
            for r in page.search_for(normalize(word)):
                rects.append(r)
                break
        if not rects:
            print(f"   ⚠️  {word}: 文字未找到")
            continue

        # 用第一个 rect
        r = rects[0]
        # 扩展 box:左右各 100,上下各 80
        cx = (r.x0 + r.x1) / 2
        cy = (r.y0 + r.y1) / 2
        box_pdf = (max(0, cx - 150), max(0, cy - 100), min(PW, cx + 200), min(PH, cy + 150))
        # 转图片坐标
        box_px = (int(box_pdf[0] * SX), int(box_pdf[1] * SY),
                  int(box_pdf[2] * SX), int(box_pdf[3] * SY))
        # 裁切
        crop = im.crop(box_px)
        dst = out_dir / f"{w_safe}.jpg"
        crop.save(dst, "JPEG", quality=85)
        cropped += 1
        print(f"   ✓ {word:20} -> {dst.name}  ({box_px[2]-box_px[0]}x{box_px[3]-box_px[1]})")

    pdf.close()
    return cropped


def main():
    with open(ROOT / "site/units_data.json") as f:
        units = json.load(f)["units"]

    total_cropped = 0
    for u in units:
        uid = u["id"]
        if uid in ("starter", "words_to_use"):
            continue  # 跳过特殊 unit
        if not u.get("topic_words") or not u.get("book_start"):
            continue
        # 检查是否已裁切
        out_dir = ROOT / f"site/assets/img/{uid}"
        existing = sum(1 for _ in out_dir.glob("*.jpg")) if out_dir.exists() else 0
        if existing >= len(u["topic_words"]):
            print(f"⏭️  {uid}: 已有 {existing} 张图,跳过")
            continue

        print(f"\n=== {uid} ===")
        n = crop_unit_words(uid, u["book_start"], u["topic_words"])
        total_cropped += n

    print(f"\n📊 总裁切 {total_cropped} 张图")


if __name__ == "__main__":
    main()
