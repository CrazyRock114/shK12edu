#!/usr/bin/env python3
"""
G3A + G5A 22 单元主题词中英对照 + extra 拓展字典
按 starter 精修标准给所有单元主题词加 zh + extra
"""
# G3A 三年级上册 unit1-10
G3A_EXTRA = {
    'unit1': {
        'school': {'zh':'学校', 'extra':'🏫 buildings/classroom'},
        'classmate': {'zh':'同学', 'extra':'👫 同班同学'},
        'teacher': {'zh':'老师', 'extra':'👩‍🏫 教书的人'},
        'play sports': {'zh':'做运动', 'extra':'⚽ 跑跳打球'},
        'read': {'zh':'读', 'extra':'📖 看书'},
        'book': {'zh':'书', 'extra':'📚 有故事'},
        'study': {'zh':'学习', 'extra':'✏️ 用功读书'},
        'friend': {'zh':'朋友', 'extra':'👫 buddy'},
    },
    'unit2': {
        'draw': {'zh':'画', 'extra':'🎨 用笔'},
        'tell a story': {'zh':'讲故事', 'extra':'📖 给别人听'},
        'dance': {'zh':'跳舞', 'extra':'💃 音乐'},
        'sing': {'zh':'唱歌', 'extra':'🎤 出声'},
        'use the computer': {'zh':'用电脑', 'extra':'💻 上网/打字'},
        'run': {'zh':'跑', 'extra':'🏃 快速走'},
        'jump': {'zh':'跳', 'extra':'🤸 离地'},
    },
    'unit3': {
        'garden': {'zh':'花园', 'extra':'🌷 植物园地'},
        'flower': {'zh':'花', 'extra':'🌸 美丽'},
        'vegetable': {'zh':'蔬菜', 'extra':'🥬 吃的植物'},
        'plant': {'zh':'植物', 'extra':'🌱 活的'},
        'orange tree': {'zh':'橙子树', 'extra':'🍊 柑橘'},
        'tomato': {'zh':'番茄', 'extra':'🍅 红色果实'},
        'carrot': {'zh':'胡萝卜', 'extra':'🥕 橙色根'},
    },
    'unit4': {
        'water': {'zh':'水', 'extra':'💧 H2O · 无色无味'},
        'river': {'zh':'河', 'extra':'🏞 陆地流动'},
        'lake': {'zh':'湖', 'extra':'🌊 内陆静水'},
        'sea': {'zh':'海', 'extra':'🌊 咸的'},
        'water vapour': {'zh':'水蒸气', 'extra':'☁️ 气体形态'},
        'cloud': {'zh':'云', 'extra':'☁️ 空中水滴'},
        'rain': {'zh':'雨', 'extra':'🌧 水滴落下'},
        'snow': {'zh':'雪', 'extra':'❄️ 冰晶'},
        'ice': {'zh':'冰', 'extra':'🧊 固体水'},
    },
    'unit5': {
        'help': {'zh':'帮助', 'extra':'🤝 协助'},
        'cook': {'zh':'做饭', 'extra':'🍳 厨房'},
        'do the dishes': {'zh':'洗碗', 'extra':'🍽 饭后清洁'},
        'clean the table': {'zh':'擦桌子', 'extra':'🧽 餐桌清洁'},
        'walk the dog': {'zh':'遛狗', 'extra':'🐕 户外活动'},
        'chore': {'zh':'家务', 'extra':'🧹 家务活'},
        'give your seat': {'zh':'让座', 'extra':'💺 给需要的人'},
    },
    'unit6': {
        'happy': {'zh':'开心', 'extra':'😊 高兴'},
        'sad': {'zh':'难过', 'extra':'😢 不开心'},
        'good': {'zh':'好', 'extra':'👍 棒'},
        'bad': {'zh':'坏', 'extra':'👎 不好'},
        'excited': {'zh':'兴奋', 'extra':'🤩 激动'},
        'scared': {'zh':'害怕', 'extra':'😨 怕'},
        'tired': {'zh':'累', 'extra':'😴 疲倦'},
        'unhappy': {'zh':'不开心', 'extra':'🙁 难受'},
    },
    'unit7': {
        'driver': {'zh':'司机', 'extra':'🚗 开车'},
        'police officer': {'zh':'警察', 'extra':'👮 抓坏人'},
        'engineer': {'zh':'工程师', 'extra':'👷 造东西'},
        'writer': {'zh':'作家', 'extra':'✍️ 写书'},
        'doctor': {'zh':'医生', 'extra':'👨‍⚕️ 治病'},
        'chef': {'zh':'厨师', 'extra':'👨‍🍳 做饭'},
        'astronaut': {'zh':'宇航员', 'extra':'🚀 太空'},
    },
    'unit8': {
        'library': {'zh':'图书馆', 'extra':'📚 借书/看书'},
        'find the way': {'zh':'找路', 'extra':'🗺 看地图'},
        'get to': {'zh':'到达', 'extra':'🎯 去某地'},
        'walk along': {'zh':'沿着走', 'extra':'🚶 顺路走'},
        'road': {'zh':'路', 'extra':'🛣 道路'},
        'left': {'zh':'左', 'extra':'⬅️ 反义 right'},
        'right': {'zh':'右', 'extra':'➡️ 也"对的"'},
        'museum': {'zh':'博物馆', 'extra':'🏛 看展品'},
    },
    'unit9': {
        'special days': {'zh':'特殊日子', 'extra':'🎉 节日'},
        'the Double Ninth Festival': {'zh':'重阳节', 'extra':'🏔 农历九月初九·敬老'},
        'celebrate': {'zh':'庆祝', 'extra':'🎊 过节'},
        'Chinese New Year': {'zh':'春节', 'extra':'🧧 农历新年'},
        'the Spring Festival': {'zh':'春节', 'extra':'🧧 农历新年·同 Chinese New Year'},
        'the Lantern Festival': {'zh':'元宵节', 'extra':'🏮 农历正月十五·吃汤圆'},
        'holiday': {'zh':'假日', 'extra':'🏖 放假'},
    },
    'unit10': {
        'food': {'zh':'食物', 'extra':'🍴 吃的'},
        'noodles': {'zh':'面条', 'extra':'🍜 中国·长条'},
        'pizza': {'zh':'披萨', 'extra':'🍕 意大利·圆形'},
        'sandwich': {'zh':'三明治', 'extra':'🥪 夹心面包'},
        'hot dog': {'zh':'热狗', 'extra':'🌭 美国·香肠面包'},
        'fish and chips': {'zh':'炸鱼薯条', 'extra':'🐟 英国经典'},
        'beef': {'zh':'牛肉', 'extra':'🐄 红色肉类'},
        'bread': {'zh':'面包', 'extra':'🍞 西方主食'},
        'cake': {'zh':'蛋糕', 'extra':'🎂 生日庆祝'},
    },
}

# G5A 五年级上册 unit1-10
G5A_EXTRA = {
    'unit1': {
        'art': {'zh':'艺术', 'extra':'🎨 美术课', 'full':'art club 艺术社团'},
        'gardening': {'zh':'园艺', 'extra':'🌷 种花种菜', 'full':'gardening club 园艺社'},
        'storytelling': {'zh':'讲故事', 'extra':'📖 表演故事', 'full':'storytelling club 故事社'},
        'take photos': {'zh':'拍照', 'extra':'📷 用相机', 'full':'take photos 拍照'},
    },
    'unit2': {
        'traditional': {'zh':'传统的', 'extra':'🏛 古老的', 'full':'traditional games 传统游戏'},
        'Chinese yo-yo': {'zh':'中国溜溜球', 'extra':'🪀 空竹', 'full':'Chinese yo-yo 中国溜溜球'},
        'kite-flying': {'zh':'放风筝', 'extra':'🪁 春季活动', 'full':'kite-flying 放风筝'},
        'dragon dance': {'zh':'舞龙', 'extra':'🐉 春节表演', 'full':'dragon dance 舞龙'},
        'tug of war': {'zh':'拔河', 'extra':'🪢 团队比赛', 'full':'tug of war 拔河'},
    },
    'unit3': {
        'root': {'zh':'根', 'extra':'🌱 地下部分', 'full':'root 根'},
        'stem': {'zh':'茎', 'extra':'🌿 支撑', 'full':'stem 茎'},
        'leaf': {'zh':'叶', 'extra':'🍃 光合作用', 'full':'leaf 叶'},
        'soil': {'zh':'土壤', 'extra':'🪨 植物生长', 'full':'soil 土壤'},
        'water lily': {'zh':'睡莲', 'extra':'🪷 池塘花', 'full':'water lily 睡莲'},
        'pine cone': {'zh':'松果', 'extra':'🌲 松树果实', 'full':'pine cone 松果'},
        'morning glory': {'zh':'牵牛花', 'extra':'🌸 喇叭花', 'full':'morning glory 牵牛花'},
    },
    'unit4': {
        'safari park': {'zh':'野生动物园', 'extra':'🦁 半野生', 'full':'safari park 野生动物园'},
        'tiger': {'zh':'老虎', 'extra':'🐅 丛林之王', 'full':'tiger 老虎'},
        'lion': {'zh':'狮子', 'extra':'🦁 万兽之王', 'full':'lion 狮子'},
        'whale': {'zh':'鲸鱼', 'extra':'🐋 海洋最大', 'full':'whale 鲸鱼'},
        'panda': {'zh':'熊猫', 'extra':'🐼 中国国宝', 'full':'panda 熊猫'},
        'giraffe': {'zh':'长颈鹿', 'extra':'🦒 最高动物', 'full':'giraffe 长颈鹿'},
        'hippo': {'zh':'河马', 'extra':'🦛 水中巨兽', 'full':'hippo 河马'},
        'elephant': {'zh':'大象', 'extra':'🐘 陆地最大', 'full':'elephant 大象'},
    },
    'unit5': {
        'doctor': {'zh':'医生', 'extra':'👨‍⚕️ 看病', 'full':'doctor 医生'},
        'cough': {'zh':'咳嗽', 'extra':'😷 喉咙', 'full':'cough 咳嗽'},
        'runny nose': {'zh':'流鼻涕', 'extra':'🤧 感冒症状', 'full':'runny nose 流鼻涕'},
        'nurse': {'zh':'护士', 'extra':'👩‍⚕️ 协助医生', 'full':'nurse 护士'},
        'fever': {'zh':'发烧', 'extra':'🤒 体温高', 'full':'fever 发烧'},
        'medicine': {'zh':'药', 'extra':'💊 治疗', 'full':'medicine 药'},
    },
    'unit6': {
        'try my best': {'zh':'尽我所能', 'extra':'💪 努力', 'full':'try my best 尽我所能'},
        'will': {'zh':'将', 'extra':'⏰ 将来时', 'full':'will will 将会'},
        'succeed': {'zh':'成功', 'extra':'🏆 达成', 'full':'succeed 成功'},
        'practice': {'zh':'练习', 'extra':'🎯 反复', 'full':'practice 练习'},
        'better': {'zh':'更好', 'extra':'📈 进步', 'full':'better 更好'},
        'give up': {'zh':'放弃', 'extra':'🚫 停止', 'full':'give up 放弃'},
    },
    'unit7': {
        'scientist': {'zh':'科学家', 'extra':'🔬 研究自然', 'full':'scientist 科学家'},
        'explore': {'zh':'探索', 'extra':'🔍 寻找', 'full':'explore 探索'},
        'famous': {'zh':'著名的', 'extra':'⭐ 出名', 'full':'famous 著名的'},
        'discover': {'zh':'发现', 'extra':'💡 找到新的', 'full':'discover 发现'},
        'creative': {'zh':'有创造力的', 'extra':'💡 创新', 'full':'creative 有创造力的'},
        'hard-working': {'zh':'勤奋的', 'extra':'💪 努力', 'full':'hard-working 勤奋的'},
        '(be) known as': {'zh':'被称为', 'extra':'🏷 名字是', 'full':'(be) known as 被称为'},
    },
    'unit8': {
        'useful': {'zh':'有用的', 'extra':'👍 有帮助', 'full':'useful 有用的'},
        'invention': {'zh':'发明', 'extra':'💡 新创造', 'full':'invention 发明'},
        'problem': {'zh':'问题', 'extra':'❓ 困难', 'full':'problem 问题'},
        'wheel': {'zh':'轮子', 'extra':'☸️ 圆形', 'full':'wheel 轮子'},
        'printing': {'zh':'印刷', 'extra':'📖 印书', 'full':'printing 印刷'},
        'television': {'zh':'电视', 'extra':'📺 看节目', 'full':'television 电视'},
        'light': {'zh':'灯', 'extra':'💡 照明', 'full':'light 灯/光'},
        'robot': {'zh':'机器人', 'extra':'🤖 智能', 'full':'robot 机器人'},
    },
    'unit9': {
        'laptop': {'zh':'笔记本电脑', 'extra':'💻 便携', 'full':'laptop 笔记本电脑'},
        'password': {'zh':'密码', 'extra':'🔒 保密', 'full':'password 密码'},
        'mouse': {'zh':'鼠标', 'extra':'🖱 电脑配件', 'full':'mouse 鼠标'},
        'click': {'zh':'点击', 'extra':'👆 鼠标动作', 'full':'click 点击'},
        'keyboard': {'zh':'键盘', 'extra':'⌨️ 打字', 'full':'keyboard 键盘'},
        'email': {'zh':'电子邮件', 'extra':'📧 网络信件', 'full':'email 电子邮件'},
        'delete': {'zh':'删除', 'extra':'🗑 移除', 'full':'delete 删除'},
    },
    'unit10': {
        'reduce': {'zh':'减少', 'extra':'📉 变少', 'full':'reduce 减少使用'},
        'reuse': {'zh':'再利用', 'extra':'♻️ 重复用', 'full':'reuse 再利用'},
        'recycle': {'zh':'回收', 'extra':'♻️ 分类处理', 'full':'recycle 回收'},
        'throw away': {'zh':'扔掉', 'extra':'🗑 丢弃', 'full':'throw away 扔掉'},
        'turn off': {'zh':'关掉', 'extra':'🔌 关闭电源', 'full':'turn off 关掉'},
        'pick up': {'zh':'捡起', 'extra':'✋ 拾起', 'full':'pick up 捡起'},
    },
}


def enrich_topic_words(grade, uid, raw_words):
    """把 units.json 的字符串列表或简 dict 升级为带 zh + extra 的 dict list"""
    if grade == 'g3a':
        extra_dict = G3A_EXTRA.get(uid, {})
    elif grade == 'g5a':
        extra_dict = G5A_EXTRA.get(uid, {})
    else:
        extra_dict = {}

    enriched = []
    for w in raw_words:
        # 已经是 dict
        if isinstance(w, dict):
            en = w.get('en', w.get('word', ''))
        else:
            en = w

        # 查 extra 字典
        ex = extra_dict.get(en, {})
        if isinstance(w, dict):
            # 合并, 优先 extra_dict 字段
            merged = dict(w)
            merged.setdefault('zh', ex.get('zh', ''))
            merged.setdefault('full', ex.get('full', ''))
            merged.setdefault('extra', ex.get('extra', ''))
            enriched.append(merged)
        else:
            enriched.append({
                'en': en,
                'zh': ex.get('zh', ''),
                'full': ex.get('full', ''),
                'extra': ex.get('extra', ''),
            })
    return enriched


if __name__ == '__main__':
    import json
    # 测试
    test_words = ['school', 'classmate', 'teacher', 'play sports', 'read', 'book', 'study', 'friend']
    result = enrich_topic_words('g3a', 'unit1', test_words)
    print(json.dumps(result, ensure_ascii=False, indent=2))
