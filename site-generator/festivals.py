"""Festival packs: type a festival name -> colours, text, emblem and effects are chosen automatically.
Placeholders in text: {n}=Name, {N}=NAME, {year}, {date}. Unknown names fall back to GENERIC + a name-based palette."""
import re
from datetime import datetime, timedelta

def _p(g, r, c, p, rd, gd, i):
    return dict(green=g, green2=r, cream=c, paper=p, red=rd, gold=gd, ink=i)

EXTRA_PRESETS = {
    "diwali":    _p("#2b0f14", "#46161d", "#fff4e0", "#f8e6c8", "#e8681a", "#f4b942", "#2b0f14"),
    "navratri":  _p("#4a0f2e", "#6b1b45", "#fff3e3", "#f9e1c4", "#c62f5a", "#f6b73c", "#3a0b23"),
    "holi":      _p("#3b1f6b", "#5a2f99", "#fff8f0", "#fdebdc", "#e6397a", "#2ec4b6", "#2b1650"),
    "eid":       _p("#0d3b36", "#145248", "#f6f1e4", "#ebe3cf", "#a0702a", "#e6cf8f", "#0d3b36"),
    "uttarayan": _p("#0b3d6b", "#14568f", "#f4f8fb", "#e3eef6", "#f26b21", "#ffd23f", "#0b2f52"),
}

GENERIC = {
    "page_title": "A {n} Celebration", "meta_desc": "You're invited to celebrate {n} on {date}.",
    "announcement": "CELEBRATING {N} TOGETHER", "headline": "Celebrate<br><em>{n}</em> with us.",
    "hero_intro": "Good people. Great food. Wonderful memories.<br class=\"desktop-only\"> Join us for a {n} to remember.",
    "art_caption": "{N}<br>{year}", "hero_foot": "MADE WITH LOVE", "occasion": "{n} <em>Party</em>", "vibe": "Joyful <em>&</em> Bright",
    "intro_title": "Come for the<br>celebration.<br><em>Stay for the memories.</em>", "intro_lead": "{n} is better when we're together.",
    "intro_p1": "So gather with us for delicious food, wonderful music and all the little moments that make {n} special.",
    "intro_p2": "Dress up, bring your family and friends, and let the celebrations begin.",
    "moments_sub": "Everything you need for a<br>proper {n} celebration.",
    "moments": [{"icon": "✳", "title": "Festive<br>feasting", "text": "Tasty bites, sweet treats<br>and something delicious.", "scribble": "YUM!"},
                {"icon": "♫", "title": "Good tunes<br>only", "text": "Great music and<br>dance-floor favourites.", "scribble": "♪ ♫ ♪"},
                {"icon": "♡", "title": "Joy all<br>around", "text": "Lovely people, little surprises<br>and plenty of cheer.", "scribble": "CHEERS!"}],
    "quote": "“The best way to spread joy is to celebrate together.”", "quote_by": "— THE {N} SPIRIT",
    "countdown_title": "See you at<br>the <em>celebration.</em>", "party_time": "It’s {n}<br>time, <em>everyone!</em>",
    "rsvp_subject": "{n} Party RSVP", "foot_tag": "HAPPY {N}", "footer_line": "MAKE ROOM FOR A LITTLE JOY.",
    "marquee": ["HAPPY {N}", "GOOD FOOD", "GREAT MUSIC", "LOVELY PEOPLE"],
}

def _m(i, t, x, s): return {"icon": i, "title": t, "text": x, "scribble": s}

FESTIVALS = {
    "christmas": dict(name="Christmas", aka=["xmas", "x-mas"], fixed=(12, 25), hour=18, keep_default=True, preset="christmas", hero_art="tree", particle="snow"),
    "diwali": dict(name="Diwali", aka=["deepavali"], preset="diwali", hero_art="emblem", emblem="🪔", particle="embers",
        announcement="THE FESTIVAL OF LIGHTS", headline="Light up the night,<br><em>Happy</em> Diwali.",
        hero_intro="Diyas, sweets and the people we love.<br class=\"desktop-only\"> Let's make this Diwali shine.", art_caption="FESTIVAL<br>OF LIGHTS",
        occasion="Diwali <em>Celebration</em>", vibe="Bright <em>&</em> Beautiful", dress="Traditional / festive Indian wear",
        moments=[_m("🪔", "Diyas &<br>rangoli", "Glowing lamps and<br>colourful designs.", "SHUBH!"), _m("🍬", "Mithai &<br>feasting", "Sweets, snacks and<br>a festive spread.", "YUM!"), _m("🎆", "Lights &<br>laughter", "Fireworks, music and<br>joyful company.", "WOW!")],
        marquee=["HAPPY DIWALI", "DIYAS", "MITHAI", "LIGHTS", "FAMILY"], quote="“Let the light within us outshine the darkness.”", quote_by="— THE DIWALI SPIRIT",
        footer_line="MAY YOUR HOME GLOW WITH JOY.", foot_tag="SHUBH DIWALI"),
    "navratri": dict(name="Navratri", aka=["garba", "dandiya"], preset="navratri", hero_art="emblem", emblem="💃", particle="confetti",
        announcement="NINE NIGHTS OF GARBA", headline="Nine nights.<br><em>One</em> grand garba.",
        hero_intro="Dandiya, dance and divine energy.<br class=\"desktop-only\"> Come celebrate Navratri with us.", art_caption="GARBA<br>& DANDIYA",
        occasion="Garba <em>Night</em>", vibe="Colourful <em>&</em> Energetic", dress="Chaniya choli / kediyu — go colourful!",
        moments=[_m("💃", "Garba &<br>dandiya", "Twirl, clap and dance<br>till the beat drops.", "DHOOM!"), _m("🍛", "Festive<br>bites", "Snacks, chai and<br>a delicious spread.", "YUM!"), _m("🙏", "Aarti &<br>blessings", "Begin the night with<br>devotion and joy.", "JAI MATA DI")],
        marquee=["NAVRATRI", "GARBA", "DANDIYA", "JAI MATA DI", "DANCE"], quote="“When the music starts, the whole world dances.”", quote_by="— THE GARBA SPIRIT",
        footer_line="TILL THE LAST DANDIYA.", foot_tag="HAPPY NAVRATRI"),
    "holi": dict(name="Holi", aka=["rangwali holi"], preset="holi", hero_art="emblem", emblem="🎨", particle="confetti",
        announcement="THE FESTIVAL OF COLOURS", headline="Play with<br><em>colour.</em> Happy Holi.",
        hero_intro="Colour, sweets and endless laughter.<br class=\"desktop-only\"> Wear white — leave colourful.", art_caption="RANG<br>BARSE",
        occasion="Holi <em>Party</em>", vibe="Messy <em>&</em> Magical", dress="White clothes (they won't stay white!)",
        moments=[_m("🎨", "Colours &<br>gulal", "Organic colours and<br>water-play fun.", "RANG!"), _m("🥛", "Thandai &<br>sweets", "Cool drinks, gujiya and<br>festive snacks.", "YUM!"), _m("🥁", "Dhol &<br>dance", "Beats that keep you<br>dancing all day.", "HOLI HAI!")],
        marquee=["HAPPY HOLI", "COLOURS", "GUJIYA", "THANDAI", "DHOL"], quote="“Life is better when it's colourful.”", quote_by="— THE HOLI SPIRIT",
        footer_line="COLOUR YOUR WORLD.", foot_tag="HAPPY HOLI"),
    "eid": dict(name="Eid", aka=["eid mubarak", "eid al-fitr", "eid ul fitr", "eid al-adha"], preset="eid", hero_art="emblem", emblem="🌙", particle="embers",
        announcement="EID MUBARAK", headline="Eid<br><em>Mubarak</em> to all.",
        hero_intro="Family, feasting and gratitude.<br class=\"desktop-only\"> Let's celebrate Eid together.", art_caption="EID<br>MUBARAK",
        occasion="Eid <em>Gathering</em>", vibe="Warm <em>&</em> Joyful", dress="Festive traditional wear",
        moments=[_m("🍽️", "Feast &<br>sweets", "Biryani, sheer khurma<br>and so much more.", "YUM!"), _m("🤲", "Gratitude &<br>blessings", "A day for family,<br>prayer and giving.", "MUBARAK!"), _m("🎁", "Eidi &<br>smiles", "Little surprises and<br>joyful greetings.", "EIDI!")],
        marquee=["EID MUBARAK", "FEAST", "FAMILY", "GRATITUDE", "JOY"], quote="“Eid is a time to share joy and gratitude.”", quote_by="— THE EID SPIRIT",
        footer_line="EID MUBARAK TO YOU AND YOURS.", foot_tag="EID MUBARAK"),
    "uttarayan": dict(name="Uttarayan", aka=["makar sankranti", "sankranti", "kite festival", "pongal"], fixed=(1, 14), hour=9, preset="uttarayan", hero_art="emblem", emblem="🪁", particle="confetti",
        announcement="KITES UP, SKIES ALIVE", headline="Fly high,<br><em>Happy</em> Uttarayan.",
        hero_intro="Kites, undhiyu and rooftop fun.<br class=\"desktop-only\"> Come celebrate Makar Sankranti!", art_caption="KAI PO<br>CHE!",
        occasion="Kite <em>Festival</em>", vibe="Sunny <em>&</em> Sky-high", dress="Comfy, colourful & sun-ready",
        moments=[_m("🪁", "Kites &<br>manjha", "Rooftop battles and<br>a sky full of colour.", "KAI PO CHE!"), _m("🍲", "Undhiyu &<br>chikki", "Winter specials, jalebi<br>and tilgul treats.", "YUM!"), _m("🎶", "Music &<br>rooftop vibes", "Loud beats, family<br>and good company.", "LAPET!")],
        marquee=["KAI PO CHE", "KITES", "UNDHIYU", "CHIKKI", "JALEBI"], quote="“Let your spirit fly higher than the kites.”", quote_by="— THE UTTARAYAN SPIRIT",
        footer_line="HIGHER THAN THE KITES.", foot_tag="HAPPY UTTARAYAN"),
    "halloween": dict(name="Halloween", fixed=(10, 31), hour=19, preset="halloween", hero_art="emblem", emblem="🎃", particle="embers",
        announcement="TRICKS, TREATS & SPOOKY SEASON", headline="Something<br><em>wicked</em> this way comes.",
        hero_intro="Costumes, candy and a few friendly frights.<br class=\"desktop-only\"> Dare to join us?", art_caption="TRICK<br>OR TREAT",
        occasion="Halloween <em>Party</em>", vibe="Spooky <em>&</em> Fun", dress="Costume required — the creepier the better",
        moments=[_m("🎃", "Costume<br>contest", "Show off your scariest<br>or silliest look.", "BOO!"), _m("🍬", "Treats &<br>potions", "Candy, cider and<br>spooky snacks.", "TREAT!"), _m("👻", "Spooky<br>games", "Ghost stories, games<br>and surprise scares.", "EEEK!")],
        marquee=["TRICK OR TREAT", "BOO", "CANDY", "COSTUMES", "SPOOKY"], quote="“Life's a little more fun with a touch of fright.”", quote_by="— THE HALLOWEEN SPIRIT",
        footer_line="STAY SPOOKY.", foot_tag="HAPPY HALLOWEEN"),
    "new year": dict(name="New Year", aka=["new year's eve", "nye", "newyear"], fixed=(12, 31), hour=21, preset="newyear", hero_art="emblem", emblem="🥂", particle="confetti",
        announcement="COUNTDOWN TO A NEW YEAR", headline="Cheers to<br><em>new</em> beginnings.",
        hero_intro="Music, midnight and a fresh start.<br class=\"desktop-only\"> Let's ring in the new year together.", art_caption="MIDNIGHT<br>COUNTDOWN",
        occasion="New Year <em>Party</em>", vibe="Sparkly <em>&</em> Hopeful", dress="Sparkle, sequins & smart casual",
        moments=[_m("🥂", "Toasts &<br>bites", "Bubbles, canapés and<br>sweet treats.", "CHEERS!"), _m("🎧", "Dance<br>floor", "Countdown beats until<br>the clock strikes twelve.", "DANCE!"), _m("🎆", "Midnight<br>magic", "Fireworks, resolutions<br>and big hugs.", "3 · 2 · 1!")],
        marquee=["HAPPY NEW YEAR", "CHEERS", "MIDNIGHT", "SPARKLE", "NEW BEGINNINGS"], quote="“Every moment is a fresh beginning.”", quote_by="— THE NEW YEAR SPIRIT",
        footer_line="HERE'S TO NEW BEGINNINGS.", foot_tag="HAPPY NEW YEAR"),
    "birthday": dict(name="Birthday", aka=["birthday party", "bday"], preset="birthday", hero_art="emblem", emblem="🎂", particle="confetti", announcement="IT'S PARTY TIME"),
    "wedding": dict(name="Wedding", aka=["shaadi", "marriage"], preset="wedding", hero_art="emblem", emblem="💍", particle="embers", announcement="TWO HEARTS, ONE CELEBRATION"),
}

def names(): return [p["name"] for p in FESTIVALS.values()]

def festival_config(name, now=None):
    """Returns config overrides for a festival name (known or unknown)."""
    now, q = now or datetime.now(), name.strip().lower()
    p = next((dict(v) for k, v in FESTIVALS.items() if q == k or q in v.get("aka", [])), None)
    names_ = sorted(list(EXTRA_PRESETS) + ["birthday", "newyear"])
    p = p or dict(preset=names_[sum(map(ord, q)) % len(names_)], hero_art="emblem", emblem="✨", particle="confetti")
    display = p.pop("name", name.strip().title() if name.islower() else name.strip())
    fixed, hour, keep = p.pop("fixed", None), p.pop("hour", 19), p.pop("keep_default", False)
    p.pop("aka", None)
    cfg = {} if keep else dict(GENERIC)
    cfg.update(p)
    cfg.update(name=display, brand=display.upper(), slug=re.sub(r"[^a-z0-9]+", "-", display.lower()).strip("-") + "-party")
    if fixed:
        d = datetime(now.year, fixed[0], fixed[1], hour)
        cfg["date"] = (d if d > now else d.replace(year=now.year + 1)).strftime("%Y-%m-%dT%H:%M")
    else:  # movable / unknown festival: placeholder date, the generator warns until a real one is given
        cfg["date"] = (now + timedelta(days=45)).strftime("%Y-%m-%dT19:00"); cfg["_date_guess"] = True
    return cfg
