#!/usr/bin/env python3
"""
v2 压缩版：仅调整 JPEG 质量（92 → 85），保持 1544x2165 尺寸不变
- 源：raw/trimmed/（v1 裁切后）
- 输出：raw/trimmed_v2/（与 v1 对比）
- 单一变量：JPEG quality，方便质量对比
"""
import sys
from pathlib import Path
from PIL import Image

# ============== 配置 ==============
SRC_DIR = Path(__file__).resolve().parent.parent / "raw" / "trimmed"
DST_DIR = Path(__file__).resolve().parent.parent / "raw" / "trimmed_v2"
QUALITY = 85  # v1 用 92，对比用 85
# ================================


def main():
    DST_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(SRC_DIR.glob("page*.jpg"))
    if not files:
        print(f"❌  在 {SRC_DIR} 没找到文件")
        sys.exit(1)

    print(f"📁 源:   {SRC_DIR} (v1, quality=92)")
    print(f"📁 输出: {DST_DIR} (v2, quality={QUALITY})")
    print(f"📊 文件数: {len(files)}")
    print()

    total_src = 0
    total_dst = 0

    for f in files:
        dst = DST_DIR / f.name
        img = Image.open(f).convert("RGB")
        img.save(dst, "JPEG", quality=QUALITY, optimize=True)
        src_size = f.stat().st_size
        dst_size = dst.stat().st_size
        total_src += src_size
        total_dst += dst_size
        saved = (1 - dst_size / src_size) * 100 if src_size else 0
        print(f"  ✓ {f.name}  {src_size/1024:>6.1f}KB → {dst_size/1024:>6.1f}KB  (省 {saved:.1f}%)")

    print()
    print("=" * 60)
    print(f"✅ 完成 {len(files)} 张")
    print(f"💾 磁盘: {(total_src/1024/1024):.1f}MB → {(total_dst/1024/1024):.1f}MB  (省 {(1-total_dst/total_src)*100:.1f}%)")


if __name__ == "__main__":
    main()
