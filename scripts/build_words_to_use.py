#!/usr/bin/env python3
"""生成 words_to_use 页面 - 全册词汇复习"""
from pathlib import Path

ROOT = Path("/Users/paulshi/Documents/MiniMax/shK12edu")
OUT = ROOT / "site/units/words_to_use.html"

# 12 个 unit 的 topic words 汇总
ALL_WORDS = [
    # Starter
    ("alphabet", "字母表 A-Z", "starter"),
    ("spring", "春天", "starter"),
    ("summer", "夏天", "starter"),
    ("autumn", "秋天", "starter"),
    ("winter", "冬天", "starter"),
    ("one", "1", "starter"),
    ("two", "2", "starter"),
    ("three", "3", "starter"),
    ("China", "中国", "starter"),
    ("Italy", "意大利", "starter"),
    ("UK", "英国", "starter"),
    ("USA", "美国", "starter"),
    ("France", "法国", "starter"),
    ("Germany", "德国", "starter"),
    ("New Zealand", "新西兰", "starter"),
    # Unit 1
    ("school", "学校", "unit1"),
    ("classmate", "同学", "unit1"),
    ("teacher", "老师", "unit1"),
    ("play sports", "做运动", "unit1"),
    ("read", "读", "unit1"),
    ("book", "书", "unit1"),
    ("study", "学习", "unit1"),
    ("friend", "朋友", "unit1"),
    # Unit 2
    ("draw", "画", "unit2"),
    ("tell a story", "讲故事", "unit2"),
    ("dance", "跳舞", "unit2"),
    ("sing", "唱", "unit2"),
    ("use the computer", "用电脑", "unit2"),
    ("run", "跑", "unit2"),
    ("jump", "跳", "unit2"),
    # Unit 3
    ("garden", "花园", "unit3"),
    ("flower", "花", "unit3"),
    ("vegetable", "蔬菜", "unit3"),
    ("plant", "植物", "unit3"),
    ("orange tree", "橙子树", "unit3"),
    ("tomato", "番茄", "unit3"),
    ("carrot", "胡萝卜", "unit3"),
    # Unit 4
    ("water", "水", "unit4"),
    ("river", "河", "unit4"),
    ("lake", "湖", "unit4"),
    ("sea", "海", "unit4"),
    ("water vapour", "水蒸气", "unit4"),
    ("cloud", "云", "unit4"),
    ("rain", "雨", "unit4"),
    ("snow", "雪", "unit4"),
    ("ice", "冰", "unit4"),
    # Unit 5
    ("help", "帮忙", "unit5"),
    ("cook", "做饭", "unit5"),
    ("do the dishes", "洗碗", "unit5"),
    ("clean the table", "擦桌子", "unit5"),
    ("walk the dog", "遛狗", "unit5"),
    ("chore", "家务", "unit5"),
    ("give your seat", "让座", "unit5"),
    # Unit 6
    ("happy", "开心", "unit6"),
    ("sad", "难过", "unit6"),
    ("good", "好", "unit6"),
    ("bad", "坏", "unit6"),
    ("excited", "兴奋", "unit6"),
    ("scared", "害怕", "unit6"),
    ("tired", "累", "unit6"),
    ("unhappy", "不开心", "unit6"),
    # Unit 7
    ("driver", "司机", "unit7"),
    ("police officer", "警察", "unit7"),
    ("engineer", "工程师", "unit7"),
    ("writer", "作家", "unit7"),
    ("doctor", "医生", "unit7"),
    ("chef", "厨师", "unit7"),
    ("astronaut", "宇航员", "unit7"),
    # Unit 8
    ("library", "图书馆", "unit8"),
    ("find the way", "找路", "unit8"),
    ("get to", "到达", "unit8"),
    ("walk along", "沿...走", "unit8"),
    ("road", "路", "unit8"),
    ("left", "左", "unit8"),
    ("right", "右", "unit8"),
    ("museum", "博物馆", "unit8"),
    # Unit 9
    ("special days", "特别的日子", "unit9"),
    ("celebrate", "庆祝", "unit9"),
    ("Chinese New Year", "中国新年", "unit9"),
    ("holiday", "假期", "unit9"),
    # Unit 10
    ("food", "食物", "unit10"),
    ("noodles", "面条", "unit10"),
    ("pizza", "披萨", "unit10"),
    ("sandwich", "三明治", "unit10"),
    ("hot dog", "热狗", "unit10"),
    ("fish and chips", "炸鱼薯条", "unit10"),
    ("beef", "牛肉", "unit10"),
    ("bread", "面包", "unit10"),
    ("cake", "蛋糕", "unit10"),
]

# 按 unit 分组
units_grouped = {}
for word, meaning, unit in ALL_WORDS:
    units_grouped.setdefault(unit, []).append((word, meaning))


# 生成 HTML
html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Words to use · 全册词汇复习</title>
<link rel="stylesheet" href="../style.css">
<style>
.word-card .word-img { width: 100%; max-height: 80px; object-fit: contain; margin-bottom: 4px; border-radius: 6px; background: #f8f9fa; }
.unit-section { margin-bottom: 32px; }
.unit-section h2 { color: var(--primary); margin-bottom: 12px; font-size: 1.3rem; border-bottom: 2px solid var(--primary-light); padding-bottom: 6px; }
.word-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 8px; }
.mini-card { background: var(--white); border-radius: 10px; padding: 8px; text-align: center; box-shadow: var(--shadow); cursor: pointer; transition: all 0.15s; }
.mini-card:hover { transform: translateY(-2px); border: 2px solid var(--primary-light); }
.mini-card .w { font-weight: 700; font-size: 0.95rem; margin-bottom: 2px; }
.mini-card .m { font-size: 0.78rem; color: var(--text-soft); }
.mini-card .audio-row { display: flex; gap: 2px; margin-top: 4px; justify-content: center; }
.mini-card .audio-row button { font-size: 0.65rem; padding: 2px 4px; border: none; border-radius: 4px; cursor: pointer; }
.btn-tts-mini { background: #ffe66d; }
.btn-orig-mini { background: #4ecdc4; color: white; }
</style>
</head>
<body>

<header class="unit-header">
  <a class="back" href="../index.html">← 返回选单元</a>
  <h1>📖 Words to use · 全册词汇复习</h1>
  <p class="sub">Starter + Unit 1-10 共 85 个单词 · ⏱ 11:19</p>
</header>

<audio id="unit-audio" src="../assets/audio/words_to_use.mp3" preload="metadata"></audio>
<audio id="word-audio" src="" preload="auto"></audio>

<div class="audio-bar">
  <button class="play-btn" id="play-unit">▶</button>
  <div class="audio-info">
    <div class="audio-title">📖 教材原声 (整段 11:19)</div>
    <div class="audio-progress"><div class="audio-progress-fill" id="unit-progress"></div></div>
    <div class="audio-time"><span id="unit-cur">0:00</span><span id="unit-dur">11:19</span></div>
  </div>
</div>

<div class="stage active" style="max-width: 1000px; margin: 0 auto; padding: 20px;">"""

unit_titles = {
    "starter": "🌱 Starter 预备单元",
    "unit1": "Unit 1 · A new start",
    "unit2": "Unit 2 · Proud of you",
    "unit3": "Unit 3 · Our garden",
    "unit4": "Unit 4 · Water",
    "unit5": "Unit 5 · I can help",
    "unit6": "Unit 6 · How do you feel?",
    "unit7": "Unit 7 · Jobs",
    "unit8": "Unit 8 · Finding places",
    "unit9": "Unit 9 · Special days in China",
    "unit10": "Unit 10 · Foods around the world",
}

for unit in ["starter", "unit1", "unit2", "unit3", "unit4", "unit5", "unit6", "unit7", "unit8", "unit9", "unit10"]:
    words = units_grouped.get(unit, [])
    if not words:
        continue
    html += f'\n  <div class="unit-section">\n    <h2>{unit_titles.get(unit, unit)}</h2>\n    <div class="word-grid">'
    for word, meaning in words:
        w_safe = word.replace(" ", "_")
        # 主教材 Topic words 整段 + Whisper 单词切片
        html += f'''
      <div class="mini-card" data-word="{word}" data-unit="{unit}">
        <div class="w">{word}</div>
        <div class="m">{meaning}</div>
        <div class="audio-row">
          <button class="btn-tts-mini" data-action="tts">🔊</button>
          <button class="btn-orig-mini" data-action="orig">🎵</button>
        </div>
      </div>'''
    html += '\n    </div>\n  </div>'

html += """
</div>

<script>
const UNIT_AUDIO = document.getElementById('unit-audio');
const WORD_AUDIO = document.getElementById('word-audio');
let englishVoice = null;
function loadEnglishVoice() {
  if (!window.speechSynthesis) return;
  const voices = window.speechSynthesis.getVoices();
  englishVoice = voices.find(v => v.lang.startsWith('en')) || voices[0];
}
if (window.speechSynthesis) { loadEnglishVoice(); window.speechSynthesis.onvoiceschanged = loadEnglishVoice; }

function speak(text) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  if (englishVoice) u.voice = englishVoice;
  u.rate = 0.85;
  window.speechSynthesis.speak(u);
}

function speakOrig(word, unit) {
  // 优先用对应 unit 的 Topic words 整段
  const topic = new Audio(`../assets/audio/${unit}/sections/topic_words.mp3`);
  topic.play().catch(() => {
    // 降级用 TTS
    speak(word);
  });
}

const playBtn = document.getElementById('play-unit');
const progressFill = document.getElementById('unit-progress');
const curTime = document.getElementById('unit-cur');
const durTime = document.getElementById('unit-dur');
if (playBtn && UNIT_AUDIO) {
  UNIT_AUDIO.addEventListener('loadedmetadata', () => {
    const d = UNIT_AUDIO.duration;
    if (d && isFinite(d)) { const m = Math.floor(d/60), s = Math.floor(d%60); durTime.textContent = `${m}:${String(s).padStart(2,'0')}`; }
  });
  UNIT_AUDIO.addEventListener('timeupdate', () => {
    const pct = (UNIT_AUDIO.currentTime / UNIT_AUDIO.duration) * 100;
    progressFill.style.width = `${pct}%`;
    const c = UNIT_AUDIO.currentTime;
    curTime.textContent = `${Math.floor(c/60)}:${String(Math.floor(c%60)).padStart(2,'0')}`;
  });
  UNIT_AUDIO.addEventListener('ended', () => { playBtn.classList.remove('playing'); playBtn.textContent = '▶'; });
  playBtn.addEventListener('click', () => {
    if (UNIT_AUDIO.paused) { UNIT_AUDIO.play(); playBtn.classList.add('playing'); playBtn.textContent = '⏸'; }
    else { UNIT_AUDIO.pause(); playBtn.classList.remove('playing'); playBtn.textContent = '▶'; }
  });
}

document.querySelectorAll('.mini-card').forEach(card => {
  const word = card.dataset.word;
  const unit = card.dataset.unit;
  card.querySelector('[data-action="tts"]').addEventListener('click', e => { e.stopPropagation(); speak(word); });
  card.querySelector('[data-action="orig"]').addEventListener('click', e => { e.stopPropagation(); speakOrig(word, unit); });
  card.addEventListener('click', e => { if (e.target.dataset.action) return; speak(word); });
});

window.addEventListener('beforeunload', () => {
  if (UNIT_AUDIO) UNIT_AUDIO.pause();
  if (window.speechSynthesis) window.speechSynthesis.cancel();
});
</script>
</body>
</html>"""

OUT.write_text(html, encoding="utf-8")
print(f"✓ {OUT}")
print(f"  共 {len(ALL_WORDS)} 个单词,{len(units_grouped)} 个 unit")
