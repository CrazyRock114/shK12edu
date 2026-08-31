// Unit 1 互动学习 JS - 教材原图 + 单词切片音频

// ===== 单词数据(图片 + 双发音) =====
const WORDS = [
  { word: 'school',      meaning: '学校',  img: 'assets/img/unit1/school.jpg',      orig: 'assets/audio/words/school.mp3' },
  { word: 'classmate',   meaning: '同学',  img: 'assets/img/unit1/classmate.jpg',   orig: 'assets/audio/words/classmate.mp3' },
  { word: 'teacher',     meaning: '老师',  img: 'assets/img/unit1/teacher.jpg',     orig: 'assets/audio/words/teacher.mp3' },
  { word: 'play sports', meaning: '做运动', img: 'assets/img/unit1/play_sports.jpg', orig: 'assets/audio/words/play_sports.mp3' },
  { word: 'read',        meaning: '读',    img: 'assets/img/unit1/read.jpg',        orig: 'assets/audio/words/read.mp3' },
  { word: 'book',        meaning: '书',    img: 'assets/img/unit1/book.jpg',        orig: 'assets/audio/words/book.mp3' },
  { word: 'study',       meaning: '学习',  img: 'assets/img/unit1/study.jpg',       orig: 'assets/audio/words/study.mp3' },
  { word: 'friend',      meaning: '朋友',  img: 'assets/img/unit1/friend.jpg',      orig: 'assets/audio/words/friend.mp3' },
];

// 关键短语
const PHRASES = [
  { text: "I want to make new friends.", meaning: "我想要交新朋友" },
  { text: "I want to speak English well.", meaning: "我想要说好英语" },
  { text: "What's your goal?", meaning: "你的目标是什么?" },
  { text: "I want to study hard.", meaning: "我想努力学习" },
];

// ===== 单元音频(教材原声 4:31) =====
const UNIT_AUDIO = document.getElementById('unit-audio');
// 单词切片(教材原声切分)
const WORD_AUDIO = document.getElementById('word-audio');

// ===== Web Speech API =====
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
  // 优先播放教材原声切片(若有)
  const w = WORDS.find(x => x.word === word);
  if (w) {
    WORD_AUDIO.src = '../' + w.orig;
    WORD_AUDIO.play().catch(() => {
      // 切片缺失则降级到 TTS
      speak(word);
    });
  }
}

// ===== Tab 切换 =====
const tabs = document.querySelectorAll('.stage-tab');
const stages = document.querySelectorAll('.stage');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.stage;
    tabs.forEach(t => t.classList.toggle('active', t === tab));
    stages.forEach(s => s.classList.toggle('active', s.id === `stage-${target}`));
    if (UNIT_AUDIO) UNIT_AUDIO.pause();
    if (WORD_AUDIO) WORD_AUDIO.pause();
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});

// ===== 单元音频条 =====
const playBtn = document.getElementById('play-unit');
const progressFill = document.getElementById('unit-progress');
const curTime = document.getElementById('unit-cur');
const durTime = document.getElementById('unit-dur');

if (playBtn && UNIT_AUDIO) {
  UNIT_AUDIO.addEventListener('loadedmetadata', () => {
    const d = UNIT_AUDIO.duration;
    if (d && isFinite(d)) {
      const m = Math.floor(d / 60);
      const s = Math.floor(d % 60);
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

// ===== 教材原页查看 =====
document.getElementById('view-textbook').addEventListener('click', () => {
  document.getElementById('textbook-modal').style.display = 'flex';
});

// ===== 词卡工厂 =====
function makeWordCard(w) {
  return `
    <div class="word-card" data-word="${w.word}">
      <img class="word-img" src="../${w.img}" alt="${w.word}" onerror="this.style.display='none'" />
      <div class="word">${w.word}</div>
      <div class="meaning">${w.meaning}</div>
      <div class="audio-row">
        <button class="btn-tts" data-action="tts">🔊 跟读</button>
        <button class="btn-orig" data-action="orig">🎵 原声</button>
      </div>
    </div>
  `;
}

function bindCardEvents(container) {
  container.querySelectorAll('.word-card').forEach(card => {
    const word = card.dataset.word;
    card.querySelector('[data-action="tts"]').addEventListener('click', (e) => {
      e.stopPropagation();
      speak(word);
    });
    card.querySelector('[data-action="orig"]').addEventListener('click', (e) => {
      e.stopPropagation();
      speakOrig(word);
    });
    card.addEventListener('click', (e) => {
      if (e.target.dataset.action) return;
      speak(word);
    });
  });
}

// ===== 阶段 1: 预习 =====
const previewGrid = document.getElementById('word-grid-preview');
if (previewGrid) {
  previewGrid.innerHTML = WORDS.map(makeWordCard).join('');
  bindCardEvents(previewGrid);
}

// ===== 阶段 2: 学习(同词卡,但可以加录音) =====
const learnGrid = document.getElementById('word-grid-learn');
if (learnGrid) {
  learnGrid.innerHTML = WORDS.map(makeWordCard).join('');
  bindCardEvents(learnGrid);
  // 加上录音功能
  let mediaRecorder = null;
  let audioChunks = [];
  learnGrid.addEventListener('click', async (e) => {
    const card = e.target.closest('.word-card');
    if (!card) return;
    // 录音:长按 1.5s
    // 这里简化为"双击录音"
  });
}

// ===== 阶段 3: 复习(闪卡) =====
let fcIndex = 0;
let fcRevealed = false;
let fcOrder = WORDS.map((_, i) => i);

const fcImg = document.getElementById('fc-img');
const fcWord = document.getElementById('fc-word');
const fcMeaning = document.getElementById('fc-meaning');
const fcProgress = document.getElementById('fc-progress');
const flashcard = document.getElementById('flashcard');

function renderFlashcard() {
  const w = WORDS[fcOrder[fcIndex]];
  fcImg.src = '../' + w.img;
  fcImg.style.display = 'block';
  fcWord.textContent = w.word;
  fcMeaning.textContent = w.meaning;
  fcProgress.textContent = `${fcIndex + 1} / ${fcOrder.length}`;
  flashcard.classList.remove('revealed');
  fcRevealed = false;
}
renderFlashcard();

document.getElementById('fc-prev').addEventListener('click', () => {
  fcIndex = (fcIndex - 1 + fcOrder.length) % fcOrder.length;
  renderFlashcard();
});
document.getElementById('fc-next').addEventListener('click', () => {
  fcIndex = (fcIndex + 1) % fcOrder.length;
  renderFlashcard();
});
document.getElementById('fc-flip').addEventListener('click', () => {
  flashcard.classList.toggle('revealed');
  fcRevealed = !fcRevealed;
});
flashcard.addEventListener('click', () => {
  flashcard.classList.toggle('revealed');
  fcRevealed = !fcRevealed;
});
document.getElementById('fc-sound').addEventListener('click', () => {
  speakOrig(WORDS[fcOrder[fcIndex]].word);
});
document.getElementById('fc-shuffle').addEventListener('click', () => {
  fcOrder = [...fcOrder].sort(() => Math.random() - 0.5);
  fcIndex = 0;
  renderFlashcard();
});
document.getElementById('fc-reset').addEventListener('click', () => {
  fcOrder = WORDS.map((_, i) => i);
  fcIndex = 0;
  renderFlashcard();
});

// ===== 阶段 4: 练习(选择题,无变化) =====
document.querySelectorAll('.practice-card').forEach(card => {
  const choices = card.querySelectorAll('.practice-choice');
  const correct = card.querySelector('.practice-choices').dataset.correct;
  const explanation = card.querySelector('.practice-explanation');
  let answered = false;
  choices.forEach(choice => {
    choice.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const text = choice.dataset.text;
      if (text === correct) {
        choice.classList.add('correct');
        explanation.textContent = '🎉 ' + explanation.textContent.replace('✅ ', '');
        explanation.style.background = '#d3f9d8';
        explanation.style.color = '#2b8a3e';
        speak(text);
      } else {
        choice.classList.add('wrong');
        choices.forEach(c => {
          if (c.dataset.text === correct) c.classList.add('correct');
        });
        explanation.textContent = '😅 再想想,正确答案是: ' + correct;
        explanation.style.background = '#fff3bf';
        explanation.style.color = '#e67700';
      }
      explanation.classList.add('show');
      choices.forEach(c => c.disabled = true);
    });
  });
});

// ===== 阶段 5: 游戏(听教材原声选词) =====
let gameCorrect = 0;
let gameWrong = 0;
let gameCurrent = null;
let gameAnswered = false;

const gameIcon = document.getElementById('game-icon');
const gamePrompt = document.getElementById('game-prompt');
const gameOptions = document.getElementById('game-options');
const gameCorrectEl = document.getElementById('game-correct');
const gameWrongEl = document.getElementById('game-wrong');

function startGame() {
  gameCorrect = 0;
  gameWrong = 0;
  gameCorrectEl.textContent = '0';
  gameWrongEl.textContent = '0';
  nextRound();
}

function nextRound() {
  const correctIdx = Math.floor(Math.random() * WORDS.length);
  gameCurrent = WORDS[correctIdx];

  const distractors = [];
  while (distractors.length < 3) {
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
      <img src="../${o.img}" style="max-height:60px; border-radius:6px; margin-right:8px" />
      ${o.word}
    </button>`
  ).join('');
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

  // 自动播放原声
  setTimeout(() => speakOrig(gameCurrent.word), 400);
}

document.getElementById('game-restart').addEventListener('click', startGame);
startGame();

// ===== 清理 =====
window.addEventListener('beforeunload', () => {
  if (UNIT_AUDIO) UNIT_AUDIO.pause();
  if (WORD_AUDIO) WORD_AUDIO.pause();
  if (window.speechSynthesis) window.speechSynthesis.cancel();
});
