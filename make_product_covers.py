# Naslovne slike recenzija iz stvarnih fotografija proizvoda (instagram/_proizvodi).
# Izlaz: assets/slike/<slug>.jpg + .webp, 1200x900. Proizvod je centriran i stane u
# srednji 16:9 isječak jer kartice na stranici režu sliku na 8:5 i 16:9.
# Pokreni sa sustavnim python3 (ima Pillow): python3 make_product_covers.py
import json
import os

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "instagram", "_proizvodi")
OUT = os.path.join(ROOT, "assets", "slike")
W, H = 1200, 900
MAX_W, MAX_H = 1000, 600

# slug članka -> (fotografija, način): "fit" = proizvod na pozadini fotografije, "cover" = izrez cijele fotografije,
# "pad" = cijela fotografija, pozadina razvučena iz lijevog ruba (za pozadinu s prijelazom),
# "blur" = cijela fotografija na zamućenoj vlastitoj pozadini (za fotke s mobitela)
COVERS = {
    "babe-mineralni-spf-50-recenzija": ("babe-mineral-pack.jpg", "fit"),
    "babe-lip-cheek-spf-50-mocca-recenzija": ("babe-lip.jpg", "fit"),
    "chanel-water-fresh-tint-recenzija": ("chanel-wft.jpg", "fit"),
    "bioderma-sensibio-h2o-micelarna-voda-recenzija": ("bioderma-h2o.jpg", "fit"),
    "bioderma-photoderm-ar-spf-50-recenzija": ("bioderma-ar.jpg", "fit"),
    "avene-b-protect-spf-50-recenzija": ("avene-bprotect.jpg", "pad"),
    "avene-termalna-voda-rozacea-recenzija": ("avene-voda.jpg", "fit"),
    "avene-couvrance-tekuci-puder-recenzija": ("avene-couvrance.jpg", "fit"),
    "avene-cicalfate-serum-recenzija": ("avene-cicalfate.jpg", "fit"),
    "biologique-recherche-p50w-recenzija": ("p50w.jpg", "fit"),
    "erborian-cc-red-correct-recenzija": ("erborian-cc.jpg", "fit"),
    "rhode-pocket-blush-tan-line-recenzija": ("rhode-blush.jpg", "cover"),
    "rhode-peptide-lip-shape-recenzija": ("rhode-lip.jpg", "fit"),
    "la-roche-posay-cicaplast-baume-b5-recenzija": ("cicaplast.jpg", "fit"),
    "jane-iredale-hydropure-tinted-serum-recenzija": ("jane-iredale-tinted-web.jpg", "cover"),
    "jane-iredale-hydropure-color-correcting-serum-recenzija": ("jane-iredale-cc-web.jpg", "cover"),
}


def rgb(s):
    return tuple(int(v) for v in s[4:-1].split(","))


def fit(im, box):
    x0, y0, x1, y1 = box["x0"], box["y0"], box["x1"] + 1, box["y1"] + 1
    prod = im.crop((x0, y0, x1, y1))
    k = min(MAX_W / prod.width, MAX_H / prod.height)
    prod = prod.resize((round(prod.width * k), round(prod.height * k)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), rgb(box["bg"]))
    canvas.paste(prod, ((W - prod.width) // 2, (H - prod.height) // 2))
    return canvas


def cover(im, box):
    k = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    cy = round((box["y0"] + box["y1"]) / 2 * k)
    top = min(max(cy - H // 2, 0), im.height - H)
    left = (im.width - W) // 2
    return im.crop((left, top, left + W, top + H))


def pad(im, box):
    k = MAX_H * 1.2 / im.height
    small = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    canvas = im.crop((0, 0, 8, im.height)).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(20))
    canvas.paste(small, ((W - small.width) // 2, (H - small.height) // 2))
    return canvas


def blur(im, box):
    k = MAX_H * 1.1 / im.height
    small = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    canvas = cover(im, box).filter(ImageFilter.GaussianBlur(40))
    canvas = Image.blend(canvas, Image.new("RGB", (W, H), (255, 255, 255)), 0.25)
    canvas.paste(small, ((W - small.width) // 2, (H - small.height) // 2))
    return canvas


def main():
    boxes = json.load(open(os.path.join(SRC, "okviri.json")))
    for slug, (name, mode) in COVERS.items():
        im = Image.open(os.path.join(SRC, name)).convert("RGB")
        out = {"fit": fit, "cover": cover, "pad": pad, "blur": blur}[mode](im, boxes[name])
        out.save(os.path.join(OUT, slug + ".jpg"), quality=86, optimize=True, progressive=True)
        out.save(os.path.join(OUT, slug + ".webp"), quality=82, method=6)
        print(slug, "<-", name)


if __name__ == "__main__":
    main()
