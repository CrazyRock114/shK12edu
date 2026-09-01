#!/usr/bin/env python3
"""
批量处理 12 个 unit:
1. Whisper 转写 audio
2. 按 topic_words + key_phrases 切片
3. 切整页图 (教材原页)
"""
import json
import re
import subprocess
import os
import sys
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
FFMPEG = Path.home() / ".local" / "bin" / "ffmpeg"
os.environ["PATH"] = str(FFMPEG.parent) + ":" + os.environ.get("PATH", "")

import whisper
import fitz
from PIL import Image


def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower()).strip()


def find_segment(segments, target_text, fallback_time=None):
    target_norm = normalize(target_text)
    for seg in segments:
        if normalize(seg["text"]) == target_norm:
            return seg
    target_words = set(target_norm.split())
    for seg in segments:
        seg_norm = normalize(seg["text"])
        seg_words = set(seg_norm.split())
        if target_words.issubset(seg_words):
            return seg
    if fallback_time:
        class FakeSeg:
            def __init__(self, s, e):
                self.start, self.end = s, e
                self.text = target_text
        return FakeSeg(*fallback_time)
    return None


def slice_audio(src, start, end, dst, padding=0.15):
    start_pad = max(0, start - padding)
    end_pad = end + padding
    duration = end_pad - start_pad
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(FFMPEG), "-y", "-loglevel", "error",
        "-i", str(src),
        "-ss", f"{start_pad:.3f}",
        "-t", f"{duration:.3f}",
        "-af", f"afade=t=in:st=0:d=0.05,afade=t=out:st={duration-0.1:.3f}:d=0.05",
        "-ar", "22050", "-ac", "1", "-b:a", "64k",
        str(dst),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"   ❌ ffmpeg: {r.stderr[:200]}")
        return False
    return True


def find_topics_page(pdf, pdf_start, pdf_end, topic_words):
    """找包含 topic words 的页码"""
    for page_idx in range(pdf_start - 1, pdf_end):
        if page_idx >= len(pdf):
            break
        page = pdf[page_idx]
        text = page.get_text().lower()
        # 检查这一页是否包含所有 topic_words
        found_count = sum(1 for w in topic_words if normalize(w) in text or normalize(w.split()[0]) in text)
        if found_count >= max(1, len(topic_words) // 2):
            return page_idx + 1, page  # 1-indexed
    return pdf_start, pdf[pdf_start - 1]


def auto_crop_topic_words(pdf_page, img_w, img_h, topic_words, page_idx):
    """通用方法:在 topic words 页自动裁切单词图
    教材布局: 顶部 60% 是 topic words 大场景图,8 个词标签散布其中
    简化方案:整页作为一个 lesson_full,不再细分单词图(后续手动精修)
    """
    PW, PH = pdf_page.rect.width, pdf_page.rect.height
    SX, SY = img_w / PW, img_h / PH
    # 返回 1 个大区域(整页)
    return [(0, 0, img_w, img_h)]


def process_unit(unit_id, unit_info, model):
    """处理单个 unit"""
    audio_path = ROOT / "raw" / "audio" / unit_info["audio_file"]
    if not audio_path.exists():
        print(f"⚠️  {unit_id}: 音频文件不存在 {audio_path}")
        return False

    print(f"\n=== {unit_id} ({unit_info['audio_file']}) ===")

    # 1. Whisper 转写
    whisper_json = ROOT / f"raw/transcripts/{unit_id}.json"
    whisper_json.parent.mkdir(parents=True, exist_ok=True)
    if not whisper_json.exists():
        print(f"  🔊 Whisper 转写...")
        result = model.transcribe(
            str(audio_path),
            language="en",
            word_timestamps=True,
            verbose=False,
        )
        with open(whisper_json, "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  ✓ 转写完成 ({len(result.get('segments', []))} segments)")
    else:
        print(f"  ✓ 转写已存在")

    with open(whisper_json) as f:
        result = json.load(f)
    segments = result.get("segments", [])

    # 2. 切片
    items = []
    # topic words (每个词)
    for w in unit_info.get("topic_words", []):
        items.append({"text": w, "save_as": f"words/{w.replace(' ', '_')}.mp3"})
    # 关键短语
    for p in unit_info.get("key_phrases", []):
        # 文件名: 取前 5 个词
        slug = "_".join(p.lower().split()[:5])
        slug = re.sub(r"[^a-z0-9_]", "", slug)
        items.append({"text": p, "save_as": f"phrases/{slug}.mp3"})

    out_dir = ROOT / "site" / "assets" / "audio" / unit_id
    out_dir.mkdir(parents=True, exist_ok=True)

    saved = 0
    print(f"  ✂️  切片 {len(items)} 个 item...")
    for item in items:
        target_text = item["text"]
        save_as = item["save_as"]
        seg = find_segment(segments, target_text)
        if not seg:
            print(f"   ⚠️  '{target_text[:30]}' 未找到")
            continue
        if isinstance(seg, dict):
            start, end = seg["start"], seg["end"]
        else:
            start, end = seg.start, seg.end
        dst = out_dir / save_as
        if slice_audio(audio_path, start, end, dst):
            saved += 1
    print(f"  ✓ 切片完成 {saved}/{len(items)}")

    # 3. 切整页 lesson_full.jpg
    img_dir = ROOT / "site" / "assets" / "img" / unit_id
    img_dir.mkdir(parents=True, exist_ok=True)
    lesson_path = img_dir / "lesson_full.jpg"
    pdf = fitz.open(str(ROOT / "raw" / "G3A_English(OCR).pdf"))
    pdf_start = unit_info.get("pdf_start", 1)
    pdf_end = unit_info.get("pdf_end", pdf_start)
    # 找 topic words 页
    topics_page_idx, topics_page = find_topics_page(
        pdf, pdf_start, pdf_end, unit_info.get("topic_words", [])
    )
    pdf.close()

    # 教材页:找 p.8 (book) 对应的 PDF 页(在 pdf_start 之后)
    book_start = unit_info.get("book_start")
    if book_start:
        # 教材 p.book_start 对应 PDF p.(book_start+7)
        # 因为教材 p.1 = PDF p.8 (封面)
        topics_pdf_page = book_start + 7
    else:
        topics_pdf_page = topics_page_idx

    # 找 trimmed 图
    trimmed_pdf_page = topics_pdf_page
    img_path = ROOT / "raw" / "trimmed" / f"page{trimmed_pdf_page:03d}.jpg"
    if img_path.exists():
        im = Image.open(img_path)
        # 保存为 lesson_full
        im.save(lesson_path, "JPEG", quality=80)
        print(f"  📷 教材原页: {img_path.name} -> {lesson_path.name}")
    else:
        print(f"  ⚠️  教材图 {img_path} 不存在")

    return saved > 0


def main():
    # 加载 units.json
    with open(ROOT / "raw/structure/units.json") as f:
        units_data = json.load(f)
    units_list = units_data["units"]

    # 加载 units_data.json (音频文件映射)
    with open(ROOT / "site/units_data.json") as f:
        site_units = {u["id"]: u for u in json.load(f)["units"]}

    # 合并:raw structure + site audio mapping
    all_units = []
    for u in units_list:
        unit_id = u["id"]
        site_u = site_units.get(unit_id, {})
        all_units.append({
            "id": unit_id,
            "audio_file": site_u.get("audio_file", f"{unit_id.replace('unit', 'unit_')}.mp3"),
            "topic_words": u.get("topic_words") or u.get("sections", []),  # starter 没 topic_words 用 sections
            "key_phrases": u.get("key_phrases", []),
            "pdf_start": u.get("pdf_start", 1),
            "pdf_end": u.get("pdf_end", 1),
            "book_start": u.get("book_start"),
        })

    # 加上 starter
    all_units.insert(0, {
        "id": "starter",
        "audio_file": "starter.mp3",
        "topic_words": ["alphabet", "spring", "summer", "autumn", "winter", "one", "two", "three"],
        "key_phrases": [],
        "pdf_start": 9,
        "pdf_end": 13,
        "book_start": 2,
    })

    # 加上 words_to_use
    all_units.append({
        "id": "words_to_use",
        "audio_file": "words_to_use.mp3",
        "topic_words": [],
        "key_phrases": [],
        "pdf_start": 94,
        "pdf_end": 94,
        "book_start": 87,
    })

    print(f"将处理 {len(all_units)} 个 unit")
    print("加载 Whisper 模型 (tiny)...")
    model = whisper.load_model("tiny")
    print("模型就绪\n")

    for u in all_units:
        try:
            process_unit(u["id"], u, model)
        except Exception as e:
            print(f"❌ {u['id']}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
