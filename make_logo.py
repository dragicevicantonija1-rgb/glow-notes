# Logo: okrugla roza značka s monogramom i natpis u fontu Fraunces Black (meki), pretvoreno u krivulje.
import json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib.instancer import instantiateVariableFont

NAME = json.load(open("config.json", encoding="utf-8"))["site_name"]
MONO = "".join(w[0] for w in NAME.split())[:2].upper()


def load(style, wght):
    return [instantiateVariableFont(TTFont(f"fonts/fraunces-{style}{sub}.woff2"), {"wght": wght, "opsz": 72, "SOFT": 100, "WONK": 0})
            for sub in ["latin", "latin-ext"]]


BLACK = load("", 900)
ITAL = load("italic-", 800)


def glyph(fonts, ch):
    for t in fonts:
        cmap = t.getBestCmap()
        if ord(ch) in cmap:
            return t, cmap[ord(ch)]
    raise KeyError(ch)


def outline(fonts, text, size):
    s = size / fonts[0]["head"].unitsPerEm
    x, parts = 0, []
    for ch in text:
        t, g = glyph(fonts, ch)
        gs = t.getGlyphSet()
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
        parts.append(pen.getCommands())
        x += t["hmtx"][g][0] * s
    return " ".join(parts), x


BURG, PINK, PAPER, RED = "#7A1730", "#F4A7BB", "#FFFBF7", "#D7263D"
md, mw = outline(ITAL, MONO, 16.5)
SPARK = "M39 3Q40 8 45 9Q40 10 39 15Q38 10 33 9Q38 8 39 3Z"
MONO_T = f"translate({24 - mw / 2:.2f} 30.6)"


def mark(ring=BURG, fill=PINK, mono=BURG, spark=RED, cls=False):
    if cls:
        return (f'<circle class="m-fill" cx="24" cy="25" r="20"/><circle class="m-ring" cx="24" cy="25" r="20"/>'
                f'<circle class="m-ring2" cx="24" cy="25" r="16.5"/>'
                f'<path class="m-mono" transform="{MONO_T}" d="{md}"/><path class="m-spark" d="{SPARK}"/>')
    return (f'<circle cx="24" cy="25" r="20" fill="{fill}"/><circle cx="24" cy="25" r="20" fill="none" stroke="{ring}" stroke-width="2.5"/>'
            f'<circle cx="24" cy="25" r="16.5" fill="none" stroke="{ring}" stroke-width="0.8" stroke-dasharray="1.6 1.6"/>'
            f'<path transform="{MONO_T}" d="{md}" fill="{mono}"/><path d="{SPARK}" fill="{spark}"/>')


# fragment za stranicu (boje dolaze iz CSS-a)
open("assets/brand/mark-fragment.svg", "w").write(mark(cls=True))

d, w = outline(BLACK, NAME, 28)
W = int(56 + w + 6)


def horiz(txt, **kw):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 50" width="{W*4}" height="200"><title>{NAME}</title>'
            f'{mark(**kw)}<path transform="translate(56 35)" d="{d}" fill="{txt}"/></svg>')


open("assets/brand/logo.svg", "w").write(horiz(BURG))
open("assets/brand/logo-svijetli.svg", "w").write(horiz(PINK, ring=PAPER, spark=PAPER))
d2, w2 = outline(BLACK, NAME, 20)
SW = int(w2) + 20
open("assets/brand/logo-okomiti.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SW} 84" width="{SW*4}" height="336"><title>{NAME}</title>'
    f'<g transform="translate({SW/2-24} 0)">{mark()}</g><path transform="translate(10 76)" d="{d2}" fill="{BURG}"/></svg>')
open("assets/brand/znak.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="2 1 46 46" width="460" height="460"><title>{NAME}</title>{mark()}</svg>')
open("assets/favicon.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="3 4 42 42">{mark(spark=BURG)}</svg>')
print("ok", W, MONO)
