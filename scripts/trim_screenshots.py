#!/usr/bin/env python3
"""
裁切 98 张截图四周的黑色 letterbox 区域
- 黑色阈值：RGB 任一通道 > threshold 视为非黑
- 输出到 raw/trimmed/，原图保留
"""
import sys
from pathlib import Path
from PIL import Image
import numpy as np

# ============== 配置 ==============
SRC_DIR = Path(__file__).resolve().parent.parent / "raw" / "screenshots"
DST_DIR = Path(__file__).resolve().parent.parent / "raw" / "trimmed"
THRESHOLD = 15  # 黑色阈值，0=纯黑，可放宽到 15-30 容忍 JPEG 压缩噪声
PADDING = 8     # 裁切后保留 8px 黑色边距，避免切到 PDF 边线
# ================================


def trim_one(src: Path, dst: Path, threshold: int = THRESHOLD, padding: int = PADDING) -> tuple:
    """裁切一张图，返回 (原尺寸, 裁切后尺寸, 节省比例)"""
    img = Image.open(src).convert("RGB")
    orig_w, orig_h = img.size
    arr = np.array(img)

    # 非黑 mask：任一通道 > threshold
    mask = (arr > threshold).any(axis=2)

    rows_has = mask.any(axis=1)
    cols_has = mask.any(axis=0)

    if not rows_has.any() or not cols_has.any():
        # 全黑图（如 page86 之前那张）
        return (orig_w, orig_h), (0, 0), 0.0

    top = int(rows_has.argmax())
    bottom = len(rows_has) - int(rows_has[::-1].argmax()) - 1
    left = int(cols_has.argmax())
    right = len(cols_has) - int(cols_has[::-1].argmax()) - 1

    # 加 padding（向外扩展，但不超过原图边界）
    top = max(0, top - padding)
    left = max(0, left - padding)
    bottom = min(orig_h - 1, bottom + padding)
    right = min(orig_w - 1, right + padding)

    trimmed = img.crop((left, top, right + 1, bottom + 1))
    new_w, new_h = trimmed.size
    trimmed.save(dst, "JPEG", quality=92, optimize=True)

    orig_px = orig_w * orig_h
    new_px = new_w * new_h
    saved_pct = (1 - new_px / orig_px) * 100 if orig_px else 0

    return (orig_w, orig_h), (new_w, new_h), saved_pct


def main():
    DST_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(SRC_DIR.glob("page*.jpg"))
    if not files:
        print(f"❌  在 {SRC_DIR} 没找到截图")
        sys.exit(1)

    print(f"📁 源目录: {SRC_DIR}")
    print(f"📁 输出:   {DST_DIR}")
    print(f"🔍 黑色阈值: RGB > {THRESHOLD}")
    print(f"📏 边距保留: {PADDING}px")
    print(f"📊 文件数: {len(files)}")
    print()

    total_orig = 0
    total_new = 0
    skipped = 0

    for f in files:
        dst = DST_DIR / f.name
        try:
            orig, new, saved = trim_one(f, dst)
            if new == (0, 0):
                print(f"  ⏭️  {f.name}  全黑/无效，跳过")
                skipped += 1
                continue
            orig_px = orig[0] * orig[1]
            new_px = new[0] * new[1]
            total_orig += orig_px
            total_new += new_px
            print(f"  ✓ {f.name}  {orig[0]}x{orig[1]} → {new[0]}x{new[1]}  (省 {saved:.1f}%)")
        except Exception as e:
            print(f"  ❌ {f.name}  失败: {e}")

    print()
    print("=" * 60)
    print(f"✅ 完成：成功 {len(files) - skipped - 0} 张，跳过 {skipped} 张")
    if total_orig > 0:
        total_saved = (1 - total_new / total_orig) * 100
        print(f"📊 总像素: {(total_orig / 1e6):.1f}M → {(total_new / 1e6):.1f}M  (省 {total_saved:.1f}%)")

    # 磁盘大小对比
    src_size = sum(f.stat().st_size for f in files)
    dst_files = list(DST_DIR.glob("page*.jpg"))
    dst_size = sum(f.stat().st_size for f in dst_files)
    if src_size > 0:
        print(f"💾 磁盘: {(src_size / 1024 / 1024):.1f}MB → {(dst_size / 1024 / 1024):.1f}MB  (省 {(1 - dst_size / src_size) * 100:.1f}%)")


if __name__ == "__main__":
    main()
