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
            "word_coords": {
                        "art": {
                                    "bbox": [
                                                [
                                                            994.229112833764,
                                                            832.5068971136151
                                                ],
                                                [
                                                            1056.8906115417742,
                                                            832.5068971136151
                                                ],
                                                [
                                                            1056.8906115417742,
                                                            894.3514067875228
                                                ],
                                                [
                                                            994.229112833764,
                                                            894.3514067875228
                                                ]
                                    ],
                                    "cy": 863.4291519505689,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "gardening": {
                                    "bbox": [
                                                [
                                                            357.17054263565893,
                                                            985.8315372834121
                                                ],
                                                [
                                                            545.1550387596899,
                                                            985.8315372834121
                                                ],
                                                [
                                                            545.1550387596899,
                                                            1055.171236033803
                                                ],
                                                [
                                                            357.17054263565893,
                                                            1055.171236033803
                                                ]
                                    ],
                                    "cy": 1020.5013866586075,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "storytelling": {
                                    "bbox": [
                                                [
                                                            967.0757967269595,
                                                            308.3037150722912
                                                ],
                                                [
                                                            1182.2137364429404,
                                                            308.3037150722912
                                                ],
                                                [
                                                            1182.2137364429404,
                                                            379.4951825218993
                                                ],
                                                [
                                                            967.0757967269595,
                                                            379.4951825218993
                                                ]
                                    ],
                                    "cy": 343.89944879709526,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "take photos": {
                                    "bbox": [
                                                [
                                                            388.5012919896641,
                                                            295.8770549912192
                                                ],
                                                [
                                                            601.5505150820447,
                                                            295.8770549912192
                                                ],
                                                [
                                                            601.5505150820447,
                                                            366.96309090394806
                                                ],
                                                [
                                                            388.5012919896641,
                                                            366.96309090394806
                                                ]
                                    ],
                                    "cy": 331.4200729475836,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [-1.00, -1.00, -1.00, 5.00],
            
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
            "word_coords": {
                        "traditional": {
                                    "bbox": [
                                                [
                                                            1127.906976744186,
                                                            1410.2099628169506
                                                ],
                                                [
                                                            1328.4236451246736,
                                                            1410.2099628169506
                                                ],
                                                [
                                                            1328.4236451246736,
                                                            1476.5349308099078
                                                ],
                                                [
                                                            1127.906976744186,
                                                            1476.5349308099078
                                                ]
                                    ],
                                    "cy": 1443.3724468134292,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "Chinese yo-yo": {
                                    "bbox": [
                                                [
                                                            106.52454780361757,
                                                            917.5706654608111
                                                ],
                                                [
                                                            361.34794401157325,
                                                            917.5706654608111
                                                ],
                                                [
                                                            361.34794401157325,
                                                            988.6567332067335
                                                ],
                                                [
                                                            106.52454780361757,
                                                            988.6567332067335
                                                ]
                                    ],
                                    "cy": 953.1136993337724,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "kite-flying": {
                                    "bbox": [
                                                [
                                                            1063.1567614125754,
                                                            132.21087666453536
                                                ],
                                                [
                                                            1253.2298466750613,
                                                            132.21087666453536
                                                ],
                                                [
                                                            1253.2298466750613,
                                                            206.38756550120058
                                                ],
                                                [
                                                            1063.1567614125754,
                                                            206.38756550120058
                                                ]
                                    ],
                                    "cy": 169.29922108286797,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "dragon dance": {
                                    "bbox": [
                                                [
                                                            969.1645133505599,
                                                            816.8477035651673
                                                ],
                                                [
                                                            1240.6978019037501,
                                                            816.8477035651673
                                                ],
                                                [
                                                            1240.6978019037501,
                                                            886.1874023155582
                                                ],
                                                [
                                                            969.1645133505599,
                                                            886.1874023155582
                                                ]
                                    ],
                                    "cy": 851.5175529403627,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "tug of war": {
                                    "bbox": [
                                                [
                                                            726.8733850129199,
                                                            273.97919218020775
                                                ],
                                                [
                                                            923.2128751164978,
                                                            273.97919218020775
                                                ],
                                                [
                                                            923.2128751164978,
                                                            348.2659602000036
                                                ],
                                                [
                                                            726.8733850129199,
                                                            348.2659602000036
                                                ]
                                    ],
                                    "cy": 311.1225761901057,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [-1.00, -1.00, 6.56, -1.00, 10.88],
            
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
            "en": "leaf",
            "zh": "叶",
            "full": "leaf 叶",
            "extra": "🍃 光合作用"
          },
          {
            "en": "stem",
            "zh": "茎",
            "full": "stem 茎",
            "extra": "🌿 支撑"
          },
          {
            "en": "root",
            "zh": "根",
            "full": "root 根",
            "extra": "🌱 地下部分"
          },
          {
            "en": "soil",
            "zh": "土壤",
            "full": "soil 土壤",
            "extra": "🪨 植物生长"
          },
          {
            "en": "morning glory",
            "zh": "牵牛花",
            "full": "morning glory 牵牛花",
            "extra": "🌸 喇叭花"
          },
          {
            "en": "pine cone",
            "zh": "松果",
            "full": "pine cone 松果",
            "extra": "🌲 松树果实"
          },
          {
            "en": "water lily",
            "zh": "睡莲",
            "full": "water lily 睡莲",
            "extra": "🪷 池塘花"
          }
        ],
            "word_coords": {
                        "root": {
                                    "bbox": [
                                                [
                                                            609.9052540913005,
                                                            1050.2458133359796
                                                ],
                                                [
                                                            691.3652661542868,
                                                            1050.2458133359796
                                                ],
                                                [
                                                            691.3652661542868,
                                                            1124.4591740115593
                                                ],
                                                [
                                                            609.9052540913005,
                                                            1124.4591740115593
                                                ]
                                    ],
                                    "cy": 1087.3524936737695,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "stem": {
                                    "bbox": [
                                                [
                                                            576.4857881136951,
                                                            918.2993909264638
                                                ],
                                                [
                                                            668.3892558095375,
                                                            918.2993909264638
                                                ],
                                                [
                                                            668.3892558095375,
                                                            984.2668084900043
                                                ],
                                                [
                                                            576.4857881136951,
                                                            984.2668084900043
                                                ]
                                    ],
                                    "cy": 951.2830997082341,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "leaf": {
                                    "bbox": [
                                                [
                                                            261.08957795004306,
                                                            492.6400613527834
                                                ],
                                                [
                                                            336.2833763996555,
                                                            492.6400613527834
                                                ],
                                                [
                                                            336.2833763996555,
                                                            554.5456907582154
                                                ],
                                                [
                                                            261.08957795004306,
                                                            554.5456907582154
                                                ]
                                    ],
                                    "cy": 523.5928760554995,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "soil": {
                                    "bbox": [
                                                [
                                                            601.5503875968992,
                                                            1285.2075059052336
                                                ],
                                                [
                                                            672.566752799311,
                                                            1285.2075059052336
                                                ],
                                                [
                                                            672.566752799311,
                                                            1340.9225978366771
                                                ],
                                                [
                                                            601.5503875968992,
                                                            1340.9225978366771
                                                ]
                                    ],
                                    "cy": 1313.0650518709554,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "water lily": {
                                    "bbox": [
                                                [
                                                            806.244616709733,
                                                            1287.685911018542
                                                ],
                                                [
                                                            977.5194435875339,
                                                            1287.685911018542
                                                ],
                                                [
                                                            977.5194435875339,
                                                            1355.7822052307363
                                                ],
                                                [
                                                            806.244616709733,
                                                            1355.7822052307363
                                                ]
                                    ],
                                    "cy": 1321.7340581246392,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "pine cone": {
                                    "bbox": [
                                                [
                                                            806.244616709733,
                                                            888.1040152299395
                                                ],
                                                [
                                                            985.8743100819354,
                                                            888.1040152299395
                                                ],
                                                [
                                                            985.8743100819354,
                                                            953.5027646247564
                                                ],
                                                [
                                                            806.244616709733,
                                                            953.5027646247564
                                                ]
                                    ],
                                    "cy": 920.8033899273479,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "morning glory": {
                                    "bbox": [
                                                [
                                                            816.6881998277347,
                                                            280.04169654993024
                                                ],
                                                [
                                                            1069.4230387685218,
                                                            280.04169654993024
                                                ],
                                                [
                                                            1069.4230387685218,
                                                            348.1379270957377
                                                ],
                                                [
                                                            816.6881998277347,
                                                            348.1379270957377
                                                ]
                                    ],
                                    "cy": 314.08981182283395,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [5.24, 9.74, 13.82, 17.22, 20.96, 26.22, 29.52],
            
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
            "en": "giraffe",
            "zh": "长颈鹿",
            "full": "giraffe 长颈鹿",
            "extra": "🦒 最高动物"
          },
          {
            "en": "whale",
            "zh": "鲸鱼",
            "full": "whale 鲸鱼",
            "extra": "🐋 海洋最大"
          },
          {
            "en": "elephant",
            "zh": "大象",
            "full": "elephant 大象",
            "extra": "🐘 陆地最大"
          },
          {
            "en": "lion",
            "zh": "狮子",
            "full": "lion 狮子",
            "extra": "🦁 万兽之王"
          },
          {
            "en": "tiger",
            "zh": "老虎",
            "full": "tiger 老虎",
            "extra": "🐅 丛林之王"
          },
          {
            "en": "panda",
            "zh": "熊猫",
            "full": "panda 熊猫",
            "extra": "🐼 中国国宝"
          },
          {
            "en": "hippo",
            "zh": "河马",
            "full": "hippo 河马",
            "extra": "🦛 水中巨兽"
          }
        ],
            "word_coords": {
                        "safari park": {
                                    "bbox": [
                                                [
                                                            401.03359173126614,
                                                            264.1295564459139
                                                ],
                                                [
                                                            758.204134366925,
                                                            264.1295564459139
                                                ],
                                                [
                                                            758.204134366925,
                                                            384.66677130507543
                                                ],
                                                [
                                                            401.03359173126614,
                                                            384.66677130507543
                                                ]
                                    ],
                                    "cy": 324.3981638754947,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "tiger": {
                                    "bbox": [
                                                [
                                                            655.8570198105082,
                                                            935.3635106369383
                                                ],
                                                [
                                                            749.8493316150964,
                                                            935.3635106369383
                                                ],
                                                [
                                                            749.8493316150964,
                                                            1006.0258149109592
                                                ],
                                                [
                                                            655.8570198105082,
                                                            1006.0258149109592
                                                ]
                                    ],
                                    "cy": 970.6946627739487,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "lion": {
                                    "bbox": [
                                                [
                                                            144.12144702842377,
                                                            837.8113258132759
                                                ],
                                                [
                                                            217.2265607257222,
                                                            837.8113258132759
                                                ],
                                                [
                                                            217.2265607257222,
                                                            896.6217501481007
                                                ],
                                                [
                                                            144.12144702842377,
                                                            896.6217501481007
                                                ]
                                    ],
                                    "cy": 867.2165379806883,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "whale": {
                                    "bbox": [
                                                [
                                                            1140.439276485788,
                                                            359.20082133398137
                                                ],
                                                [
                                                            1257.4074074074074,
                                                            359.20082133398137
                                                ],
                                                [
                                                            1257.4074074074074,
                                                            421.0147711421271
                                                ],
                                                [
                                                            1140.439276485788,
                                                            421.0147711421271
                                                ]
                                    ],
                                    "cy": 390.1077962380542,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "panda": {
                                    "bbox": [
                                                [
                                                            1121.640826873385,
                                                            1226.288212048631
                                                ],
                                                [
                                                            1240.697546933459,
                                                            1226.288212048631
                                                ],
                                                [
                                                            1240.697546933459,
                                                            1286.5835911939473
                                                ],
                                                [
                                                            1121.640826873385,
                                                            1286.5835911939473
                                                ]
                                    ],
                                    "cy": 1256.4359016212893,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "giraffe": {
                                    "bbox": [
                                                [
                                                            131.5891472868217,
                                                            192.6166055751269
                                                ],
                                                [
                                                            263.1783105092866,
                                                            192.6166055751269
                                                ],
                                                [
                                                            263.1783105092866,
                                                            266.903357678326
                                                ],
                                                [
                                                            131.5891472868217,
                                                            266.903357678326
                                                ]
                                    ],
                                    "cy": 229.75998162672647,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "hippo": {
                                    "bbox": [
                                                [
                                                            116.96813092161929,
                                                            1335.959930302456
                                                ],
                                                [
                                                            227.67008010115117,
                                                            1335.959930302456
                                                ],
                                                [
                                                            227.67008010115117,
                                                            1410.1366191391214
                                                ],
                                                [
                                                            116.96813092161929,
                                                            1410.1366191391214
                                                ]
                                    ],
                                    "cy": 1373.0482747207889,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "elephant": {
                                    "bbox": [
                                                [
                                                            250.64599483204134,
                                                            456.5160398652133
                                                ],
                                                [
                                                            419.83213695752835,
                                                            456.5160398652133
                                                ],
                                                [
                                                            419.83213695752835,
                                                            527.6020439447486
                                                ],
                                                [
                                                            250.64599483204134,
                                                            527.6020439447486
                                                ]
                                    ],
                                    "cy": 492.059041904981,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [5.90, 10.34, 13.54, 17.14, 20.76, -1.00, -1.00, -1.00],
            
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
            "en": "nurse",
            "zh": "护士",
            "full": "nurse 护士",
            "extra": "👩‍⚕️ 协助医生"
          },
          {
            "en": "runny nose",
            "zh": "流鼻涕",
            "full": "runny nose 流鼻涕",
            "extra": "🤧 感冒症状"
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
          },
          {
            "en": "cough",
            "zh": "咳嗽",
            "full": "cough 咳嗽",
            "extra": "😷 喉咙"
          }
        ],
            "word_coords": {
                        "doctor": {
                                    "bbox": [
                                                [
                                                            1092.3987941429803,
                                                            164.736680874373
                                                ],
                                                [
                                                            1219.8103806974557,
                                                            164.736680874373
                                                ],
                                                [
                                                            1219.8103806974557,
                                                            231.06161703413684
                                                ],
                                                [
                                                            1092.3987941429803,
                                                            231.06161703413684
                                                ]
                                    ],
                                    "cy": 197.8991489542549,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "cough": {
                                    "bbox": [
                                                [
                                                            902.3255813953488,
                                                            1110.648152011463
                                                ],
                                                [
                                                            1019.2936485743953,
                                                            1110.648152011463
                                                ],
                                                [
                                                            1019.2936485743953,
                                                            1184.8248408481284
                                                ],
                                                [
                                                            902.3255813953488,
                                                            1184.8248408481284
                                                ]
                                    ],
                                    "cy": 1147.7364964297958,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "runny nose": {
                                    "bbox": [
                                                [
                                                            779.0913006029285,
                                                            398.73583317170056
                                                ],
                                                [
                                                            981.6966856070164,
                                                            398.73583317170056
                                                ],
                                                [
                                                            981.6966856070164,
                                                            476.79171496854553
                                                ],
                                                [
                                                            779.0913006029285,
                                                            476.79171496854553
                                                ]
                                    ],
                                    "cy": 437.763774070123,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "nurse": {
                                    "bbox": [
                                                [
                                                            160.83118001722653,
                                                            385.4339512684788
                                                ],
                                                [
                                                            267.35575969213045,
                                                            385.4339512684788
                                                ],
                                                [
                                                            267.35575969213045,
                                                            457.7048504765535
                                                ],
                                                [
                                                            160.83118001722653,
                                                            457.7048504765535
                                                ]
                                    ],
                                    "cy": 421.5694008725161,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "fever": {
                                    "bbox": [
                                                [
                                                            315.39621016365203,
                                                            555.4227589055885
                                                ],
                                                [
                                                            417.74338846264163,
                                                            555.4227589055885
                                                ],
                                                [
                                                            417.74338846264163,
                                                            623.5189894513959
                                                ],
                                                [
                                                            315.39621016365203,
                                                            623.5189894513959
                                                ]
                                    ],
                                    "cy": 589.4708741784922,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "medicine": {
                                    "bbox": [
                                                [
                                                            1255.3186907838071,
                                                            575.0528886778892
                                                ],
                                                [
                                                            1420.3274315333797,
                                                            575.0528886778892
                                                ],
                                                [
                                                            1420.3274315333797,
                                                            629.3187426419511
                                                ],
                                                [
                                                            1255.3186907838071,
                                                            629.3187426419511
                                                ]
                                    ],
                                    "cy": 602.1858156599202,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [5.82, 9.36, 12.76, 17.30, 20.04, 24.10],
            
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
            "word_coords": {
                        "try my best": {
                                    "bbox": [
                                                [
                                                            77.28251507321275,
                                                            754.2610984843359
                                                ],
                                                [
                                                            279.8880594337325,
                                                            754.2610984843359
                                                ],
                                                [
                                                            279.8880594337325,
                                                            823.6007972347268
                                                ],
                                                [
                                                            77.28251507321275,
                                                            823.6007972347268
                                                ]
                                    ],
                                    "cy": 788.9309478595313,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "will": {
                                    "bbox": [
                                                [
                                                            1182.213608957795,
                                                            1434.6663867225088
                                                ],
                                                [
                                                            1261.5848406546081,
                                                            1434.6663867225088
                                                ],
                                                [
                                                            1261.5848406546081,
                                                            1499.6673485313222
                                                ],
                                                [
                                                            1182.213608957795,
                                                            1499.6673485313222
                                                ]
                                    ],
                                    "cy": 1467.1668676269155,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "succeed": {
                                    "bbox": [
                                                [
                                                            1249.052540913006,
                                                            1047.749008636827
                                                ],
                                                [
                                                            1397.351293703485,
                                                            1047.749008636827
                                                ],
                                                [
                                                            1397.351293703485,
                                                            1105.0295933583225
                                                ],
                                                [
                                                            1249.052540913006,
                                                            1105.0295933583225
                                                ]
                                    ],
                                    "cy": 1076.3893009975748,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "practice": {
                                    "bbox": [
                                                [
                                                            977.5193798449612,
                                                            134.87426446528505
                                                ],
                                                [
                                                            1136.2618432385875,
                                                            134.87426446528505
                                                ],
                                                [
                                                            1136.2618432385875,
                                                            206.81288879958367
                                                ],
                                                [
                                                            977.5193798449612,
                                                            206.81288879958367
                                                ]
                                    ],
                                    "cy": 170.84357663243435,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "better": {
                                    "bbox": [
                                                [
                                                            1104.9310938845822,
                                                            376.86197258858977
                                                ],
                                                [
                                                            1219.8106356677467,
                                                            376.86197258858977
                                                ],
                                                [
                                                            1219.8106356677467,
                                                            431.12779471945817
                                                ],
                                                [
                                                            1104.9310938845822,
                                                            431.12779471945817
                                                ]
                                    ],
                                    "cy": 403.99488365402397,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "give up": {
                                    "bbox": [
                                                [
                                                            346.7269595176572,
                                                            418.49593787307094
                                                ],
                                                [
                                                            480.4048552993656,
                                                            418.49593787307094
                                                ],
                                                [
                                                            480.4048552993656,
                                                            496.97443714685124
                                                ],
                                                [
                                                            346.7269595176572,
                                                            496.97443714685124
                                                ]
                                    ],
                                    "cy": 457.73518750996107,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00],
            
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
            "word_coords": {
                        "scientist": {
                                    "bbox": [
                                                [
                                                            643.3247200689061,
                                                            586.1465656142495
                                                ],
                                                [
                                                            793.712316968131,
                                                            586.1465656142495
                                                ],
                                                [
                                                            793.712316968131,
                                                            646.7142458967836
                                                ],
                                                [
                                                            643.3247200689061,
                                                            646.7142458967836
                                                ]
                                    ],
                                    "cy": 616.4304057555165,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "explore": {
                                    "bbox": [
                                                [
                                                            645.4134366925065,
                                                            647.7791935522066
                                                ],
                                                [
                                                            781.1801447116743,
                                                            647.7791935522066
                                                ],
                                                [
                                                            781.1801447116743,
                                                            706.5895542206445
                                                ],
                                                [
                                                            645.4134366925065,
                                                            706.5895542206445
                                                ]
                                    ],
                                    "cy": 677.1843738864255,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "famous": {
                                    "bbox": [
                                                [
                                                            647.5021533161068,
                                                            708.1030315725137
                                                ],
                                                [
                                                            781.1799534839561,
                                                            708.1030315725137
                                                ],
                                                [
                                                            781.1799534839561,
                                                            760.7228547669631
                                                ],
                                                [
                                                            647.5021533161068,
                                                            760.7228547669631
                                                ]
                                    ],
                                    "cy": 734.4129431697385,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "discover": {
                                    "bbox": [
                                                [
                                                            647.5021533161068,
                                                            767.6943241439478
                                                ],
                                                [
                                                            793.712316968131,
                                                            767.6943241439478
                                                ],
                                                [
                                                            793.712316968131,
                                                            818.9453836841891
                                                ],
                                                [
                                                            647.5021533161068,
                                                            818.9453836841891
                                                ]
                                    ],
                                    "cy": 793.3198539140685,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "creative": {
                                    "bbox": [
                                                [
                                                            647.5021533161068,
                                                            820.9900297028363
                                                ],
                                                [
                                                            789.5348199783575,
                                                            820.9900297028363
                                                ],
                                                [
                                                            789.5348199783575,
                                                            878.1928140994124
                                                ],
                                                [
                                                            647.5021533161068,
                                                            878.1928140994124
                                                ]
                                    ],
                                    "cy": 849.5914219011244,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "hard-working": {
                                    "bbox": [
                                                [
                                                            645.4134366925065,
                                                            878.8939720194921
                                                ],
                                                [
                                                            889.7933453963195,
                                                            878.8939720194921
                                                ],
                                                [
                                                            889.7933453963195,
                                                            942.2041455886289
                                                ],
                                                [
                                                            645.4134366925065,
                                                            942.2041455886289
                                                ]
                                    ],
                                    "cy": 910.5490588040605,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "(be) known as": {
                                    "bbox": [
                                                [
                                                            647.5021533161068,
                                                            949.6103927224668
                                                ],
                                                [
                                                            891.8820620199199,
                                                            949.6103927224668
                                                ],
                                                [
                                                            891.8820620199199,
                                                            998.6156204611269
                                                ],
                                                [
                                                            647.5021533161068,
                                                            998.6156204611269
                                                ]
                                    ],
                                    "cy": 974.1130065917969,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [6.18, 9.52, 14.00, 16.68, 20.70, 24.64, 28.58],
            
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
            "en": "invention",
            "zh": "发明",
            "full": "invention 发明",
            "extra": "💡 新创造"
          },
          {
            "en": "printing",
            "zh": "印刷",
            "full": "printing 印刷",
            "extra": "📖 印书"
          },
          {
            "en": "light",
            "zh": "灯",
            "full": "light 灯/光",
            "extra": "💡 照明"
          },
          {
            "en": "problem",
            "zh": "问题",
            "full": "problem 问题",
            "extra": "❓ 困难"
          },
          {
            "en": "robot",
            "zh": "机器人",
            "full": "robot 机器人",
            "extra": "🤖 智能"
          },
          {
            "en": "television",
            "zh": "电视",
            "full": "television 电视",
            "extra": "📺 看节目"
          },
          {
            "en": "useful",
            "zh": "有用的",
            "full": "useful 有用的",
            "extra": "👍 有帮助"
          },
          {
            "en": "wheel",
            "zh": "轮子",
            "full": "wheel 轮子",
            "extra": "☸️ 圆形"
          }
        ],
            "word_coords": {
                        "useful": {
                                    "bbox": [
                                                [
                                                            1042.269595176572,
                                                            1490.6120783076826
                                                ],
                                                [
                                                            1152.9714487422448,
                                                            1490.6120783076826
                                                ],
                                                [
                                                            1152.9714487422448,
                                                            1549.4225026425074
                                                ],
                                                [
                                                            1042.269595176572,
                                                            1549.4225026425074
                                                ]
                                    ],
                                    "cy": 1520.017290475095,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "invention": {
                                    "bbox": [
                                                [
                                                            240.2024117140396,
                                                            229.65610195803038
                                                ],
                                                [
                                                            544.2290504054711,
                                                            229.65610195803038
                                                ],
                                                [
                                                            544.2290504054711,
                                                            323.89348042571055
                                                ],
                                                [
                                                            240.2024117140396,
                                                            323.89348042571055
                                                ]
                                    ],
                                    "cy": 276.77479119187046,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "problem": {
                                    "bbox": [
                                                [
                                                            1019.2937123169681,
                                                            1431.7421895673956
                                                ],
                                                [
                                                            1171.7701533249387,
                                                            1431.7421895673956
                                                ],
                                                [
                                                            1171.7701533249387,
                                                            1495.0522994701453
                                                ],
                                                [
                                                            1019.2937123169681,
                                                            1495.0522994701453
                                                ]
                                    ],
                                    "cy": 1463.3972445187703,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "wheel": {
                                    "bbox": [
                                                [
                                                            540.9776055124893,
                                                            1305.9642760619647
                                                ],
                                                [
                                                            651.6796503058803,
                                                            1305.9642760619647
                                                ],
                                                [
                                                            651.6796503058803,
                                                            1361.5968563558506
                                                ],
                                                [
                                                            540.9776055124893,
                                                            1361.5968563558506
                                                ]
                                    ],
                                    "cy": 1333.7805662089077,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "printing": {
                                    "bbox": [
                                                [
                                                            208.87166236003446,
                                                            696.8329987441512
                                                ],
                                                [
                                                            359.2592273879729,
                                                            696.8329987441512
                                                ],
                                                [
                                                            359.2592273879729,
                                                            772.0415923813841
                                                ],
                                                [
                                                            208.87166236003446,
                                                            772.0415923813841
                                                ]
                                    ],
                                    "cy": 734.4372955627676,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "television": {
                                    "bbox": [
                                                [
                                                            954.5434969853575,
                                                            795.7242786856776
                                                ],
                                                [
                                                            1127.906976744186,
                                                            795.7242786856776
                                                ],
                                                [
                                                            1127.906976744186,
                                                            848.3441018801271
                                                ],
                                                [
                                                            954.5434969853575,
                                                            848.3441018801271
                                                ]
                                    ],
                                    "cy": 822.0341902829024,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "light": {
                                    "bbox": [
                                                [
                                                            873.083548664944,
                                                            588.857798704833
                                                ],
                                                [
                                                            967.0757329843867,
                                                            588.857798704833
                                                ],
                                                [
                                                            967.0757329843867,
                                                            663.0344875414983
                                                ],
                                                [
                                                            873.083548664944,
                                                            663.0344875414983
                                                ]
                                    ],
                                    "cy": 625.9461431231656,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "robot": {
                                    "bbox": [
                                                [
                                                            1265.7622739018088,
                                                            1279.1332232539153
                                                ],
                                                [
                                                            1366.02054434948,
                                                            1279.1332232539153
                                                ],
                                                [
                                                            1366.02054434948,
                                                            1336.4138716417979
                                                ],
                                                [
                                                            1265.7622739018088,
                                                            1336.4138716417979
                                                ]
                                    ],
                                    "cy": 1307.7735474478566,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [5.56, 10.68, 14.08, -1.00, -1.00, -1.00, -1.00, -1.00],
            
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
            "word_coords": {
                        "laptop": {
                                    "bbox": [
                                                [
                                                            1163.4151593453919,
                                                            1407.6927212075695
                                                ],
                                                [
                                                            1290.826618414722,
                                                            1407.6927212075695
                                                ],
                                                [
                                                            1290.826618414722,
                                                            1485.0747579643596
                                                ],
                                                [
                                                            1163.4151593453919,
                                                            1485.0747579643596
                                                ]
                                    ],
                                    "cy": 1446.3837395859646,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "password": {
                                    "bbox": [
                                                [
                                                            438.6304909560723,
                                                            747.4621013497461
                                                ],
                                                [
                                                            614.082751081074,
                                                            747.4621013497461
                                                ],
                                                [
                                                            614.082751081074,
                                                            810.7722749188829
                                                ],
                                                [
                                                            438.6304909560723,
                                                            810.7722749188829
                                                ]
                                    ],
                                    "cy": 779.1171881343146,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "mouse": {
                                    "bbox": [
                                                [
                                                            1136.2618432385875,
                                                            1226.197933111859
                                                ],
                                                [
                                                            1259.4961240310076,
                                                            1226.197933111859
                                                ],
                                                [
                                                            1259.4961240310076,
                                                            1313.936199044337
                                                ],
                                                [
                                                            1136.2618432385875,
                                                            1313.936199044337
                                                ]
                                    ],
                                    "cy": 1270.067066078098,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "click": {
                                    "bbox": [
                                                [
                                                            1163.4151593453919,
                                                            1038.1616784169914
                                                ],
                                                [
                                                            1253.2298466750613,
                                                            1038.1616784169914
                                                ],
                                                [
                                                            1253.2298466750613,
                                                            1103.06624931588
                                                ],
                                                [
                                                            1163.4151593453919,
                                                            1103.06624931588
                                                ]
                                    ],
                                    "cy": 1070.6139638664356,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "keyboard": {
                                    "bbox": [
                                                [
                                                            352.9931093884582,
                                                            1007.6689170267693
                                                ],
                                                [
                                                            528.4453057708871,
                                                            1007.6689170267693
                                                ],
                                                [
                                                            528.4453057708871,
                                                            1080.0233465345939
                                                ],
                                                [
                                                            352.9931093884582,
                                                            1080.0233465345939
                                                ]
                                    ],
                                    "cy": 1043.8461317806816,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "email": {
                                    "bbox": [
                                                [
                                                            956.6322136089577,
                                                            517.4785790799488
                                                ],
                                                [
                                                            1065.245605521321,
                                                            517.4785790799488
                                                ],
                                                [
                                                            1065.245605521321,
                                                            579.3842403185744
                                                ],
                                                [
                                                            956.6322136089577,
                                                            579.3842403185744
                                                ]
                                    ],
                                    "cy": 548.4314096992616,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "delete": {
                                    "bbox": [
                                                [
                                                            1213.5443583118001,
                                                            711.6813371877105
                                                ],
                                                [
                                                            1332.6013333421652,
                                                            711.6813371877105
                                                ],
                                                [
                                                            1332.6013333421652,
                                                            768.961985575593
                                                ],
                                                [
                                                            1213.5443583118001,
                                                            768.961985575593
                                                ]
                                    ],
                                    "cy": 740.3216613816518,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00],
            
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
            "en": "turn off",
            "zh": "关掉",
            "full": "turn off 关掉",
            "extra": "🔌 关闭电源"
          },
          {
            "en": "throw away",
            "zh": "扔掉",
            "full": "throw away 扔掉",
            "extra": "🗑 丢弃"
          },
          {
            "en": "recycle",
            "zh": "回收",
            "full": "recycle 回收",
            "extra": "♻️ 分类处理"
          },
          {
            "en": "pick up",
            "zh": "捡起",
            "full": "pick up 捡起",
            "extra": "✋ 拾起"
          },
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
          }
        ],
            "word_coords": {
                        "reduce": {
                                    "bbox": [
                                                [
                                                            1161.3264427217916,
                                                            1307.1396848988404
                                                ],
                                                [
                                                            1286.6495676229576,
                                                            1307.1396848988404
                                                ],
                                                [
                                                            1286.6495676229576,
                                                            1361.4054751965152
                                                ],
                                                [
                                                            1161.3264427217916,
                                                            1361.4054751965152
                                                ]
                                    ],
                                    "cy": 1334.2725800476778,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "reuse": {
                                    "bbox": [
                                                [
                                                            1173.8587424633936,
                                                            1367.8966453499386
                                                ],
                                                [
                                                            1274.11714039621,
                                                            1367.8966453499386
                                                ],
                                                [
                                                            1274.11714039621,
                                                            1440.1676718907875
                                                ],
                                                [
                                                            1173.8587424633936,
                                                            1440.1676718907875
                                                ]
                                    ],
                                    "cy": 1404.032158620363,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "recycle": {
                                    "bbox": [
                                                [
                                                            1098.6649440137812,
                                                            594.8452404042773
                                                ],
                                                [
                                                            1236.520241171404,
                                                            594.8452404042773
                                                ],
                                                [
                                                            1236.520241171404,
                                                            662.9414709500847
                                                ],
                                                [
                                                            1098.6649440137812,
                                                            662.9414709500847
                                                ]
                                    ],
                                    "cy": 628.893355677181,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "throw away": {
                                    "bbox": [
                                                [
                                                            889.7932816537467,
                                                            424.99732648160847
                                                ],
                                                [
                                                            1107.019937993328,
                                                            424.99732648160847
                                                ],
                                                [
                                                            1107.019937993328,
                                                            496.08336239433726
                                                ],
                                                [
                                                            889.7932816537467,
                                                            496.08336239433726
                                                ]
                                    ],
                                    "cy": 460.54034443797286,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "turn off": {
                                    "bbox": [
                                                [
                                                            131.5891472868217,
                                                            444.6373882102819
                                                ],
                                                [
                                                            277.79927906755944,
                                                            444.6373882102819
                                                ],
                                                [
                                                            277.79927906755944,
                                                            512.7336187560894
                                                ],
                                                [
                                                            131.5891472868217,
                                                            512.7336187560894
                                                ]
                                    ],
                                    "cy": 478.6855034831857,
                                    "img_w": 1552,
                                    "img_h": 2168
                        },
                        "pick up": {
                                    "bbox": [
                                                [
                                                            630.7924203273041,
                                                            1283.5691151020617
                                                ],
                                                [
                                                            764.4702842377261,
                                                            1283.5691151020617
                                                ],
                                                [
                                                            764.4702842377261,
                                                            1357.7458039387268
                                                ],
                                                [
                                                            630.7924203273041,
                                                            1357.7458039387268
                                                ]
                                    ],
                                    "cy": 1320.6574595203942,
                                    "img_w": 1552,
                                    "img_h": 2168
                        }
            },
            "word_starts": [5.48, 9.60, 13.24, 18.72, 21.96, 26.56],
            
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
