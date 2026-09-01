#!/bin/bash
# 一键安装脚本
set -e
echo "=== 1. 安装 playwright ==="
pip3 install playwright
echo ""
echo "=== 2. 安装 chromium 浏览器 ==="
python3 -m playwright install chromium
echo ""
echo "=== 3. 安装 macOS 系统依赖 (如有提示) ==="
if [[ "$OSTYPE" == "darwin"* ]]; then
    python3 -m playwright install-deps chromium 2>/dev/null || echo "  (跳过，可能需要 sudo)"
fi
echo ""
echo "✅  安装完成！"
echo "运行:  python3 $(dirname "$0")/capture.py"
