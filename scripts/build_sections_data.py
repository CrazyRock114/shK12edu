#!/usr/bin/env python3
"""
从 units.json + audio 目录 生成 sections_data.js
每单元按 PDF 物理页切分 sections，每段含 {id, name, icon, pages[], audio, words[]}
"""
import json
import os
import re
import sys
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from words_extra import enrich_topic_words

# 加载 G3A starter 教材图 OCR 坐标 (用于图片高亮)
import json as _json
G3A_OCR = {}
_OCR_PATH = Path('/Users/paulshi/Documents/MiniMax/shK12edu/site/eng-g3a/assets/img/_ocr_coords.json')
if _OCR_PATH.exists():
    with open(_OCR_PATH) as f:
        G3A_OCR = _json.load(f)
IMG_W, IMG_H = 1544, 2168  # 教材图原始分辨率

def get_ocr_for_section(sec_id, page):
    if not G3A_OCR: return {}
    page_key = str(page)
    if page_key not in G3A_OCR: return {}
    items = {}
    for w in G3A_OCR[page_key]:
        key = w['text'].lower()
        items.setdefault(key, []).append(w)
    return items

def find_phrase_bbox(ocr_index, phrase, img_w=IMG_W, img_h=IMG_H):
    """在 OCR 索引中找短语 bbox，支持空格/拆分词合并。
    策略:
    1. 完全匹配 (lowercase) - 用 cy 最接近中央的
    2. split 后按 token 顺序找 cy 相邻 (< 80px) 且 cx 紧邻的 bbox 合并
    返回 { bbox: [[x1,y1],[x2,y2],[x3,y3],[x4,y4]], cy, img_w, img_h } 或 None
    """
    p = phrase.lower()
    if p in ocr_index and ocr_index[p]:
        best = min(ocr_index[p], key=lambda m: abs(m['cy'] - img_h/2))
        return {'bbox': best['bbox'], 'cy': best['cy'], 'img_w': img_w, 'img_h': img_h}
    # 拆分匹配: "Ms Yu" → ["Ms", "Yu"]
    tokens = p.split()
    if len(tokens) < 2:
        return None
    # 对每 token 找 cy 最接近 img_h/2 的命中
    hits = []
    for tok in tokens:
        cands = ocr_index.get(tok, [])
        if not cands:
            return None
        best = min(cands, key=lambda m: abs(m['cy'] - img_h/2))
        hits.append(best)
    # 检查 cy 都在相近的 80px 内
    cys = [h['cy'] for h in hits]
    if max(cys) - min(cys) > 80:
        return None
    # 合并 bbox
    all_pts = []
    for h in hits:
        for pt in h['bbox']:
            all_pts.append(pt)
    xs = [p[0] for p in all_pts]
    ys = [p[1] for p in all_pts]
    merged = [[min(xs), min(ys)], [max(xs), min(ys)], [max(xs), max(ys)], [min(xs), max(ys)]]
    return {'bbox': merged, 'cy': sum(cys)/len(cys), 'img_w': img_w, 'img_h': img_h}

ROOT = Path('/Users/paulshi/Documents/MiniMax/shK12edu')

# section 默认 icon 映射
ICON = {
    'families_and_friends': '👨‍👩‍👧‍👦',
    'our_teachers': '👩‍🏫',
    'at_school': '🏫',
    'study_skills': '📖',
    'alphabet': '🔤',
    'seasons': '🌤',
    'numbers': '🔢',
    'months': '📅',
    'countries': '🌍',
    'topic_words': '📚',
    'sound': '🗣',
    'song_time': '🎵',
    'rhyme_time': '🎶',
    'chant_time': '🗣',
    'fun_time': '🎮',
    'talking_time': '💬',
    'story_time': '📖',
    'reading_time': '📚',
    'big_task': '🎯',
}

NAME_ZH = {
    'families_and_friends': '我们的家人与朋友',
    'our_teachers': '我们的老师',
    'at_school': '在学校',
    'study_skills': '学习技巧',
    'alphabet': '字母表',
    'seasons': '季节',
    'numbers': '数字',
    'months': '月份',
    'countries': '国家',
    'topic_words': '主题词',
    'sound': '发音',
    'song_time': '歌曲',
    'rhyme_time': '韵文',
    'chant_time': 'chant 跟读',
    'fun_time': '趣味活动',
    'talking_time': '对话',
    'story_time': '故事',
    'reading_time': '阅读',
    'big_task': '大任务',
}


def get_audio_file(unit_id, section_id, materials_audio_dir, site_audio_dir):
    """从 materials 找音频，返回 site 端相对路径"""
    if unit_id == 'starter':
        # G3A starter 整段, G5A starter 分段
        m = list(materials_audio_dir.glob('starter*/Starter*.mp3'))
        if m and section_id in ['at_school', 'study_skills', 'numbers', 'months']:
            # G5A 风格: Starter-{Section}.mp3
            audio_name = f'Starter-{NAME_ZH.get(section_id, section_id)}.mp3'
            if (materials_audio_dir / '01 Starter' / audio_name).exists():
                return f'starter/sections/{section_id}.mp3'
        return 'starter.mp3'

    # unit1-10
    folder_names = {
        'unit1': '02 Unit 1', 'unit2': '03 Unit 2', 'unit3': '04 Unit 3',
        'unit4': '05 Unit 4', 'unit5': '06 Unit 5', 'unit6': '07 Unit 6',
        'unit7': '08 Unit 7', 'unit8': '09 Unit 8', 'unit9': '10 Unit 9',
        'unit10': '11 Unit 10',
    }
    folder = folder_names.get(unit_id)
    if not folder:
        return None
    # 检查 site 端 sections 目录
    site_sections = site_audio_dir / f'unit{unit_id[4:]}' / 'sections'
    if (site_sections / f'{section_id}.mp3').exists():
        return f'unit{unit_id[4:]}/sections/{section_id}.mp3'
    return None


# 各 section 类型的元数据提取器
def get_sound_meta(u):
    s = u.get('sound', {}) or {}
    return {
        'sound_letter': s.get('letter', ''),
        'sound_pattern': s.get('pattern', ''),
        'sound_example': s.get('example', ''),
    }

def get_song_meta(u):
    s = u.get('song_time', {}) or {}
    return {'song_title': s.get('title', ''), 'song_lyrics': s.get('lyrics', [])}

def get_chant_meta(u):
    s = u.get('chant_time', {}) or {}
    return {'chant_title': s.get('title', ''), 'chant_lyrics': s.get('lyrics', [])}

def get_rhyme_meta(u):
    s = u.get('rhyme_time', {}) or {}
    return {'rhyme_title': s.get('title', ''), 'rhyme_lyrics': s.get('lyrics', [])}

def get_fun_meta(u):
    s = u.get('fun_time', {}) or {}
    return {'fun_title': s.get('title', ''), 'fun_content': s.get('content', '')}

def get_talking_meta(u):
    s = u.get('talking_time', {}) or {}
    return {
        'talking_title': s.get('title', ''),
        'talking_pattern': s.get('pattern', ''),
        'talking_phrases': s.get('key_phrases', []),
        'talking_scenario': s.get('scenario', ''),
    }

def get_story_meta(u):
    s = u.get('story_time', {}) or {}
    return {
        'story_title': s.get('title', ''),
        'story_summary': s.get('summary', ''),
        'story_moral': s.get('moral', ''),
    }

def get_reading_meta(u):
    s = u.get('reading_time', {}) or {}
    return {
        'reading_title': s.get('title', ''),
        'reading_content': s.get('content', ''),
    }

def get_big_task_meta(u):
    s = u.get('project', {}) or {}
    return {
        'project_title': s.get('title', ''),
        'project_output': s.get('output', ''),
    }

SECTION_META = {
    'sound': get_sound_meta,
    'song_time': get_song_meta,
    'chant_time': get_chant_meta,
    'rhyme_time': get_rhyme_meta,
    'fun_time': get_fun_meta,
    'talking_time': get_talking_meta,
    'story_time': get_story_meta,
    'reading_time': get_reading_meta,
    'big_task': get_big_task_meta,
}


def get_words_for_section(unit_id, section_id, units_json):
    """从 units.json 提取 section 关联的 words"""
    units = units_json.get('units', units_json) if isinstance(units_json, dict) else units_json
    for u in units:
        if u.get('id') == unit_id:
            if section_id == 'topic_words':
                return u.get('topic_words', [])
    return []


# G3A / G5A section 切分规则（按 PDF 编排 + audio 实际命名）
# 每单元：[(section_id, [pages], audio_path_override or None), ...]
G3A_SECTIONS = {
    'starter': [
        # families_and_friends + our_teachers: 链式合成 .m4a (starter.mp3 不含这两段内容)
        ('families_and_friends', [9], 'starter/sections/families_chain.m4a'),
        ('our_teachers', [10], 'starter/sections/teachers_chain.m4a'),
        # alphabet/seasons/numbers/countries 有分段 mp3 (来自配套音频)
        ('alphabet', [11], 'starter/sections/the_alphabet.mp3'),
        ('seasons', [12], 'starter/sections/seasons.mp3'),
        ('numbers', [12], 'starter/sections/numbers.mp3'),
        ('countries', [13], 'starter/sections/countries.mp3'),
    ],
    'unit1': [  # PDF p14-21
        ('topic_words', [15], 'unit1/sections/topic_words.mp3'),
        ('song_time', [16], 'unit1/sections/song_time.mp3'),
        ('sound', [16], 'unit1/sections/sound.mp3'),
        ('talking_time', [17, 18], 'unit1/sections/talking_time.mp3'),
        ('story_time', [19, 20], 'unit1/sections/story_time.mp3'),
        ('big_task', [21], 'unit1/sections/big_task.mp3'),
    ],
    'unit2': [  # p22-29
        ('topic_words', [23], 'unit2/sections/topic_words.mp3'),
        ('fun_time', [24], 'unit2/sections/fun_time.mp3'),
        ('sound', [24], 'unit2/sections/sound.mp3'),
        ('talking_time', [25, 26], 'unit2/sections/talking_time.mp3'),
        ('story_time', [27, 28], 'unit2/sections/story_time.mp3'),
        ('big_task', [29], 'unit2/sections/big_task.mp3'),
    ],
    'unit3': [  # p30-37
        ('topic_words', [31], 'unit3/sections/topic_words.mp3'),
        ('fun_time', [32], 'unit3/sections/fun_time.mp3'),
        ('sound', [32], 'unit3/sections/sound.mp3'),
        ('talking_time', [33, 34], 'unit3/sections/talking_time.mp3'),
        ('story_time', [35, 36], 'unit3/sections/story_time.mp3'),
        ('big_task', [37], 'unit3/sections/big_task.mp3'),
    ],
    'unit4': [  # p38-45
        ('topic_words', [39], 'unit4/sections/topic_words.mp3'),
        ('rhyme_time', [40], 'unit4/sections/rhyme_time.mp3'),
        ('sound', [40], 'unit4/sections/sound.mp3'),
        ('talking_time', [41, 42], 'unit4/sections/talking_time.mp3'),
        ('reading_time', [43, 44], 'unit4/sections/reading_time.mp3'),
        ('big_task', [45], 'unit4/sections/big_task.mp3'),
    ],
    'unit5': [  # p46-53
        ('topic_words', [47], 'unit5/sections/topic_words.mp3'),
        ('song_time', [48], 'unit5/sections/song_time.mp3'),
        ('sound', [48], 'unit5/sections/sound.mp3'),
        ('talking_time', [49, 50], 'unit5/sections/talking_time.mp3'),
        ('story_time', [51, 52], 'unit5/sections/story_time.mp3'),
        ('big_task', [53], 'unit5/sections/big_task.mp3'),
    ],
    'unit6': [  # p54-61
        ('topic_words', [55], 'unit6/sections/topic_words.mp3'),
        ('fun_time', [56], 'unit6/sections/fun_time.mp3'),
        ('sound', [56], 'unit6/sections/sound.mp3'),
        ('talking_time', [57, 58], 'unit6/sections/talking_time.mp3'),
        ('story_time', [59, 60], 'unit6/sections/story_time.mp3'),
        ('big_task', [61], 'unit6/sections/big_task.mp3'),
    ],
    'unit7': [  # p62-69
        ('topic_words', [63], 'unit7/sections/topic_words.mp3'),
        ('song_time', [64], 'unit7/sections/song_time.mp3'),
        ('sound', [64], 'unit7/sections/sound.mp3'),
        ('talking_time', [65, 66], 'unit7/sections/talking_time.mp3'),
        ('reading_time', [67, 68], 'unit7/sections/reading_time.mp3'),
        ('big_task', [69], 'unit7/sections/big_task.mp3'),
    ],
    'unit8': [  # p70-77
        ('topic_words', [71], 'unit8/sections/topic_words.mp3'),
        ('fun_time', [72], 'unit8/sections/fun_time.mp3'),
        ('sound', [72], 'unit8/sections/sound.mp3'),
        ('talking_time', [73, 74], 'unit8/sections/talking_time.mp3'),
        ('story_time', [75, 76], 'unit8/sections/story_time.mp3'),
        ('big_task', [77], 'unit8/sections/big_task.mp3'),
    ],
    'unit9': [  # p78-85
        ('topic_words', [79], 'unit9/sections/topic_words.mp3'),
        ('fun_time', [80], 'unit9/sections/fun_time.mp3'),
        ('sound', [80], 'unit9/sections/sound.mp3'),
        ('talking_time', [81, 82], 'unit9/sections/talking_time.mp3'),
        ('reading_time', [83, 84], 'unit9/sections/reading_time.mp3'),
        ('big_task', [85], 'unit9/sections/big_task.mp3'),
    ],
    'unit10': [  # p86-93
        ('topic_words', [87], 'unit10/sections/topic_words.mp3'),
        ('chant_time', [88], 'unit10/sections/chant_time.mp3'),
        ('sound', [88], 'unit10/sections/sound.mp3'),
        ('talking_time', [89, 90], 'unit10/sections/talking_time.mp3'),
        ('story_time', [91, 92], 'unit10/sections/story_time.mp3'),
        ('big_task', [93], 'unit10/sections/big_task.mp3'),
    ],
}

G5A_SECTIONS = {
    'starter': [  # p9-15
        ('families_and_friends', [9], None),  # 整段 starter.mp3
        ('our_teachers', [10], None),
        ('at_school', [11, 12], 'starter/sections/at_school.mp3'),
        ('study_skills', [13, 14], 'starter/sections/study_skills.mp3'),
        ('numbers', [15], 'starter/sections/numbers.mp3'),
        ('months', [15], 'starter/sections/months.mp3'),
    ],
    'unit1': [  # Clubs in our school p16-23
        ('topic_words', [17], 'unit1/sections/topic_words.mp3'),
        ('fun_time', [18], 'unit1/sections/fun_time.mp3'),
        ('sound', [19], 'unit1/sections/sound.mp3'),
        ('talking_time', [20, 21], 'unit1/sections/talking_time.mp3'),
        ('story_time', [22], 'unit1/sections/story_time.mp3'),
        ('big_task', [23], 'unit1/sections/big_task.mp3'),
    ],
    'unit2': [  # Traditional games p24-31
        ('topic_words', [25], 'unit2/sections/topic_words.mp3'),
        ('fun_time', [26], 'unit2/sections/fun_time.mp3'),
        ('sound', [27], 'unit2/sections/sound.mp3'),
        ('talking_time', [28, 29], 'unit2/sections/talking_time.mp3'),
        ('story_time', [30], 'unit2/sections/story_time.mp3'),
        ('big_task', [31], 'unit2/sections/big_task.mp3'),
    ],
    'unit3': [  # Amazing plants p32-39
        ('topic_words', [33], 'unit3/sections/topic_words.mp3'),
        ('chant_time', [34], 'unit3/sections/chant_time.mp3'),  # G5A unit3 是 chant
        ('sound', [34], 'unit3/sections/sound.mp3'),
        ('talking_time', [35, 36], 'unit3/sections/talking_time.mp3'),
        ('reading_time', [37, 38], 'unit3/sections/reading_time.mp3'),
        ('big_task', [39], 'unit3/sections/big_task.mp3'),
    ],
    'unit4': [  # Together with animals p40-47
        ('topic_words', [41], 'unit4/sections/topic_words.mp3'),
        ('fun_time', [42], 'unit4/sections/fun_time.mp3'),
        ('sound', [42], 'unit4/sections/sound.mp3'),
        ('talking_time', [43, 44], 'unit4/sections/talking_time.mp3'),
        ('reading_time', [45, 46], 'unit4/sections/reading_time.mp3'),
        ('big_task', [47], 'unit4/sections/big_task.mp3'),
    ],
    'unit5': [  # Seeing a doctor p48-55
        ('topic_words', [49], 'unit5/sections/topic_words.mp3'),
        ('rhyme_time', [50], 'unit5/sections/rhyme_time.mp3'),
        ('sound', [51], 'unit5/sections/sound.mp3'),
        ('talking_time', [52, 53], 'unit5/sections/talking_time.mp3'),
        ('story_time', [54], 'unit5/sections/story_time.mp3'),
        ('big_task', [55], 'unit5/sections/big_task.mp3'),
    ],
    'unit6': [  # Try my best p56-63
        ('topic_words', [57], 'unit6/sections/topic_words.mp3'),
        ('fun_time', [58], 'unit6/sections/fun_time.mp3'),
        ('sound', [58], 'unit6/sections/sound.mp3'),
        ('talking_time', [59, 60], 'unit6/sections/talking_time.mp3'),
        ('story_time', [61, 62], 'unit6/sections/story_time.mp3'),
        ('big_task', [63], 'unit6/sections/big_task.mp3'),
    ],
    'unit7': [  # Great scientists p64-71
        ('topic_words', [65], 'unit7/sections/topic_words.mp3'),
        ('rhyme_time', [66], 'unit7/sections/rhyme_time.mp3'),
        ('sound', [66], 'unit7/sections/sound.mp3'),
        ('talking_time', [67, 68], 'unit7/sections/talking_time.mp3'),
        ('reading_time', [69, 70], 'unit7/sections/reading_time.mp3'),
        ('big_task', [71], 'unit7/sections/big_task.mp3'),
    ],
    'unit8': [  # Useful inventions p72-79
        ('topic_words', [73], 'unit8/sections/topic_words.mp3'),
        ('fun_time', [74], 'unit8/sections/fun_time.mp3'),
        ('sound', [74], 'unit8/sections/sound.mp3'),
        ('talking_time', [75, 76], 'unit8/sections/talking_time.mp3'),
        ('reading_time', [77, 78], 'unit8/sections/reading_time.mp3'),
        ('big_task', [79], 'unit8/sections/big_task.mp3'),
    ],
    'unit9': [  # Using computers p80-87
        ('topic_words', [81], 'unit9/sections/topic_words.mp3'),
        ('fun_time', [82], 'unit9/sections/fun_time.mp3'),
        ('sound', [82], 'unit9/sections/sound.mp3'),
        ('talking_time', [83, 84], 'unit9/sections/talking_time.mp3'),
        ('reading_time', [85, 86], 'unit9/sections/reading_time.mp3'),
        ('big_task', [87], 'unit9/sections/big_task.mp3'),
    ],
    'unit10': [  # A greener life p88-95
        ('topic_words', [89], 'unit10/sections/topic_words.mp3'),
        ('song_time', [90], 'unit10/sections/song_time.mp3'),
        ('sound', [90], 'unit10/sections/sound.mp3'),
        ('talking_time', [91, 92], 'unit10/sections/talking_time.mp3'),
        ('story_time', [93, 94], 'unit10/sections/story_time.mp3'),
        ('big_task', [95], 'unit10/sections/big_task.mp3'),
    ],
}


def build_sections_data(grade, sections_map, units_json_path, site_audio_dir, materials_audio_dir):
    """生成 sections_data.js 内容（自动检测 mp3 存在性，缺失段自动移除）"""
    units = json.load(open(units_json_path))
    units_list = units.get('units', units) if isinstance(units, dict) else units

    data = {}
    for u in units_list:
        uid = u['id']
        if uid not in sections_map:
            continue
        sections = []
        for sec_id, pages, audio_path in sections_map[uid]:
            # 自动检测 mp3 是否真实存在于 site 端
            is_fallback = False
            actual_audio = None
            if audio_path:
                full_path = site_audio_dir / audio_path
                if full_path.exists():
                    actual_audio = audio_path
                else:
                    # mp3 缺失 → 降级用整段 unit_N.mp3，标记 is_fallback
                    if uid == 'starter':
                        actual_audio = 'starter.mp3'
                    else:
                        actual_audio = f'unit_{uid[4:]}.mp3'
                    is_fallback = True
                    print(f'  ⚠️  {grade}.{uid}.{sec_id} 缺失 {audio_path}, 降级用 {actual_audio}')
            else:
                # 无分段 mp3 配置时用整段
                if uid == 'starter':
                    actual_audio = 'starter.mp3'
                else:
                    actual_audio = f'unit_{uid[4:]}.mp3'

            section = {
                'id': sec_id,
                'name': NAME_ZH.get(sec_id, sec_id),
                'icon': ICON.get(sec_id, '📘'),
                'pages': pages,
                'audio': actual_audio,
            }
            if is_fallback:
                section['is_fallback'] = True
            # 注入 units.json 元数据 (歌词/故事/句型/关键短语等)
            if sec_id in SECTION_META:
                section.update(SECTION_META[sec_id](u))
            # topic_words 段加 words 列表 (从 words_extra 升级 zh + extra)
            if sec_id == 'topic_words':
                raw_words = u.get('topic_words', [])
                section['words'] = enrich_topic_words(grade, uid, raw_words)
                section['big_task'] = u.get('big_task', '')

            # G3A starter 6 段加 words 列表 (带 extra 拓展)
            if grade == 'g3a' and uid == 'starter':
                if sec_id == 'families_and_friends':
                    section['words'] = [
                        {'en':'Dad', 'zh':'爸爸', 'extra':'👨 father'},
                        {'en':'Mum', 'zh':'妈妈', 'extra':'👩 mother'},
                        {'en':'Grandpa', 'zh':'爷爷/外公', 'extra':'👴 父亲的父亲'},
                        {'en':'Grandma', 'zh':'奶奶/外婆', 'extra':'👵 父亲的母亲'},
                        {'en':'family', 'zh':'家庭', 'extra':'👨‍👩‍👧‍👦 一家人'},
                        {'en':'friend', 'zh':'朋友', 'extra':'👫 buddy'},
                    ]
                elif sec_id == 'our_teachers':
                    section['words'] = [
                        {'en':'Ms Yu', 'zh':'余老师', 'extra':'👩‍🏫 女老师 (未婚)'},
                        {'en':'Miss Li', 'zh':'李老师', 'extra':'👩‍🏫 Miss = 未婚'},
                        {'en':'Mr Zhong', 'zh':'钟老师', 'extra':'👨‍🏫 男老师'},
                        {'en':'Mr Qian', 'zh':'钱老师', 'extra':'👨‍🏫 Mr = 男老师'},
                        {'en':'teacher', 'zh':'老师', 'extra':'👩‍🏫'},
                    ]
                elif sec_id == 'alphabet':
                    letter_data = [
                        ('A','Apple','🍎 /eɪ/'), ('B','Book','📚 /biː/'), ('C','Cat','🐱 /siː/'),
                        ('D','Dog','🐶 /diː/'), ('E','Egg','🥚 /iː/'), ('F','Fish','🐟 /ɛf/'),
                        ('G','Goose','🦢 /dʒiː/'), ('H','Hand','✋ /eɪtʃ/'), ('I','Ice cream','🍦 /aɪ/'),
                        ('J','Jam','🍓 /dʒeɪ/'), ('K','Kite','🪁 /keɪ/'), ('L','Lion','🦁 /ɛl/'),
                        ('M','Milk','🥛 /ɛm/'), ('N','Nose','👃 /ɛn/'), ('O','Orange','🍊 /oʊ/'),
                        ('P','Pen','🖊 /piː/'), ('Q','Queen','👸 /kjuː/'), ('R','Rain','🌧 /ɑːr/'),
                        ('S','Sun','☀️ /ɛs/'), ('T','Tree','🌳 /tiː/'), ('U','Umbrella','☂️ /juː/'),
                        ('V','Volcano','🌋 /viː/'), ('W','Whale','🐋 /dʌbljuː/'), ('X','X-ray','🩻 /ɛks/'),
                        ('Y','Yogurt','🥛 /waɪ/'), ('Z','Zebra','🦓 /ziː/'),
                    ]
                    section['words'] = [
                        {'en': f'{up}{lo}', 'zh': '', 'extra': f'{ex} · 例: {ex_word}'}
                        for up, ex_word, ex in letter_data
                        for lo in [up.lower()]
                    ]
                elif sec_id == 'seasons':
                    section['words'] = [
                        {'en':'spring','zh':'春','extra':'3-5月 · 花开 🌸'},
                        {'en':'summer','zh':'夏','extra':'6-8月 · 炎热 ☀️'},
                        {'en':'autumn','zh':'秋','extra':'9-11月 · 落叶 🍂'},
                        {'en':'winter','zh':'冬','extra':'12-2月 · 下雪 ❄️'},
                    ]
                elif sec_id == 'numbers':
                    cn = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十']
                    extras = ['1·一个','2·两个','3·三个','4·四季','5·五指','6·六角','7·一周','8·八爪','9·久','10·十全','11·11','12·月份','13·不吉利','14·情人节','15·15分','16·16岁','17·青春','18·成年','19·19','20·20/20']
                    section['words'] = [
                        {'en': w, 'zh': cn[i], 'extra': extras[i]}
                        for i, w in enumerate(['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty'])
                    ]
                elif sec_id == 'countries':
                    section['words'] = [
                        {'en':'China',         'zh':'中国',         'full':'the People\'s Republic of China',   'extra':'🇨🇳 东亚 · 首都北京 · 14亿人口 · 长城/故宫'},
                        {'en':'Italy',         'zh':'意大利',       'full':'the Italian Republic',              'extra':'🇮🇹 南欧 · 形似靴子 · 罗马/披萨/意面'},
                        {'en':'UK',            'zh':'英国',         'full':'the United Kingdom',                'extra':'🇬🇧 西欧岛国 · 首都伦敦 · 女王/大本钟'},
                        {'en':'USA',           'zh':'美国',         'full':'the United States of America',      'extra':'🇺🇸 北美 · 50州 · 首都华盛顿 · 自由女神'},
                        {'en':'France',        'zh':'法国',         'full':'the French Republic',               'extra':'🇫🇷 西欧 · 首都巴黎 · 埃菲尔铁塔/卢浮宫'},
                        {'en':'Germany',       'zh':'德国',         'full':'the Federal Republic of Germany',   'extra':'🇩🇪 中欧 · 首都柏林 · 啤酒/香肠/汽车'},
                        {'en':'New Zealand',   'zh':'新西兰',       'full':'Aotearoa (毛利语: 长白云之乡)',   'extra':'🇳🇿 大洋洲 · 岛国 · 羊比人多 · 几维鸟'},
                    ]
            # 注入 OCR 坐标 (G3A starter): { word_text: { bbox, cy, conf } }
            # 必须在 words 赋值之后跑
            sec_words = section.get('words', [])
            if grade == 'g3a' and sec_words and pages:
                ocr_index = get_ocr_for_section(sec_id, pages[0])
                word_coords = {}
                for w in sec_words:
                    en = (w['en'] if isinstance(w, dict) else w)
                    # 优先精确匹配,失败再 fuzzy split-match
                    hit = find_phrase_bbox(ocr_index, en)
                    if hit:
                        word_coords[en] = hit
                if word_coords:
                    section['word_coords'] = word_coords
            sections.append(section)

        data[uid] = {
            'num': u.get('num', uid),
            'name': u.get('name', ''),
            'description': u.get('description', ''),
            'duration': u.get('duration', ''),
            'audio_file': (
                'starter.mp3' if uid == 'starter' else f'unit_{uid[4:]}.mp3'
            ),
            'pdf_start': u.get('pdf_start'),
            'pdf_end': u.get('pdf_end'),
            'sections': sections,
        }

    return data


def write_js(grade, data, out_path):
    js = f'// {grade.upper()} 11 单元 sections 切分（数据驱动）\n'
    js += f'// 每段含 {{id, name, icon, pages[], audio, words?}}\n'
    js += f'const SECTIONS_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n'
    with open(out_path, 'w') as f:
        f.write(js)
    print(f'✅ {grade} sections_data.js 写入: {out_path} ({len(data)} 单元)')


if __name__ == '__main__':
    # G3A
    g3a_data = build_sections_data(
        'g3a',
        G3A_SECTIONS,
        ROOT / 'materials/eng-g3a/structure/units.json',
        ROOT / 'site/eng-g3a/assets/audio',
        ROOT / 'materials/eng-g3a/audio',
    )
    write_js('g3a', g3a_data, ROOT / 'site/eng-g3a/units/sections_data.js')

    # G5A
    g5a_data = build_sections_data(
        'g5a',
        G5A_SECTIONS,
        ROOT / 'materials/eng-g5a/structure/units.json',
        ROOT / 'site/eng-g5a/assets/audio',
        ROOT / 'materials/eng-g5a/audio',
    )
    write_js('g5a', g5a_data, ROOT / 'site/eng-g5a/units/sections_data.js')
