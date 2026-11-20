# Pinterest pinovi za članke (1000x1500, 2:3), na engleskom (EU publika).
# Pokretanje: python3.12 make_pins.py  -> pinterest/<slug>.png + pinterest/pinovi.md (naslov, opis, link)
import os, subprocess, html
import content_en as C

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "pinterest")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE = "https://glownotes.eu"
W, H = 1000, 1500

# slug (HR) -> (tekst na pinu, naslov pina, opis pina)
PINS = {
    "rhode-pocket-blush-tan-line-recenzija": ("Rhode Pocket Blush Tan Line: worth the hype?",
        "Rhode Pocket Blush Tan Line review: worth the hype?",
        "Honest review of Rhode Pocket Blush in Tan Line, the pinky-bronze cream blush that looks like a natural sun flush. Tested on sensitive, rosacea-prone skin."),
    "chanel-water-fresh-tint-recenzija": ("The skin tint my rosacea skin loves",
        "Chanel Water-Fresh Tint review on sensitive skin",
        "Chanel Les Beiges Water-Fresh Tint: light coverage, a natural glow and no reaction on my rosacea-prone skin. My honest review."),
    "la-roche-posay-cicaplast-baume-b5-recenzija": ("Cicaplast Baume B5+: instant calm for red skin",
        "La Roche-Posay Cicaplast Baume B5+ review for sensitive skin",
        "Why La Roche-Posay Cicaplast Baume B5+ became my moisturiser morning and night: calm, comfortable skin with rosacea. Honest review."),
    "babe-mineralni-spf-50-recenzija": ("The mineral SPF 50 I keep repurchasing",
        "Babé Mineral SPF 50 review: mineral sunscreen for sensitive skin",
        "Babé Mineral Super Fluid SPF 50: 100% mineral filters, no stinging eyes and easy to reapply. Honest review on fair, sensitive skin."),
    "mineralni-spf-recenzije-poredak": ("Mineral sunscreens for sensitive skin, ranked",
        "Best mineral sunscreens for sensitive skin, ranked",
        "6 mineral sunscreens tested on fair, sensitive skin with rosacea, from holy grail to total flop. Which leaves no white cast?"),
    "erborian-cc-red-correct-recenzija": ("Erborian CC Red Correct: great coverage, but…",
        "Erborian CC Red Correct review on rosacea skin",
        "Erborian CC Red Correct neutralises redness beautifully, but here is what happened to my rosacea skin after I took it off. Honest review."),
    "avene-couvrance-tekuci-puder-recenzija": ("Avène Couvrance foundation on rosacea skin",
        "Avène Couvrance liquid foundation review for sensitive skin",
        "Avène Couvrance SPF 20 foundation: pretty, even finish and good redness coverage, but was it right for my rosacea? Honest review."),
    "bioderma-photoderm-ar-spf-50-recenzija": ("Bioderma Photoderm AR: SPF for redness?",
        "Bioderma Photoderm AR SPF 50+ review on rosacea skin",
        "Bioderma Photoderm AR SPF 50+ promises to tone down redness. Here is how it worked on my sensitive, rosacea-prone skin."),
    "jane-iredale-hydropure-tinted-serum-recenzija": ("jane iredale HydroPure Tinted Serum: honest review",
        "jane iredale HydroPure Tinted Serum review on sensitive skin",
        "Weightless coverage with hyaluronic acid and CoQ10, but how did my rosacea skin react? Honest jane iredale HydroPure review."),
    "avene-cicalfate-serum-recenzija": ("Avène Cicalfate+ serum: worth it for redness?",
        "Avène Cicalfate+ serum review for sensitive skin",
        "Avène Cicalfate+ restorative serum on rosacea-prone skin: hydration, redness and whether I would buy it again."),
}

CSS = """
@font-face{font-family:'Fraunces';font-weight:100 900;src:url(../fonts/fraunces-latin.woff2) format('woff2')}
@font-face{font-family:'Instrument Sans';font-weight:400 700;src:url(../fonts/instrumentsans-latin.woff2) format('woff2')}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1000px;height:1500px;overflow:hidden}
body{background:#fffbf7;color:#3b1a22;font-family:'Instrument Sans',sans-serif;position:relative}
.gingham{position:absolute;left:0;right:0;top:0;height:120px;background:repeating-linear-gradient(0deg,rgba(232,104,140,.28) 0 30px,transparent 30px 60px),repeating-linear-gradient(90deg,rgba(232,104,140,.28) 0 30px,transparent 30px 60px),#fffbf7}
.photo{position:absolute;left:60px;top:70px;width:880px;height:660px;border-radius:36px;overflow:hidden;border:4px solid #7a1730;box-shadow:0 18px 40px rgba(122,23,48,.18)}
.photo img{width:100%;height:100%;object-fit:cover}
.kick{position:absolute;left:60px;top:780px;font-weight:700;font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:#7a1730;background:#fde6ec;border:3px solid #7a1730;border-radius:999px;padding:12px 26px}
h1{position:absolute;left:60px;right:60px;top:870px;font-family:'Fraunces',Georgia,serif;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1;font-size:84px;line-height:1.02;letter-spacing:-.01em;color:#3b1a22}
.rate{position:absolute;left:60px;bottom:170px;font-weight:700;font-size:34px;color:#fff;background:#e8688c;border-radius:999px;padding:14px 30px}
.foot{position:absolute;left:60px;right:60px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#7a1730;border-top:3px solid #f2d3db;padding-top:28px}
"""


def page(slug, text, rating):
    img = f"../assets/slike/{slug}.jpg"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="gingham"></div>
<div class="photo"><img src="{img}"></div>
<div class="kick">Honest review · sensitive skin</div>
<h1>{html.escape(text)}</h1>
{f'<div class="rate">{html.escape(rating)}</div>' if rating else ''}
<div class="foot"><span>glownotes.eu</span><span>Glow Notes</span></div>
</body></html>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    md = ["# Pinterest pinovi\n", "Svaki pin vodi na članak (pravilo linkova u objavama).\n"]
    for slug, (text, title, desc) in PINS.items():
        a = C.ARTICLES_EN[slug]
        verdict = a.get("verdict", "")
        rating = verdict.split(":")[0] if verdict.startswith("Rating") else ""
        src = os.path.join(OUT, f"_{slug}.html")
        open(src, "w").write(page(slug, text, rating))
        png = os.path.join(OUT, f"{slug}.png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                        f"--window-size={W},{H}", f"--screenshot={png}", "file://" + src],
                       check=True, capture_output=True)
        os.remove(src)
        url = f"{BASE}/en/articles/{a['slug']}/"
        md.append(f"## {title}\n\n- Slika: `pinterest/{slug}.png`\n- Link: {url}\n- Opis: {desc}\n")
        print(slug)
    open(os.path.join(OUT, "pinovi.md"), "w").write("\n".join(md))


if __name__ == "__main__":
    main()
