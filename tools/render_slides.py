"""Render WFCditasik .dc.html artboards to 1080x1350 PNGs.
Usage: python3 render_slides.py <project_dir> <out_dir> <fonts_dir> File1.dc.html File2.dc.html ...
"""
import re, sys, pathlib
from playwright.sync_api import sync_playwright

proj, out, fonts = map(pathlib.Path, sys.argv[1:4])
files = sys.argv[4:]
out.mkdir(parents=True, exist_ok=True)
VALS = {"maroon": "#7A1C1C", "accent": "#7A1C1C"}

head = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Plus Jakarta Sans';src:url('file://{(fonts/'PlusJakartaSans[wght].ttf').as_posix()}') format('truetype');font-weight:200 800;}}
@font-face{{font-family:'Caveat';src:url('file://{(fonts/'Caveat[wght].ttf').as_posix()}') format('truetype');font-weight:400 700;}}
html,body{{margin:0;padding:0;background:#fff}}
</style></head><body>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    for i, name in enumerate(files, 1):
        src = (proj / name).read_text()
        body = re.search(r"<x-dc>(.*)</x-dc>", src, re.S).group(1)
        body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
        body = re.sub(r"\{\{\s*(\w+)\s*\}\}", lambda m: VALS.get(m.group(1), m.group(0)), body)
        html = out / f"_tmp_{i}.html"
        html.write_text(head + body + "</body></html>")
        pg.goto(html.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(out / f"slide-{i:02d}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        html.unlink()
        print("rendered", name)
    b.close()
