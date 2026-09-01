# 教材批量截图脚本

## 快速开始

```bash
cd /Users/paulshi/Documents/MiniMax/shK12edu/scripts
chmod +x install.sh
./install.sh
python3 capture.py
```

## 第一次运行（会登录）

1. 浏览器自动打开到 smartedu 详情页
2. 脚本检测到未登录，会在终端暂停并提示
3. 在浏览器里点右上角「登录」→ 扫码 / 手机号 / 教育账号
4. 登录后回终端按回车
5. 脚本继续，开始批量截图

## 第二次运行（已登录态）

直接 `python3 capture.py`，浏览器会复用 `~/.cache/smartedu-browser/` 里的登录态，跳过登录步骤。

## 输出

- 路径：`/Users/paulshi/Documents/MiniMax/shK12edu/raw/screenshots/page001.jpg ~ page098.jpg`
- 命名：3 位补零，方便按顺序查看
- 黑屏/异常文件 < 30KB 的会单独标出来，可以重跑覆盖

## 调整

- **修改总页数**：编辑 `capture.py` 里的 `total_pages = 98` 变量
- **修改每页等待**：编辑 `DELAY_MS = 2200`（单位毫秒，PDF 翻页+渲染）
- **换课程**：修改 `URL` 常量，运行前先在浏览器里打开新 URL 登录一次

## 常见问题

- **`playwright: command not found`** → 用 `python3 -m playwright install chromium`
- **登录后还报"未登录"** → 检查浏览器右上角是否真出现头像，cookie 状态可能在 persistent context 里没正确保留
- **截图黑屏** → DELAY_MS 调大到 3000+；或者 PDF.js 跨域 iframe 加载慢
