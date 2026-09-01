#!/usr/bin/env python3
"""
从 units.json 自动生成 unit2-10 + starter + words_to_use 的 HTML 页面
基于 unit1.html 模板
"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
SITE = ROOT / "site"
UNITS = ROOT / "raw" / "structure" / "units.json"

# 加载数据
with open(UNITS) as f:
    raw_units = json.load(f)["units"]

# 构建 unit id -> 数据
UNITS_DATA = {}
for u in raw_units:
    UNITS_DATA[u["id"]] = u

# 关键词对应 emoji(无图时降级用)
EMOJI_FALLBACK = {
    "school": "🏫", "classmate": "👫", "teacher": "👩‍🏫",
    "play sports": "⚽", "read": "📖", "book": "📕", "study": "✏️", "friend": "🤝",
    "draw": "🎨", "tell a story": "📚", "dance": "💃", "sing": "🎤",
    "use the computer": "💻", "run": "🏃", "jump": "🦘",
    "garden": "🌻", "flower": "🌸", "vegetable": "🥕", "plant": "🌱",
    "orange tree": "🍊", "tomato": "🍅", "carrot": "🥕",
    "water": "💧", "river": "🏞️", "lake": "🏞️", "sea": "🌊",
    "water vapour": "☁️", "cloud": "☁️", "rain": "🌧️", "snow": "❄️", "ice": "🧊",
    "help": "🤝", "cook": "🍳", "do the dishes": "🍽️", "clean the table": "🧹",
    "walk the dog": "🐕", "chore": "🧹", "give your seat": "💺",
    "happy": "😊", "sad": "😢", "good": "👍", "bad": "👎",
    "excited": "🤩", "scared": "😨", "tired": "😴", "unhappy": "😞",
    "driver": "🚗", "police officer": "👮", "engineer": "👷", "writer": "✍️",
    "doctor": "👨‍⚕️", "chef": "👨‍🍳", "astronaut": "🧑‍🚀",
    "library": "📚", "find the way": "🧭", "get to": "📍", "walk along": "🚶",
    "road": "🛣️", "left": "⬅️", "right": "➡️", "museum": "🏛️",
    "special days": "📅", "the double ninth festival": "🌼", "celebrate": "🎉",
    "chinese new year": "🧧", "the spring festival": "🧧", "the lantern festival": "🏮", "holiday": "🏖️",
    "food": "🍱", "noodles": "🍜", "pizza": "🍕", "sandwich": "🥪",
    "hot dog": "🌭", "fish and chips": "🐟", "beef": "🥩", "bread": "🍞", "cake": "🎂",
}

# 中文释义
MEANINGS = {
    "school": "学校", "classmate": "同学", "teacher": "老师",
    "play sports": "做运动", "read": "读", "book": "书", "study": "学习", "friend": "朋友",
    "draw": "画", "tell a story": "讲故事", "dance": "跳舞", "sing": "唱",
    "use the computer": "用电脑", "run": "跑", "jump": "跳",
    "garden": "花园", "flower": "花", "vegetable": "蔬菜", "plant": "植物",
    "orange tree": "橙子树", "tomato": "番茄", "carrot": "胡萝卜",
    "water": "水", "river": "河", "lake": "湖", "sea": "海",
    "water vapour": "水蒸气", "cloud": "云", "rain": "雨", "snow": "雪", "ice": "冰",
    "help": "帮忙", "cook": "做饭", "do the dishes": "洗碗", "clean the table": "擦桌子",
    "walk the dog": "遛狗", "chore": "家务", "give your seat": "让座",
    "happy": "开心", "sad": "难过", "good": "好", "bad": "坏",
    "excited": "兴奋", "scared": "害怕", "tired": "累", "unhappy": "不开心",
    "driver": "司机", "police officer": "警察", "engineer": "工程师", "writer": "作家",
    "doctor": "医生", "chef": "厨师", "astronaut": "宇航员",
    "library": "图书馆", "find the way": "找路", "get to": "到达", "walk along": "沿...走",
    "road": "路", "left": "左", "right": "右", "museum": "博物馆",
    "special days": "特别的日子", "the double ninth festival": "重阳节", "celebrate": "庆祝",
    "chinese new year": "中国新年", "the spring festival": "春节", "the lantern festival": "元宵节", "holiday": "假期",
    "food": "食物", "noodles": "面条", "pizza": "披萨", "sandwich": "三明治",
    "hot dog": "热狗", "fish and chips": "炸鱼薯条", "beef": "牛肉", "bread": "面包", "cake": "蛋糕",
}


def render_unit_page(unit_id, unit_data):
    """生成单个 unit 的 HTML 页面"""
    # name: e.g. "Unit 1", title: e.g. "A new start"
    # Header: "Unit 1 · A new start" (用 name 作为标签 + title 作为内容)
    name = unit_data.get("name", unit_id)
    title = unit_data.get("title", unit_data.get("name", unit_id))
    if not title or title == name:
        # name 和 title 一样(比如 "Unit 1" / "Unit 1"),用真名
        title = unit_data.get("name", unit_id)
    description = unit_data.get("description", "")
    audio_file = f"{unit_id.replace('unit', 'unit_')}.mp3" if unit_id.startswith("unit") else f"{unit_id}.mp3"
    duration = unit_data.get("duration", "5:00")
    big_task = unit_data.get("big_task", "")
    topic_words = unit_data.get("topic_words", [])
    key_phrases = unit_data.get("key_phrases", [])
    song = unit_data.get("song_title", "")
    story = unit_data.get("story_title", "")
    sound_letter = unit_data.get("sound_letter", "")
    sound_example = unit_data.get("sound_example", "")

    # 教材页:book_start + 7 = PDF 页码
    book_start = unit_data.get("book_start")
    pdf_page = (book_start + 7) if book_start else None

    # 单词卡数据
    words_json = []
    for w in topic_words:
        w_safe = w.replace(" ", "_")
        words_json.append({
            "word": w,
            "meaning": MEANINGS.get(w, ""),
            "img": f"../assets/img/{unit_id}/{w_safe}.jpg",
            "orig": f"../assets/audio/{unit_id}/words/{w_safe}.mp3",
        })

    # Section 按钮(主教材 sections + 练习部分)
    sections_dir = ROOT / f"site/assets/audio/{unit_id}/sections"
    practice_dir = ROOT / f"site/assets/audio/{unit_id}/practice"

    section_buttons = []
    section_icons = {
        "full": "🎬", "big_task": "🎯", "topic_words": "📚", "sound": "🔤",
        "song_time": "🎵", "chant_time": "🎵", "talking_time": "💬", "story_time": "📖",
        "fun_time": "🎮", "reading_time": "📖", "rhyme_time": "🎵",
    }
    section_labels = {
        "full": "完整", "big_task": "大任务", "topic_words": "单词", "sound": "字母",
        "song_time": "歌曲", "chant_time": "吟唱", "talking_time": "对话", "story_time": "故事",
        "fun_time": "趣味", "reading_time": "阅读", "rhyme_time": "韵文",
    }
    # 跟 unit1 一致:不显示 "big_task" (用户嫌丑)
    skip_sections = {"big_task"}

    if sections_dir.exists():
        for mp3 in sorted(sections_dir.glob("*.mp3")):
            if mp3.stem in skip_sections:
                continue
            section_buttons.append((mp3.stem, section_icons.get(mp3.stem, "🔊"), section_labels.get(mp3.stem, mp3.stem), f"sections/{mp3.stem}.mp3"))
    if practice_dir.exists():
        for mp3 in sorted(practice_dir.glob("*.mp3")):
            section_buttons.append((mp3.stem + "_prac", "🎯", section_labels.get(mp3.stem, mp3.stem) + " (练习)", f"practice/{mp3.stem}.mp3"))

    section_buttons_html = "".join(
        f'<button class="section-btn" data-section="{sid}" data-audio="{path}"><span class="icon">{icon}</span>{label}</button>'
        for sid, icon, label, path in section_buttons
    )

    # 关键短语
    phrases_html = ""
    for p in key_phrases:
        slug = re.sub(r"[^a-z0-9_]", "", "_".join(p.lower().split()[:5]))
        phrases_html += f"""
            <button class="practice-choice" data-text="{p}">{p}</button>"""

    # 5 阶段内容 - 简化版本(可后续手动精修)
    preview_html = ""
    for w in topic_words:
        w_safe = w.replace(" ", "_")
        preview_html += f"""
            <div class="word-card" data-word="{w}">
              <img class="word-img" src="../assets/img/{unit_id}/{w_safe}.jpg" alt="{w}" onerror="this.style.display='none'" />
              <div class="word">{w}</div>
              <div class="meaning">{MEANINGS.get(w, '')}</div>
              <div class="audio-row">
                <button class="btn-tts" data-action="tts">🔊 跟读</button>
                <button class="btn-orig" data-action="orig">🎵 原声</button>
              </div>
            </div>"""

    # HTML
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} · {title} · 互动学习</title>
<link rel="stylesheet" href="../style.css">
<style>
.word-card .word-img {{
  width: 100%;
  max-height: 110px;
  object-fit: contain;
  margin-bottom: 6px;
  border-radius: 8px;
  background: #f8f9fa;
}}
.word-card .audio-row {{
  display: flex;
  gap: 4px;
  margin-top: 6px;
  justify-content: center;
}}
.word-card .audio-row button {{
  font-size: 0.7rem;
  padding: 4px 8px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}}
.btn-tts {{ background: #ffe66d; color: var(--text); }}
.btn-orig {{ background: #4ecdc4; color: white; }}

/* ===== Section 切换器 - 紧凑标签式 (跟 unit1 一致) ===== */
.section-tabs {{
  display: flex;
  gap: 0;
  margin: 0 0 20px 0;
  background: var(--white);
  border-radius: 14px;
  padding: 4px;
  box-shadow: var(--shadow);
  overflow: hidden;
}}
.section-btn {{
  flex: 1;
  background: transparent;
  border: none;
  padding: 10px 8px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-soft);
  cursor: pointer;
  border-radius: 10px;
  transition: all 0.15s;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  min-width: 0;
}}
.section-btn .icon {{ font-size: 1.1rem; }}
.section-btn:hover {{ background: var(--bg); color: var(--text); }}
.section-btn.active {{
  background: var(--primary);
  color: white;
}}
@media (max-width: 600px) {{
  .section-btn {{ font-size: 0.7rem; padding: 8px 4px; }}
  .section-btn .icon {{ font-size: 1rem; }}
}}
</style>
</head>
<body>

<header class="unit-header">
  <a class="back" href="../index.html">← 返回选单元</a>
  <h1>{name} · {title}</h1>
  <p class="sub">{description} · ⏱ {duration}</p>
</header>
<!-- name 字段含 "Unit N" 标签,title 是真实内容,避免重复 -->

<nav class="stage-tabs">
  <button class="stage-tab active" data-stage="preview"><span class="icon">👀</span>预习</button>
  <button class="stage-tab" data-stage="review"><span class="icon">🔄</span>复习</button>
  <button class="stage-tab" data-stage="play"><span class="icon">🎮</span>游戏</button>
</nav>

<audio id="unit-audio" src="../assets/audio/{audio_file}" preload="metadata"></audio>
<audio id="word-audio" src="" preload="auto"></audio>

<!-- 阶段 1: 预习 -->
<section class="stage active" id="stage-preview">
  <h2>👀 预习:看教材原图猜词</h2>
  <p class="stage-intro">{big_task or '看图猜词,点 🔊 跟读 / 🎵 原声'}</p>

  <div class="audio-bar">
    <button class="play-btn" id="play-unit">▶</button>
    <div class="audio-info">
      <div class="audio-title">📖 教材原声 (整段 {duration})</div>
      <div class="audio-progress"><div class="audio-progress-fill" id="unit-progress"></div></div>
      <div class="audio-time">
        <span id="unit-cur">0:00</span>
        <span id="unit-dur">{duration}</span>
      </div>
    </div>
  </div>

  <div class="section-tabs">
    {section_buttons_html}
  </div>

  <div style="text-align: center; margin-bottom: 20px;">
    <button class="btn btn-accent" id="view-textbook">📖 查看教材原页</button>
  </div>

  <div id="textbook-modal" style="display:none; position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 200; align-items: center; justify-content: center; padding: 20px;" onclick="this.style.display='none'">
    <img src="../assets/img/{unit_id}/lesson_full.jpg" style="max-width: 100%; max-height: 100%; border-radius: 8px;" onerror="this.src=''" />
  </div>

  <div class="word-card-grid">{preview_html}
  </div>
</section>

<!-- 阶段 2: 复习(闪卡) -->
<section class="stage" id="stage-review">
  <h2>🔄 复习:闪卡</h2>
  <p class="stage-intro">看英文,想中文,点翻面</p>

  <div class="flashcard-stage" id="flashcard">
    <img id="fc-img" style="max-height: 180px; border-radius: 12px; margin-bottom: 16px;" />
    <div class="flashcard-word" id="fc-word"></div>
    <div class="flashcard-meaning" id="fc-meaning"></div>
    <div style="font-size: 0.9rem; color: var(--text-soft);" id="fc-progress">1 / {len(topic_words)}</div>
  </div>

  <div class="flashcard-controls">
    <button class="btn btn-soft" id="fc-prev">← 上一个</button>
    <button class="btn btn-primary" id="fc-flip">翻面看意思</button>
    <button class="btn btn-soft" id="fc-sound">🔊 听发音</button>
    <button class="btn btn-secondary" id="fc-next">下一个 →</button>
  </div>
</section>

<!-- 阶段 3: 游戏 -->
<section class="stage" id="stage-play">
  <h2>🎮 游戏:听教材原声选词</h2>
  <p class="game-prompt" id="game-prompt">点击 🔊 开始</p>

  <div class="game-board">
    <div class="game-listening-icon" id="game-icon">🔊</div>
    <div class="game-options" id="game-options"></div>
    <div class="game-score">
      答对 <span class="num" id="game-correct">0</span> · 答错 <span class="num" id="game-wrong">0</span>
    </div>
    <div style="margin-top: 16px;">
      <button class="btn btn-accent" id="game-restart">↺ 重新开始</button>
    </div>
  </div>
</section>

<script>
const WORDS = {json.dumps(words_json, ensure_ascii=False)};

// 复用 unit1 的逻辑
{get_unit_js_logic()}
</script>
</body>
</html>"""
    return html


def get_unit_js_logic():
    """返回通用的 unit JS 逻辑"""
    return """
const UNIT_AUDIO = document.getElementById('unit-audio');
const WORD_AUDIO = document.getElementById('word-audio');

let englishVoice = null;
function loadEnglishVoice() {
  if (!window.speechSynthesis) return;
  const voices = window.speechSynthesis.getVoices();
  englishVoice = voices.find(v => v.lang.startsWith('en')) || voices[0];
}
if (window.speechSynthesis) {
  loadEnglishVoice();
  window.speechSynthesis.onvoiceschanged = loadEnglishVoice;
}

function speak(text, rate = 0.85) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'en-US';
  if (englishVoice) utter.voice = englishVoice;
  utter.rate = rate;
  utter.pitch = 1.1;
  window.speechSynthesis.speak(utter);
}

function speakOrig(word) {
  const w = WORDS.find(x => x.word === word);
  if (w) {
    WORD_AUDIO.src = w.orig;
    WORD_AUDIO.play().catch(() => speak(word));
  }
}

// Tab
document.querySelectorAll('.stage-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.stage;
    document.querySelectorAll('.stage-tab').forEach(t => t.classList.toggle('active', t === tab));
    document.querySelectorAll('.stage').forEach(s => s.classList.toggle('active', s.id === `stage-${target}`));
    if (UNIT_AUDIO) UNIT_AUDIO.pause();
    if (WORD_AUDIO) WORD_AUDIO.pause();
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});

// Unit audio
const playBtn = document.getElementById('play-unit');
const progressFill = document.getElementById('unit-progress');
const curTime = document.getElementById('unit-cur');
const durTime = document.getElementById('unit-dur');
if (playBtn && UNIT_AUDIO) {
  UNIT_AUDIO.addEventListener('loadedmetadata', () => {
    const d = UNIT_AUDIO.duration;
    if (d && isFinite(d)) {
      const m = Math.floor(d / 60), s = Math.floor(d % 60);
      durTime.textContent = `${m}:${String(s).padStart(2, '0')}`;
    }
  });
  UNIT_AUDIO.addEventListener('timeupdate', () => {
    const pct = (UNIT_AUDIO.currentTime / UNIT_AUDIO.duration) * 100;
    progressFill.style.width = `${pct}%`;
    const c = UNIT_AUDIO.currentTime;
    curTime.textContent = `${Math.floor(c/60)}:${String(Math.floor(c%60)).padStart(2,'0')}`;
  });
  UNIT_AUDIO.addEventListener('ended', () => {
    playBtn.classList.remove('playing');
    playBtn.textContent = '▶';
  });
  playBtn.addEventListener('click', () => {
    if (UNIT_AUDIO.paused) {
      UNIT_AUDIO.play();
      playBtn.classList.add('playing');
      playBtn.textContent = '⏸';
    } else {
      UNIT_AUDIO.pause();
      playBtn.classList.remove('playing');
      playBtn.textContent = '▶';
    }
  });
}

// Section 按钮:点击切换音频源
const SECTION_AUDIO = new Audio();
SECTION_AUDIO.preload = 'auto';
let currentSectionBtn = null;
document.querySelectorAll('.section-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const audioPath = btn.dataset.audio;
    if (currentSectionBtn) currentSectionBtn.classList.remove('active');
    if (currentSectionBtn === btn) {
      // toggle off
      SECTION_AUDIO.pause();
      currentSectionBtn = null;
      return;
    }
    btn.classList.add('active');
    currentSectionBtn = btn;
    SECTION_AUDIO.src = '../assets/audio/{unit_id}/' + audioPath;
    SECTION_AUDIO.play().catch(e => console.error(e));
  });
});
SECTION_AUDIO.addEventListener('ended', () => {
  if (currentSectionBtn) currentSectionBtn.classList.remove('active');
  currentSectionBtn = null;
});

document.getElementById('view-textbook').addEventListener('click', () => {
  document.getElementById('textbook-modal').style.display = 'flex';
});

// 词卡交互
document.querySelectorAll('#stage-preview .word-card').forEach(card => {
  const word = card.dataset.word;
  card.querySelector('[data-action="tts"]').addEventListener('click', (e) => { e.stopPropagation(); speak(word); });
  card.querySelector('[data-action="orig"]').addEventListener('click', (e) => { e.stopPropagation(); speakOrig(word); });
  card.addEventListener('click', (e) => { if (e.target.dataset.action) return; speak(word); });
});

// 闪卡
let fcIndex = 0, fcRevealed = false;
let fcOrder = WORDS.map((_, i) => i);
const fcImg = document.getElementById('fc-img');
const fcWord = document.getElementById('fc-word');
const fcMeaning = document.getElementById('fc-meaning');
const fcProgress = document.getElementById('fc-progress');
const flashcard = document.getElementById('flashcard');

function renderFC() {
  const w = WORDS[fcOrder[fcIndex]];
  if (w) {
    fcImg.src = w.img;
    fcImg.onerror = () => { fcImg.style.display = 'none'; };
    fcImg.style.display = 'block';
    fcWord.textContent = w.word;
    fcMeaning.textContent = w.meaning;
    fcProgress.textContent = `${fcIndex + 1} / ${fcOrder.length}`;
    flashcard.classList.remove('revealed');
  }
}
if (WORDS.length > 0) renderFC();
document.getElementById('fc-prev').addEventListener('click', () => { fcIndex = (fcIndex - 1 + fcOrder.length) % fcOrder.length; renderFC(); });
document.getElementById('fc-next').addEventListener('click', () => { fcIndex = (fcIndex + 1) % fcOrder.length; renderFC(); });
document.getElementById('fc-flip').addEventListener('click', () => { flashcard.classList.toggle('revealed'); });
if (flashcard) flashcard.addEventListener('click', () => { flashcard.classList.toggle('revealed'); });
document.getElementById('fc-sound').addEventListener('click', () => { speakOrig(WORDS[fcOrder[fcIndex]].word); });

// 游戏
let gameCorrect = 0, gameWrong = 0, gameCurrent = null, gameAnswered = false;
const gameIcon = document.getElementById('game-icon');
const gamePrompt = document.getElementById('game-prompt');
const gameOptions = document.getElementById('game-options');
const gameCorrectEl = document.getElementById('game-correct');
const gameWrongEl = document.getElementById('game-wrong');

function startGame() {
  if (WORDS.length < 2) { gamePrompt.textContent = '需要至少 2 个词'; return; }
  gameCorrect = 0; gameWrong = 0;
  gameCorrectEl.textContent = '0'; gameWrongEl.textContent = '0';
  nextRound();
}

function nextRound() {
  const correctIdx = Math.floor(Math.random() * WORDS.length);
  gameCurrent = WORDS[correctIdx];
  const distractors = [];
  while (distractors.length < Math.min(3, WORDS.length - 1)) {
    const d = WORDS[Math.floor(Math.random() * WORDS.length)];
    if (d.word !== gameCurrent.word && !distractors.find(x => x.word === d.word)) {
      distractors.push(d);
    }
  }
  const options = [gameCurrent, ...distractors].sort(() => Math.random() - 0.5);
  gameIcon.textContent = '🔊';
  gamePrompt.textContent = '点 🔊 听原声,选单词';
  gameOptions.innerHTML = options.map(o =>
    `<button class="game-option" data-word="${o.word}">
      <img src="${o.img}" style="max-height:60px; border-radius:6px; margin-right:8px" onerror="this.style.display='none'" />
      ${o.word}
    </button>`).join('');
  gameAnswered = false;
  gameIcon.onclick = () => speakOrig(gameCurrent.word);
  gameOptions.querySelectorAll('.game-option').forEach(btn => {
    btn.addEventListener('click', () => {
      if (gameAnswered) return;
      gameAnswered = true;
      const chosen = btn.dataset.word;
      if (chosen === gameCurrent.word) {
        btn.classList.add('correct');
        gameCorrect++;
        gameCorrectEl.textContent = gameCorrect;
        gamePrompt.textContent = '🎉 答对了!';
        speakOrig(gameCurrent.word);
      } else {
        btn.classList.add('wrong');
        gameOptions.querySelectorAll('.game-option').forEach(b => {
          if (b.dataset.word === gameCurrent.word) b.classList.add('correct');
        });
        gameWrong++;
        gameWrongEl.textContent = gameWrong;
        gamePrompt.textContent = `😅 正确答案是 ${gameCurrent.word}`;
      }
      setTimeout(nextRound, 1800);
    });
  });
  setTimeout(() => speakOrig(gameCurrent.word), 400);
}

document.getElementById('game-restart').addEventListener('click', startGame);
if (WORDS.length >= 2) startGame();
"""


def main():
    # 加载 site/units_data.json(包含 topic_words + 音频映射)
    with open(SITE / "units_data.json") as f:
        site_data = json.load(f)

    # 合并 raw units + site data (site_data 优先,覆盖 name)
    for u in site_data["units"]:
        uid = u["id"]
        if uid in UNITS_DATA:
            UNITS_DATA[uid].update({
                "name": u.get("name", UNITS_DATA[uid].get("name")),  # 用 site 的短名
                "audio_file": u.get("audio_file"),
                "duration": u.get("duration"),
                "title": u.get("title"),
                "description": u.get("description"),
                "topic_words": u.get("topic_words", UNITS_DATA[uid].get("topic_words", [])),
                "book_start": u.get("book_start"),
            })

    # 生成所有 unit 页面
    units_dir = SITE / "units"
    units_dir.mkdir(parents=True, exist_ok=True)

    # unit1: 复制现有的完整版
    # 其他: 模板生成
    for uid, udata in UNITS_DATA.items():
        if uid == "unit1":
            continue  # 已有完整的
        if not udata.get("audio_file"):
            continue
        if not udata.get("topic_words"):
            continue

        html = render_unit_page(uid, udata)
        out_path = units_dir / f"{uid}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"  ✓ {uid}.html ({len(udata.get('topic_words', []))} words)")

    # starter 和 words_to_use 简单生成
    for uid in ["starter", "words_to_use"]:
        if uid not in UNITS_DATA:
            continue
        udata = UNITS_DATA[uid]
        if not udata.get("audio_file"):
            continue
        # 给 starter / words_to_use 一个基础内容
        if uid == "starter":
            udata["topic_words"] = ["alphabet", "spring", "summer", "autumn", "winter", "one", "two", "three"]
        elif uid == "words_to_use":
            udata["topic_words"] = []  # 没有具体单词
            udata["description"] = "全册词汇复习"
        if not udata.get("topic_words"):
            continue
        html = render_unit_page(uid, udata)
        out_path = units_dir / f"{uid}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"  ✓ {uid}.html")


if __name__ == "__main__":
    main()
