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

## Content strategy
WFCditasik = the ecosystem of working from anywhere in Tasikmalaya: community + media + lifestyle/culture + events + skill growth. Educate, but also embrace the culture and lifestyle.

Pillars (check the Pillar column in topics.md and keep this rough mix):
- **Skills & Tools (~40%)** — tool recommendations, productivity, career, client communication, skills in demand, being a smart/skillful/good worker, Gen Z work life, dreams, quality of life.
- **Lifestyle & Culture (~40%)** — fun, shareable posts: e.g. "Minuman kamu = kerjaan kamu" (drink vs job), "Tipe-tipe orang WFC" (playful, never mean), WFC bingo, focus playlists, kopi vs matcha.
- **Community (~10%)** — only ideas that need NO photos or member details: "Kenapa kerja bareng bikin lebih semangat", "Kamu tim kopi atau tim matcha?" (comment prompt), WFCbareng invite (every Thursday, no location).
- **Trending (~10%, only when there's a strong hook)** — react to something current/viral in work, career, AI, remote work or the industry (search the web that morning; prefer Indonesian/Gen Z relevance). Explain what it means for workers and how to stay smart and skillful. Facts must come from real sources; mention the source in the caption.

Photos: never ask Diah for photos or member details. Default to the built-in line drawings. Optionally use real event photos from her Google Drive (Google Drive connector) when they clearly fit and look good (polaroid frame), otherwise skip photos:
- "2026 - RW Hangout" folder id 1RSPFzpm8nWWF9nDJTukU7g5Q5j4Dbg2G (Remote Worker Hangout = RWH, sister community of WFCditasik): subfolders RW Hangout Vol 1–4, e.g. Vol 3 > "Foto" (1W_cQB8oBzJpjUrlebUkdKhpJPJiph9kZ, 100+ photos), Vol 2 > "Vol 2" (1i7TXBMVp19EqLuBQWpYikPXd989tlT5P)
- "2026 - WFCditasik" folder id 1LppiND7ro_4KpNzwKB17ajSWApEVnubW (subfolder "WFCbareng Dokum")
- "WFCbareng" folder id 17ktQaAh529frxK4_pY5R9lx3x0R5mGIL (shared from englishspotbykerang@gmail.com; one subfolder per Thursday session, e.g. "Kamis, 3 Sep 2026") — best source for WFCbareng/community photos
- "Remote Worker Hangout" folder id 1ZQWPwlv6fR5KCX-5hdcGRKvvMUljIhdU (shared from englishspotbykerang@gmail.com)
- Search inside with the Drive connector: `parentId = '<folder id>'`, then go into subfolders.
- Most files are iPhone HEIC: convert with `pip install --break-system-packages pillow-heif` then Pillow (register_heif_opener) to JPG before use. Look at a photo before using it; pick bright, natural, flattering shots; never a close-up of one identifiable person without context.

## Metricool
- Brand blogId 4176662 (Instagram @wfcditasik), timezone Asia/Jakarta.
- Media = raw GitHub URLs: https://raw.githubusercontent.com/asmardiahva-spec/wfcditasik-asset/main/carousels/<folder>/slide-NN.png
