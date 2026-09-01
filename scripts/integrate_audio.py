#!/usr/bin/env python3
"""
整合老师提供的两套音频到 site/assets/audio/
- 主教材 (section 切分) -> site/assets/audio/{unit_id}/sections/
- 练习部分 -> site/assets/audio/{unit_id}/practice/
"""
import json
import shutil
import re
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
MAIN_DIR = ROOT / "raw/audio/《义务教育教科书（五・四学制）英语（三年级上册）》配套音频"
PRAC_DIR = ROOT / "raw/audio/《义务教育教科书（五・四学制）英语练习部分（三年级上册）》配套音频"


# unit_id 映射: 目录名 -> unit_id
MAIN_DIR_TO_UNIT = {
    "01 Starter": "starter",
    "02 Unit 1": "unit1",
    "03 Unit 2": "unit2",
    "04 Unit 3": "unit3",
    "05 Unit 4": "unit4",
    "06 Unit 5": "unit5",
    "07 Unit 6": "unit6",
    "08 Unit 7": "unit7",
    "09 Unit 8": "unit8",
    "10 Unit 9": "unit9",
    "11 Unit 10": "unit10",
    "12 Words to use": "words_to_use",
}

# 练习部分 unit id 提取规则
def parse_prac_filename(fname: str) -> tuple[str, str]:
    """'01 Unit 1 Topic words.mp3' -> ('unit1', 'topic_words')"""
    m = re.match(r"\d+\s+Unit\s+(\d+|1[0-9])\s+(.+)\.mp3", fname, re.IGNORECASE)
    if not m:
        return None, None
    num = m.group(1)
    section = m.group(2).lower().replace(" ", "_")
    if num == "1":
        return "unit1", section
    elif num == "2":
        return "unit2", section
    elif num == "3":
        return "unit3", section
    elif num == "4":
        return "unit4", section
    elif num == "5":
        return "unit5", section
    elif num == "6":
        return "unit6", section
    elif num == "7":
        return "unit7", section
    elif num == "8":
        return "unit8", section
    elif num == "9":
        return "unit9", section
    elif num == "10":
        return "unit10", section
    return None, None


def parse_main_filename(fname: str) -> tuple[str, str]:
    """'06 Unit 1-Topic words.mp3' -> ('unit1', 'topic_words')"""
    # 数字 + Unit + num + - + section
    m = re.match(r"\d+\s+Unit\s+(\d+|1[0-9])-?(.+)\.mp3", fname, re.IGNORECASE)
    if not m:
        return None, None
    num = m.group(1)
    section = m.group(2).strip().lower().replace(" ", "_")
    section = re.sub(r"[^a-z0-9_]", "", section)
    # 移除 "完整版" 标记
    if "完整版" in fname:
        return f"unit{num}" if num != "1" else "unit1", "full"
    # 移除中文括号
    if not num.isdigit():
        return None, None
    if int(num) < 1 or int(num) > 10:
        return None, None
    return f"unit{num}", section


def safe_filename(s: str) -> str:
    return re.sub(r"[^a-z0-9_]", "", s.lower().replace(" ", "_"))


def main():
    print("=" * 60)
    print("整合主教材音频")
    print("=" * 60)
    total_main = 0
    if MAIN_DIR.exists():
        for d in MAIN_DIR.iterdir():
            if not d.is_dir():
                continue
            unit_id = MAIN_DIR_TO_UNIT.get(d.name)
            if not unit_id:
                print(f"⚠️  跳过未知目录: {d.name}")
                continue
            target_dir = ROOT / f"site/assets/audio/{unit_id}/sections"
            target_dir.mkdir(parents=True, exist_ok=True)
            count = 0
            for mp3 in sorted(d.glob("*.mp3")):
                # 解析 section 名
                if "完整版" in mp3.name:
                    section = "full"
                else:
                    # "06 Unit 1-Topic words.mp3" -> "topic_words"
                    parts = mp3.stem.split("-", 1)
                    section = safe_filename(parts[1] if len(parts) > 1 else parts[0])
                dst = target_dir / f"{section}.mp3"
                shutil.copy2(mp3, dst)
                count += 1
                total_main += 1
            print(f"  ✓ {unit_id}: {count} sections -> {target_dir.name}/")
    print(f"\n主教材共 {total_main} 个音频")

    print()
    print("=" * 60)
    print("整合练习部分音频")
    print("=" * 60)
    total_prac = 0
    if PRAC_DIR.exists():
        for mp3 in sorted(PRAC_DIR.glob("*.mp3")):
            unit_id, section = parse_prac_filename(mp3.name)
            if not unit_id:
                print(f"⚠️  无法解析: {mp3.name}")
                continue
            section = safe_filename(section)
            target_dir = ROOT / f"site/assets/audio/{unit_id}/practice"
            target_dir.mkdir(parents=True, exist_ok=True)
            dst = target_dir / f"{section}.mp3"
            shutil.copy2(mp3, dst)
            total_prac += 1
        print(f"\n练习部分共 {total_prac} 个音频")

    # 更新 units_data.json
    print()
    print("=" * 60)
    print("更新 units_data.json")
    print("=" * 60)
    units_data_path = ROOT / "site/units_data.json"
    with open(units_data_path) as f:
        data = json.load(f)
    for u in data["units"]:
        uid = u["id"]
        sections_dir = ROOT / f"site/assets/audio/{uid}/sections"
        practice_dir = ROOT / f"site/assets/audio/{uid}/practice"
        u["sections_audio"] = sorted([f.stem for f in sections_dir.glob("*.mp3")]) if sections_dir.exists() else []
        u["practice_audio"] = sorted([f.stem for f in practice_dir.glob("*.mp3")]) if practice_dir.exists() else []
    with open(units_data_path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ {units_data_path} 已更新")


if __name__ == "__main__":
    main()
