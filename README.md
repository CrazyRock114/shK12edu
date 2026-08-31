# 小学英语三年级上册 · 互动学习站

上海教育出版社《义务教育教科书(五·四学制)英语(三年级上册)》配套互动学习站。

## 特性

- ✅ 12 单元完整配套(Starter + Unit 1-10 + Words to use)
- ✅ 教材原图 + 单词图裁切
- ✅ 三层音频(主教材 section 切分 + 练习部分 + Whisper 单词切片)
- ✅ TTS 跟读(Web Speech API)+ 教材原声双轨
- ✅ 5 阶段学习流程:预习 / 学习 / 复习 / 练习 / 游戏
- ✅ 响应式设计(桌面 + 移动端)
- ✅ 零构建,纯静态,GitHub Pages 一键部署

## 部署

### 方案 1: GitHub Pages (推荐)

```bash
# 在项目根目录初始化 git
cd shK12edu/site
git init
git add -A
git commit -m "Initial commit"
# 创建 GitHub repo 后推送
git remote add origin https://github.com/YOUR_USERNAME/shK12edu.git
git branch -M main
git push -u origin main
# 在 GitHub repo Settings > Pages 选 main 分支 / root 目录
# 访问 https://YOUR_USERNAME.github.io/shK12edu/
```

### 方案 2: 本地预览

```bash
cd site
python3 -m http.server 8000
# 访问 http://localhost:8000/
```

## 目录结构

```
site/
├── index.html                # 主页:12 单元卡片
├── style.css                 # 全局样式
├── units/                    # 13 个页面
│   ├── starter.html
│   ├── unit1.html + unit1.js  # Unit 1 完整 5 阶段
│   ├── unit2-10.html         # Unit 2-10 (模板生成)
│   └── words_to_use.html     # 全册复习
├── units_data.json           # 12 单元元数据
└── assets/
    ├── audio/                # 112 个音频
    │   ├── starter/
    │   ├── unit1/
    │   │   ├── unit_1.mp3 (整段)
    │   │   ├── sections/  (主教材 7 个)
    │   │   ├── practice/  (练习 2-3 个)
    │   │   ├── words/     (Whisper 单词切片)
    │   │   └── phrases/   (Whisper 短语切片)
    │   └── ... 12 个 unit
    └── img/                   # 教材原图
        ├── unit1/
        │   ├── teacher.jpg  # 单词裁切
        │   ├── school.jpg
        │   └── lesson_full.jpg  # 教材整页
        └── ... 12 个 unit
```

## 数据来源

- **音频**: 老师提供的主教材 + 练习部分 (smartedu 12 单元配套)
- **图片**: 教材 PDF 截图 (`raw/trimmed/page001-098.jpg`)
- **结构**: `raw/structure/units.json` (OCR 提取的教材结构)
- **Whisper 切片**: `openai-whisper` 转写 + `ffmpeg` 切片

## 已知限制

- starter 字母/数字音频未精确切片(用整段 fallback)
- unit 4 `lake`/`water vapour` 音频未找到
- 单词图位置用通用 OCR 坐标(可能略偏)
