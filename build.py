#!/usr/bin/env python3
"""Generator statične stranice (ime i ključevi su u config.json).

    python3 build.py            -> dist/     (produkcija: čisti URL-ovi, fontovi s vlastitog servera)
    python3 build.py --preview  -> preview/  (relativne poveznice, za pregled bez servera)

Ključevi (PostHog, Search Console, AdSense) upisuju se samo u config.json.
"""
import html, json, math, os, re, shutil, sys
from datetime import date
from content import ARTICLES, BRANDS, CATEGORIES

ROOT = os.path.dirname(os.path.abspath(__file__))
PREVIEW = "--preview" in sys.argv
OUT = os.path.join(ROOT, "preview" if PREVIEW else "dist")
CFG = json.load(open(os.path.join(ROOT, "config.json"), encoding="utf-8"))
BASE = CFG["base_url"].rstrip("/")
CSS = open(os.path.join(ROOT, "assets", "site.css"), encoding="utf-8").read()
FONT_CSS = open(os.path.join(ROOT, "fonts", "fonts.css"), encoding="utf-8").read()
CAT = {c["slug"]: c for c in CATEGORIES}
ARTICLES = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
for _b in BRANDS:
    _b["slug"] = re.sub(r"[^a-z0-9]+", "-", _b["name"].lower().replace("é", "e").replace("è", "e").replace("'", "")).strip("-")
    _b["articles"] = [a for a in ARTICLES if any(al.lower() in re.sub(r"<[^>]+>", " ", a["body"]).lower() for al in _b["aliases"])]
BRANDS = sorted(BRANDS, key=lambda x: x["name"].lower())
MONTHS = ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja",
          "kolovoza", "rujna", "listopada", "studenoga", "prosinca"]
e = html.escape


def hr_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day}. {MONTHS[d.month - 1]} {d.year}."


def has_image(slug):
    return os.path.exists(os.path.join(ROOT, "assets", "slike", slug + ".jpg"))


def picture(slug, alt, w, h, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<picture class="{cls}"><source srcset="/slike/{slug}.webp" type="image/webp">'
            f'<img src="/slike/{slug}.jpg" alt="{e(alt)}" width="{w}" height="{h}" {load} decoding="async"></picture>')


def plural(n):
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} članak"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return f"{n} članka"
    return f"{n} članaka"


def reading_time(body):
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return max(1, math.ceil(words / 200))


MARK = ('<svg class="mark{cls}" viewBox="2 1 46 46" aria-hidden="true" focusable="false">'
        + open(os.path.join(ROOT, "assets", "brand", "mark-fragment.svg"), encoding="utf-8").read() + "</svg>")


def mark(cls=""):
    return MARK.replace("{cls}", cls)


# ---------- dijelovi stranice ----------

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": CFG["site_name"], "url": BASE + "/",
       "logo": {"@type": "ImageObject", "url": BASE + "/brand/logo-512.png", "width": 512, "height": 512}}
PERSON = {"@type": "Person", "@id": BASE + "/#autorica", "name": CFG["author"], "url": BASE + "/o-meni/"}


def head(title, desc, path, og_type="website", extra_ld=None, noindex=False, full_title=True, image=None):
    url = BASE + path
    t = f"{title} | {CFG['site_name']}" if full_title else title
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&family=Instrument+Sans:wght@400..700&display=swap">') if PREVIEW else (
        '<link rel="preload" href="/fonts/instrumentsans-latin.woff2" as="font" type="font/woff2" crossorigin>'
        '<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>'
        f"<style>{FONT_CSS}</style>")
    gsc = f'<meta name="google-site-verification" content="{e(CFG["google_site_verification"])}">' if CFG["google_site_verification"] else ""
    ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(CFG["adsense_client"])}" crossorigin="anonymous"></script>'
           if CFG["adsense_client"] and not PREVIEW else "")
    ph = posthog_snippet() if CFG["posthog_key"] and not PREVIEW else ""
    ld = [ORG, {"@type": "WebSite", "@id": BASE + "/#web", "url": BASE + "/", "name": CFG["site_name"],
                "inLanguage": "hr-HR", "publisher": {"@id": BASE + "/#org"}}] + (extra_ld or [])
    return f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-image-preview:large'}">
<meta property="og:locale" content="hr_HR">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(CFG['site_name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{image or '/brand/og-image.png'}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="{750 if image else 630}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fffbf7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#24090f" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="{e(CFG['site_name'])}" href="/rss.xml">
{gsc}
{fonts}
<style>{CSS}</style>
{jsonld({"@context": "https://schema.org", "@graph": ld})}
{ph}
{ads}
</head>
<body>
<a class="skip" href="#sadrzaj">Preskoči na sadržaj</a>
<div class="stripes" aria-hidden="true"></div>
"""


def posthog_snippet():
    # Bez kolačića dok posjetitelj ne pristane (persistence: memory), zatim localStorage+cookie.
    return """<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
var mkConsent=null;try{mkConsent=localStorage.getItem("mk-consent")}catch(_){}
posthog.init(%s,{api_host:%s,person_profiles:"identified_only",persistence:mkConsent==="da"?"localStorage+cookie":"memory",capture_pageview:true,capture_pageleave:true});
</script>""" % (json.dumps(CFG["posthog_key"]), json.dumps(CFG["posthog_host"]))


NAV = [("/", "Naslovnica")] + [(f"/kategorije/{c['slug']}/", c.get("nav", c["name"])) for c in CATEGORIES] + [("/brendovi/", "Brendovi"), ("/o-meni/", "O meni")]


def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{e(n)}</a>' for h, n in NAV[1:])
    return f"""<header class="site-header"><div class="wrap">
<a class="brand" href="/" aria-label="{e(CFG['site_name'])}, naslovnica">{mark()}<span class="brand__name">{e(CFG['site_name'])}</span></a>
<nav class="nav" aria-label="Glavna navigacija">{links}</nav>
</div></header>
<main id="sadrzaj">"""


def footer():
    cats = "".join(f'<li><a href="/kategorije/{c["slug"]}/">{e(c["name"])}</a></li>' for c in CATEGORIES)
    return f"""</main>
<footer class="site-footer"><div class="wrap">
<div><a class="brand" href="/">{mark()}<span class="brand__name">{e(CFG['site_name'])}</span></a>
<p class="note">{e(CFG['tagline'])}. Sadržaj je informativan i ne zamjenjuje savjet dermatologa.</p></div>
<div><h2>Kategorije</h2><ul>{cats}</ul></div>
<div><h2>Portal</h2><ul><li><a href="/o-meni/">O meni</a></li><li><a href="/kontakt/">Kontakt</a></li>
<li><a href="/politika-privatnosti/">Privatnost i kolačići</a></li><li><button type="button" class="btn-link" id="mk-consent-open">Postavke kolačića</button></li>{'<li><a href="/brand/identitet.html">Vizualni identitet (pregled)</a></li>' if PREVIEW else ''}</ul></div>
</div><div class="wrap"><p>© {date.today().year} {e(CFG['site_name'])}</p></div></footer>
<div class="consent" id="mk-consent" hidden role="dialog" aria-label="Kolačići"><div class="consent__in">
<p>Koristimo kolačiće za analitiku posjeta i prikaz oglasa. Nužni rade uvijek, ostale uključujemo samo uz vaš pristanak. <a href="/politika-privatnosti/">Više o tome</a></p>
<div class="consent__btns"><button type="button" class="no" id="mk-consent-no">Samo nužni</button><button type="button" class="yes" id="mk-consent-yes">Prihvaćam</button></div>
</div></div>
<script>
(function(){{var b=document.getElementById("mk-consent"),v=null;try{{v=localStorage.getItem("mk-consent")}}catch(_){{}}
if(!v)b.hidden=false;
function set(x){{try{{localStorage.setItem("mk-consent",x)}}catch(_){{}}b.hidden=true;
if(window.posthog&&posthog.set_config){{if(x==="da"){{posthog.set_config({{persistence:"localStorage+cookie"}});posthog.opt_in_capturing()}}else{{posthog.set_config({{persistence:"memory"}})}}}}}}
document.getElementById("mk-consent-yes").onclick=function(){{set("da")}};
document.getElementById("mk-consent-no").onclick=function(){{set("ne")}};
document.getElementById("mk-consent-open").onclick=function(){{b.hidden=false}};
{"(adsbygoogle=window.adsbygoogle||[]);document.querySelectorAll('ins.adsbygoogle').forEach(function(){(adsbygoogle).push({})});" if CFG["adsense_client"] and not PREVIEW else ""}
}})();
</script>
</body></html>"""


def ad_slot():
    if CFG["adsense_client"] and CFG["adsense_slot_in_article"] and not PREVIEW:
        return (f'<div class="ad"><p class="ad__label">Oglas</p><ins class="adsbygoogle" style="display:block;text-align:center" '
                f'data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="{e(CFG["adsense_client"])}" '
                f'data-ad-slot="{e(CFG["adsense_slot_in_article"])}"></ins></div>')
    if CFG["show_ad_placeholders"]:
        return '<div class="ad ad--placeholder" aria-hidden="true">Mjesto za AdSense oglas</div>'
    return ""


def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>' for h, n in items)
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": BASE + h} if h else {})} for i, (h, n) in enumerate(items)]}
    return f'<nav class="crumbs wrap read" aria-label="Putanja"><ol>{lis}</ol></nav>', ld


def post_row(a, feature=False):
    img = (f'<a class="post__img" href="/clanci/{a["slug"]}/" tabindex="-1" aria-hidden="true">{picture(a["slug"], a["h1"], 1200, 750)}</a>'
           if has_image(a["slug"]) else "")
    return f"""<article class="post{' post--feature' if feature else ''}{' post--img' if img else ''}">{img}
<div><div class="post__meta"><span class="eyebrow">{e(a['kicker'])}</span><time datetime="{a['date']}">{hr_date(a['date'])}</time><span>{reading_time(a['body'])} min čitanja</span></div>
<h3><a href="/clanci/{a['slug']}/">{e(a['h1'])}</a></h3><p>{e(a['excerpt'])}</p>
<div class="tags">{''.join(f'<a class="tag" href="/kategorije/{s}/"><span class="dot hue-{CAT[s]["hue"]}"></span>{e(CAT[s]["name"])}</a>' for s in a['categories'])}</div></div>
</article>"""


# ---------- stranice ----------

def page_home():
    def tiles(group):
        return "".join(f"""<a class="cat hue-{c['hue']}" href="/kategorije/{c['slug']}/"><span class="cat__dot"></span>
<h3>{e(c['name'])}</h3><p>{e(c['short'])}</p><span class="cat__count">{plural(sum(c['slug'] in a['categories'] for a in ARTICLES))} →</span></a>""" for c in CATEGORIES if c["group"] == group)
    posts = "".join(post_row(a, i == 0) for i, a in enumerate(ARTICLES))
    return head(f"{CFG['site_name']} – iskrene beauty recenzije na hrvatskom",
                "Beauty recenzije na hrvatskom: njega, šminka i SPF, od Rhode i Chanela do ljekarničke kozmetike. Testirano na osjetljivoj koži, bez plaćenih recenzija.",
                "/", full_title=False) + header("/") + f"""
<section class="hero"><div class="wrap">
<div><p class="eyebrow">Beauty bilješke na hrvatskom</p>
<h1>Beauty recenzije <em>bez filtera</em>, od Rhode do Chanela.</h1>
<p class="lede">Hej, ja sam <strong>{e(CFG['author'])}</strong>. Isprobavam hit proizvode, luksuzne klasike i ljekarničku kozmetiku na svojoj osjetljivoj koži s rozaceom i pišem što je vrijedilo, a što je završilo u smeću.</p>
<a class="btn" href="/o-meni/">Upoznaj me</a></div>
<div class="hero__panel">{picture("foto-naslovnica", "Kozmetika na roza podlozi: bočica s pumpicom, serum, krema, SPF tuba i ruž", 1000, 1000, "hero__img", eager=True)}<span class="hero__sticker">Testirano na osjetljivoj koži</span><span class="hero__sticker hero__sticker--b">Bez plaćenih recenzija</span></div>
</div></section>
<div class="stripes" aria-hidden="true"></div>
<section class="section"><div class="wrap">
<div class="section__head"><h2>Recenzije po kategoriji</h2></div>
<div class="cats cats--3">{tiles("proizvod")}</div>
<div class="section__head" style="margin-top:56px"><h2>Po tipu kože</h2><p class="eyebrow">Moja specijalnost</p></div>
<div class="cats">{tiles("koza")}</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
<div class="section__head"><h2>Najnovije recenzije</h2></div>
<div class="posts">{posts}</div>
</div></section>
<section class="section principles"><div class="wrap">
<div class="section__head"><h2>Kako recenziram</h2></div>
<ul>
<li><h3>Na vlastitoj koži</h3><p>Pišem samo o proizvodima koje sam koristila tjednima, na osjetljivoj koži sklonoj crvenilu.</p></li>
<li><h3>I ono što ne valja</h3><p>Promašaji su jednako važni kao favoriti. Ako je nešto peklo ili curilo, to piše.</p></li>
<li><h3>Bez plaćenih recenzija</h3><p>Portal se financira oglasima. Brendovi ne plaćaju ocjene niti čitaju tekstove prije objave.</p></li>
</ul></div></section>
""" + footer()


def brand_chips(a):
    bs = [x for x in BRANDS if a in x["articles"]]
    if not bs:
        return ""
    return '<div class="brands-in"><p class="eyebrow">Brendovi u ovom članku</p><div class="tags">' + "".join(
        f'<a class="tag" href="/brendovi/{x["slug"]}/">{e(x["name"])}</a>' for x in bs) + "</div></div>"


def page_brands():
    path = "/brendovi/"
    cr, cr_ld = crumbs([("/", "Naslovnica"), (None, "Brendovi")])
    cr = cr.replace("wrap read", "wrap")
    groups = {}
    for x in BRANDS:
        groups.setdefault(x["name"][0].upper(), []).append(x)
    body = "".join(f'''<section class="az"><h2 class="az__letter">{L}</h2><ul class="brand-list">{"".join(
        f'<li><a class="brand-tile{" brand-tile--soon" if not x["articles"] else ""}" href="/brendovi/{x["slug"]}/"><span class="brand-tile__name">{e(x["name"])}</span>'
        f'<span class="brand-tile__count">{plural(len(x["articles"])) if x["articles"] else "recenzija uskoro"}</span></a></li>' for x in xs)}</ul></section>'''
        for L, xs in groups.items())
    ld = [cr_ld, {"@type": "CollectionPage", "name": "Brendovi", "url": BASE + path,
                  "hasPart": [{"@type": "WebPage", "name": x["name"], "url": f"{BASE}/brendovi/{x['slug']}/"} for x in BRANDS if x["articles"]]}]
    return head("Brendovi – beauty recenzije od A do Ž", f"Popis svih brendova na {CFG['site_name']}: od Avène i Babé do Chanela, Kiehl's i Rhode. Kliknite brend za sve recenzije.", path, extra_ld=ld) + header(path) + f"""
{cr}<div class="wrap"><header class="page-head"><p class="eyebrow">Od A do Ž</p><h1>Brendovi</h1>
<p class="page-sub">Svi brendovi koje sam isprobala. Kliknite brend za recenzije i spominjanja u člancima.</p></header>
<div class="az-wrap">{body}</div></div>
""" + footer()


def page_brand(x):
    path = f"/brendovi/{x['slug']}/"
    cr, cr_ld = crumbs([("/", "Naslovnica"), ("/brendovi/", "Brendovi"), (None, x["name"])])
    arts = x["articles"]
    if arts:
        intro = f"<p>Sve što sam napisala o proizvodima brenda {e(x['name'])}: recenzije, favoriti i promašaji, testirano na mojoj osjetljivoj koži.</p>"
        lst = f'<div class="posts">{"".join(post_row(a) for a in arts)}</div>'
    else:
        intro = f"<p>Detaljna recenzija proizvoda brenda {e(x['name'])} stiže uskoro. Pratite portal ili mi javite koji vas proizvod najviše zanima.</p>"
        lst = ""
    desc = f"{x['name']} recenzije na hrvatskom: iskrena iskustva s proizvodima brenda {x['name']} na osjetljivoj koži sklonoj crvenilu."
    ld = [cr_ld, {"@type": "CollectionPage", "name": f"{x['name']} recenzije", "url": BASE + path, "about": {"@type": "Brand", "name": x["name"]}}]
    return head(f"{x['name']} recenzije i iskustva", desc, path, extra_ld=ld, noindex=not arts) + header("/brendovi/") + f"""
{cr}<div class="wrap read"><header class="page-head"><p class="eyebrow">Brend</p><h1>{e(x['name'])}</h1></header>
<div class="page-intro prose">{x.get('intro') or intro}</div></div>
<section class="section" style="padding-top:24px"><div class="wrap read">{lst}<p style="margin-top:28px"><a href="/brendovi/">← Svi brendovi</a></p></div></section>
""" + footer()


def page_article(a):
    path = f"/clanci/{a['slug']}/"
    c = CAT[a["categories"][0]]
    cr, cr_ld = crumbs([("/", "Naslovnica"), (f"/kategorije/{c['slug']}/", c["name"]), (None, a["h1"])])
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a["body"])
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads)
    body = re.sub(r"<!--IMG:([\w-]+)\|([^|]*)\|([^>]*)-->", lambda m: f'<figure class="inline-fig{" inline-fig--sm" if m.group(1).startswith("foto-spf-") else ""}">{picture(m.group(1), m.group(2), 1200, 900 if m.group(1).startswith("foto-spf-") else 750)}<figcaption>{m.group(3)}</figcaption></figure>', a["body"])
    body = body.replace("<!--AD-->", ad_slot())
    ld = [cr_ld, {
        "@type": "BlogPosting", "headline": a["title"], "description": a["description"], "inLanguage": "hr-HR",
        "datePublished": a["date"], "dateModified": a.get("updated", a["date"]),
        "mainEntityOfPage": BASE + path, "image": BASE + (f"/slike/{a['slug']}.jpg" if has_image(a["slug"]) else "/brand/og-image.png"),
        "author": PERSON, "publisher": {"@id": BASE + "/#org"},
        "articleSection": [CAT[s]["name"] for s in a["categories"]],
        "wordCount": len(re.sub(r"<[^>]+>", " ", a["body"]).split())}]
    if a.get("itemlist"):
        ld.append({"@type": "ItemList", "name": a["h1"], "itemListOrder": "https://schema.org/ItemListOrderAscending",
                   "numberOfItems": len(a["itemlist"]),
                   "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(a["itemlist"])]})
    related = [x for x in ARTICLES if x is not a][:2]
    upd = f'<span>Ažurirano <time datetime="{a["updated"]}">{hr_date(a["updated"])}</time></span>' if a.get("updated") and a["updated"] != a["date"] else ""
    return head(a["title"], a["description"], path, "article", ld, image=f"/slike/{a['slug']}.jpg" if has_image(a["slug"]) else None) + header(None) + f"""
{cr}
<article class="wrap read">
<header class="article-head">
<p class="eyebrow">{e(a['kicker'])}</p>
<h1>{e(a['h1'])}</h1>
<div class="byline"><span>Piše <a href="/o-meni/">{e(CFG['author'])}</a></span><time datetime="{a['date']}">{hr_date(a['date'])}</time>{upd}<span>{reading_time(a['body'])} min čitanja</span></div>
<div class="tags">{''.join(f'<a class="tag" href="/kategorije/{s}/"><span class="dot hue-{CAT[s]["hue"]}"></span>{e(CAT[s]["name"])}</a>' for s in a['categories'])}</div>
<p class="verdict">{mark()}{e(a['verdict'])}</p>
</header>
{('<figure class="cover">' + picture(a["slug"], a["h1"], 1200, 750, eager=True) + '</figure>') if has_image(a["slug"]) else ''}
<details class="toc" open><summary>Sadržaj</summary><ul>{toc}</ul></details>
<div class="prose">{body}</div>
{ad_slot()}
{brand_chips(a)}
<aside class="author">{mark()}<div><strong>{e(CFG['author'])}</strong><p>{e(CFG['author_bio'])}</p></div></aside>
<p class="disclosure">Proizvode sam kupila sama ili ih dobila na dar, a mišljenje je uvijek moje. Tekst opisuje osobno iskustvo i ne zamjenjuje savjet dermatologa.</p>
</article>
<section class="section"><div class="wrap read"><div class="section__head"><h2>Pročitaj i ovo</h2></div>
<div class="posts">{''.join(post_row(x) for x in related)}</div></div></section>
""" + footer()


def page_category(c):
    path = f"/kategorije/{c['slug']}/"
    arts = [a for a in ARTICLES if c["slug"] in a["categories"]]
    cr, cr_ld = crumbs([("/", "Naslovnica"), (None, c["name"])])
    ld = [cr_ld, {"@type": "CollectionPage", "name": c["title"], "url": BASE + path, "description": c["description"],
                  "inLanguage": "hr-HR", "hasPart": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{BASE}/clanci/{a['slug']}/"} for a in arts]}]
    return head(c["title"], c["description"], path, extra_ld=ld) + header(path) + f"""
{cr}
<div class="wrap read">
<header class="page-head"><p class="eyebrow"><span class="dot hue-{c['hue']}"></span> Kategorija</p><h1>{e(c['name'])}</h1></header>
<div class="page-intro prose">{c['intro']}</div>
</div>
<section class="section"><div class="wrap read"><div class="section__head"><h2>Recenzije i liste</h2></div>
<div class="posts">{''.join(post_row(a) for a in arts)}</div></div></section>
""" + footer()


def page_simple(slug, title, desc, h1, body, noindex=False):
    path = f"/{slug}/"
    cr, cr_ld = crumbs([("/", "Naslovnica"), (None, h1)])
    return head(title, desc, path, extra_ld=[cr_ld], noindex=noindex) + header(path) + f"""
{cr}<div class="wrap read"><header class="page-head"><h1>{e(h1)}</h1></header><div class="prose">{body}</div></div>
""" + footer()


ABOUT = f"""<figure class="inline-fig">{picture("foto-polica", "Kozmetika na svijetloplavoj podlozi: krema, serum, tonik, SPF i ruž", 1200, 750)}</figure>
<p class="lead">Bok, ja sam {e(CFG['author'])}. Imam osjetljivu, reaktivnu kožu s rozaceom i ten svijetao kao sir, kako to volim reći.</p>
<p>Godinama tražim kozmetiku koja moju kožu neće razljutiti. Usput sam potrošila previše novca na proizvode koji se “preporučuju za osjetljivu kožu”, a meni su izazvali crvenilo, peckanje ili ljuštenje. {e(CFG['site_name'])} je nastao da drugima taj put bude kraći, i da o svakom proizvodu, od Rhode do Chanela, dobijete iskreno mišljenje na hrvatskom.</p>
<h2 id="kako">Kako pišem recenzije</h2>
<ul><li>Pišem samo o proizvodima koje sam stvarno koristila, i to dovoljno dugo da znam kako se ponašaju.</li>
<li>Uz svaki proizvod navodim što brend tvrdi, a što sam iskusila.</li>
<li>Pišem i o promašajima, jer iz njih se najviše nauči.</li>
<li>Ne primam novac za recenzije. Portal se financira oglasima (Google AdSense).</li></ul>
<h2 id="napomena">Važna napomena</h2>
<p>Nisam liječnica ni dermatologinja. Sadržaj na portalu temelji se na osobnom iskustvu i informativne je naravi. Za dijagnozu i liječenje rozacee ili bilo kojeg stanja kože obratite se dermatologu.</p>"""

CONTACT = f"""<p>Imate pitanje, prijedlog proizvoda za recenziju ili ispravak? Pišite mi na <strong>{e(CFG['contact_email'])}</strong>.</p>
<p>Brendovi i PR agencije su dobrodošli poslati proizvod na testiranje, uz napomenu da ne jamčim objavu ni pozitivnu recenziju.</p>"""

PRIVACY = f"""<p class="lead">Ova stranica objašnjava koje podatke {e(CFG['site_name'])} prikuplja i zašto, u skladu s Općom uredbom o zaštiti podataka (GDPR).</p>
<h2 id="voditelj">Voditelj obrade</h2><p>{e(CFG['author'])}, {e(CFG['site_name'])}. Kontakt: {e(CFG['contact_email'])}.</p>
<h2 id="analitika">Analitika (PostHog)</h2><p>Za mjerenje posjećenosti koristimo PostHog s poslužiteljima u Europskoj uniji. Bez vašeg pristanka analitika radi bez kolačića i ne pamti vas između posjeta. Ako pristanete, PostHog sprema anonimni identifikator u kolačić i lokalnu pohranu preglednika kako bismo razumjeli koji su članci korisni.</p>
<h2 id="oglasi">Oglasi (Google AdSense)</h2><p>Portal prikazuje oglase putem usluge Google AdSense. Google i njegovi partneri mogu koristiti kolačiće za prikaz oglasa na temelju vaših prethodnih posjeta ovoj i drugim stranicama. Za posjetitelje iz EU pristanak za oglase prikuplja se putem Googleove platforme za upravljanje pristankom. Personalizirane oglase možete isključiti u <a href="https://adssettings.google.com" rel="nofollow noopener">Googleovim postavkama oglasa</a>. Više o tome kako Google koristi podatke: <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2 id="kolacici">Kolačići i lokalna pohrana</h2><ul>
<li><strong>mk-consent</strong> (lokalna pohrana, nužno): pamti vaš izbor o kolačićima.</li>
<li><strong>ph_*</strong> (PostHog, analitika): samo uz pristanak.</li>
<li><strong>Google AdSense kolačići</strong> (oglašavanje): prema postavkama pristanka.</li></ul>
<p>Svoj izbor možete promijeniti bilo kad putem poveznice “Postavke kolačića” na dnu stranice.</p>
<h2 id="prava">Vaša prava</h2><p>Imate pravo na pristup, ispravak i brisanje podataka te pravo na prigovor Agenciji za zaštitu osobnih podataka (azop.hr).</p>
<p><em>Zadnja izmjena: {hr_date(date.today().isoformat())}</em></p>"""


def page_404():
    return head("Stranica nije pronađena", "Tražena stranica ne postoji.", "/404.html", noindex=True) + header(None) + """
<div class="wrap read"><header class="page-head"><h1>Ova stranica ne postoji</h1></header>
<div class="prose"><p>Možda je premještena. Vratite se na <a href="/">naslovnicu</a> ili odaberite kategoriju u izborniku.</p></div></div>
""" + footer()


# ---------- pomoćne datoteke ----------

def sitemap():
    urls = [("/", ARTICLES[0]["updated"], "1.0")]
    urls += [(f"/kategorije/{c['slug']}/", max(a.get("updated", a["date"]) for a in ARTICLES if c["slug"] in a["categories"]), "0.8") for c in CATEGORIES]
    urls += [(f"/clanci/{a['slug']}/", a.get("updated", a["date"]), "0.9") for a in ARTICLES]
    urls += [("/brendovi/", date.today().isoformat(), "0.7")]
    urls += [(f"/brendovi/{x['slug']}/", max(a.get("updated", a["date"]) for a in x["articles"]), "0.6") for x in BRANDS if x["articles"]]
    urls += [("/o-meni/", date.today().isoformat(), "0.4"), ("/kontakt/", date.today().isoformat(), "0.3"),
             ("/politika-privatnosti/", date.today().isoformat(), "0.2")]
    rows = "".join(f"<url><loc>{BASE}{p}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n" for p, d, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'


def rss():
    items = "".join(f"<item><title>{e(a['title'])}</title><link>{BASE}/clanci/{a['slug']}/</link><guid>{BASE}/clanci/{a['slug']}/</guid>"
                    f"<pubDate>{date.fromisoformat(a['date']).strftime('%a, %d %b %Y')} 08:00:00 +0000</pubDate><description>{e(a['excerpt'])}</description></item>"
                    for a in ARTICLES)
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{e(CFG["site_name"])}</title>'
            f'<link>{BASE}/</link><description>{e(CFG["tagline"])}</description><language>hr</language>{items}</channel></rss>')


def relativize(doc, path):
    """Za --preview: /a/b/ -> ../../a/b/index.html, da poveznice rade bez servera."""
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    up = "../" * depth

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith("//"):
            return m.group(0)
        frag = ""
        if "#" in url:
            url, frag = url.split("#", 1)
            frag = "#" + frag
        u = url.lstrip("/")
        if u == "" or u.endswith("/"):
            u += "index.html"
        return f'{attr}="{up}{u}{frag}"'
    return re.sub(r'(href|src|srcset)="(/[^"]*)"', fix, doc)


def write(path, doc):
    fs = os.path.join(OUT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(fs), exist_ok=True)
    if PREVIEW and fs.endswith(".html"):
        doc = relativize(doc, path if path.endswith("/") else os.path.dirname(path) + "/")
    open(fs, "w", encoding="utf-8").write(doc)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    write("/", page_home())
    for a in ARTICLES:
        write(f"/clanci/{a['slug']}/", page_article(a))
    for c in CATEGORIES:
        write(f"/kategorije/{c['slug']}/", page_category(c))
    write("/brendovi/", page_brands())
    for x in BRANDS:
        write(f"/brendovi/{x['slug']}/", page_brand(x))
    write("/o-meni/", page_simple("o-meni", "O meni", f"Tko piše {CFG['site_name']} i kako nastaju recenzije kozmetike za osjetljivu kožu i rozaceu.", "O meni", ABOUT))
    write("/kontakt/", page_simple("kontakt", "Kontakt", "Kontakt za pitanja, prijedloge i suradnje.", "Kontakt", CONTACT))
    write("/politika-privatnosti/", page_simple("politika-privatnosti", "Politika privatnosti i kolačića", f"Kako {CFG['site_name']} koristi kolačiće, PostHog analitiku i Google AdSense oglase.", "Privatnost i kolačići", PRIVACY))
    write("/404.html", page_404())
    write("/sitemap.xml", sitemap())
    write("/rss.xml", rss())
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    if CFG["adsense_client"]:
        write("/ads.txt", f"google.com, {CFG['adsense_client'].replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    write("/site.webmanifest", json.dumps({"name": CFG["site_name"], "short_name": CFG["site_name"], "lang": "hr",
                                           "icons": [{"src": "/brand/logo-192.png", "sizes": "192x192", "type": "image/png"},
                                                     {"src": "/brand/logo-512.png", "sizes": "512x512", "type": "image/png"}],
                                           "theme_color": "#f4a7bb", "background_color": "#fffbf7", "display": "standalone"}, ensure_ascii=False))
    # statične datoteke
    for src, dst in [("assets/brand", "brand"), ("fonts", "fonts"), ("assets/slike", "slike")]:
        if os.path.isdir(os.path.join(ROOT, src)):
            shutil.copytree(os.path.join(ROOT, src), os.path.join(OUT, dst), ignore=shutil.ignore_patterns("*.css") if dst == "fonts" else shutil.ignore_patterns("*.svg") if dst == "slike" else None)
    for f in ["favicon.svg", "favicon-32.png", "apple-touch-icon.png", "_headers"]:
        p = os.path.join(ROOT, "assets", f)
        if os.path.exists(p):
            shutil.copy(p, OUT)
    print("Gotovo:", OUT)


if __name__ == "__main__":
    main()
