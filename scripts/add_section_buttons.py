#!/usr/bin/env python3
"""
给 unit1.html 加 section 按钮 + JS
"""
from pathlib import Path

UNIT1 = Path("/Users/paulshi/Documents/MiniMax/shK12edu/site/units/unit1.html")
html = UNIT1.read_text()

SECTION_BUTTONS = '''  <div class="section-tabs">
    <button class="section-btn" data-section="big_task" data-audio="sections/big_task.mp3"><span class="icon">🎯</span>大任务</button>
    <button class="section-btn" data-section="full" data-audio="sections/full.mp3"><span class="icon">🎬</span>完整版</button>
    <button class="section-btn" data-section="fun_time" data-audio="sections/fun_time.mp3"><span class="icon">🎮</span>趣味</button>
    <button class="section-btn" data-section="sound" data-audio="sections/sound.mp3"><span class="icon">🔤</span>字母</button>
    <button class="section-btn" data-section="story_time" data-audio="sections/story_time.mp3"><span class="icon">📖</span>故事</button>
    <button class="section-btn" data-section="talking_time" data-audio="sections/talking_time.mp3"><span class="icon">💬</span>对话</button>
    <button class="section-btn" data-section="topic_words" data-audio="sections/topic_words.mp3"><span class="icon">📚</span>单词</button>
    <button class="section-btn" data-section="fun_time_prac" data-audio="practice/fun_time.mp3"><span class="icon">🎯</span>趣味(练习)</button>
    <button class="section-btn" data-section="sound_prac" data-audio="practice/sound.mp3"><span class="icon">🎯</span>字母(练习)</button>
    <button class="section-btn" data-section="topic_words_prac" data-audio="practice/topic_words.mp3"><span class="icon">🎯</span>单词(练习)</button>
  </div>'''

SECTION_CSS = '''
.section-tabs { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 16px; justify-content: center; }
.section-btn { background: var(--white); border: 2px solid var(--bg); padding: 8px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: all 0.15s; display: inline-flex; align-items: center; gap: 6px; color: var(--text); box-shadow: var(--shadow); }
.section-btn:hover { background: var(--accent); transform: translateY(-2px); }
.section-btn.active { background: var(--primary); color: white; border-color: var(--primary); }
.section-btn .icon { font-size: 1.1rem; }
'''

SECTION_JS = '''
// ===== Section 按钮 =====
const SECTION_AUDIO = new Audio();
SECTION_AUDIO.preload = 'auto';
let currentSectionBtn = null;
document.querySelectorAll('.section-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const audioPath = btn.dataset.audio;
    if (currentSectionBtn) currentSectionBtn.classList.remove('active');
    if (currentSectionBtn === btn) {
      SECTION_AUDIO.pause();
      currentSectionBtn = null;
      return;
    }
    btn.classList.add('active');
    currentSectionBtn = btn;
    SECTION_AUDIO.src = '../assets/audio/unit1/' + audioPath;
    SECTION_AUDIO.play().catch(e => console.error('播放失败', e));
  });
});
SECTION_AUDIO.addEventListener('ended', () => {
  if (currentSectionBtn) currentSectionBtn.classList.remove('active');
  currentSectionBtn = null;
});

'''

# 1. 加 CSS
if '.section-btn {' not in html:
    # 在 .btn-orig 后面加
    html = html.replace(
        '.btn-orig {\n  background: #4ecdc4;\n  color: white;\n}',
        '.btn-orig {\n  background: #4ecdc4;\n  color: white;\n}' + SECTION_CSS
    )
    print("✓ CSS 已加")

# 2. 加 section 按钮(在 "查看教材" 按钮前)
if 'class="section-tabs"' not in html:
    html = html.replace(
        '<div style="text-align: center; margin-bottom: 20px;">\n    <button class="btn btn-accent" id="view-textbook">',
        SECTION_BUTTONS + '\n  <div style="text-align: center; margin-bottom: 20px;">\n    <button class="btn btn-accent" id="view-textbook">'
    )
    print("✓ 按钮已加")

# 3. 加 JS
if 'SECTION_AUDIO' not in html:
    # 在 "const UNIT_AUDIO = document.getElementById('unit-audio');" 之后
    html = html.replace(
        'const UNIT_AUDIO = document.getElementById(\'unit-audio\');',
        'const UNIT_AUDIO = document.getElementById(\'unit-audio\');\n' + SECTION_JS
    )
    print("✓ JS 已加")

UNIT1.write_text(html)
print(f"\n✓ unit1.html 更新完成")

# 验证
new_html = UNIT1.read_text()
print(f"  section-btn 按钮数: {new_html.count('data-audio=')}")
print(f"  CSS 引用: {'section-btn {' in new_html}")
print(f"  JS 引用: {'SECTION_AUDIO' in new_html}")
