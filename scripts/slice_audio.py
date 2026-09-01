#!/usr/bin/env python3
"""
用 Whisper 转写结果按时间戳把 unit 音频切分为单词/短句
"""
import json
import subprocess
import re
import os
import sys
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
FFMPEG = Path.home() / ".local" / "bin" / "ffmpeg"

# 配置:unit_id -> (audio_file, 单词/短语列表)
# 每个 item 是 dict {text_normalized, time_range_text, save_as}
UNITS = {
    "unit1": {
        "audio": "site/assets/audio/unit_1.mp3",
        "whisper_json": "/tmp/whisper_unit1.json",
        "items": [
            # 8 个 topic words
            {"text": "school", "save_as": "words/school.mp3"},
            {"text": "classmate", "save_as": "words/classmate.mp3"},
            {"text": "teacher", "save_as": "words/teacher.mp3"},
            {"text": "play sports", "save_as": "words/play_sports.mp3"},
            {"text": "read", "save_as": "words/read.mp3"},
            {"text": "book", "save_as": "words/book.mp3"},
            {"text": "study", "save_as": "words/study.mp3"},
            {"text": "friend", "save_as": "words/friend.mp3"},
            # 4 个关键短语
            {"text": "i want to make some new friends", "save_as": "phrases/i_want_to_make_new_friends.mp3"},
            {"text": "i want to speak english well", "save_as": "phrases/i_want_to_speak_english_well.mp3"},
            {"text": "what's your goal", "save_as": "phrases/whats_your_goal.mp3"},
            {"text": "i want to study", "save_as": "phrases/i_want_to_study.mp3", "fallback_time": (70.0, 74.5)},
        ],
    },
}


def normalize(text):
    """归一化文本,用于匹配"""
    return re.sub(r"[^\w\s]", "", text.lower()).strip()


def find_segment(segments, target_text, fallback_time=None):
    """在 segments 中找包含 target_text 的 segment,支持 fallback 时间区间"""
    target_norm = normalize(target_text)
    # 优先精确匹配(整段)
    for seg in segments:
        if normalize(seg["text"]) == target_norm:
            return seg
    # 部分匹配:找包含 target_norm 所有词的 segment
    target_words = set(target_norm.split())
    for seg in segments:
        seg_norm = normalize(seg["text"])
        seg_words = set(seg_norm.split())
        if target_words.issubset(seg_words):
            return seg
    # Fallback 到指定时间区间
    if fallback_time:
        class FakeSeg:
            def __init__(self, s, e):
                self.start, self.end = s, e
                self.text = target_text
        return FakeSeg(*fallback_time)
    return None


def slice_audio(src, start, end, dst, padding=0.15):
    """用 ffmpeg 切音频[start-padding, end+padding]"""
    start_pad = max(0, start - padding)
    end_pad = end + padding
    duration = end_pad - start_pad
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(FFMPEG),
        "-y", "-loglevel", "error",
        "-i", str(src),
        "-ss", f"{start_pad:.3f}",
        "-t", f"{duration:.3f}",
        "-af", f"afade=t=in:st=0:d=0.05,afade=t=out:st={duration-0.1:.3f}:d=0.05",
        "-ar", "22050",  # 降采样省空间
        "-ac", "1",  # mono
        "-b:a", "64k",  # 64kbps(单词/短语够用)
        str(dst),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"   ❌ {dst.name}: ffmpeg error: {result.stderr[:200]}")
        return False
    return True


def process_unit(unit_id, config):
    src = ROOT / config["audio"]
    json_path = Path(config["whisper_json"])

    if not json_path.exists():
        print(f"⚠️  {unit_id}: 未找到 {json_path},跳过")
        return

    with open(json_path) as f:
        whisper_data = json.load(f)
    segments = whisper_data.get("segments", [])

    print(f"\n=== {unit_id} ===")
    out_dir = ROOT / "site" / "assets" / "audio"
    saved = 0
    for item in config["items"]:
        target_text = item["text"]
        save_as = item["save_as"]
        fallback = item.get("fallback_time")
        seg = find_segment(segments, target_text, fallback_time=fallback)
        if not seg:
            print(f"   ❌ '{target_text}' 未找到 segment")
            continue
        # FakeSeg 是类实例(用属性),真实 seg 是 dict(用 key)
        if isinstance(seg, dict):
            start, end = seg["start"], seg["end"]
        else:
            start, end = seg.start, seg.end
        dst = out_dir / save_as
        if slice_audio(src, start, end, dst):
            size = dst.stat().st_size
            print(f"   ✓ {save_as}  ({start:.1f}-{end:.1f}s, {size/1024:.1f} KB)")
            saved += 1
    print(f"   共保存 {saved}/{len(config['items'])} 个文件")


def main():
    if not FFMPEG.exists():
        print(f"❌ ffmpeg 不存在: {FFMPEG}")
        sys.exit(1)

    for unit_id, config in UNITS.items():
        process_unit(unit_id, config)


if __name__ == "__main__":
    main()
