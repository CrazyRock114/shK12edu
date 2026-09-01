#!/usr/bin/env python3
"""
按 G3A 标准切分 G5A 音频 - v2 (用 section marker 词分段)
- 找 whisper 转写里的 "Topic words" / "Fun time" / "Talking time" / "Story time" / "Sound" 等标记
- 标记点为 section 边界
- 每个 section 切 [marker_start, next_marker_start]
- 同时切 Topic words 单个 word 切片
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
FFMPEG = Path.home() / ".local" / "bin" / "ffmpeg"
UNITS_JSON = ROOT / "raw" / "structure" / "units.json"
WHISPER_DIR = ROOT / "raw" / "whisper_g5"
AUDIO_DIR = ROOT / "raw" / "audio"
OUT_DIR = ROOT / "raw" / "audio" / "G5A_配套音频"

UNIT_NUM = {
    "starter": "01 Starter",
    "unit1": "02 Unit 1", "unit2": "03 Unit 2", "unit3": "04 Unit 3",
    "unit4": "05 Unit 4", "unit5": "06 Unit 5", "unit6": "07 Unit 6",
    "unit7": "08 Unit 7", "unit8": "09 Unit 8", "unit9": "10 Unit 9",
    "unit10": "11 Unit 10",
}

# Section marker 词(whisper 转写里识别出来的格式)
SECTION_MARKERS = {
    "topic_words": ["topic words"],
    "fun_time": ["fun time"],
    "song_time": ["song time"],
    "rhyme_time": ["rhyme time"],
    "talking_time": ["talking time"],
    "sound": ["sound family", "sound"],  # 避开 "Sound" 在其他地方的出现
    "story_time": ["story time"],
    "reading_time": ["reading time"],
    "project": ["project"],
    "big_task": ["big task"],
}


def load_units():
    with open(UNITS_JSON, encoding="utf-8") as f:
        return json.load(f)


def load_whisper(name: str):
    candidates = [f"{name}.json"]
    if name.startswith("unit_"):
        candidates.append(f"{name.replace('unit_', 'unit')}.json")
    elif name.startswith("unit") and name[4:].isdigit():
        candidates.append(f"unit_{name[4:]}.json")
    for c in candidates:
        p = WHISPER_DIR / c
        if p.exists():
            with open(p, encoding="utf-8") as f:
                return json.load(f)
    return None


def get_audio_path(uid: str) -> Path:
    if uid == "starter":
        return AUDIO_DIR / "starter.mp3"
    if uid.startswith("unit"):
        n = uid[4:]
        return AUDIO_DIR / f"unit_{n}.mp3"
    return AUDIO_DIR / f"{uid}.mp3"


def find_section_boundaries(whisper_data):
    """
    在 whisper segments 里找每个 section marker 的位置
    返回: list of (start_time, end_time, section_type)
    按时间顺序,无重叠
    """
    if not whisper_data:
        return []
    segs = whisper_data.get("segments", [])
    if not segs:
        return []

    # 收集所有 marker hits
    hits = []  # (time, idx, type)
    for i, s in enumerate(segs):
        text = s.get("text", "").lower()
        for stype, keywords in SECTION_MARKERS.items():
            for kw in keywords:
                # 用 word boundary 匹配(避免 "sound" 匹配到 "sound" 在 "sound of" 等)
                pattern = r"\b" + re.escape(kw) + r"\b"
                if re.search(pattern, text):
                    hits.append((s["start"], s["end"], stype, i, s.get("text", "")))
                    break

    if not hits:
        return []

    # 按时间排序
    hits.sort()

    # 优先选择第一个出现,后续重复 marker 跳过
    # 关键规则: 同一 type 只保留第一个出现,且只保留一次
    # 但 Sound 比较特殊(sound family 算一个,sound 也算一个)
    # 简化:对每种 type 只保留第一个 hit
    seen = set()
    boundaries = []
    for start, end, stype, idx, text in hits:
        if stype in seen:
            continue
        seen.add(stype)
        boundaries.append((start, end, stype, idx, text))
    boundaries.sort()

    # 构造 [start, end] 范围
    result = []
    audio_end = segs[-1]["end"]
    for i, (s, e, stype, idx, text) in enumerate(boundaries):
        if i + 1 < len(boundaries):
            next_start = boundaries[i + 1][0]
            section_end = next_start
        else:
            section_end = audio_end
        result.append((s, section_end, stype, text))
    return result


def slice_audio(src: Path, start: float, end: float, dst: Path, padding=0.2):
    s = max(0, start - padding)
    dur = (end - start) + 2 * padding
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(FFMPEG), "-y", "-loglevel", "error",
        "-i", str(src), "-ss", f"{s:.3f}", "-t", f"{dur:.3f}",
        "-af", "afade=t=in:st=0:d=0.05,afade=t=out:st={:.3f}:d=0.1".format(max(0, dur - 0.1)),
        "-ar", "22050", "-ac", "1", "-b:a", "96k",
        str(dst),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0, r.stderr[:200] if r.returncode else ""


def fmt_time(t):
    m, s = divmod(int(t), 60)
    return f"{m}:{s:02d}"


def main():
    if not FFMPEG.exists():
        print(f"❌ ffmpeg 不存在: {FFMPEG}")
        sys.exit(1)

    data = load_units()
    print(f"📁 输出: {OUT_DIR}\n")

    # 清空旧输出
    if OUT_DIR.exists():
        import shutil
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    summary = []

    for unit in data["units"]:
        uid = unit["id"]
        uname = unit["name"]
        folder = UNIT_NUM.get(uid)
        if not folder:
            continue

        audio_src = get_audio_path(uid)
        if not audio_src.exists():
            print(f"⚠️  {uid}: 缺音频")
            continue

        # whisper 文件名约定
        whisper_name = "starter" if uid == "starter" else uid
        whisper = load_whisper(whisper_name)
        if not whisper:
            print(f"⚠️  {uid}: 缺 whisper")
            continue

        unit_out = OUT_DIR / folder
        unit_out.mkdir(parents=True, exist_ok=True)
        print(f"\n=== {folder} ===")

        # Starter 特殊处理:用关键词切
        if uid == "starter":
            boundaries = []
            segs = whisper.get("segments", [])
            text_starts = []
            for i, s in enumerate(segs):
                t = s.get("text", "").lower()
                for kw, label in [
                    ("at school", "At school"),
                    ("study skills", "Study skills"),
                    ("numbers", "Numbers"),
                    ("months", "Months"),
                ]:
                    if kw in t and not any(b[2] == label for b in boundaries):
                        boundaries.append((s["start"], s["end"], label, s.get("text", "")))
                        break
            boundaries.sort()
            # 加末尾
            audio_end = segs[-1]["end"] if segs else 0
            ranges = []
            for i, (s, e, stype, text) in enumerate(boundaries):
                if i + 1 < len(boundaries):
                    end = boundaries[i + 1][0]
                else:
                    end = audio_end
                ranges.append((s, end, stype, text))
            boundaries = ranges
        else:
            boundaries = find_section_boundaries(whisper)

        if not boundaries:
            print("   ⚠️  没找到 section marker")
            continue

        saved = 0
        for s, e, stype, text in boundaries:
            dur = e - s
            if dur < 3:
                # 太短(< 3s)跳过
                continue
            label = stype.replace("_", " ").title()
            dst = unit_out / f"{uname}-{label}.mp3"
            ok, err = slice_audio(audio_src, s, e, dst)
            if ok:
                size = dst.stat().st_size
                print(f"   ✓ {dst.name:42} ({fmt_time(s)}-{fmt_time(e)}, {dur:.0f}s, {size/1024:.0f} KB)")
                saved += 1
            else:
                print(f"   ✗ {dst.name}: {err[:80]}")

        # 额外:整段复制一份作为 fallback
        full_dst = unit_out / f"{uname} 完整版.mp3"
        import shutil
        shutil.copy2(audio_src, full_dst)
        print(f"   ✓ {full_dst.name:42} (full, {(full_dst.stat().st_size)/1024/1024:.1f} MB)")

        summary.append((folder, saved, len(boundaries)))

    print(f"\n{'='*60}")
    print("📊 切分汇总:")
    for folder, ok, total in summary:
        print(f"   {folder:20}  {ok} sections (含完整版)")
    print(f"\n📁 输出目录: {OUT_DIR}")


if __name__ == "__main__":
    main()
