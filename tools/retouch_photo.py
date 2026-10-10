"""Retouch a photo for WFCditasik slides: fix orientation, straighten, crop, and give a clean bright natural look.
Usage: python3 tools/retouch_photo.py <in> <out.jpg> <width> <height> [focus_y 0-1, default 0.5] [rotate_deg, default 0]
- focus_y picks where the crop sits vertically (0 = top, 1 = bottom) so people/drinks stay in frame.
- rotate_deg straightens a tilted horizon (small values like -1.5).
Requires: pip install --break-system-packages pillow-heif
"""
import sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pillow_heif import register_heif_opener

register_heif_opener()
src, out, W, H = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
focus_y = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
rot = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0

im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
if rot:
    w0, h0 = im.size
    im = im.rotate(rot, resample=Image.BICUBIC, expand=False)
    m = int(max(w0, h0) * abs(rot) / 57)  # trim the empty corners
    im = im.crop((m, m, w0 - m, h0 - m))

# crop to target ratio around focus
w, h = im.size
tr = W / H
if w / h > tr:
    nw = int(h * tr); x = (w - nw) // 2; im = im.crop((x, 0, x + nw, h))
else:
    nh = int(w / tr); y = int((h - nh) * focus_y); im = im.crop((0, y, w, y + nh))
im = im.resize((W, H), Image.LANCZOS)

# clean, bright, natural look
im = ImageOps.autocontrast(im, cutoff=0.6)
im = ImageEnhance.Brightness(im).enhance(1.06)
im = ImageEnhance.Contrast(im).enhance(1.05)
im = ImageEnhance.Color(im).enhance(1.06)
r, g, b = im.split()  # subtle warm cafe tone
r = r.point(lambda v: min(255, int(v * 1.025)))
b = b.point(lambda v: int(v * 0.975))
im = Image.merge("RGB", (r, g, b))
im = im.filter(ImageFilter.UnsharpMask(radius=1.4, percent=70, threshold=3))
im.save(out, quality=92)
print("saved", out, im.size)
