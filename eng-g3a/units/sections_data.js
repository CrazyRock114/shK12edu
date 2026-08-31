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
        "id": "alphabet",
        "name": "字母表",
        "icon": "🔤",
        "pages": [
          11
        ],
        "audio": "starter.mp3"
      },
      {
        "id": "seasons",
        "name": "季节",
        "icon": "🌤",
        "pages": [
          12
        ],
        "audio": "starter.mp3"
      },
      {
        "id": "numbers",
        "name": "数字",
        "icon": "🔢",
        "pages": [
          12
        ],
        "audio": "starter.mp3"
      },
      {
        "id": "countries",
        "name": "国家",
        "icon": "🌍",
        "pages": [
          13
        ],
        "audio": "starter.mp3"
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
          "school",
          "classmate",
          "teacher",
          "play sports",
          "read",
          "book",
          "study",
          "friend"
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
        "audio": "unit1/sections/song_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          16
        ],
        "audio": "unit1/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          17,
          18
        ],
        "audio": "unit1/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          19,
          20
        ],
        "audio": "unit1/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          21
        ],
        "audio": "unit1/sections/big_task.mp3"
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
          "draw",
          "tell a story",
          "dance",
          "sing",
          "use the computer",
          "run",
          "jump"
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
        "audio": "unit2/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          24
        ],
        "audio": "unit2/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          25,
          26
        ],
        "audio": "unit2/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          27,
          28
        ],
        "audio": "unit2/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          29
        ],
        "audio": "unit2/sections/big_task.mp3"
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
          "garden",
          "flower",
          "vegetable",
          "plant",
          "orange tree",
          "tomato",
          "carrot"
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
        "audio": "unit3/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          32
        ],
        "audio": "unit3/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          33,
          34
        ],
        "audio": "unit3/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          35,
          36
        ],
        "audio": "unit3/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          37
        ],
        "audio": "unit3/sections/big_task.mp3"
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
          "water",
          "river",
          "lake",
          "sea",
          "water vapour",
          "cloud",
          "rain",
          "snow",
          "ice"
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
        "audio": "unit4/sections/rhyme_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          40
        ],
        "audio": "unit4/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          41,
          42
        ],
        "audio": "unit4/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          43,
          44
        ],
        "audio": "unit4/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          45
        ],
        "audio": "unit4/sections/big_task.mp3"
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
          "help",
          "cook",
          "do the dishes",
          "clean the table",
          "walk the dog",
          "chore",
          "give your seat"
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
        "audio": "unit5/sections/song_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          48
        ],
        "audio": "unit5/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          49,
          50
        ],
        "audio": "unit5/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          51,
          52
        ],
        "audio": "unit5/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          53
        ],
        "audio": "unit5/sections/big_task.mp3"
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
          "happy",
          "sad",
          "good",
          "bad",
          "excited",
          "scared",
          "tired",
          "unhappy"
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
        "audio": "unit6/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          56
        ],
        "audio": "unit6/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          57,
          58
        ],
        "audio": "unit6/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          59,
          60
        ],
        "audio": "unit6/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          61
        ],
        "audio": "unit6/sections/big_task.mp3"
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
          "driver",
          "police officer",
          "engineer",
          "writer",
          "doctor",
          "chef",
          "astronaut"
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
        "audio": "unit7/sections/song_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          64
        ],
        "audio": "unit7/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          65,
          66
        ],
        "audio": "unit7/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          67,
          68
        ],
        "audio": "unit7/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          69
        ],
        "audio": "unit7/sections/big_task.mp3"
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
          "library",
          "find the way",
          "get to",
          "walk along",
          "road",
          "left",
          "right",
          "museum"
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
        "audio": "unit8/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          72
        ],
        "audio": "unit8/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          73,
          74
        ],
        "audio": "unit8/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          75,
          76
        ],
        "audio": "unit8/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          77
        ],
        "audio": "unit8/sections/big_task.mp3"
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
          "special days",
          "the Double Ninth Festival",
          "celebrate",
          "Chinese New Year",
          "the Spring Festival",
          "the Lantern Festival",
          "holiday"
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
        "audio": "unit9/sections/fun_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          80
        ],
        "audio": "unit9/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          81,
          82
        ],
        "audio": "unit9/sections/talking_time.mp3"
      },
      {
        "id": "reading_time",
        "name": "阅读",
        "icon": "📚",
        "pages": [
          83,
          84
        ],
        "audio": "unit9/sections/reading_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          85
        ],
        "audio": "unit9/sections/big_task.mp3"
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
          "food",
          "noodles",
          "pizza",
          "sandwich",
          "hot dog",
          "fish and chips",
          "beef",
          "bread",
          "cake"
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
        "audio": "unit10/sections/chant_time.mp3"
      },
      {
        "id": "sound",
        "name": "发音",
        "icon": "🗣",
        "pages": [
          88
        ],
        "audio": "unit10/sections/sound.mp3"
      },
      {
        "id": "talking_time",
        "name": "对话",
        "icon": "💬",
        "pages": [
          89,
          90
        ],
        "audio": "unit10/sections/talking_time.mp3"
      },
      {
        "id": "story_time",
        "name": "故事",
        "icon": "📖",
        "pages": [
          91,
          92
        ],
        "audio": "unit10/sections/story_time.mp3"
      },
      {
        "id": "big_task",
        "name": "大任务",
        "icon": "🎯",
        "pages": [
          93
        ],
        "audio": "unit10/sections/big_task.mp3"
      }
    ]
  }
};
