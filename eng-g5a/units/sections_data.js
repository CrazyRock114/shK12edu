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
          "art",
          "gardening",
          "storytelling",
          "take photos"
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
        "audio": "unit1/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          19
        ],
        "audio": "unit1/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          20,
          21
        ],
        "audio": "unit1/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          22
        ],
        "audio": "unit_1.mp3",
        "is_fallback": true
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          23
        ],
        "audio": "unit1/sections/big_task.mp3"
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
          "traditional",
          "Chinese yo-yo",
          "kite-flying",
          "dragon dance",
          "tug of war"
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
        "audio": "unit2/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          27
        ],
        "audio": "unit2/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          28,
          29
        ],
        "audio": "unit2/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          30
        ],
        "audio": "unit_2.mp3",
        "is_fallback": true
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          31
        ],
        "audio": "unit_2.mp3",
        "is_fallback": true
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
          "root",
          "stem",
          "leaf",
          "soil",
          "water lily",
          "pine cone",
          "morning glory"
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
        "is_fallback": true
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          34
        ],
        "audio": "unit3/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          35,
          36
        ],
        "audio": "unit3/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          37,
          38
        ],
        "audio": "unit3/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          39
        ],
        "audio": "unit3/sections/big_task.mp3"
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
          "safari park",
          "tiger",
          "lion",
          "whale",
          "panda",
          "giraffe",
          "hippo",
          "elephant"
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
        "audio": "unit4/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          42
        ],
        "audio": "unit4/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          43,
          44
        ],
        "audio": "unit4/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          45,
          46
        ],
        "audio": "unit4/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          47
        ],
        "audio": "unit4/sections/big_task.mp3"
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
          "doctor",
          "cough",
          "runny nose",
          "nurse",
          "fever",
          "medicine"
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
        "is_fallback": true
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          51
        ],
        "audio": "unit5/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          52,
          53
        ],
        "audio": "unit5/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          54
        ],
        "audio": "unit_5.mp3",
        "is_fallback": true
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          55
        ],
        "audio": "unit5/sections/big_task.mp3"
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
          "try my best",
          "will",
          "succeed",
          "practice",
          "better",
          "give up"
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
        "audio": "unit6/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          58
        ],
        "audio": "unit_6.mp3",
        "is_fallback": true
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          59,
          60
        ],
        "audio": "unit6/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          61,
          62
        ],
        "audio": "unit6/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          63
        ],
        "audio": "unit6/sections/big_task.mp3"
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
          "scientist",
          "explore",
          "famous",
          "discover",
          "creative",
          "hard-working",
          "(be) known as"
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
        "is_fallback": true
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          66
        ],
        "audio": "unit_7.mp3",
        "is_fallback": true
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          67,
          68
        ],
        "audio": "unit7/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          69,
          70
        ],
        "audio": "unit7/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          71
        ],
        "audio": "unit7/sections/big_task.mp3"
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
          "useful",
          "invention",
          "problem",
          "wheel",
          "printing",
          "television",
          "light",
          "robot"
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
        "audio": "unit8/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          74
        ],
        "audio": "unit8/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          75,
          76
        ],
        "audio": "unit8/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          77,
          78
        ],
        "audio": "unit8/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          79
        ],
        "audio": "unit8/sections/big_task.mp3"
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
          "laptop",
          "password",
          "mouse",
          "click",
          "keyboard",
          "email",
          "delete"
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
        "audio": "unit9/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          82
        ],
        "audio": "unit9/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          83,
          84
        ],
        "audio": "unit9/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          85,
          86
        ],
        "audio": "unit9/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          87
        ],
        "audio": "unit9/sections/big_task.mp3"
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
          "reduce",
          "reuse",
          "recycle",
          "throw away",
          "turn off",
          "pick up"
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
        "is_fallback": true
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          90
        ],
        "audio": "unit10/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          91,
          92
        ],
        "audio": "unit10/sections/talking_time.mp3"
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
        "is_fallback": true
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          95
        ],
        "audio": "unit10/sections/big_task.mp3"
      }
    ]
  }
};
