# Event Website Generator (Python)

Turns one JSON file into a complete animated event site (index.html + style.css + script.js). No dependencies — Python 3.8+ only.

## Quick start: just change the festival name
```bash
python generator.py                                   # asks: festival name, date, venue, email -> builds the whole site
python generator.py -f Diwali --date "2027-10-29 19:00" --venue "Our Home" --email me@mail.com
python generator.py -f "Ganesh Chaturthi"             # ANY name works (generic text + auto colours)
python generator.py -f Holi --serve                   # build + preview at http://localhost:8000
python generator.py --list                            # built-in festivals
```
Built-in packs (own colours, hero emblem, falling effect, text, ticker): Christmas, Diwali, Navratri/Garba, Holi, Eid, Uttarayan, Halloween, New Year, Birthday, Wedding.
Output goes to `<festival>-party-site/` (add `--zip` for a zip). Fixed-date festivals get their next date automatically; movable ones (Diwali, Holi, Eid, Navratri) need `--date`.
Use `--brand "SHARMA"` to change the header logo text. Everything a pack sets can be overridden in a JSON file: `python generator.py my.json` (`"festival": "Diwali"` + any field).

Add your own festival: copy a block in `festivals.py` (`FESTIVALS`) and, optionally, a palette in `EXTRA_PRESETS`.

Other commands: `--init my.json --preset halloween` (full starter config), `examples/birthday.json` (fully custom example).

## How it works
- `templates/` = the site with `{{PLACEHOLDERS}}`. `festivals.py` = festival packs. `generator.py` merges: defaults < festival pack < your JSON < command-line flags, then fills the templates.
- Repeated blocks (3 highlight cards, schedule rows, ticker items) are generated from lists in the config.
- Dates are computed for you: hero line, `25 / 12 / 26` strip, full date, countdown target, calendar (.ics) file.
- Colours come from a preset; override any with `"colors": {"red": "#ff0055"}`. Fonts: `"fonts": {"serif": "...", "sans": "..."}` (any Google Font).
- `"hero_art"`: `"tree"` (CSS Christmas tree), `"emblem"` (big glowing emoji set by `"emblem"`), or `false`. `"particle"`: `snow`, `confetti`, `embers`, `none`.
- Text fields accept simple HTML (`<br>`, `<em>` = gold italic word). Keep 3 items in `moments` (3-column grid).

## Theme analysis (what the generator reproduces)
- **Design tokens:** 7 CSS variables (dark green, cream, red, gold, ink…) + 2 font variables; everything else derives from them.
- **Type:** Playfair Display (serif headlines, one `<em>` word in gold italic) + DM Sans (tiny, wide-tracked uppercase labels). Section kickers numbered 01–05.
- **Layout:** sticky header, hero with CSS-shape illustration, ticker, 3-item date strip, 2-column intro, 3-card grid, timeline, details card, countdown, RSVP form, footer. 2 breakpoints (900px, 650px).
- **Motion/JS:** preloader curtain, scroll progress bar, header shrink, active-link highlight, IntersectionObserver reveals (staggered), hero parallax, card tilt, canvas snow, countdown, .ics download, toasts, `prefers-reduced-motion` support.
- **Limits:** tree/gift illustration colours and the snow are Christmas-specific; the RSVP form opens the visitor's email app (connect a form service to store replies).
