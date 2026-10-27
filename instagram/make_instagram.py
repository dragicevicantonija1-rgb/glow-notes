# Instagram objave 1080×1350 (4:5) za svaki članak, u stilu stranice: prugice, karo okvir, GN značka.
# Pokretanje: python3 instagram/make_instagram.py  ->  instagram/objave/*.jpg + instagram/opisi.md
import html
import json
import os
import re
import subprocess
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DIR)
sys.path.insert(0, DIR)
from objave import OBJAVE, ZAJEDNICKI  # noqa: E402

OUT = os.path.join(DIR, "objave")
TMP = os.path.join(DIR, ".html")
os.makedirs(OUT, exist_ok=True)
os.makedirs(TMP, exist_ok=True)
FONTS = "file://" + os.path.join(ROOT, "fonts")
SLIKE = "file://" + os.path.join(ROOT, "assets", "slike")
ZNAK = "file://" + os.path.join(ROOT, "assets", "brand", "znak.svg")
TON = {"top": ("#7a1730", "#fffbf7"), "ok": ("#fbe7a6", "#7a1730"), "flop": ("#d7263d", "#fffbf7")}
ISKRA = '<svg class="iskra" viewBox="0 0 40 40"><path d="M20 0C22 13 27 18 40 20 27 22 22 27 20 40 18 27 13 22 0 20 13 18 18 13 20 0Z" fill="#d7263d"/></svg>'

CSS = f"""
@font-face {{ font-family: Fraunces; font-weight: 100 900; src: url({FONTS}/fraunces-latin.woff2); unicode-range: U+0000-00FF, U+2000-206F; }}
@font-face {{ font-family: Fraunces; font-weight: 100 900; src: url({FONTS}/fraunces-latin-ext.woff2); unicode-range: U+0100-02FF; }}
@font-face {{ font-family: Fraunces; font-style: italic; font-weight: 100 900; src: url({FONTS}/fraunces-italic-latin.woff2); unicode-range: U+0000-00FF, U+2000-206F; }}
@font-face {{ font-family: Fraunces; font-style: italic; font-weight: 100 900; src: url({FONTS}/fraunces-italic-latin-ext.woff2); unicode-range: U+0100-02FF; }}
@font-face {{ font-family: Instrument; font-weight: 400 700; src: url({FONTS}/instrumentsans-latin.woff2); unicode-range: U+0000-00FF, U+2000-206F; }}
@font-face {{ font-family: Instrument; font-weight: 400 700; src: url({FONTS}/instrumentsans-latin-ext.woff2); unicode-range: U+0100-02FF; }}
* {{ box-sizing: border-box; margin: 0; }}
body {{ width: 1080px; height: 1350px; background: #fffbf7; color: #3b1a22; font-family: Instrument, sans-serif; display: flex; flex-direction: column; overflow: hidden; }}
.pruge {{ height: 30px; flex: none; background: repeating-linear-gradient(90deg, #f4a7bb 0 30px, #fffbf7 30px 60px); }}
.glava {{ display: flex; align-items: center; justify-content: space-between; padding: 34px 64px 26px; }}
.marka {{ display: flex; align-items: center; gap: 16px; font: 900 44px/1 Fraunces; font-variation-settings: "SOFT" 100; color: #7a1730; }}
.marka img {{ width: 78px; height: 78px; }}
.oznaka {{ font: 700 22px/1 Instrument; letter-spacing: .18em; text-transform: uppercase; padding: 16px 26px; border-radius: 999px; }}
.foto {{ position: relative; margin: 0 64px; padding: 16px; border-radius: 280px 280px 36px 36px;
  background: repeating-linear-gradient(0deg, rgba(232,104,140,.38) 0 16px, transparent 16px 32px), repeating-linear-gradient(90deg, rgba(232,104,140,.38) 0 16px, #fffbf7 16px 32px); }}
.foto img.slika {{ display: block; width: 100%; height: VISINApx; object-fit: cover; border-radius: 264px 264px 24px 24px; }}
.ocjena {{ position: absolute; right: -20px; bottom: -44px; width: 190px; height: 190px; border-radius: 50%; background: #f4a7bb; border: 6px solid #7a1730;
  display: flex; align-items: center; justify-content: center; color: #7a1730; font: 900 70px/1 Fraunces; font-variation-settings: "SOFT" 100; }}
.ocjena::before {{ content: ""; position: absolute; inset: 12px; border: 2.5px dashed #7a1730; border-radius: 50%; }}
.ocjena small {{ font-size: 34px; margin-top: 22px; }}
.iskra {{ position: absolute; width: 54px; height: 54px; right: 6px; top: -10px; }}
.tekst {{ flex: 1; padding: 52px 64px 0; display: flex; flex-direction: column; }}
h1 {{ font: 900 VELpx/1.06 Fraunces; font-variation-settings: "SOFT" 100; letter-spacing: -.01em; color: #7a1730; text-wrap: balance; padding-right: DESNOpx; }}
h1 em {{ font-style: italic; font-weight: 800; color: #e8688c; }}
ul {{ list-style: none; padding: 0; margin-top: 30px; display: grid; gap: 14px; }}
li {{ display: flex; align-items: center; gap: 16px; font: 500 29px/1.25 Instrument; }}
li b {{ flex: none; width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; font: 700 26px/1 Instrument; }}
li b.plus {{ background: #d7efe2; color: #1f7a50; }} li b.minus {{ background: #fde6ec; color: #d7263d; }}
ol {{ list-style: none; padding: 0; margin-top: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px 28px; counter-reset: n; }}
ol li {{ font: 600 25px/1.2 Instrument; gap: 14px; }}
ol li::before {{ counter-increment: n; content: counter(n); flex: none; width: 42px; height: 42px; border-radius: 50%; background: #7a1730; color: #fffbf7;
  display: grid; place-items: center; font: 900 24px/1 Fraunces; }}
.dno {{ margin-top: auto; background: #fde6ec; padding: 26px 64px; display: flex; justify-content: space-between; align-items: center; }}
.dno span {{ font: 600 26px/1.2 Instrument; color: #6e4a53; }}
.dno strong {{ font: 900 34px/1 Fraunces; font-variation-settings: "SOFT" 100; color: #7a1730; }}
.dno .bio {{ font: 700 22px/1 Instrument; letter-spacing: .14em; text-transform: uppercase; color: #fffbf7; background: #e8688c; padding: 14px 22px; border-radius: 999px; }}
"""

def naslov(t):
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(t))


def ocjena(n):
    return f"{n:g}".replace(".", ",")


def stranica(o):
    lista = "lista" in o
    bg, fg = TON[o["ton"]]
    duljina = len(o["naslov"])
    vel = 70 if duljina < 44 else 62 if duljina < 56 else 56
    visina = 520 if lista or duljina >= 56 else 540
    css = CSS.replace("VISINA", str(visina)).replace("VEL", str(vel)).replace("DESNO", "0")
    rate = f'<div class="ocjena">{ocjena(o["ocjena"])}<small>/5</small>{ISKRA}</div>' if o.get("ocjena") else ""
    if lista:
        stavke = "<ol>" + "".join(f"<li>{html.escape(x)}</li>" for x in o["lista"]) + "</ol>"
    else:
        stavke = "<ul>" + "".join(f'<li><b class="{"plus" if z == "+" else "minus"}">{"+" if z == "+" else "–"}</b>{html.escape(t)}</li>' for z, t in o["tocke"]) + "</ul>"
    dno = "Cijeli članak na" if lista else "Cijela recenzija na"
    return f"""<!doctype html><html lang="hr"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="pruge"></div>
<header class="glava"><div class="marka"><img src="{ZNAK}" alt="">Glow Notes</div><div class="oznaka" style="background:{bg};color:{fg}">{html.escape(o["oznaka"])}</div></header>
<div class="foto"><img class="slika" src="{SLIKE}/{o["slug"]}.jpg" alt="">{rate}</div>
<div class="tekst"><h1>{naslov(o["naslov"])}</h1>{stavke}</div>
<footer class="dno"><div><span>{dno}</span><br><strong>glownotes.eu</strong></div><div class="bio">Link u bio →</div></footer>
<div class="pruge"></div>
</body></html>"""


def main():
    poslovi = []
    for i, o in enumerate(OBJAVE, 1):
        ime = f"{i:02d}-{o['slug']}"
        p = os.path.join(TMP, ime + ".html")
        with open(p, "w", encoding="utf-8") as f:
            f.write(stranica(o))
        poslovi.append({"html": p, "jpg": os.path.join(OUT, ime + ".jpg")})
    subprocess.run(["node", os.path.join(DIR, "render.js"), json.dumps(poslovi)], check=True)

    md = ["# Instagram objave – Glow Notes", "",
          "Jedna objava po članku, redom kojim ih predlažem objaviti. Slike su 1080×1350 (format 4:5) u mapi `objave/`.", ""]
    for i, o in enumerate(OBJAVE, 1):
        tags = " ".join(dict.fromkeys(o["hashtagovi"] + ZAJEDNICKI))
        md += [f"## {i:02d}. {o['naslov'].replace('*', '')}", "",
               f"Slika: `objave/{i:02d}-{o['slug']}.jpg`  ", f"Članak: https://glownotes.eu/clanci/{o['slug']}/", "",
               "```", o["opis"], "", tags, "```", ""]
    with open(os.path.join(DIR, "opisi.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"{len(OBJAVE)} objava gotovo")


if __name__ == "__main__":
    main()
