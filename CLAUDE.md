# wfcditasik-asset

Public image host for @wfcditasik Instagram carousels (Metricool pulls images from raw.githubusercontent.com links).

## Layout
- `carousels/<YYYY-MM-DD>-<slug>/slide-01.png …` — published carousel images, 1080×1350 PNG
- `templates/tips-wfc/*.dc.html` — reference slide designs (cover = Main, content = Tip1–5, CTA)
- `tools/render_slides.py` — renders .dc.html slides to PNG:
  `python3 tools/render_slides.py <slides_dir> <out_dir> tools/fonts Main.dc.html Tip1.dc.html … CTA.dc.html`
- `topics.md` — log of carousel topics already posted (never repeat one)

## Brand rules (full guideline: https://claude.ai/code/artifact/205a854c-4c6f-4ed8-9c12-3d1d67b05464)
- Format: Instagram carousel 1080×1350, 88px padding, 5–8 slides: cover → content slides → CTA
- Colors: WHITE #FFFFFF dominant background on every slide. Accents only: maroon #7A1C1C (headlines, icons, buttons) and matcha #D5E0BC (highlighted word, callouts, tags). Pale matcha #EEF3E2 callouts/icon tiles. Ink #2B2424 body, mocha grey #6E605B small text, borders #E6DCCF. No blue, no gradients, no full maroon/matcha slides, no emoji in designs.
- Fonts: Plus Jakarta Sans (ExtraBold 800 headlines, tight tracking, sentence case; Regular body), Caveat Bold for 2–5 word handwritten accents ("tip no. 1", "geser →").
- Notion-style components: breadcrumb + page number top, Notion page icon tile (104px pale matcha) with a maroon line drawing, callouts, tables with tags, checklists, cards. One component per content slide.
- Elements: only the built-in maroon line drawings (coffee cup, iced matcha, headphones, laptop, WiFi, plant, plug, clipboard). Keep sparse: max 2 on cover/CTA. No real/stock photos.
- Voice: casual, friendly Bahasa Indonesia; not too chatty; never salty, sarcastic or blaming. Say what to do, kindly.
- CTA slide: always "Follow @wfcditasik" (maroon pill button).
- WFCbareng: only as an invite to cowork with @wfcditasik every Thursday. Never name the cafe or location.
- Never invent cafe names, WiFi speeds, prices or dates.

## Metricool
- Brand blogId 4176662 (Instagram @wfcditasik), timezone Asia/Jakarta.
- Media = raw GitHub URLs: https://raw.githubusercontent.com/asmardiahva-spec/wfcditasik-asset/main/carousels/<folder>/slide-NN.png
