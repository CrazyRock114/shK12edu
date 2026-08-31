// G3A 11 单元 sections 切分（数据驱动）
// 每段含 {id, name, icon, pages[], audio, words?}
const SECTIONS_DATA = {
  "starter": {
    "num": "starter",
    "name": "Starter",
    "description": "",
    "duration": "",
    "audio_file": "starter.mp3",
    "pdf_start": 9,
    "pdf_end": 13,
    "sections": [
      {
        "id": "families_and_friends",
        "name": "我们的家人与朋友",
        "icon": "👨‍👩‍👧‍👦",
        "pages": [
          9
        ],
        "audio": "starter.mp3",
        "words": [
          {
            "en": "Dad",
            "zh": "爸爸",
            "extra": "👨 father"
          },
          {
            "en": "Mum",
            "zh": "妈妈",
            "extra": "👩 mother"
          },
          {
            "en": "Grandpa",
            "zh": "爷爷/外公",
            "extra": "👴 父亲的父亲"
          },
          {
            "en": "Grandma",
            "zh": "奶奶/外婆",
            "extra": "👵 父亲的母亲"
          },
          {
            "en": "family",
            "zh": "家庭",
            "extra": "👨‍👩‍👧‍👦 一家人"
          },
          {
            "en": "friend",
            "zh": "朋友",
            "extra": "👫 buddy"
          }
        ]
      },
      {
        "id": "our_teachers",
        "name": "我们的老师",
        "icon": "👩‍🏫",
        "pages": [
          10
        ],
        "audio": "starter.mp3",
        "words": [
          {
            "en": "Ms Yu",
            "zh": "余老师",
            "extra": "👩‍🏫 女老师 (未婚)"
          },
          {
            "en": "Miss Li",
            "zh": "李老师",
            "extra": "👩‍🏫 Miss = 未婚"
          },
          {
            "en": "Mr Zhong",
            "zh": "钟老师",
            "extra": "👨‍🏫 男老师"
          },
          {
            "en": "Mr Qian",
            "zh": "钱老师",
            "extra": "👨‍🏫 Mr = 男老师"
          },
          {
            "en": "teacher",
            "zh": "老师",
            "extra": "👩‍🏫"
          }
        ]
      },
      {
        "id": "alphabet",
        "name": "字母表",
        "icon": "🔤",
        "pages": [
          11
        ],
        "audio": "starter/sections/the_alphabet.mp3",
        "words": [
          {
            "en": "Aa",
            "zh": "",
            "extra": "🍎 /eɪ/ · 例: Apple"
          },
          {
            "en": "Bb",
            "zh": "",
            "extra": "📚 /biː/ · 例: Book"
          },
          {
            "en": "Cc",
            "zh": "",
            "extra": "🐱 /siː/ · 例: Cat"
          },
          {
            "en": "Dd",
            "zh": "",
            "extra": "🐶 /diː/ · 例: Dog"
          },
          {
            "en": "Ee",
            "zh": "",
            "extra": "🥚 /iː/ · 例: Egg"
          },
          {
            "en": "Ff",
            "zh": "",
            "extra": "🐟 /ɛf/ · 例: Fish"
          },
          {
            "en": "Gg",
            "zh": "",
            "extra": "🦢 /dʒiː/ · 例: Goose"
          },
          {
            "en": "Hh",
            "zh": "",
            "extra": "✋ /eɪtʃ/ · 例: Hand"
          },
          {
            "en": "Ii",
            "zh": "",
            "extra": "🍦 /aɪ/ · 例: Ice cream"
          },
          {
            "en": "Jj",
            "zh": "",
            "extra": "🍓 /dʒeɪ/ · 例: Jam"
          },
          {
            "en": "Kk",
            "zh": "",
            "extra": "🪁 /keɪ/ · 例: Kite"
          },
          {
            "en": "Ll",
            "zh": "",
            "extra": "🦁 /ɛl/ · 例: Lion"
          },
          {
            "en": "Mm",
            "zh": "",
            "extra": "🥛 /ɛm/ · 例: Milk"
          },
          {
            "en": "Nn",
            "zh": "",
            "extra": "👃 /ɛn/ · 例: Nose"
          },
          {
            "en": "Oo",
            "zh": "",
            "extra": "🍊 /oʊ/ · 例: Orange"
          },
          {
            "en": "Pp",
            "zh": "",
            "extra": "🖊 /piː/ · 例: Pen"
          },
          {
            "en": "Qq",
            "zh": "",
            "extra": "👸 /kjuː/ · 例: Queen"
          },
          {
            "en": "Rr",
            "zh": "",
            "extra": "🌧 /ɑːr/ · 例: Rain"
          },
          {
            "en": "Ss",
            "zh": "",
            "extra": "☀️ /ɛs/ · 例: Sun"
          },
          {
            "en": "Tt",
            "zh": "",
            "extra": "🌳 /tiː/ · 例: Tree"
          },
          {
            "en": "Uu",
            "zh": "",
            "extra": "☂️ /juː/ · 例: Umbrella"
          },
          {
            "en": "Vv",
            "zh": "",
            "extra": "🌋 /viː/ · 例: Volcano"
          },
          {
            "en": "Ww",
            "zh": "",
            "extra": "🐋 /dʌbljuː/ · 例: Whale"
          },
          {
            "en": "Xx",
            "zh": "",
            "extra": "🩻 /ɛks/ · 例: X-ray"
          },
          {
            "en": "Yy",
            "zh": "",
            "extra": "🥛 /waɪ/ · 例: Yogurt"
          },
          {
            "en": "Zz",
            "zh": "",
            "extra": "🦓 /ziː/ · 例: Zebra"
          }
        ]
      },
      {
        "id": "seasons",
        "name": "季节",
        "icon": "🌤",
        "pages": [
          12
        ],
        "audio": "starter/sections/seasons.mp3",
        "words": [
          {
            "en": "spring",
            "zh": "春",
            "extra": "3-5月 · 花开 🌸"
          },
          {
            "en": "summer",
            "zh": "夏",
            "extra": "6-8月 · 炎热 ☀️"
          },
          {
            "en": "autumn",
            "zh": "秋",
            "extra": "9-11月 · 落叶 🍂"
          },
          {
            "en": "winter",
            "zh": "冬",
            "extra": "12-2月 · 下雪 ❄️"
          }
        ]
      },
      {
        "id": "numbers",
        "name": "数字",
        "icon": "🔢",
        "pages": [
          12
        ],
        "audio": "starter/sections/numbers.mp3",
        "words": [
          {
            "en": "one",
            "zh": "一",
            "extra": "1·一个"
          },
          {
            "en": "two",
            "zh": "二",
            "extra": "2·两个"
          },
          {
            "en": "three",
            "zh": "三",
            "extra": "3·三个"
          },
          {
            "en": "four",
            "zh": "四",
            "extra": "4·四季"
          },
          {
            "en": "five",
            "zh": "五",
            "extra": "5·五指"
          },
          {
            "en": "six",
            "zh": "六",
            "extra": "6·六角"
          },
          {
            "en": "seven",
            "zh": "七",
            "extra": "7·一周"
          },
          {
            "en": "eight",
            "zh": "八",
            "extra": "8·八爪"
          },
          {
            "en": "nine",
            "zh": "九",
            "extra": "9·久"
          },
          {
            "en": "ten",
            "zh": "十",
            "extra": "10·十全"
          },
          {
            "en": "eleven",
            "zh": "十一",
            "extra": "11·11"
          },
          {
            "en": "twelve",
            "zh": "十二",
            "extra": "12·月份"
          },
          {
            "en": "thirteen",
            "zh": "十三",
            "extra": "13·不吉利"
          },
          {
            "en": "fourteen",
            "zh": "十四",
            "extra": "14·情人节"
          },
          {
            "en": "fifteen",
            "zh": "十五",
            "extra": "15·15分"
          },
          {
            "en": "sixteen",
            "zh": "十六",
            "extra": "16·16岁"
          },
          {
            "en": "seventeen",
            "zh": "十七",
            "extra": "17·青春"
          },
          {
            "en": "eighteen",
            "zh": "十八",
            "extra": "18·成年"
          },
          {
            "en": "nineteen",
            "zh": "十九",
            "extra": "19·19"
          },
          {
            "en": "twenty",
            "zh": "二十",
            "extra": "20·20/20"
          }
        ]
      },
      {
        "id": "countries",
        "name": "国家",
        "icon": "🌍",
        "pages": [
          13
        ],
        "audio": "starter/sections/countries.mp3",
        "words": [
          {
            "en": "China",
            "zh": "中国",
            "full": "the People's Republic of China",
            "extra": "🇨🇳 东亚 · 首都北京 · 14亿人口 · 长城/故宫"
          },
          {
            "en": "Italy",
            "zh": "意大利",
            "full": "the Italian Republic",
            "extra": "🇮🇹 南欧 · 形似靴子 · 罗马/披萨/意面"
          },
          {
            "en": "UK",
            "zh": "英国",
            "full": "the United Kingdom",
            "extra": "🇬🇧 西欧岛国 · 首都伦敦 · 女王/大本钟"
          },
          {
            "en": "USA",
            "zh": "美国",
            "full": "the United States of America",
            "extra": "🇺🇸 北美 · 50州 · 首都华盛顿 · 自由女神"
          },
          {
            "en": "France",
            "zh": "法国",
            "full": "the French Republic",
            "extra": "🇫🇷 西欧 · 首都巴黎 · 埃菲尔铁塔/卢浮宫"
          },
          {
            "en": "Germany",
            "zh": "德国",
            "full": "the Federal Republic of Germany",
            "extra": "🇩🇪 中欧 · 首都柏林 · 啤酒/香肠/汽车"
          },
          {
            "en": "New Zealand",
            "zh": "新西兰",
            "full": "Aotearoa (毛利语: 长白云之乡)",
            "extra": "🇳🇿 大洋洲 · 岛国 · 羊比人多 · 几维鸟"
          }
        ]
      }
    ]
  },
  "unit1": {
    "num": "unit1",
    "name": "A new start",
    "description": "",
    "duration": "",
    "audio_file": "unit_1.mp3",
    "pdf_start": 14,
    "pdf_end": 21,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          15
        ],
        "audio": "unit1/sections/topic_words.mp3",
        "words": [
          {
            "en": "school",
            "zh": "学校",
            "full": "",
            "extra": "🏫 buildings/classroom"
          },
          {
            "en": "classmate",
            "zh": "同学",
            "full": "",
            "extra": "👫 同班同学"
          },
          {
            "en": "teacher",
            "zh": "老师",
            "full": "",
            "extra": "👩‍🏫 教书的人"
          },
          {
            "en": "play sports",
            "zh": "做运动",
            "full": "",
            "extra": "⚽ 跑跳打球"
          },
          {
            "en": "read",
            "zh": "读",
            "full": "",
            "extra": "📖 看书"
          },
          {
            "en": "book",
            "zh": "书",
            "full": "",
            "extra": "📚 有故事"
          },
          {
            "en": "study",
            "zh": "学习",
            "full": "",
            "extra": "✏️ 用功读书"
          },
          {
            "en": "friend",
            "zh": "朋友",
            "full": "",
            "extra": "👫 buddy"
          }
        ],
        "big_task": "Making a goal leaf"
      },
      {
        "id": "song_time",
        "name": "歌曲",
        "icon": "🎵",
        "pages": [
          16
        ],
        "audio": "unit1/sections/song_time.mp3",
        "song_title": "A new start",
        "song_lyrics": [
          "It's time for school.",
          "We're back at school.",
          "Meet my classmates. Meet my teachers.",
          "Play new sports. Read new books.",
          "Let's study hard. Let's play hard."
        ]
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          16
        ],
        "audio": "unit1/sections/sound.mp3",
        "sound_letter": "b",
        "sound_pattern": "",
        "sound_example": "book"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          17,
          18
        ],
        "audio": "unit1/sections/talking_time.mp3",
        "talking_title": "What's your goal?",
        "talking_pattern": "I want to ...",
        "talking_phrases": [
          "I want to make new friends.",
          "I want to speak English well.",
          "What's your goal?",
          "I want to study hard."
        ],
        "talking_scenario": "James 介绍自己，谈论新学期目标"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          19,
          20
        ],
        "audio": "unit1/sections/story_time.mp3",
        "story_title": "Minmin's goal",
        "story_summary": "Mr Zhong 告诉 Minmin 要实现目标可以 make a plan and follow it。Minmin 想成为 good football player，30 mins 练习，最后成功。",
        "story_moral": "设定目标 + 制定计划 + 坚持执行"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          21
        ],
        "audio": "unit1/sections/big_task.mp3",
        "project_title": "My goal leaf",
        "project_output": "制作 goal leaf 写下自己的目标"
      }
    ]
  },
  "unit2": {
    "num": "unit2",
    "name": "Proud of you, proud of myself",
    "description": "",
    "duration": "",
    "audio_file": "unit_2.mp3",
    "pdf_start": 22,
    "pdf_end": 29,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          23
        ],
        "audio": "unit2/sections/topic_words.mp3",
        "words": [
          {
            "en": "draw",
            "zh": "画",
            "full": "",
            "extra": "🎨 用笔"
          },
          {
            "en": "tell a story",
            "zh": "讲故事",
            "full": "",
            "extra": "📖 给别人听"
          },
          {
            "en": "dance",
            "zh": "跳舞",
            "full": "",
            "extra": "💃 音乐"
          },
          {
            "en": "sing",
            "zh": "唱歌",
            "full": "",
            "extra": "🎤 出声"
          },
          {
            "en": "use the computer",
            "zh": "用电脑",
            "full": "",
            "extra": "💻 上网/打字"
          },
          {
            "en": "run",
            "zh": "跑",
            "full": "",
            "extra": "🏃 快速走"
          },
          {
            "en": "jump",
            "zh": "跳",
            "full": "",
            "extra": "🤸 离地"
          }
        ],
        "big_task": "Talking about yourself and your classmates"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          24
        ],
        "audio": "unit2/sections/fun_time.mp3",
        "fun_title": "Guess who?",
        "fun_content": ""
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          24
        ],
        "audio": "unit2/sections/sound.mp3",
        "sound_letter": "d",
        "sound_pattern": "",
        "sound_example": "dance"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          25,
          26
        ],
        "audio": "unit2/sections/talking_time.mp3",
        "talking_title": "Proud of you",
        "talking_pattern": "I'm/You are/She is/He is good at (doing)...",
        "talking_phrases": [
          "I'm good at drawing.",
          "She's good at dancing.",
          "He's good at singing."
        ],
        "talking_scenario": "比赛后安慰输了的队伍，鼓励大家的擅长"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          27,
          28
        ],
        "audio": "unit2/sections/story_time.mp3",
        "story_title": "Snail's little house",
        "story_summary": "Snail 用各种材料做 house，最后发现最好的是 leaves 做的。",
        "story_moral": "适合自己的才是最好的"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          29
        ],
        "audio": "unit2/sections/big_task.mp3",
        "project_title": "A class meeting",
        "project_output": "开班会，介绍同学擅长什么"
      }
    ]
  },
  "unit3": {
    "num": "unit3",
    "name": "Our garden",
    "description": "",
    "duration": "",
    "audio_file": "unit_3.mp3",
    "pdf_start": 30,
    "pdf_end": 37,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          31
        ],
        "audio": "unit3/sections/topic_words.mp3",
        "words": [
          {
            "en": "garden",
            "zh": "花园",
            "full": "",
            "extra": "🌷 植物园地"
          },
          {
            "en": "flower",
            "zh": "花",
            "full": "",
            "extra": "🌸 美丽"
          },
          {
            "en": "vegetable",
            "zh": "蔬菜",
            "full": "",
            "extra": "🥬 吃的植物"
          },
          {
            "en": "plant",
            "zh": "植物",
            "full": "",
            "extra": "🌱 活的"
          },
          {
            "en": "orange tree",
            "zh": "橙子树",
            "full": "",
            "extra": "🍊 柑橘"
          },
          {
            "en": "tomato",
            "zh": "番茄",
            "full": "",
            "extra": "🍅 红色果实"
          },
          {
            "en": "carrot",
            "zh": "胡萝卜",
            "full": "",
            "extra": "🥕 橙色根"
          }
        ],
        "big_task": "Making a school garden report"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          32
        ],
        "audio": "unit3/sections/fun_time.mp3",
        "fun_title": "",
        "fun_content": ""
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          32
        ],
        "audio": "unit3/sections/sound.mp3",
        "sound_letter": "g",
        "sound_pattern": "",
        "sound_example": "garden"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          33,
          34
        ],
        "audio": "unit3/sections/talking_time.mp3",
        "talking_title": "A beautiful school garden",
        "talking_pattern": "What's this/that? It's a/an ...",
        "talking_phrases": [
          "What's this?",
          "It's a flower.",
          "It's an orange tree."
        ],
        "talking_scenario": ""
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          35,
          36
        ],
        "audio": "unit3/sections/story_time.mp3",
        "story_title": "Grandpa's garden",
        "story_summary": "Grandpa 教孩子认识蔬菜水果：tomato, carrot, vegetable 等",
        "story_moral": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          37
        ],
        "audio": "unit3/sections/big_task.mp3",
        "project_title": "My school garden report",
        "project_output": "写学校花园报告"
      }
    ]
  },
  "unit4": {
    "num": "unit4",
    "name": "Water",
    "description": "",
    "duration": "",
    "audio_file": "unit_4.mp3",
    "pdf_start": 38,
    "pdf_end": 45,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          39
        ],
        "audio": "unit4/sections/topic_words.mp3",
        "words": [
          {
            "en": "water",
            "zh": "水",
            "full": "",
            "extra": "💧 H2O · 无色无味"
          },
          {
            "en": "river",
            "zh": "河",
            "full": "",
            "extra": "🏞 陆地流动"
          },
          {
            "en": "lake",
            "zh": "湖",
            "full": "",
            "extra": "🌊 内陆静水"
          },
          {
            "en": "sea",
            "zh": "海",
            "full": "",
            "extra": "🌊 咸的"
          },
          {
            "en": "water vapour",
            "zh": "水蒸气",
            "full": "",
            "extra": "☁️ 气体形态"
          },
          {
            "en": "cloud",
            "zh": "云",
            "full": "",
            "extra": "☁️ 空中水滴"
          },
          {
            "en": "rain",
            "zh": "雨",
            "full": "",
            "extra": "🌧 水滴落下"
          },
          {
            "en": "snow",
            "zh": "雪",
            "full": "",
            "extra": "❄️ 冰晶"
          },
          {
            "en": "ice",
            "zh": "冰",
            "full": "",
            "extra": "🧊 固体水"
          }
        ],
        "big_task": "Making a lab report"
      },
      {
        "id": "rhyme_time",
        "name": "韵文",
        "icon": "🎶",
        "pages": [
          40
        ],
        "audio": "unit4/sections/rhyme_time.mp3",
        "rhyme_title": "",
        "rhyme_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          40
        ],
        "audio": "unit4/sections/sound.mp3",
        "sound_letter": "s",
        "sound_pattern": "",
        "sound_example": "sea"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          41,
          42
        ],
        "audio": "unit4/sections/talking_time.mp3",
        "talking_title": "Where does it come from?",
        "talking_pattern": "Where does/do ... come from? It comes from ...",
        "talking_phrases": [
          "Where does water come from?",
          "It comes from clouds."
        ],
        "talking_scenario": ""
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          43,
          44
        ],
        "audio": "unit4/sections/reading_time.mp3",
        "reading_title": "",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          45
        ],
        "audio": "unit4/sections/big_task.mp3",
        "project_title": "My lab report",
        "project_output": "水的来源实验报告"
      }
    ]
  },
  "unit5": {
    "num": "unit5",
    "name": "I can help",
    "description": "",
    "duration": "",
    "audio_file": "unit_5.mp3",
    "pdf_start": 46,
    "pdf_end": 53,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          47
        ],
        "audio": "unit5/sections/topic_words.mp3",
        "words": [
          {
            "en": "help",
            "zh": "帮助",
            "full": "",
            "extra": "🤝 协助"
          },
          {
            "en": "cook",
            "zh": "做饭",
            "full": "",
            "extra": "🍳 厨房"
          },
          {
            "en": "do the dishes",
            "zh": "洗碗",
            "full": "",
            "extra": "🍽 饭后清洁"
          },
          {
            "en": "clean the table",
            "zh": "擦桌子",
            "full": "",
            "extra": "🧽 餐桌清洁"
          },
          {
            "en": "walk the dog",
            "zh": "遛狗",
            "full": "",
            "extra": "🐕 户外活动"
          },
          {
            "en": "chore",
            "zh": "家务",
            "full": "",
            "extra": "🧹 家务活"
          },
          {
            "en": "give your seat",
            "zh": "让座",
            "full": "",
            "extra": "💺 给需要的人"
          }
        ],
        "big_task": "Being a good helper"
      },
      {
        "id": "song_time",
        "name": "歌曲",
        "icon": "🎵",
        "pages": [
          48
        ],
        "audio": "unit5/sections/song_time.mp3",
        "song_title": "Help with family chores",
        "song_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          48
        ],
        "audio": "unit5/sections/sound.mp3",
        "sound_letter": "i",
        "sound_pattern": "",
        "sound_example": "dish"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          49,
          50
        ],
        "audio": "unit5/sections/talking_time.mp3",
        "talking_title": "Helping others",
        "talking_pattern": "I can ... / Can you ...?",
        "talking_phrases": [
          "I can help my mum.",
          "I can cook."
        ],
        "talking_scenario": ""
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          51,
          52
        ],
        "audio": "unit5/sections/story_time.mp3",
        "story_title": "The ant and the bird",
        "story_summary": "蚂蚁被困，小鸟帮忙；后来小鸟遇险，蚂蚁相助",
        "story_moral": "互相帮助"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          53
        ],
        "audio": "unit5/sections/big_task.mp3",
        "project_title": "Our good helpers",
        "project_output": "做家务的好帮手展示"
      }
    ]
  },
  "unit6": {
    "num": "unit6",
    "name": "How do you feel?",
    "description": "",
    "duration": "",
    "audio_file": "unit_6.mp3",
    "pdf_start": 54,
    "pdf_end": 61,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          55
        ],
        "audio": "unit6/sections/topic_words.mp3",
        "words": [
          {
            "en": "happy",
            "zh": "开心",
            "full": "",
            "extra": "😊 高兴"
          },
          {
            "en": "sad",
            "zh": "难过",
            "full": "",
            "extra": "😢 不开心"
          },
          {
            "en": "good",
            "zh": "好",
            "full": "",
            "extra": "👍 棒"
          },
          {
            "en": "bad",
            "zh": "坏",
            "full": "",
            "extra": "👎 不好"
          },
          {
            "en": "excited",
            "zh": "兴奋",
            "full": "",
            "extra": "🤩 激动"
          },
          {
            "en": "scared",
            "zh": "害怕",
            "full": "",
            "extra": "😨 怕"
          },
          {
            "en": "tired",
            "zh": "累",
            "full": "",
            "extra": "😴 疲倦"
          },
          {
            "en": "unhappy",
            "zh": "不开心",
            "full": "",
            "extra": "🙁 难受"
          }
        ],
        "big_task": "Writing a letter to Mr Tree"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          56
        ],
        "audio": "unit6/sections/fun_time.mp3",
        "fun_title": "",
        "fun_content": ""
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          56
        ],
        "audio": "unit6/sections/sound.mp3",
        "sound_letter": "a",
        "sound_pattern": "",
        "sound_example": "happy"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          57,
          58
        ],
        "audio": "unit6/sections/talking_time.mp3",
        "talking_title": "How do you feel?",
        "talking_pattern": "How do you feel? I'm/We're ...",
        "talking_phrases": [
          "How do you feel?",
          "I'm happy/excited."
        ],
        "talking_scenario": ""
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          59,
          60
        ],
        "audio": "unit6/sections/story_time.mp3",
        "story_title": "Minmin's bad feelings",
        "story_summary": "Minmin 心情不好，朋友们安慰她",
        "story_moral": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          61
        ],
        "audio": "unit6/sections/big_task.mp3",
        "project_title": "A letter to Mr Tree",
        "project_output": "给 Mr Tree 写信倾诉心情"
      }
    ]
  },
  "unit7": {
    "num": "unit7",
    "name": "Jobs",
    "description": "",
    "duration": "",
    "audio_file": "unit_7.mp3",
    "pdf_start": 62,
    "pdf_end": 69,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          63
        ],
        "audio": "unit7/sections/topic_words.mp3",
        "words": [
          {
            "en": "driver",
            "zh": "司机",
            "full": "",
            "extra": "🚗 开车"
          },
          {
            "en": "police officer",
            "zh": "警察",
            "full": "",
            "extra": "👮 抓坏人"
          },
          {
            "en": "engineer",
            "zh": "工程师",
            "full": "",
            "extra": "👷 造东西"
          },
          {
            "en": "writer",
            "zh": "作家",
            "full": "",
            "extra": "✍️ 写书"
          },
          {
            "en": "doctor",
            "zh": "医生",
            "full": "",
            "extra": "👨‍⚕️ 治病"
          },
          {
            "en": "chef",
            "zh": "厨师",
            "full": "",
            "extra": "👨‍🍳 做饭"
          },
          {
            "en": "astronaut",
            "zh": "宇航员",
            "full": "",
            "extra": "🚀 太空"
          }
        ],
        "big_task": "Doing a group interview"
      },
      {
        "id": "song_time",
        "name": "歌曲",
        "icon": "🎵",
        "pages": [
          64
        ],
        "audio": "unit7/sections/song_time.mp3",
        "song_title": "What do you want to be?",
        "song_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          64
        ],
        "audio": "unit7/sections/sound.mp3",
        "sound_letter": "t",
        "sound_pattern": "",
        "sound_example": "teacher"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          65,
          66
        ],
        "audio": "unit7/sections/talking_time.mp3",
        "talking_title": "Dream jobs",
        "talking_pattern": "What's ...? ... is ...",
        "talking_phrases": [
          "What's your job?",
          "I'm an astronaut."
        ],
        "talking_scenario": ""
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          67,
          68
        ],
        "audio": "unit7/sections/reading_time.mp3",
        "reading_title": "",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          69
        ],
        "audio": "unit7/sections/big_task.mp3",
        "project_title": "My group interview",
        "project_output": "小组采访，介绍职业"
      }
    ]
  },
  "unit8": {
    "num": "unit8",
    "name": "Finding places",
    "description": "",
    "duration": "",
    "audio_file": "unit_8.mp3",
    "pdf_start": 70,
    "pdf_end": 77,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          71
        ],
        "audio": "unit8/sections/topic_words.mp3",
        "words": [
          {
            "en": "library",
            "zh": "图书馆",
            "full": "",
            "extra": "📚 借书/看书"
          },
          {
            "en": "find the way",
            "zh": "找路",
            "full": "",
            "extra": "🗺 看地图"
          },
          {
            "en": "get to",
            "zh": "到达",
            "full": "",
            "extra": "🎯 去某地"
          },
          {
            "en": "walk along",
            "zh": "沿着走",
            "full": "",
            "extra": "🚶 顺路走"
          },
          {
            "en": "road",
            "zh": "路",
            "full": "",
            "extra": "🛣 道路"
          },
          {
            "en": "left",
            "zh": "左",
            "full": "",
            "extra": "⬅️ 反义 right"
          },
          {
            "en": "right",
            "zh": "右",
            "full": "",
            "extra": "➡️ 也\"对的\""
          },
          {
            "en": "museum",
            "zh": "博物馆",
            "full": "",
            "extra": "🏛 看展品"
          }
        ],
        "big_task": "Finding the places"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          72
        ],
        "audio": "unit8/sections/fun_time.mp3",
        "fun_title": "",
        "fun_content": ""
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          72
        ],
        "audio": "unit8/sections/sound.mp3",
        "sound_letter": "m",
        "sound_pattern": "",
        "sound_example": "many"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          73,
          74
        ],
        "audio": "unit8/sections/talking_time.mp3",
        "talking_title": "Where is the library?",
        "talking_pattern": "Where is the library/museum? It's ... / Walk along ... Turn left/right at ...",
        "talking_phrases": [
          "Walk along this road.",
          "Turn left at the school."
        ],
        "talking_scenario": ""
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          75,
          76
        ],
        "audio": "unit8/sections/story_time.mp3",
        "story_title": "At the museum",
        "story_summary": "参观博物馆，问路找地方",
        "story_moral": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          77
        ],
        "audio": "unit8/sections/big_task.mp3",
        "project_title": "Finding the places",
        "project_output": "画地图并标注路线"
      }
    ]
  },
  "unit9": {
    "num": "unit9",
    "name": "Special days in China",
    "description": "",
    "duration": "",
    "audio_file": "unit_9.mp3",
    "pdf_start": 78,
    "pdf_end": 85,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          79
        ],
        "audio": "unit9/sections/topic_words.mp3",
        "words": [
          {
            "en": "special days",
            "zh": "特殊日子",
            "full": "",
            "extra": "🎉 节日"
          },
          {
            "en": "the Double Ninth Festival",
            "zh": "重阳节",
            "full": "",
            "extra": "🏔 农历九月初九·敬老"
          },
          {
            "en": "celebrate",
            "zh": "庆祝",
            "full": "",
            "extra": "🎊 过节"
          },
          {
            "en": "Chinese New Year",
            "zh": "春节",
            "full": "",
            "extra": "🧧 农历新年"
          },
          {
            "en": "the Spring Festival",
            "zh": "春节",
            "full": "",
            "extra": "🧧 农历新年·同 Chinese New Year"
          },
          {
            "en": "the Lantern Festival",
            "zh": "元宵节",
            "full": "",
            "extra": "🏮 农历正月十五·吃汤圆"
          },
          {
            "en": "holiday",
            "zh": "假日",
            "full": "",
            "extra": "🏖 放假"
          }
        ],
        "big_task": "Planning New Year activities"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          80
        ],
        "audio": "unit9/sections/fun_time.mp3",
        "fun_title": "",
        "fun_content": ""
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          80
        ],
        "audio": "unit9/sections/sound.mp3",
        "sound_letter": "e",
        "sound_pattern": "",
        "sound_example": "festival"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          81,
          82
        ],
        "audio": "unit9/sections/talking_time.mp3",
        "talking_title": "The Double Ninth Festival",
        "talking_pattern": "Let's ...",
        "talking_phrases": [
          "Let's celebrate together.",
          "Let's visit grandparents."
        ],
        "talking_scenario": ""
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          83,
          84
        ],
        "audio": "unit9/sections/reading_time.mp3",
        "reading_title": "",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          85
        ],
        "audio": "unit9/sections/big_task.mp3",
        "project_title": "My New Year plan",
        "project_output": "新年活动计划"
      }
    ]
  },
  "unit10": {
    "num": "unit10",
    "name": "Foods around the world",
    "description": "",
    "duration": "",
    "audio_file": "unit_10.mp3",
    "pdf_start": 86,
    "pdf_end": 93,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          87
        ],
        "audio": "unit10/sections/topic_words.mp3",
        "words": [
          {
            "en": "food",
            "zh": "食物",
            "full": "",
            "extra": "🍴 吃的"
          },
          {
            "en": "noodles",
            "zh": "面条",
            "full": "",
            "extra": "🍜 中国·长条"
          },
          {
            "en": "pizza",
            "zh": "披萨",
            "full": "",
            "extra": "🍕 意大利·圆形"
          },
          {
            "en": "sandwich",
            "zh": "三明治",
            "full": "",
            "extra": "🥪 夹心面包"
          },
          {
            "en": "hot dog",
            "zh": "热狗",
            "full": "",
            "extra": "🌭 美国·香肠面包"
          },
          {
            "en": "fish and chips",
            "zh": "炸鱼薯条",
            "full": "",
            "extra": "🐟 英国经典"
          },
          {
            "en": "beef",
            "zh": "牛肉",
            "full": "",
            "extra": "🐄 红色肉类"
          },
          {
            "en": "bread",
            "zh": "面包",
            "full": "",
            "extra": "🍞 西方主食"
          },
          {
            "en": "cake",
            "zh": "蛋糕",
            "full": "",
            "extra": "🎂 生日庆祝"
          }
        ],
        "big_task": "Making a food card"
      },
      {
        "id": "chant_time",
        "name": "chant 跟读",
        "icon": "🗣",
        "pages": [
          88
        ],
        "audio": "unit10/sections/chant_time.mp3",
        "chant_title": "",
        "chant_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          88
        ],
        "audio": "unit10/sections/sound.mp3",
        "sound_letter": "n",
        "sound_pattern": "",
        "sound_example": "noodles"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          89,
          90
        ],
        "audio": "unit10/sections/talking_time.mp3",
        "talking_title": "World Food Festival",
        "talking_pattern": "There is/are ...",
        "talking_phrases": [
          "There is pizza.",
          "There are noodles."
        ],
        "talking_scenario": ""
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          91,
          92
        ],
        "audio": "unit10/sections/story_time.mp3",
        "story_title": "Magic Flour",
        "story_summary": "魔法面粉做各国食物",
        "story_moral": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          93
        ],
        "audio": "unit10/sections/big_task.mp3",
        "project_title": "My food card",
        "project_output": "做食物卡片"
      }
    ]
  }
};
