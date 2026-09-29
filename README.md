# Mira's Birthday Cards 🎂
Two pop-up birthday cards (navy starry + pink tile). Tap "Open your card" for the popup.

- `mira-birthday-navy.html` / `mira-birthday-pink.html` — editable versions (keep the `assets/` folder next to them)
- `standalone/` — same pages with all stickers embedded; just one file to send or upload anywhere
- `assets/` — cut-out stickers
- `prep.py` — script that cut the stickers out of the screenshots; `make_standalone.py` — re-embeds `assets/` into the single-file versions after you edit a page

Navy card film strip photos: `assets/photo1.jpg`, `photo2.jpg`, `photo3.jpg` (swap in new ones with the same names, then run `python3 make_standalone.py`).
To edit the message, search for "Thank you soo much" in either HTML file.
Free hosting: drag `standalone/*.html` into Netlify Drop or GitHub Pages.
