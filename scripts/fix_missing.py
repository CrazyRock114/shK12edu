#!/usr/bin/env python3
"""修缺失:starter 字母/数字/国家 + unit4 lake/water vapour + words_to_use phrases"""
import json
import re
import subprocess
import os
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
FFMPEG = Path.home() / ".local" / "bin" / "ffmpeg"
os.environ["PATH"] = str(FFMPEG.parent) + ":" + os.environ.get("PATH", "")


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
    return r.returncode == 0


def process(unit_id, audio_file, items, out_dir):
    src = ROOT / "raw" / "audio" / audio_file
    with open(ROOT / f"raw/transcripts/{unit_id}.json") as f:
        segments = json.load(f)["segments"]

    out_dir.mkdir(parents=True, exist_ok=True)
    saved = 0
    for item in items:
        text = item["text"]
        save_as = item["save_as"]
        seg = find_segment(segments, text)
        if not seg:
            print(f"   ⚠️  '{text}' 未找到")
            continue
        if isinstance(seg, dict):
            start, end = seg["start"], seg["end"]
        else:
            start, end = seg.start, seg.end
        dst = out_dir / save_as
        if slice_audio(src, start, end, dst):
            saved += 1
            print(f"   ✓ {save_as}  ({start:.1f}-{end:.1f}s)")
    print(f"   共 {saved}/{len(items)}")


# ===== Starter: 字母 + 数字 + 国家 =====
print("=== Starter ===")
starter_items = []
# 26 letters
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    starter_items.append({"text": c, "save_as": f"words/letter_{c.lower()}.mp3"})
# 20 numbers
for n, word in enumerate(["one","two","three","four","five","six","seven","eight","nine","ten",
                          "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"], 1):
    starter_items.append({"text": word, "save_as": f"words/number_{n:02d}_{word}.mp3"})
# 7 countries
for c in ["china", "italy", "uk", "usa", "france", "germany", "new zealand"]:
    starter_items.append({"text": c, "save_as": f"words/country_{c.replace(' ', '_')}.mp3"})

process("starter", "starter.mp3", starter_items, ROOT / "site/assets/audio/starter")

# ===== Unit 4: 补 lake / water vapour =====
print("\n=== Unit 4 ===")
unit4_items = [
    {"text": "lake", "save_as": "words/lake.mp3"},
    {"text": "water vapour", "save_as": "words/water_vapour.mp3", "fallback_time": (None, None)},
]
# 找 fallback 时间 - 从 segments 里找
with open(ROOT / "raw/transcripts/unit4.json") as f:
    u4segs = json.load(f)["segments"]

# 找包含 "lake" 或 "vapour" 的段
for seg in u4segs:
    txt = seg["text"].lower()
    if "lake" in txt and "lake" not in [x["text"] for x in unit4_items if "fallback_time" not in x]:
        unit4_items[0]["fallback_time"] = (seg["start"], seg["end"])
    if "vapour" in txt or "vapor" in txt:
        unit4_items[1]["fallback_time"] = (seg["start"], seg["end"])

# 如果没找到,用附近位置
if unit4_items[0].get("fallback_time") == (None, None):
    # 找 "river" 旁边的 "lake"
    for i, seg in enumerate(u4segs):
        if "river" in seg["text"].lower():
            unit4_items[0]["fallback_time"] = (seg["end"], seg["end"] + 1.5)
            break

if unit4_items[1].get("fallback_time") == (None, None):
    # 找 "cloud" 旁边的
    for i, seg in enumerate(u4segs):
        if "cloud" in seg["text"].lower():
            unit4_items[1]["fallback_time"] = (seg["start"] - 1.5, seg["start"])
            break

process("unit4", "unit_4.mp3", unit4_items, ROOT / "site/assets/audio/unit4")

# ===== Words to use: 加关键 phrases (从 units.json 读) =====
print("\n=== Words to use ===")
wtu_items = []
# 从 raw/text/all_pages.txt 找 phrases
text_file = ROOT / "raw/text/all_pages.txt"
if text_file.exists():
    text = text_file.read_text()
    # 找 p.87 区域的句子
    # 实际上 words_to_use 是全册词汇朗读
    # 简单方法:切 4-5 段(每 2 分钟一段)作为复习
    with open(ROOT / "raw/transcripts/words_to_use.json") as f:
        wtu_segs = json.load(f)["segments"]
    # 找一些标志性词作为短语切分点
    for marker in ["school", "classmate", "teacher", "garden", "water", "study", "happy", "driver", "library", "celebrate", "food", "noodles"]:
        seg = find_segment(wtu_segs, marker)
        if seg:
            if isinstance(seg, dict):
                start, end = seg["start"], seg["end"]
            else:
                start, end = seg.start, seg.end
            wtu_items.append({"text": marker, "save_as": f"phrases/{marker.replace(' ', '_')}_vocab.mp3"})

process("words_to_use", "words_to_use.mp3", wtu_items, ROOT / "site/assets/audio/words_to_use")
