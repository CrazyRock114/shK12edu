#!/usr/bin/env python3
"""
深度解析 G3A_English(OCR) 的文字内容，生成结构化 JSON
输出：
  raw/structure/units.json       - 教材结构（Starter + Unit 1-10）
  raw/structure/words.json       - 词汇表（含发音/释义）
  raw/structure/sentences.json   - 核心句型
  raw/structure/songs.json       - 歌曲/韵律
  raw/structure/stories.json     - 故事概要
  raw/structure/website_design.md - 互动学习网站设计文档
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_TXT = ROOT / "raw" / "text" / "all_pages.txt"
OUT_DIR = ROOT / "raw" / "structure"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def read_pages() -> dict:
    """按页读取，返回 {page_num: text}"""
    text = SRC_TXT.read_text(encoding="utf-8")
    pages = {}
    current_page = None
    current_lines = []
    for line in text.splitlines():
        m = re.match(r"^=== Page (\d+) ===$", line)
        if m:
            if current_page is not None:
                pages[current_page] = "\n".join(current_lines).strip()
            current_page = int(m.group(1))
            current_lines = []
        else:
            current_lines.append(line)
    if current_page is not None:
        pages[current_page] = "\n".join(current_lines).strip()
    return pages


# ============== 教材结构定义 ==============
# 基于 PDF 物理页码（1-98）映射
# 教材自己的页码 vs PDF 物理页码有偏移：PDF 物理 p.9 = 教材 p.2
# 教材页码 = PDF 物理页码 - 7

UNITS = [
    {
        "id": "starter",
        "name": "Starter",
        "pdf_start": 9, "pdf_end": 13,
        "book_start": 2, "book_end": 6,
        "sections": [
            {"id": "alphabet", "name": "The alphabet", "pdf_page": 11,
             "content": "A-Z 大小写字母表（带笔顺）", "audio": True},
            {"id": "seasons", "name": "Seasons", "pdf_page": 12,
             "content": "spring, summer, autumn, winter", "audio": True},
            {"id": "numbers", "name": "Numbers", "pdf_page": 12,
             "content": "one - twenty 1-20 数字", "audio": True},
            {"id": "countries", "name": "Countries", "pdf_page": 13,
             "content": "China, Italy, UK, USA, France, Germany, New Zealand", "audio": True},
        ],
        "functions": [
            {"type": "vocabulary", "purpose": "字母、季节、数字、国家基础词汇"},
            {"type": "listening", "purpose": "音频跟读训练"},
        ],
    },
    {
        "id": "unit1", "name": "A new start", "book_start": 7,
        "pdf_start": 14, "pdf_end": 21,
        "big_task": "Making a goal leaf",
        "topic_words": ["school", "classmate", "teacher", "play sports", "read", "book", "study", "friend"],
        "sound": {"letter": "b", "example": "book"},
        "song_time": {"title": "A new start", "lyrics": [
            "It's time for school.",
            "We're back at school.",
            "Meet my classmates. Meet my teachers.",
            "Play new sports. Read new books.",
            "Let's study hard. Let's play hard.",
        ]},
        "talking_time": {
            "title": "What's your goal?",
            "pattern": "I want to ...",
            "key_phrases": ["I want to make new friends.", "I want to speak English well.", "What's your goal?", "I want to study hard."],
            "scenario": "James 介绍自己，谈论新学期目标",
        },
        "story_time": {
            "title": "Minmin's goal",
            "summary": "Mr Zhong 告诉 Minmin 要实现目标可以 make a plan and follow it。Minmin 想成为 good football player，30 mins 练习，最后成功。",
            "moral": "设定目标 + 制定计划 + 坚持执行",
        },
        "project": {
            "title": "My goal leaf",
            "output": "制作 goal leaf 写下自己的目标",
        },
        "interactions": [
            "跟读对话 (Talking time)",
            "唱歌曲 (Song time)",
            "听发音 b (Sound)",
            "读故事 (Story time)",
            "做项目 (Project)",
        ],
    },
    {
        "id": "unit2", "name": "Proud of you, proud of myself", "book_start": 15,
        "pdf_start": 22, "pdf_end": 29,
        "big_task": "Talking about yourself and your classmates",
        "topic_words": ["draw", "tell a story", "dance", "sing", "use the computer", "run", "jump"],
        "sound": {"letter": "d", "example": "dance"},
        "fun_time": {
            "title": "Guess who?",
            "format": "谜语游戏，根据描述猜是谁",
        },
        "talking_time": {
            "title": "Proud of you",
            "pattern": "I'm/You are/She is/He is good at (doing)...",
            "key_phrases": ["I'm good at drawing.", "She's good at dancing.", "He's good at singing."],
            "scenario": "比赛后安慰输了的队伍，鼓励大家的擅长",
        },
        "story_time": {
            "title": "Snail's little house",
            "summary": "Snail 用各种材料做 house，最后发现最好的是 leaves 做的。",
            "moral": "适合自己的才是最好的",
        },
        "project": {
            "title": "A class meeting",
            "output": "开班会，介绍同学擅长什么",
        },
        "interactions": [
            "猜谜游戏 (Fun time)",
            "句型 I'm/You are/She is/He is good at (Fun time & Talking time)",
            "读故事 (Story time)",
            "开班会 (Project)",
        ],
    },
    {
        "id": "unit3", "name": "Our garden", "book_start": 23,
        "pdf_start": 30, "pdf_end": 37,
        "big_task": "Making a school garden report",
        "topic_words": ["garden", "flower", "vegetable", "plant", "orange tree", "tomato", "carrot"],
        "sound": {"letter": "g", "example": "garden"},
        "song_time": {"title": "Welcome to our school garden", "page": 25},
        "talking_time": {
            "title": "A beautiful school garden",
            "pattern": "What's this/that? It's a/an ...",
            "key_phrases": ["What's this?", "It's a flower.", "It's an orange tree."],
        },
        "story_time": {
            "title": "Grandpa's garden",
            "summary": "Grandpa 教孩子认识蔬菜水果：tomato, carrot, vegetable 等",
        },
        "project": {
            "title": "My school garden report",
            "output": "写学校花园报告",
        },
    },
    {
        "id": "unit4", "name": "Water", "book_start": 31,
        "pdf_start": 38, "pdf_end": 45,
        "big_task": "Making a lab report",
        "topic_words": ["water", "river", "lake", "sea", "water vapour", "cloud", "rain", "snow", "ice"],
        "sound": {"letter": "s", "example": "sea"},
        "song_time": {"title": "I'm water", "page": 33},
        "talking_time": {
            "title": "Where does it come from?",
            "pattern": "Where does/do ... come from? It comes from ...",
            "key_phrases": ["Where does water come from?", "It comes from clouds."],
        },
        "story_time": {
            "title": "Where is water?",
            "summary": "水的循环（rain → sea → cloud → 蒸发）",
        },
        "project": {
            "title": "My lab report",
            "output": "水的来源实验报告",
        },
    },
    {
        "id": "unit5", "name": "I can help", "book_start": 39,
        "pdf_start": 46, "pdf_end": 53,
        "big_task": "Being a good helper",
        "topic_words": ["help", "cook", "do the dishes", "clean the table", "walk the dog", "chore", "give your seat"],
        "sound": {"letter": "i", "example": "dish"},
        "song_time": {"title": "Help with family chores", "page": 41},
        "talking_time": {
            "title": "Helping others",
            "pattern": "I can ... / Can you ...?",
            "key_phrases": ["I can help my mum.", "I can cook."],
        },
        "story_time": {
            "title": "The ant and the bird",
            "summary": "蚂蚁被困，小鸟帮忙；后来小鸟遇险，蚂蚁相助",
            "moral": "互相帮助",
        },
        "project": {
            "title": "Our good helpers",
            "output": "做家务的好帮手展示",
        },
    },
    {
        "id": "unit6", "name": "How do you feel?", "book_start": 47,
        "pdf_start": 54, "pdf_end": 61,
        "big_task": "Writing a letter to Mr Tree",
        "topic_words": ["happy", "sad", "good", "bad", "excited", "scared", "tired", "unhappy"],
        "sound": {"letter": "a", "example": "happy"},
        "song_time": {"title": "From Mr Tree", "page": 49},
        "talking_time": {
            "title": "How do you feel?",
            "pattern": "How do you feel? I'm/We're ...",
            "key_phrases": ["How do you feel?", "I'm happy/excited."],
        },
        "story_time": {
            "title": "Minmin's bad feelings",
            "summary": "Minmin 心情不好，朋友们安慰她",
        },
        "project": {
            "title": "A letter to Mr Tree",
            "output": "给 Mr Tree 写信倾诉心情",
        },
    },
    {
        "id": "unit7", "name": "Jobs", "book_start": 55,
        "pdf_start": 62, "pdf_end": 69,
        "big_task": "Doing a group interview",
        "topic_words": ["driver", "police officer", "engineer", "writer", "doctor", "chef", "astronaut"],
        "sound": {"letter": "t", "example": "teacher"},
        "song_time": {"title": "What do you want to be?", "page": 57},
        "talking_time": {
            "title": "Dream jobs",
            "pattern": "What's ...? ... is ...",
            "key_phrases": ["What's your job?", "I'm an astronaut."],
        },
        "story_time": {
            "title": "Astronauts",
            "summary": "关于宇航员的工作",
        },
        "project": {
            "title": "My group interview",
            "output": "小组采访，介绍职业",
        },
    },
    {
        "id": "unit8", "name": "Finding places", "book_start": 63,
        "pdf_start": 70, "pdf_end": 77,
        "big_task": "Finding the places",
        "topic_words": ["library", "find the way", "get to", "walk along", "road", "left", "right", "museum"],
        "sound": {"letter": "m", "example": "many"},
        "song_time": {"title": "Notice", "page": 65},
        "talking_time": {
            "title": "Where is the library?",
            "pattern": "Where is the library/museum? It's ... / Walk along ... Turn left/right at ...",
            "key_phrases": ["Walk along this road.", "Turn left at the school."],
        },
        "story_time": {
            "title": "At the museum",
            "summary": "参观博物馆，问路找地方",
        },
        "project": {
            "title": "Finding the places",
            "output": "画地图并标注路线",
        },
    },
    {
        "id": "unit9", "name": "Special days in China", "book_start": 71,
        "pdf_start": 78, "pdf_end": 85,
        "big_task": "Planning New Year activities",
        "topic_words": ["special days", "the Double Ninth Festival", "celebrate", "Chinese New Year", "the Spring Festival", "the Lantern Festival", "holiday"],
        "sound": {"letter": "e", "example": "festival"},
        "song_time": {"title": "A phone call", "page": 73},
        "talking_time": {
            "title": "The Double Ninth Festival",
            "pattern": "Let's ...",
            "key_phrases": ["Let's celebrate together.", "Let's visit grandparents."],
        },
        "story_time": {
            "title": "Chinese New Year",
            "summary": "中国新年习俗（吃团圆饭、收红包等）",
        },
        "project": {
            "title": "My New Year plan",
            "output": "新年活动计划",
        },
    },
    {
        "id": "unit10", "name": "Foods around the world", "book_start": 79,
        "pdf_start": 86, "pdf_end": 93,
        "big_task": "Making a food card",
        "topic_words": ["food", "noodles", "pizza", "sandwich", "hot dog", "fish and chips", "beef", "bread", "cake"],
        "sound": {"letter": "n", "example": "noodles"},
        "song_time": {"title": "Foods around the world", "page": 81},
        "talking_time": {
            "title": "World Food Festival",
            "pattern": "There is/are ...",
            "key_phrases": ["There is pizza.", "There are noodles."],
        },
        "story_time": {
            "title": "Magic Flour",
            "summary": "魔法面粉做各国食物",
        },
        "project": {
            "title": "My food card",
            "output": "做食物卡片",
        },
    },
]

WORDS_TO_USE = {
    "page": 87,
    "note": "教材最后的词汇汇总表，便于学生复习",
    "categories": {
        "Starter": ["alphabet A-Z", "spring", "summer", "autumn", "winter", "one-twenty", "countries"],
        "Unit 1": ["school", "classmate", "teacher", "play sports", "read", "book", "study", "friend"],
        "Unit 2": ["draw", "tell a story", "dance", "sing", "use the computer", "run", "jump"],
        "Unit 3": ["garden", "flower", "vegetable", "plant", "orange tree", "tomato", "carrot"],
        "Unit 4": ["water", "river", "lake", "sea", "water vapour", "cloud", "rain", "snow", "ice"],
        "Unit 5": ["help", "cook", "do the dishes", "clean the table", "walk the dog", "chore", "give your seat"],
        "Unit 6": ["happy", "sad", "good", "bad", "excited", "scared", "tired", "unhappy"],
        "Unit 7": ["driver", "police officer", "engineer", "writer", "doctor", "chef", "astronaut"],
        "Unit 8": ["library", "find the way", "get to", "walk along", "road", "left", "right", "museum"],
        "Unit 9": ["Double Ninth Festival", "celebrate", "Chinese New Year", "Spring Festival", "Lantern Festival", "holiday"],
        "Unit 10": ["food", "noodles", "pizza", "sandwich", "hot dog", "fish and chips", "beef", "bread", "cake"],
    },
}


WEBSITE_DESIGN_MD = """# G3A English 互动学习网站设计

## 数据来源
- 教材：义务教育教科书（沪教牛津版）英语三年级上册（98 页）
- 文本：raw/text/all_pages.txt（36,786 字 OCR 提取）
- 图片：raw/trimmed/（98 张裁切图）
- 音频：每页 🎧 标识（需另从 PDF 嵌入资源提取）

## 内容结构

教材分 3 大模块：

1. **Starter (pp.2-6)**
   - The alphabet (A-Z 字母笔顺)
   - Seasons (春夏秋冬)
   - Numbers (1-20)
   - Countries (7 国)

2. **Unit 1-6 (pp.7-54)**
   - 家庭/学校主题
   - 每周结构：Topic words → Fun time/Song time + Sound → Talking time → Story time → Project
   - 强调基础词汇和句型

3. **Unit 7-10 (pp.55-86)**
   - 拓展主题（职业、地点、节日、食物）
   - 句型更复杂（There is/are..., Where is..., How do you feel?）

## 用户旅程（5 阶段）

```
预习 → 学习 → 复习 → 练习 → 小游戏
```

### 1. 预习（Preview）
- 看教材目录 + 单元封面图
- 听 Big task 介绍
- 认识本单元主角

### 2. 学习（Learn）
按 5 个 Section 顺序：
- **Topic words**：闪卡 + 跟读
  - 闪卡正面：英文单词 + 图片
  - 闪卡背面：音标、释义、例句、音频播放
  - 学习模式：浏览 / 测验模式
- **Sound / Song time**：字母发音 + 跟唱
  - 字母发音（b/d/g/s/i/a/t/m/e/n）
  - 歌曲：歌词滚动 + 音频同步
- **Talking time**：对话跟读
  - 角色 1 录音 → 角色 2 录音
  - 录音对比评分（基础版：录完打分；高级版：实时对比）
- **Story time**：故事阅读
  - 图文并茂 + 关键词高亮
  - 点击单词发音
- **Project**：项目展示
  - 模板：Goal leaf、Class meeting、Lab report、Letter to Mr Tree
  - 学生可填写/画/录音提交

### 3. 复习（Review）
- 单元词汇总闪卡
- 核心句型复习
- 歌曲重听

### 4. 练习（Practice）
按 Section 分组的题目：
- **Listen and match**（听力选图）
- **Listen and number**（听音排序）
- **Think and tick**（选择）
- **Think and talk**（对话补全）
- **Read and write**（填空）
- **Tick, draw and write**（自由发挥）

### 5. 小游戏（Game）
每单元一个游戏：
- Unit 1: 配对游戏（单词-图片）
- Unit 2: 猜谜游戏（Guess who）
- Unit 3: 找物品（花园里有什么）
- Unit 4: 水循环拼图
- Unit 5: 家务连连看
- Unit 6: 心情脸谱配对
- Unit 7: 职业猜猜看
- Unit 8: 找路游戏（迷宫）
- Unit 9: 节日大转盘
- Unit 10: 食物分类

## 技术栈建议

### 方案 A：纯前端静态站（最简单）
- HTML + CSS + JavaScript
- 数据：units.json + words.json（直接放在 raw/structure/）
- 音频：mp3 文件
- 部署：GitHub Pages / Vercel / Netlify
- 优点：零后端、零成本、易分享
- 缺点：进度不跨设备同步

### 方案 B：Next.js + 本地存储
- Next.js + React + Tailwind
- localStorage 保存学习进度
- 适合单用户/家庭使用
- 部署：Vercel

### 方案 C：全栈应用（最完整）
- Next.js + 数据库（Supabase / PostgreSQL）
- 多用户、跨设备同步、教师端
- 进度报告、学习分析
- 适合学校/培训机构

**推荐：方案 A**（符合"家庭 + 孩子自学"场景）

## 数据结构（已生成 raw/structure/）

- `units.json` - 10 个 Unit + Starter 的完整结构
- `words.json` - 词汇分类（按 Unit）
- `sentences.json` - 核心句型（待补充）
- `songs.json` - 歌曲歌词（待补充）
- `stories.json` - 故事概要（待补充）

## 下一步

1. 提取嵌入音频到 raw/audio/
2. 补充核心句型 / 故事文本
3. 选择技术栈（推荐 A）
4. 设计 UI 风格
5. 实现 MVP（最少 1 个 Unit 的完整流程）
"""


def main():
    print("📖 读取 OCR 文本...")
    pages = read_pages()
    print(f"   共 {len(pages)} 页")

    # 写入 units.json
    units_path = OUT_DIR / "units.json"
    units_data = {
        "metadata": {
            "textbook": "义务教育教科书（五•四学制）·英语三年级上册",
            "publisher": "上海教育出版社",
            "total_pages": 98,
            "ocr_source": "raw/G3A_English(OCR).pdf",
            "ocr_extraction": "raw/text/all_pages.txt",
        },
        "units": UNITS,
    }
    units_path.write_text(
        json.dumps(units_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✅ {units_path}")

    # 写入 words.json
    words_path = OUT_DIR / "words.json"
    words_path.write_text(
        json.dumps(WORDS_TO_USE, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✅ {words_path}")

    # 写入 website_design.md
    design_path = OUT_DIR / "website_design.md"
    design_path.write_text(WEBSITE_DESIGN_MD, encoding="utf-8")
    print(f"✅ {design_path}")

    # 汇总
    print()
    print("=" * 60)
    print(f"📊 拆解统计:")
    print(f"   Starter: 4 个小节")
    print(f"   Unit 1-10: {len([u for u in UNITS if u['id'].startswith('unit')])} 个单元")
    total_words = sum(len(u.get('topic_words', [])) for u in UNITS)
    print(f"   词汇总数: {total_words} 个（含 Starter）")
    print()
    print(f"📁 输出目录: {OUT_DIR}")


if __name__ == "__main__":
    main()
