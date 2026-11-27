#!/usr/bin/env python3
"""Event-website generator: one JSON config -> a complete, animated, responsive site (HTML + CSS + JS).

  python generator.py --init my.json --preset halloween   # write a starter config
  python generator.py my.json -o dist --zip                # build (and zip) the site
  python generator.py my.json --serve                      # build + preview on http://localhost:8000
"""
import festivals as F
import argparse, functools, http.server, json, re, sys, zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

TPL = Path(__file__).parent / "templates"

# Colour presets: green=dark background, cream=light background, red=main accent, gold=secondary accent
PRESETS = {
    "christmas": dict(green="#102d24", green2="#1b4033", cream="#f5f0e6", paper="#eee7d9", red="#a93635", gold="#d7b978", ink="#1a3028"),
    "birthday":  dict(green="#2b1650", green2="#3d2275", cream="#fff6ee", paper="#fbe9dd", red="#e0457b", gold="#ffc857", ink="#2b1650"),
    "halloween": dict(green="#14101c", green2="#231a30", cream="#f3ece0", paper="#e9dfcd", red="#e8651a", gold="#f2b441", ink="#1c1424"),
    "wedding":   dict(green="#3b4a40", green2="#52655a", cream="#faf6f0", paper="#f1e9de", red="#b9786a", gold="#c9a96a", ink="#2b332e"),
    "newyear":   dict(green="#0b1020", green2="#16203d", cream="#f4f1ea", paper="#e8e3d6", red="#c0392b", gold="#e3c06a", ink="#101830"),
}

DEFAULT = {
    "preset": "christmas", "colors": {}, "fonts": {"serif": "Playfair Display", "sans": "DM Sans"},
    "slug": "noel-christmas-party", "brand": "NOËL", "page_title": "A Christmas Party",
    "meta_desc": "Join us for a little more Christmas magic on 25 December 2026.",
    "date": "2026-12-25T18:00", "duration_hours": 4,
    "time_text": "6:00 PM", "venue": "[ Add venue and address ]", "dress": "Festive / Come as you feel fabulous",
    "rsvp_deadline": "[ RSVP DEADLINE ]", "organizer_email": "[ADD-ORGANIZER-EMAIL]", "rsvp_subject": "Christmas Party RSVP",
    "announcement": "THE MOST WONDERFUL TIME OF THE YEAR", "eyebrow": "YOU'RE INVITED TO CELEBRATE",
    "headline": "A little more<br><em>Christmas</em> magic.",
    "hero_intro": "Good people. Warm lights. A night full of wonder.<br class=\"desktop-only\"> Let's make this one worth remembering.",
    "hero_art": "tree", "emblem": "✨", "particle": "snow", "art_caption": "A SEASON TO<br>BE TOGETHER", "hero_foot": "MADE WITH HOLIDAY SPIRIT",
    "occasion": "Christmas <em>Party</em>", "vibe": "Festive <em>&</em> Fabulous",
    "intro_title": "Come for the<br>festive feeling.<br><em>Stay for the memories.</em>",
    "intro_lead": "Christmas is better when we're together.",
    "intro_p1": "So, let's gather under the lights for an evening of delicious treats, feel-good music, cheerful company and all the little moments that make the season special.",
    "intro_p2": "Dress up, bring your best holiday spirit, and let the celebrations begin.",
    "moments_title": "Little moments.<br><em>Big memories.</em>", "moments_sub": "Everything you need for a<br>proper Christmas celebration.",
    "moments": [
        {"icon": "✳", "title": "Festive<br>feasting", "text": "Seasonal bites, sweet treats<br>and something delicious.", "scribble": "YUM!"},
        {"icon": "♫", "title": "Good tunes<br>only", "text": "Holiday classics and<br>dance-floor favourites.", "scribble": "♪ ♫ ♪"},
        {"icon": "♡", "title": "Joy all<br>around", "text": "Lovely people, little surprises<br>and plenty of cheer.", "scribble": "CHEERS!"}],
    "schedule_title": "Here's how<br>the night <em>glows.</em>", "schedule_sub": "A little structure, a lot of sparkle.<br>Adjust the times to fit your night.",
    "schedule": [
        {"time": "06:00 PM", "icon": "✧", "title": "Doors open & hellos", "text": "Arrive, settle in and soak up the festive atmosphere."},
        {"time": "07:00 PM", "icon": "✳", "title": "Let the feasting begin", "text": "Good food, great company and a little Christmas magic."},
        {"time": "08:30 PM", "icon": "♫", "title": "Music, games & cheer", "text": "Bring your best moves and your competitive spirit."},
        {"time": "10:00 PM", "icon": "♡", "title": "One last toast", "text": "Make a memory, share a laugh and wrap up the night."}],
    "details_title": "Put it in<br>your <em>calendar.</em>",
    "quote": "“The best way to spread Christmas cheer is to celebrate together.”", "quote_by": "— THE NOËL SPIRIT",
    "countdown_title": "See you under<br>the <em>mistletoe.</em>", "party_time": "It’s party<br>time, <em>Noël!</em>",
    "rsvp_title": "Save a little<br><em>room for joy.</em>", "rsvp_text": "Let us know you're coming. We can't wait to celebrate with you.",
    "foot_tag": "MERRY EVERYTHING", "footer_line": "MAKE ROOM FOR A LITTLE MAGIC.",
    "marquee": ["MERRY & BRIGHT", "GOOD FOOD", "GREAT MUSIC", "LOVELY PEOPLE"],
}

PRESETS.update(F.EXTRA_PRESETS)
esc_js = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
esc_ics = lambda s: re.sub(r"([,;])", r"\\\1", s)

def moments_html(items):  # cards cycle through the 3 colour styles defined in the CSS
    style = ["card-food", "card-music", "card-cheer"]
    return "\n".join(
        f'        <article class="moment-card {style[i % 3]}"><div class="card-number">{i+1:02d}</div><div class="moment-icon">{m["icon"]}</div>'
        f'<h3>{m["title"]}</h3><p>{m["text"]}</p><span class="{"music-lines" if i % 3 == 1 else "card-scribble"}">{m.get("scribble", "")}</span></article>'
        for i, m in enumerate(items))

def timeline_html(rows):
    return "\n".join(
        f'        <div class="timeline-row"><span class="time">[ {r["time"]} ]</span><span class="timeline-dot"></span>'
        f'<div><h3>{r["title"]}</h3><p>{r["text"]}</p></div><span class="timeline-emoji">{r["icon"]}</span></div>' for r in rows)

def tokens(cfg):
    dt = datetime.fromisoformat(cfg["date"])
    t = {k.upper(): v for k, v in cfg.items() if isinstance(v, str)}
    t.update({k.upper(): v for k, v in cfg["_colors"].items()})
    sans, serif = cfg["fonts"]["sans"], cfg["fonts"]["serif"]
    plus = lambda s: s.replace(" ", "+")
    t.update(
        SERIF=serif, SANS=sans, ORG_EMAIL=esc_js(cfg["organizer_email"]), RSVP_SUBJECT=esc_js(cfg["rsvp_subject"]), PARTY_TIME=esc_js(cfg["party_time"]),
        FONTS_URL=f"https://fonts.googleapis.com/css2?family={plus(sans)}:wght@400;500;600;700&family={plus(serif)}:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap",
        DATE_CAPS=f"{dt.day} {dt:%B %Y}".upper(), DATE_FULL=f"{dt:%A}, {dt.day} {dt:%B %Y}",
        DATE_SLASH=f"{dt:%d} <i> / </i> {dt:%m} <i> / </i> {dt:%y}", EVENT_ISO=dt.strftime("%Y-%m-%dT%H:%M:%S"),
        ICS_START=dt.strftime("%Y%m%dT%H%M%S"), ICS_END=(dt + timedelta(hours=cfg["duration_hours"])).strftime("%Y%m%dT%H%M%S"),
        ICS_STAMP=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        ICS_TITLE=esc_js(esc_ics(f'{cfg["brand"]} — {cfg["page_title"]}')), ICS_DESC=esc_js(esc_ics(cfg["meta_desc"])),
        MOMENTS=moments_html(cfg["moments"]), TIMELINE=timeline_html(cfg["schedule"]),
        MARQUEE="".join(f"<span>{'✳✦'[i % len(cfg['marquee']) % 2]} {x}</span>" for i, x in enumerate(cfg["marquee"] * 2)))
    return t

def fill(text, t):  # single pass, so placeholder-looking text inside values is never re-expanded
    def rep(m):
        if m.group(1) not in t: sys.exit(f"Template needs a value for {{{{{m.group(1)}}}}}")
        return str(t[m.group(1)])
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", rep, text)

def subst(obj, v):  # fill {n} {N} {year} {date} inside any text (also inside lists/dicts)
    if isinstance(obj, str): return re.sub(r"\{(n|N|year|date)\}", lambda m: v[m.group(1)], obj)
    if isinstance(obj, list): return [subst(o, v) for o in obj]
    if isinstance(obj, dict): return {k: subst(o, v) for k, o in obj.items()}
    return obj

def load(path=None, preset=None, festival=None, cli=None):
    user = json.loads(Path(path).read_text(encoding="utf-8")) if path else {}
    festival = festival or user.get("festival")
    base = {**DEFAULT, **(F.festival_config(festival) if festival else {})}
    cfg = {**base, **user, **{k: v for k, v in (cli or {}).items() if v}}
    cfg["fonts"] = {**DEFAULT["fonts"], **user.get("fonts", {})}
    if preset: cfg["preset"] = preset
    if cfg["preset"] not in PRESETS: sys.exit(f"Unknown preset '{cfg['preset']}'. Choose: {', '.join(PRESETS)}")
    cfg["_colors"] = {**PRESETS[cfg["preset"]], **cfg["colors"]}
    d = cfg["date"].strip().replace(" ", "T"); cfg["date"] = d + "T19:00" if len(d) == 10 else d
    try: dt = datetime.fromisoformat(cfg["date"])
    except ValueError: sys.exit('Date must look like 2027-10-29 19:00')
    given = {**user, **{k: v for k, v in (cli or {}).items() if v}}
    if cfg.pop("_date_guess", False) and "date" not in given: print(f"⚠ No date known for {cfg.get('name')} — using {cfg['date']}. Pass --date 'YYYY-MM-DD HH:MM'.")
    if "time_text" not in given: cfg["time_text"] = f"{dt:%I:%M %p}".lstrip("0")
    if "schedule" not in given:  # spread the evening from the start time
        for r, off in zip(cfg["schedule"], (0, 1, 2.5, 4)): r["time"] = f"{dt + timedelta(hours=off):%I:%M %p}"
    cfg["organizer_email"] = cfg.get("email") or cfg["organizer_email"]
    return subst(cfg, {"n": cfg.get("name", cfg["brand"]), "N": cfg.get("name", cfg["brand"]).upper(), "year": str(dt.year), "date": f"{dt:%A}, {dt.day} {dt:%B %Y}"})

def build(cfg, out):
    out.mkdir(parents=True, exist_ok=True); t = tokens(cfg)
    art = {True: "tree", False: "none"}.get(cfg["hero_art"], cfg["hero_art"])
    for name in ("index.html", "style.css", "script.js"):
        txt = (TPL / name).read_text(encoding="utf-8")
        if name == "index.html":
            for tag, keep in (("ART", art == "tree"), ("EMBLEM", art == "emblem")):
                txt = txt.replace(f"<!--{tag}-->", "").replace(f"<!--/{tag}-->", "") if keep else re.sub(rf"<!--{tag}-->.*?<!--/{tag}-->", "", txt, flags=re.S)
        (out / name).write_text(fill(txt, t), encoding="utf-8")
    todo = [k for k, v in cfg.items() if isinstance(v, str) and v.strip().startswith("[")]
    if todo: print("⚠ Still placeholders in:", ", ".join(todo), "(pass --venue / --email / edit the config)")

def ask(q, default=""):
    a = input(f"{q}" + (f" [{default}]" if default else "") + ": ").strip(); return a or default

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", nargs="?", help="optional config JSON (overrides anything the festival pack sets)")
    ap.add_argument("-f", "--festival", help="festival name, e.g. Diwali, Holi, Eid, Navratri, Halloween — or ANY name")
    ap.add_argument("--date", help="'YYYY-MM-DD HH:MM'"); ap.add_argument("--venue"); ap.add_argument("--email"); ap.add_argument("--brand", help="header logo text")
    ap.add_argument("-i", "--interactive", action="store_true", help="ask questions instead of using flags")
    ap.add_argument("--list", action="store_true", help="list built-in festivals")
    ap.add_argument("-o", "--out"); ap.add_argument("--preset", choices=PRESETS)
    ap.add_argument("--init", metavar="FILE", help="write a complete starter config and exit")
    ap.add_argument("--zip", action="store_true"); ap.add_argument("--serve", type=int, nargs="?", const=8000, metavar="PORT")
    a = ap.parse_args()
    if a.list: return print("Built-in festivals:", ", ".join(F.names()), "\nAny other name also works (generic text + auto colours).")
    if a.init:
        Path(a.init).write_text(json.dumps({**DEFAULT, "preset": a.preset or "christmas"}, ensure_ascii=False, indent=2), encoding="utf-8"); return print("Wrote", a.init)
    if a.interactive or (not a.config and not a.festival and sys.stdin.isatty()):
        print("🎉 Festival website builder\nBuilt-in:", ", ".join(F.names()), "— or type any festival name\n")
        a.festival = ask("Festival name", "Christmas"); a.date = ask("Date & time, e.g. 2027-10-29 19:00 (Enter = auto)")
        a.venue = ask("Venue / address (Enter to skip)"); a.email = ask("Your email for RSVPs (Enter to skip)")
    cli = dict(date=a.date, venue=a.venue, email=a.email, brand=a.brand)
    cfg = load(a.config, a.preset, a.festival, cli)
    out = Path(a.out or (cfg["slug"] + "-site")); build(cfg, out); print(f"✓ Built {out}/  ({cfg.get('name', cfg['brand'])} · {cfg['preset']} theme · {cfg['hero_art']} art · {cfg['particle']})")
    if a.zip:
        z = out.with_suffix(".zip")
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in out.iterdir(): zf.write(f, f"{cfg['slug']}/{f.name}")
        print("✓ Zipped", z)
    if a.serve:
        print(f"Preview: http://localhost:{a.serve}  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("", a.serve), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(out))).serve_forever()

if __name__ == "__main__": main()
