// G5A 11 单元 sections 切分（数据驱动）
// 每段含 {id, name, icon, pages[], audio, words?}
const SECTIONS_DATA = {
  "starter": {
    "num": "starter",
    "name": "Starter",
    "description": "",
    "duration": "",
    "audio_file": "starter.mp3",
    "pdf_start": 9,
    "pdf_end": 15,
    "sections": [
      {
        "id": "families_and_friends",
        "name": "我们的家人与朋友",
        "icon": "👨‍👩‍👧‍👦",
        "pages": [
          9
        ],
        "audio": "starter.mp3"
      },
      {
        "id": "our_teachers",
        "name": "我们的老师",
        "icon": "👩‍🏫",
        "pages": [
          10
        ],
        "audio": "starter.mp3"
      },
      {
        "id": "at_school",
        "name": "在学校",
        "icon": "🏫",
        "pages": [
          11,
          12
        ],
        "audio": "starter/sections/at_school.mp3"
      },
      {
        "id": "study_skills",
        "name": "学习技巧",
        "icon": "📖",
        "pages": [
          13,
          14
        ],
        "audio": "starter/sections/study_skills.mp3"
      },
      {
        "id": "numbers",
        "name": "数字",
        "icon": "🔢",
        "pages": [
          15
        ],
        "audio": "starter/sections/numbers.mp3"
      },
      {
        "id": "months",
        "name": "月份",
        "icon": "📅",
        "pages": [
          15
        ],
        "audio": "starter/sections/months.mp3"
      }
    ]
  },
  "unit1": {
    "num": "unit1",
    "name": "Clubs in our school",
    "description": "",
    "duration": "",
    "audio_file": "unit_1.mp3",
    "pdf_start": 16,
    "pdf_end": 23,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          17
        ],
        "audio": "unit1/sections/topic_words.mp3",
        "words": [
          {
            "en": "art",
            "zh": "艺术",
            "full": "art club 艺术社团",
            "extra": "🎨 美术课"
          },
          {
            "en": "gardening",
            "zh": "园艺",
            "full": "gardening club 园艺社",
            "extra": "🌷 种花种菜"
          },
          {
            "en": "storytelling",
            "zh": "讲故事",
            "full": "storytelling club 故事社",
            "extra": "📖 表演故事"
          },
          {
            "en": "take photos",
            "zh": "拍照",
            "full": "take photos 拍照",
            "extra": "📷 用相机"
          }
        ],
        "big_task": "Making a photo diary of a club"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          18
        ],
        "audio": "unit1/sections/fun_time.mp3",
        "fun_title": "Come and join our clubs!",
        "fun_content": "学校社团招新：Reading Club, Art Club, Storytelling Club, Photo Club 等"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          19
        ],
        "audio": "unit1/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "ph",
        "sound_example": "photo"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          20,
          21
        ],
        "audio": "unit1/sections/talking_time.mp3",
        "talking_title": "It's good to join clubs",
        "talking_pattern": "I'm/I'm going to...",
        "talking_phrases": [
          "I'm glad you like it.",
          "I'm going to join the Photo Club this year.",
          "You can meet new friends and have fun!"
        ],
        "talking_scenario": "Shenshen 跟 Xiaojiang 聊摄影、加入 Photo Club 的打算"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          22
        ],
        "audio": "unit_1.mp3",
        "is_fallback": true,
        "story_title": "At the Art Club",
        "story_summary": "Art Club 里 Miss Li 让大家画 brush pot, James 觉得难, Xiaopu 教他画竹子 (Don't give up), 最后 James 完成了 nice bamboo brush pot, 领悟 easy-easier。",
        "story_moral": "不放弃 + 互相帮助 + 熟能生巧"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          23
        ],
        "audio": "unit1/sections/big_task.mp3",
        "project_title": "My photo diary of a club",
        "project_output": "做一本社团照片日记"
      }
    ]
  },
  "unit2": {
    "num": "unit2",
    "name": "Traditional games",
    "description": "",
    "duration": "",
    "audio_file": "unit_2.mp3",
    "pdf_start": 24,
    "pdf_end": 31,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          25
        ],
        "audio": "unit2/sections/topic_words.mp3",
        "words": [
          {
            "en": "traditional",
            "zh": "传统的",
            "full": "traditional games 传统游戏",
            "extra": "🏛 古老的"
          },
          {
            "en": "Chinese yo-yo",
            "zh": "中国溜溜球",
            "full": "Chinese yo-yo 中国溜溜球",
            "extra": "🪀 空竹"
          },
          {
            "en": "kite-flying",
            "zh": "放风筝",
            "full": "kite-flying 放风筝",
            "extra": "🪁 春季活动"
          },
          {
            "en": "dragon dance",
            "zh": "舞龙",
            "full": "dragon dance 舞龙",
            "extra": "🐉 春节表演"
          },
          {
            "en": "tug of war",
            "zh": "拔河",
            "full": "tug of war 拔河",
            "extra": "🪢 团队比赛"
          }
        ],
        "big_task": "Talking about my favourite traditional game"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          26
        ],
        "audio": "unit2/sections/fun_time.mp3",
        "fun_title": "Welcome to our garden party!",
        "fun_content": "Garden party 邀请函，集章换奖品"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          27
        ],
        "audio": "unit2/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "ar",
        "sound_example": "garden"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          28,
          29
        ],
        "audio": "unit2/sections/talking_time.mp3",
        "talking_title": "As fast as the wind",
        "talking_pattern": "Look at me. I look/move/stand/sit like a...",
        "talking_phrases": [
          "Is this Shaolin kung fu?",
          "This is changquan. It's the mother of many kung fu styles.",
          "Stand like a pine tree.",
          "Move as fast as the wind."
        ],
        "talking_scenario": "James 问 Mr Zhong 关于长拳，描述武术动作"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          30
        ],
        "audio": "unit_2.mp3",
        "is_fallback": true,
        "story_title": "The dragon dance",
        "story_summary": "Dragon Dance Club 为 garden party 训练，Minmin 跑太快导致队伍不协调，Mr Zhong 教 teamwork，按音乐节奏齐步走，长龙活起来。",
        "story_moral": "团队协作 + 听从指挥"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          31
        ],
        "audio": "unit_2.mp3",
        "is_fallback": true,
        "project_title": "Talking about my favourite traditional game",
        "project_output": "介绍自己最喜欢的传统游戏"
      }
    ]
  },
  "unit3": {
    "num": "unit3",
    "name": "Amazing plants",
    "description": "",
    "duration": "",
    "audio_file": "unit_3.mp3",
    "pdf_start": 32,
    "pdf_end": 39,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          33
        ],
        "audio": "unit3/sections/topic_words.mp3",
        "words": [
          {
            "en": "root",
            "zh": "根",
            "full": "root 根",
            "extra": "🌱 地下部分"
          },
          {
            "en": "stem",
            "zh": "茎",
            "full": "stem 茎",
            "extra": "🌿 支撑"
          },
          {
            "en": "leaf",
            "zh": "叶",
            "full": "leaf 叶",
            "extra": "🍃 光合作用"
          },
          {
            "en": "soil",
            "zh": "土壤",
            "full": "soil 土壤",
            "extra": "🪨 植物生长"
          },
          {
            "en": "water lily",
            "zh": "睡莲",
            "full": "water lily 睡莲",
            "extra": "🪷 池塘花"
          },
          {
            "en": "pine cone",
            "zh": "松果",
            "full": "pine cone 松果",
            "extra": "🌲 松树果实"
          },
          {
            "en": "morning glory",
            "zh": "牵牛花",
            "full": "morning glory 牵牛花",
            "extra": "🌸 喇叭花"
          }
        ],
        "big_task": "Making a plant poster"
      },
      {
        "id": "chant_time",
        "name": "chant 跟读",
        "icon": "🗣",
        "pages": [
          34
        ],
        "audio": "unit_3.mp3",
        "is_fallback": true,
        "chant_title": "",
        "chant_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          34
        ],
        "audio": "unit3/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "",
        "sound_example": ""
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          35,
          36
        ],
        "audio": "unit3/sections/talking_time.mp3",
        "talking_title": "Plants and the weather",
        "talking_pattern": "look(s) like...",
        "talking_phrases": [
          "What does it look like?",
          "It looks like a...",
          "Plants can tell us about the weather."
        ],
        "talking_scenario": "描述植物外形 + 植物预兆天气"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          37,
          38
        ],
        "audio": "unit3/sections/reading_time.mp3",
        "reading_title": "Plants and the weather",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          39
        ],
        "audio": "unit3/sections/big_task.mp3",
        "project_title": "My plant poster",
        "project_output": "做植物海报"
      }
    ]
  },
  "unit4": {
    "num": "unit4",
    "name": "Together with animals",
    "description": "",
    "duration": "",
    "audio_file": "unit_4.mp3",
    "pdf_start": 40,
    "pdf_end": 47,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          41
        ],
        "audio": "unit4/sections/topic_words.mp3",
        "words": [
          {
            "en": "safari park",
            "zh": "野生动物园",
            "full": "safari park 野生动物园",
            "extra": "🦁 半野生"
          },
          {
            "en": "tiger",
            "zh": "老虎",
            "full": "tiger 老虎",
            "extra": "🐅 丛林之王"
          },
          {
            "en": "lion",
            "zh": "狮子",
            "full": "lion 狮子",
            "extra": "🦁 万兽之王"
          },
          {
            "en": "whale",
            "zh": "鲸鱼",
            "full": "whale 鲸鱼",
            "extra": "🐋 海洋最大"
          },
          {
            "en": "panda",
            "zh": "熊猫",
            "full": "panda 熊猫",
            "extra": "🐼 中国国宝"
          },
          {
            "en": "giraffe",
            "zh": "长颈鹿",
            "full": "giraffe 长颈鹿",
            "extra": "🦒 最高动物"
          },
          {
            "en": "hippo",
            "zh": "河马",
            "full": "hippo 河马",
            "extra": "🦛 水中巨兽"
          },
          {
            "en": "elephant",
            "zh": "大象",
            "full": "elephant 大象",
            "extra": "🐘 陆地最大"
          }
        ],
        "big_task": "Writing a diary"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          42
        ],
        "audio": "unit4/sections/fun_time.mp3",
        "fun_title": "A welcome letter",
        "fun_content": "Safari Park 欢迎信，介绍各种动物"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          42
        ],
        "audio": "unit4/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "",
        "sound_example": ""
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          43,
          44
        ],
        "audio": "unit4/sections/talking_time.mp3",
        "talking_title": "In a safari park",
        "talking_pattern": "feel/look/taste (adj.)...",
        "talking_phrases": [
          "The tiger looks scary.",
          "The fish tastes good.",
          "The fur feels soft."
        ],
        "talking_scenario": "在野生动物园描述动物感受"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          45,
          46
        ],
        "audio": "unit4/sections/reading_time.mp3",
        "reading_title": "An animal keeper's diary",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          47
        ],
        "audio": "unit4/sections/big_task.mp3",
        "project_title": "My diary",
        "project_output": "写一篇自己的日记（动物主题）"
      }
    ]
  },
  "unit5": {
    "num": "unit5",
    "name": "Seeing a doctor",
    "description": "",
    "duration": "",
    "audio_file": "unit_5.mp3",
    "pdf_start": 48,
    "pdf_end": 55,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          49
        ],
        "audio": "unit5/sections/topic_words.mp3",
        "words": [
          {
            "en": "doctor",
            "zh": "医生",
            "full": "doctor 医生",
            "extra": "👨‍⚕️ 看病"
          },
          {
            "en": "cough",
            "zh": "咳嗽",
            "full": "cough 咳嗽",
            "extra": "😷 喉咙"
          },
          {
            "en": "runny nose",
            "zh": "流鼻涕",
            "full": "runny nose 流鼻涕",
            "extra": "🤧 感冒症状"
          },
          {
            "en": "nurse",
            "zh": "护士",
            "full": "nurse 护士",
            "extra": "👩‍⚕️ 协助医生"
          },
          {
            "en": "fever",
            "zh": "发烧",
            "full": "fever 发烧",
            "extra": "🤒 体温高"
          },
          {
            "en": "medicine",
            "zh": "药",
            "full": "medicine 药",
            "extra": "💊 治疗"
          }
        ],
        "big_task": "Giving health tips"
      },
      {
        "id": "rhyme_time",
        "name": "韵文",
        "icon": "🎶",
        "pages": [
          50
        ],
        "audio": "unit_5.mp3",
        "is_fallback": true,
        "rhyme_title": "Nice doctors",
        "rhyme_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          51
        ],
        "audio": "unit5/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "",
        "sound_example": ""
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          52,
          53
        ],
        "audio": "unit5/sections/talking_time.mp3",
        "talking_title": "At the doctor's",
        "talking_pattern": "Don't (do)...",
        "talking_phrases": [
          "What's the matter?",
          "I have a fever.",
          "Don't eat too much candy.",
          "Take the medicine."
        ],
        "talking_scenario": "看医生时描述病症 + 健康建议"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          54
        ],
        "audio": "unit_5.mp3",
        "is_fallback": true,
        "story_title": "The story of Hua Tuo",
        "story_summary": "华佗给病人治病的故事：有人喊痛，华佗想如何减痛；另一人喝醉摔断腿，华佗用麻沸散让他睡着不感觉痛。",
        "story_moral": "医者智慧 + 减轻病人痛苦"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          55
        ],
        "audio": "unit5/sections/big_task.mp3",
        "project_title": "My health tips",
        "project_output": "做健康小贴士海报"
      }
    ]
  },
  "unit6": {
    "num": "unit6",
    "name": "Try my best",
    "description": "",
    "duration": "",
    "audio_file": "unit_6.mp3",
    "pdf_start": 56,
    "pdf_end": 63,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          57
        ],
        "audio": "unit6/sections/topic_words.mp3",
        "words": [
          {
            "en": "try my best",
            "zh": "尽我所能",
            "full": "try my best 尽我所能",
            "extra": "💪 努力"
          },
          {
            "en": "will",
            "zh": "将",
            "full": "will will 将会",
            "extra": "⏰ 将来时"
          },
          {
            "en": "succeed",
            "zh": "成功",
            "full": "succeed 成功",
            "extra": "🏆 达成"
          },
          {
            "en": "practice",
            "zh": "练习",
            "full": "practice 练习",
            "extra": "🎯 反复"
          },
          {
            "en": "better",
            "zh": "更好",
            "full": "better 更好",
            "extra": "📈 进步"
          },
          {
            "en": "give up",
            "zh": "放弃",
            "full": "give up 放弃",
            "extra": "🚫 停止"
          }
        ],
        "big_task": "Writing a letter to future me"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          58
        ],
        "audio": "unit6/sections/fun_time.mp3",
        "fun_title": "Wise words from great minds",
        "fun_content": "名人名言 / 鼓励"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          58
        ],
        "audio": "unit_6.mp3",
        "is_fallback": true,
        "sound_letter": "",
        "sound_pattern": "",
        "sound_example": ""
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          59,
          60
        ],
        "audio": "unit6/sections/talking_time.mp3",
        "talking_title": "Be better",
        "talking_pattern": "was/were...",
        "talking_phrases": [
          "I was short.",
          "Now I am tall.",
          "I was bad at English.",
          "Now I'm good at it.",
          "I will try my best."
        ],
        "talking_scenario": "对比过去和现在，展望未来"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          61,
          62
        ],
        "audio": "unit6/sections/story_time.mp3",
        "story_title": "My left foot",
        "story_summary": "讲述者 4 个月大时生病只能动左脚，妈妈不放弃教他读写，问他「喜欢这个故事吗？点头/摇头」，最终成为现在的自己。",
        "story_moral": "不放弃 + 妈妈的爱 + 意志力"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          63
        ],
        "audio": "unit6/sections/big_task.mp3",
        "project_title": "A letter to future me",
        "project_output": "给未来的自己写封信"
      }
    ]
  },
  "unit7": {
    "num": "unit7",
    "name": "Great scientists",
    "description": "",
    "duration": "",
    "audio_file": "unit_7.mp3",
    "pdf_start": 64,
    "pdf_end": 71,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          65
        ],
        "audio": "unit7/sections/topic_words.mp3",
        "words": [
          {
            "en": "scientist",
            "zh": "科学家",
            "full": "scientist 科学家",
            "extra": "🔬 研究自然"
          },
          {
            "en": "explore",
            "zh": "探索",
            "full": "explore 探索",
            "extra": "🔍 寻找"
          },
          {
            "en": "famous",
            "zh": "著名的",
            "full": "famous 著名的",
            "extra": "⭐ 出名"
          },
          {
            "en": "discover",
            "zh": "发现",
            "full": "discover 发现",
            "extra": "💡 找到新的"
          },
          {
            "en": "creative",
            "zh": "有创造力的",
            "full": "creative 有创造力的",
            "extra": "💡 创新"
          },
          {
            "en": "hard-working",
            "zh": "勤奋的",
            "full": "hard-working 勤奋的",
            "extra": "💪 努力"
          },
          {
            "en": "(be) known as",
            "zh": "被称为",
            "full": "(be) known as 被称为",
            "extra": "🏷 名字是"
          }
        ],
        "big_task": "Making a mini-book of great scientists"
      },
      {
        "id": "rhyme_time",
        "name": "韵文",
        "icon": "🎶",
        "pages": [
          66
        ],
        "audio": "unit_7.mp3",
        "is_fallback": true,
        "rhyme_title": "Science",
        "rhyme_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          66
        ],
        "audio": "unit_7.mp3",
        "is_fallback": true,
        "sound_letter": "",
        "sound_pattern": "",
        "sound_example": ""
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          67,
          68
        ],
        "audio": "unit7/sections/talking_time.mp3",
        "talking_title": "Do you know them?",
        "talking_pattern": "This is ..., a/the ...",
        "talking_phrases": [
          "This is Yuan Longping.",
          "He is known as the 'Father of Hybrid Rice'.",
          "He was creative and hard-working."
        ],
        "talking_scenario": "介绍著名科学家"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          69,
          70
        ],
        "audio": "unit7/sections/reading_time.mp3",
        "reading_title": "Great scientists",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          71
        ],
        "audio": "unit7/sections/big_task.mp3",
        "project_title": "A mini-book of great scientists",
        "project_output": "做一本科学家 mini-book"
      }
    ]
  },
  "unit8": {
    "num": "unit8",
    "name": "Useful inventions",
    "description": "",
    "duration": "",
    "audio_file": "unit_8.mp3",
    "pdf_start": 72,
    "pdf_end": 79,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          73
        ],
        "audio": "unit8/sections/topic_words.mp3",
        "words": [
          {
            "en": "useful",
            "zh": "有用的",
            "full": "useful 有用的",
            "extra": "👍 有帮助"
          },
          {
            "en": "invention",
            "zh": "发明",
            "full": "invention 发明",
            "extra": "💡 新创造"
          },
          {
            "en": "problem",
            "zh": "问题",
            "full": "problem 问题",
            "extra": "❓ 困难"
          },
          {
            "en": "wheel",
            "zh": "轮子",
            "full": "wheel 轮子",
            "extra": "☸️ 圆形"
          },
          {
            "en": "printing",
            "zh": "印刷",
            "full": "printing 印刷",
            "extra": "📖 印书"
          },
          {
            "en": "television",
            "zh": "电视",
            "full": "television 电视",
            "extra": "📺 看节目"
          },
          {
            "en": "light",
            "zh": "灯",
            "full": "light 灯/光",
            "extra": "💡 照明"
          },
          {
            "en": "robot",
            "zh": "机器人",
            "full": "robot 机器人",
            "extra": "🤖 智能"
          }
        ],
        "big_task": "Making an ad for a useful invention"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          74
        ],
        "audio": "unit8/sections/fun_time.mp3",
        "fun_title": "Great inventions around us",
        "fun_content": "身边伟大的发明"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          74
        ],
        "audio": "unit8/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "or",
        "sound_example": "important"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          75,
          76
        ],
        "audio": "unit8/sections/talking_time.mp3",
        "talking_title": "New inventions",
        "talking_pattern": "It's important to (do)...",
        "talking_phrases": [
          "What is it?",
          "It's a new invention.",
          "It's important to read more.",
          "It can help us..."
        ],
        "talking_scenario": "介绍新发明 + 表达重要性"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          77,
          78
        ],
        "audio": "unit8/sections/reading_time.mp3",
        "reading_title": "The wheel moves on",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          79
        ],
        "audio": "unit8/sections/big_task.mp3",
        "project_title": "An ad for a useful invention",
        "project_output": "为有用发明写一则广告"
      }
    ]
  },
  "unit9": {
    "num": "unit9",
    "name": "Using computers",
    "description": "",
    "duration": "",
    "audio_file": "unit_9.mp3",
    "pdf_start": 80,
    "pdf_end": 87,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          81
        ],
        "audio": "unit9/sections/topic_words.mp3",
        "words": [
          {
            "en": "laptop",
            "zh": "笔记本电脑",
            "full": "laptop 笔记本电脑",
            "extra": "💻 便携"
          },
          {
            "en": "password",
            "zh": "密码",
            "full": "password 密码",
            "extra": "🔒 保密"
          },
          {
            "en": "mouse",
            "zh": "鼠标",
            "full": "mouse 鼠标",
            "extra": "🖱 电脑配件"
          },
          {
            "en": "click",
            "zh": "点击",
            "full": "click 点击",
            "extra": "👆 鼠标动作"
          },
          {
            "en": "keyboard",
            "zh": "键盘",
            "full": "keyboard 键盘",
            "extra": "⌨️ 打字"
          },
          {
            "en": "email",
            "zh": "电子邮件",
            "full": "email 电子邮件",
            "extra": "📧 网络信件"
          },
          {
            "en": "delete",
            "zh": "删除",
            "full": "delete 删除",
            "extra": "🗑 移除"
          }
        ],
        "big_task": "Making a quiz about computers"
      },
      {
        "id": "fun_time",
        "name": "趣味活动",
        "icon": "🎮",
        "pages": [
          82
        ],
        "audio": "unit9/sections/fun_time.mp3",
        "fun_title": "Computer quiz",
        "fun_content": "电脑知识小测验"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          82
        ],
        "audio": "unit9/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "ck",
        "sound_example": "click"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          83,
          84
        ],
        "audio": "unit9/sections/talking_time.mp3",
        "talking_title": "All about computers",
        "talking_pattern": "as...as...",
        "talking_phrases": [
          "The computer is as fast as the wind.",
          "He is as tall as his father.",
          "The screen is as big as a book."
        ],
        "talking_scenario": "用 as...as 比较电脑性能/特征"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          85,
          86
        ],
        "audio": "unit9/sections/reading_time.mp3",
        "reading_title": "Got a problem? Ask Simon!",
        "reading_content": ""
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          87
        ],
        "audio": "unit9/sections/big_task.mp3",
        "project_title": "My computer quiz",
        "project_output": "做一份电脑知识小测验"
      }
    ]
  },
  "unit10": {
    "num": "unit10",
    "name": "A greener life",
    "description": "",
    "duration": "",
    "audio_file": "unit_10.mp3",
    "pdf_start": 88,
    "pdf_end": 95,
    "sections": [
      {
        "id": "topic_words",
        "name": "主题词",
        "icon": "📚",
        "pages": [
          89
        ],
        "audio": "unit10/sections/topic_words.mp3",
        "words": [
          {
            "en": "reduce",
            "zh": "减少",
            "full": "reduce 减少使用",
            "extra": "📉 变少"
          },
          {
            "en": "reuse",
            "zh": "再利用",
            "full": "reuse 再利用",
            "extra": "♻️ 重复用"
          },
          {
            "en": "recycle",
            "zh": "回收",
            "full": "recycle 回收",
            "extra": "♻️ 分类处理"
          },
          {
            "en": "throw away",
            "zh": "扔掉",
            "full": "throw away 扔掉",
            "extra": "🗑 丢弃"
          },
          {
            "en": "turn off",
            "zh": "关掉",
            "full": "turn off 关掉",
            "extra": "🔌 关闭电源"
          },
          {
            "en": "pick up",
            "zh": "捡起",
            "full": "pick up 捡起",
            "extra": "✋ 拾起"
          }
        ],
        "big_task": "Making a booklet on a greener life"
      },
      {
        "id": "song_time",
        "name": "歌曲",
        "icon": "🎵",
        "pages": [
          90
        ],
        "audio": "unit_10.mp3",
        "is_fallback": true,
        "song_title": "Reduce, reuse, recycle",
        "song_lyrics": []
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          90
        ],
        "audio": "unit10/sections/sound.mp3",
        "sound_letter": "",
        "sound_pattern": "oy",
        "sound_example": "boy"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          91,
          92
        ],
        "audio": "unit10/sections/talking_time.mp3",
        "talking_title": "Habits for a greener life",
        "talking_pattern": "It is a good way to (do)...",
        "talking_phrases": [
          "What can we do for the Earth?",
          "We can reduce, reuse and recycle.",
          "It is a good way to save water.",
          "Don't throw rubbish away."
        ],
        "talking_scenario": "讨论环保习惯"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          93,
          94
        ],
        "audio": "unit_10.mp3",
        "is_fallback": true,
        "story_title": "Baggie's new life",
        "story_summary": "塑料袋 Baggie 被丢进海里，鲸鱼和海龟先后误食都吐出，Baggie 思考自己的新生活，呼吁减少塑料污染。",
        "story_moral": "环保意识 + 减少塑料 + 保护海洋"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          95
        ],
        "audio": "unit10/sections/big_task.mp3",
        "project_title": "Our booklet on a greener life",
        "project_output": "做一本环保生活手册"
      }
    ]
  }
};
