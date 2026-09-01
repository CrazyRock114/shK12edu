#!/usr/bin/env python3
"""
OCR 提取每页文字，用 tesseract 命令行（避开 Python OCR 库的 numpy 冲突）
- 输入：raw/trimmed/page001.jpg ~ page098.jpg
- 输出：raw/text/page001.txt ~ page098.txt
- 输出：raw/text/pages.json（带页号/全文/逐项/置信度）
- 输出：raw/text/all.txt（合并全文）
"""
import sys
import json
import subprocess
import re
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "raw" / "trimmed"
TXT_DIR = Path(__file__).resolve().parent.parent / "raw" / "text"
JSON_PATH = TXT_DIR / "pages.json"
ALL_PATH = TXT_DIR / "all.txt"

# tesseract 路径
TESSERACT = "/opt/homebrew/bin/tesseract"
if not Path(TESSERACT).exists():
    # 备选
    candidates = [
        "/opt/homebrew/bin/tesseract",
        "/usr/local/bin/tesseract",
        "/usr/bin/tesseract",
    ]
    for c in candidates:
        if Path(c).exists():
            TESSERACT = c
            break
    else:
        # 用 which 查
        result = subprocess.run(["which", "tesseract"], capture_output=True, text=True)
        TESSERACT = result.stdout.strip() or "tesseract"


def ocr_one(img_path: Path, lang: str = "chi_sim+eng") -> dict:
    """对一张图调 tesseract，返回 TSV 解析结果"""
    proc = subprocess.run(
        [TESSERACT, str(img_path), "-", "-l", lang, "--psm", "6", "tsv"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if proc.returncode != 0:
        return {"text": "", "items": [], "error": proc.stderr}

    # 解析 TSV：列 = level page_num block_num par_num line_num word_num left top width height conf text
    items = []
    full_text_parts = []
    for line in proc.stdout.splitlines()[1:]:  # 跳过表头
        cols = line.split("\t")
        if len(cols) < 12:
            continue
        try:
            level = int(cols[0])
            conf = float(cols[10])
            text = cols[11].strip()
        except (ValueError, IndexError):
            continue

        # level=5 是 word
        if level == 5 and text and conf >= 0:
            items.append({
                "text": text,
                "conf": round(conf, 2),
                "left": int(cols[6]),
                "top": int(cols[7]),
                "width": int(cols[8]),
                "height": int(cols[9]),
            })
            full_text_parts.append(text)

    # 按行聚合
    text = " ".join(full_text_parts)
    return {"text": text, "items": items}


def main():
    if not SRC_DIR.exists():
        print(f"❌  源目录不存在: {SRC_DIR}")
        print("   请先跑 trim_screenshots.py")
        sys.exit(1)

    files = sorted(SRC_DIR.glob("page*.jpg"))
    if not files:
        print(f"❌  没找到截图: {SRC_DIR}")
        sys.exit(1)

    TXT_DIR.mkdir(parents=True, exist_ok=True)

    # 检查 tesseract
    print(f"📁 源目录: {SRC_DIR}")
    print(f"📁 输出:   {TXT_DIR}")
    print(f"📊 文件数: {len(files)}")
    print(f"🔧 tesseract: {TESSERACT}")
    print()

    if not Path(TESSERACT).exists():
        print(f"❌  tesseract 未找到")
        print("   请先安装: brew install tesseract tesseract-lang")
        sys.exit(1)

    pages = []
    total_items = 0
    total_chars = 0
    all_lines = []

    for i, f in enumerate(files, 1):
        result = ocr_one(f)
        text = result.get("text", "")
        items = result.get("items", [])

        # 单页 txt
        (TXT_DIR / f"{f.stem}.txt").write_text(text, encoding="utf-8")

        # json
        pages.append({
            "page": i,
            "file": f.name,
            "text": text,
            "items": items,
        })

        # 合并
        all_lines.append(f"=== {f.name} ===")
        all_lines.append(text)
        all_lines.append("")

        total_items += len(items)
        total_chars += len(text)
        print(f"  [{i:3d}/{len(files)}] {f.name}  {len(items)} 项, {len(text)} 字")

    # 写 pages.json
    JSON_PATH.write_text(
        json.dumps(pages, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 写 all.txt
    ALL_PATH.write_text("\n".join(all_lines), encoding="utf-8")

    print()
    print("=" * 60)
    print(f"✅ OCR 完成")
    print(f"📄 总页数: {len(pages)}")
    print(f"🔢 总识别项: {total_items}")
    print(f"📝 总字符数: {total_chars}")
    print(f"📁 单页 TXT: {TXT_DIR}/page001.txt ~ page098.txt")
    print(f"📁 合并 JSON: {JSON_PATH}")
    print(f"📁 合并 TXT: {ALL_PATH}")


if __name__ == "__main__":
    main()
