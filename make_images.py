# Ilustracije za stranicu (plosnate ilustracije proizvoda u bojama branda, bez stvarnih logotipa).
# Izlaz: assets/slike/*.svg -> render.js ih pretvara u .jpg
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "slike")
os.makedirs(OUT, exist_ok=True)
BURG, PINK, ROSE, RED, SKY, BUTTER, BLUSH, PAPER, PIST, PEACH = (
    "#7A1730", "#F4A7BB", "#E8688C", "#D7263D", "#C4E0F4", "#FBE7A6", "#FDE6EC", "#FFFBF7", "#D7EFE2", "#FDE0CC")
FONT = "font-family:'Fraunces',Georgia,serif;font-weight:900;font-variation-settings:'SOFT' 100"
SANS = "font-family:'Instrument Sans',sans-serif;font-weight:700;letter-spacing:.14em"


def gingham(id_, c, size=40, op=.35):
    h = size / 2
    return (f'<pattern id="{id_}" width="{size}" height="{size}" patternUnits="userSpaceOnUse">'
            f'<rect width="{size}" height="{size}" fill="{PAPER}"/>'
            f'<rect width="{h}" height="{size}" fill="{c}" opacity="{op}"/><rect width="{size}" height="{h}" fill="{c}" opacity="{op}"/></pattern>')


def stripes(id_, c, w=30):
    return (f'<pattern id="{id_}" width="{w*2}" height="10" patternUnits="userSpaceOnUse">'
            f'<rect width="{w*2}" height="10" fill="{PAPER}"/><rect width="{w}" height="10" fill="{c}"/></pattern>')


def shadow(cx, y, w):
    return f'<ellipse cx="{cx}" cy="{y}" rx="{w/2}" ry="{w*0.09}" fill="{BURG}" opacity=".12"/>'


def label(x, y, w, h, text, color=BURG, bg=PAPER, size=None, sans=False):
    size = size or h * 0.42
    style = SANS if sans else FONT
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(w,h)*0.18}" fill="{bg}"/>'
            f'<text x="{x+w/2}" y="{y+h/2+size*0.35}" text-anchor="middle" font-size="{size}" fill="{color}" style="{style}">{text}</text>')


def dropper(x, base, w, h, glass, text="serum"):
    bh = h * 0.62; by = base - bh; nh = h * 0.1; bulb = h * 0.28
    return (shadow(x + w/2, base, w * 1.3)
            + f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="{w*0.22}" fill="{glass}"/>'
            + f'<rect x="{x+w*0.12}" y="{by+bh*0.12}" width="{w*0.12}" height="{bh*0.6}" rx="{w*0.06}" fill="#fff" opacity=".45"/>'
            + f'<rect x="{x+w*0.18}" y="{by-nh}" width="{w*0.64}" height="{nh+4}" rx="6" fill="{BURG}"/>'
            + f'<rect x="{x+w*0.3}" y="{by-nh-bulb}" width="{w*0.4}" height="{bulb+6}" rx="{w*0.2}" fill="{BURG}"/>'
            + label(x + w*0.14, by + bh*0.42, w*0.72, bh*0.28, text, size=w*0.17))


def tube(x, base, w, h, body, cap, text="", crown=None):
    ch = h * 0.16; top = base - h
    path = (f'M{x+w*0.18} {base-ch} L{x} {top+h*0.08} L{x} {top} L{x+w} {top} L{x+w} {top+h*0.08} L{x+w*0.82} {base-ch} Z')
    s = (shadow(x + w/2, base, w * 1.1)
         + f'<path d="{path}" fill="{body}"/>'
         + f'<rect x="{x}" y="{top}" width="{w}" height="{h*0.05}" fill="{BURG}" opacity=".18"/>'
         + f'<rect x="{x+w*0.16}" y="{base-ch}" width="{w*0.68}" height="{ch}" rx="8" fill="{cap}"/>'
         + f'<rect x="{x+w*0.12}" y="{top+h*0.12}" width="{w*0.08}" height="{h*0.45}" rx="5" fill="#fff" opacity=".4"/>')
    if text:
        s += label(x + w*0.18, top + h*0.3, w*0.64, h*0.2, text, size=w*0.2)
    return s


def jar(x, base, w, h, body, lid, text="krema"):
    lh = h * 0.32; bh = h - lh
    return (shadow(x + w/2, base, w * 1.15)
            + f'<rect x="{x}" y="{base-bh}" width="{w}" height="{bh}" rx="{w*0.12}" fill="{body}"/>'
            + f'<rect x="{x-w*0.04}" y="{base-h}" width="{w*1.08}" height="{lh+6}" rx="{w*0.08}" fill="{lid}"/>'
            + f'<rect x="{x+w*0.08}" y="{base-bh+bh*0.15}" width="{w*0.07}" height="{bh*0.55}" rx="5" fill="#fff" opacity=".45"/>'
            + label(x + w*0.2, base - bh*0.68, w*0.6, bh*0.36, text, size=w*0.13))


def pump(x, base, w, h, body, text="tonik"):
    bh = h * 0.7; by = base - bh
    return (shadow(x + w/2, base, w * 1.2)
            + f'<rect x="{x}" y="{by}" width="{w}" height="{bh}" rx="{w*0.2}" fill="{body}"/>'
            + f'<rect x="{x+w*0.3}" y="{by-h*0.1}" width="{w*0.4}" height="{h*0.1+6}" rx="5" fill="{PAPER}"/>'
            + f'<rect x="{x+w*0.4}" y="{by-h*0.24}" width="{w*0.2}" height="{h*0.15}" fill="{PAPER}"/>'
            + f'<rect x="{x+w*0.4}" y="{by-h*0.27}" width="{w*0.62}" height="{h*0.06}" rx="6" fill="{PAPER}"/>'
            + f'<rect x="{x+w*0.12}" y="{by+bh*0.1}" width="{w*0.1}" height="{bh*0.6}" rx="6" fill="#fff" opacity=".35"/>'
            + label(x + w*0.15, by + bh*0.38, w*0.7, bh*0.24, text, size=w*0.16))


def lipstick(x, base, w, h, bullet=RED):
    bh = h * 0.5
    return (shadow(x + w/2, base, w * 1.4)
            + f'<rect x="{x}" y="{base-bh}" width="{w}" height="{bh}" rx="6" fill="{BURG}"/>'
            + f'<rect x="{x-3}" y="{base-bh-h*0.08}" width="{w+6}" height="{h*0.1}" rx="4" fill="#E9C46A"/>'
            + f'<path d="M{x+w*0.15} {base-bh-h*0.08} L{x+w*0.15} {base-h*0.86} L{x+w*0.85} {base-h} L{x+w*0.85} {base-bh-h*0.08} Z" fill="{bullet}"/>')


def compact(cx, cy, r, pan=PEACH):
    return (f'<circle cx="{cx+6}" cy="{cy+8}" r="{r}" fill="{BURG}" opacity=".12"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BURG}"/><circle cx="{cx}" cy="{cy}" r="{r*0.78}" fill="{pan}"/>'
            f'<circle cx="{cx-r*0.25}" cy="{cy-r*0.25}" r="{r*0.22}" fill="#fff" opacity=".4"/>')


def spark(cx, cy, r, c=BURG):
    return f'<path d="M{cx} {cy-r}Q{cx+r*0.18} {cy-r*0.18} {cx+r} {cy}Q{cx+r*0.18} {cy+r*0.18} {cx} {cy+r}Q{cx-r*0.18} {cy+r*0.18} {cx-r} {cy}Q{cx-r*0.18} {cy-r*0.18} {cx} {cy-r}Z" fill="{c}"/>'


def heart(cx, cy, s, c=ROSE):
    return (f'<path transform="translate({cx-s/2} {cy-s/2}) scale({s/24})" '
            f'd="M12 21s-7.5-4.6-10-9.2C0.4 8.6 2.3 4 6.4 4c2.4 0 4 1.4 5.6 3.4C13.6 5.4 15.2 4 17.6 4 21.7 4 23.6 8.6 22 11.8 19.5 16.4 12 21 12 21z" fill="{c}"/>')


def sticker(cx, cy, r, text, bg=BUTTER, rot=-10, size=None, lines=None):
    lines = lines or [text]
    size = size or r * 0.34
    t = "".join(f'<tspan x="{cx}" dy="{size*1.1 if i else -(len(lines)-1)*size*0.55+size*0.35}">{l}</tspan>' for i, l in enumerate(lines))
    return (f'<g transform="rotate({rot} {cx} {cy})"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}"/>'
            f'<text x="{cx}" y="{cy}" text-anchor="middle" font-size="{size}" fill="{BURG}" style="{FONT};font-style:italic">{t}</text></g>')


def svg(w, h, defs, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs>{defs}</defs>{body}</svg>'


# 1) Naslovnica: polica s proizvodima na roza karo podlozi
hero = svg(1000, 1000, gingham("g", ROSE, 56),
           '<rect width="1000" height="1000" fill="url(#g)"/>'
           + f'<rect x="90" y="700" width="820" height="26" rx="13" fill="{BURG}"/>'
           + pump(130, 700, 150, 420, BURG, "tonik")
           + dropper(320, 700, 120, 360, PINK, "serum")
           + jar(480, 700, 190, 200, PAPER, PINK, "krema")
           + tube(710, 700, 120, 330, SKY, BURG, "SPF 50")
           + lipstick(260, 860, 46, 150) + compact(470, 830, 70) + compact(640, 850, 48, PINK)
           + spark(820, 180, 46) + spark(180, 210, 26, RED) + heart(870, 820, 70))
open(os.path.join(OUT, "naslovnica.svg"), "w").write(hero)

# 2) Mineralni SPF poredak: šest tuba, prva s rozetom, zadnja precrtana
tubes = ""
colors = [BUTTER, PINK, SKY, PEACH, PAPER, PAPER]
for i in range(6):
    x = 80 + i * 180
    tubes += tube(x, 660, 120, 380 - i * 14, colors[i], BURG if i < 4 else ROSE, f"SPF {50 if i != 1 else 30}")
    tubes += f'<circle cx="{x+60}" cy="{720}" r="26" fill="{BURG}"/><text x="{x+60}" y="730" text-anchor="middle" font-size="28" fill="{PAPER}" style="{FONT}">{i+1}</text>'
spf = svg(1200, 750, stripes("s", PINK, 34),
          f'<rect width="1200" height="750" fill="{BLUSH}"/><rect width="1200" height="60" fill="url(#s)"/>'
          + f'<circle cx="1040" cy="190" r="110" fill="{BUTTER}"/>' + tubes
          + sticker(200, 210, 78, "", BUTTER, -12, 26, ["Sveti", "gral!"])
          + f'<g stroke="{RED}" stroke-width="16" stroke-linecap="round"><line x1="985" y1="330" x2="1095" y2="560"/><line x1="1095" y1="330" x2="985" y2="560"/></g>'
          + f'<path d="M1000 690 q30 -30 60 0 q30 30 70 -4" stroke="#fff" stroke-width="18" fill="none" stroke-linecap="round" opacity=".9"/>'
          + spark(640, 120, 30) + spark(520, 200, 16, RED))
open(os.path.join(OUT, "mineralni-spf-recenzije-poredak.svg"), "w").write(spf)

# 3) Promašaji: kanta s proizvodima koji ispadaju
bin_ = (f'<path d="M420 360 L780 360 L740 690 L460 690 Z" fill="{BURG}"/>'
        + "".join(f'<rect x="{470+i*55}" y="400" width="18" height="250" rx="9" fill="{PAPER}" opacity=".18"/>' for i in range(5))
        + f'<rect x="395" y="330" width="410" height="44" rx="14" fill="{BURG}"/><rect x="560" y="304" width="80" height="34" rx="12" fill="{BURG}"/>')
trash = svg(1200, 750, gingham("g", ROSE, 48, .28),
            '<rect width="1200" height="750" fill="url(#g)"/>'
            + f'<g transform="rotate(-18 520 300)">{tube(470, 380, 90, 260, SKY, BURG, "CC")}</g>'
            + f'<g transform="rotate(14 660 300)">{dropper(620, 360, 80, 250, PINK, "C")}</g>'
            + bin_ + shadow(600, 700, 420)
            + f'<g transform="rotate(-28 230 300)">{jar(170, 380, 130, 140, PAPER, PINK, "krema")}</g>'
            + f'<g transform="rotate(22 960 260)">{pump(910, 420, 100, 300, PEACH, "BHA")}</g>'
            + sticker(980, 590, 92, "", BUTTER, 10, 30, ["u smeću*"])
            + f'<g stroke="{RED}" stroke-width="12" stroke-linecap="round"><line x1="150" y1="560" x2="230" y2="640"/><line x1="230" y1="560" x2="150" y2="640"/></g>'
            + spark(840, 120, 28) + spark(330, 150, 18, RED))
open(os.path.join(OUT, "proizvodi-koji-nisu-odgovarali-rozacea.svg"), "w").write(trash)

# 4) Favoriti: dvije police, srca
fav = svg(1200, 750, "",
          f'<rect width="1200" height="750" fill="{SKY}"/>'
          + f'<rect x="120" y="360" width="960" height="22" rx="11" fill="{BURG}"/><rect x="120" y="650" width="960" height="22" rx="11" fill="{BURG}"/>'
          + pump(170, 360, 100, 260, PINK, "sprej") + jar(320, 360, 150, 140, PAPER, BURG, "krema") + dropper(520, 360, 80, 240, PAPER, "serum")
          + tube(650, 360, 90, 230, BUTTER, BURG, "SPF") + jar(790, 360, 120, 110, PINK, PAPER, "oči") + dropper(960, 360, 70, 220, ROSE, "lash")
          + lipstick(190, 650, 44, 150) + compact(350, 610, 56) + tube(460, 650, 80, 200, PAPER, BURG, "CC")
          + jar(600, 650, 160, 120, PEACH, BURG, "maska") + pump(820, 650, 100, 250, PAPER, "No. 3") + tube(970, 650, 80, 220, PINK, BURG, "SA")
          + heart(300, 120, 64) + heart(880, 110, 48, RED) + heart(1080, 440, 40)
          + sticker(1040, 150, 86, "", BUTTER, 10, 28, ["Kupit ću", "opet"]) + spark(560, 90, 30))
open(os.path.join(OUT, "proizvodi-koje-cu-ponovno-kupiti.svg"), "w").write(fav)
print("ok", sorted(os.listdir(OUT)))
