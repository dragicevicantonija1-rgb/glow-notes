#!/usr/bin/env python3
"""Generator statične stranice (ime i ključevi su u config.json).

    python3 build.py            -> dist/     (produkcija: čisti URL-ovi, fontovi s vlastitog servera)
    python3 build.py --preview  -> preview/  (relativne poveznice, za pregled bez servera)

Ključevi (PostHog, Search Console, AdSense) upisuju se samo u config.json.
"""
import html, json, math, os, re, shutil, sys
from datetime import date
from content import ARTICLES, BRANDS, CATEGORIES
from content_recenzije import REVIEWS
from komentari import KOMENTARI
import content_en
ARTICLES = sorted(REVIEWS, key=lambda r: r["kicker"] != "Rutina") + ARTICLES
LANG = "hr"  # main() gradi prvo hrvatsku verziju u /, zatim englesku u /en/


def T(hr, en):
    return en if LANG == "en" else hr

ROOT = os.path.dirname(os.path.abspath(__file__))
PREVIEW = "--preview" in sys.argv
OUT = os.path.join(ROOT, "preview" if PREVIEW else "dist")
CFG = json.load(open(os.path.join(ROOT, "config.json"), encoding="utf-8"))
BASE = CFG["base_url"].rstrip("/")
CSS = re.sub(r"/\*.*?\*/", "", open(os.path.join(ROOT, "assets", "site.css"), encoding="utf-8").read(), flags=re.S)
FONT_CSS = open(os.path.join(ROOT, "fonts", "fonts.css"), encoding="utf-8").read()
CAT = {c["slug"]: c for c in CATEGORIES}
ARTICLES = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
for _b in BRANDS:
    _b["slug"] = re.sub(r"[^a-z0-9]+", "-", _b["name"].lower().replace("é", "e").replace("è", "e").replace("'", "")).strip("-")
    _b["articles"] = [a for a in ARTICLES if any(al.lower() in re.sub(r"<[^>]+>", " ", a["body"]).lower() for al in _b["aliases"])]
BRANDS = sorted(BRANDS, key=lambda x: x["name"].lower())
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MONTHS = ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja",
          "kolovoza", "rujna", "listopada", "studenoga", "prosinca"]
e = html.escape


def hr_date(iso):
    d = date.fromisoformat(iso)
    if LANG == "en":
        return f"{d.day} {MONTHS_EN[d.month - 1]} {d.year}"
    return f"{d.day}. {MONTHS[d.month - 1]} {d.year}."


def has_image(slug):
    return os.path.exists(os.path.join(ROOT, "assets", "slike", slug + ".jpg"))


def picture(slug, alt, w, h, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<picture class="{cls}"><source srcset="/slike/{slug}.webp" type="image/webp">'
            f'<img src="/slike/{slug}.jpg" alt="{e(alt)}" width="{w}" height="{h}" {load} decoding="async"></picture>')


def plural(n):
    if LANG == "en":
        return f"{n} article" if n == 1 else f"{n} articles"
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


def lang_tag():
    return T("hr-HR", "en-GB")


ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": CFG["site_name"], "url": BASE + "/",
       "logo": {"@type": "ImageObject", "url": BASE + "/brand/logo-512.png", "width": 512, "height": 512}}
def person():
    return {"@type": "Person", "@id": BASE + "/#autorica", "name": CFG["author"], "url": BASE + "/o-meni/", "description": CFG["author_bio"],
            "knowsAbout": T(["osjetljiva koža", "rozacea", "reaktivna koža", "mineralni SPF", "njega lica", "šminka"],
                            ["sensitive skin", "rosacea", "reactive skin", "mineral SPF", "skincare", "make-up"])}


def head(title, desc, path, og_type="website", extra_ld=None, noindex=False, full_title=True, image=None):
    url = BASE + path
    t = f"{title} | {CFG['site_name']}" if full_title else title
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&family=Instrument+Sans:wght@400..700&display=swap">') if PREVIEW else (
        '<link rel="preload" href="/fonts/instrumentsans-latin.woff2" as="font" type="font/woff2" crossorigin>'
        '<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>'
        f"<style>{FONT_CSS}</style>")
    gsc = f'<meta name="google-site-verification" content="{e(CFG["google_site_verification"])}">' if CFG["google_site_verification"] else ""
    if CFG.get("bing_site_verification"):
        gsc += f'<meta name="msvalidate.01" content="{e(CFG["bing_site_verification"])}">'
    ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(CFG["adsense_client"])}" crossorigin="anonymous"></script>'
           if CFG["adsense_client"] and not PREVIEW else "")
    ph = posthog_snippet() if CFG["posthog_key"] and not PREVIEW else ""
    if CFG.get("ga4_id") and not PREVIEW:
        ph += (f'<script async src="https://www.googletagmanager.com/gtag/js?id={e(CFG["ga4_id"])}"></script><script>'
               'window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}'
               'var g="denied";try{if(localStorage.getItem("mk-consent")==="da")g="granted"}catch(_){}'
               'gtag("consent","default",{ad_storage:g,ad_user_data:g,ad_personalization:g,analytics_storage:g});'
               f'gtag("js",new Date());gtag("config",{json.dumps(CFG["ga4_id"])});</script>')
    ld = [ORG, {"@type": "WebSite", "@id": BASE + "/#web", "url": BASE + "/", "name": CFG["site_name"],
                "inLanguage": lang_tag(), "publisher": {"@id": BASE + "/#org"}}] + (extra_ld or [])
    return f"""<!doctype html>
<html lang="{T('hr', 'en')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<!--ALT-->
<meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-image-preview:large'}">
<meta property="og:locale" content="{T('hr_HR', 'en_GB')}"><meta property="og:locale:alternate" content="{T('en_GB', 'hr_HR')}">
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
<link rel="alternate" type="application/rss+xml" title="{e(CFG['site_name'])}" href="{T('/rss.xml', '/en/rss.xml')}">
{gsc}
{fonts}
<style>{CSS}</style>
{jsonld({"@context": "https://schema.org", "@graph": ld})}
{ph}
{ads}
</head>
<body>
<a class="skip" href="#sadrzaj">{T('Preskoči na sadržaj', 'Skip to content')}</a>
<div class="stripes" aria-hidden="true"></div>
"""


def posthog_snippet():
    # Bez kolačića dok posjetitelj ne pristane (persistence: memory), zatim localStorage+cookie.
    return """<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
var mkConsent=null;try{mkConsent=localStorage.getItem("mk-consent")}catch(_){}
posthog.init(%s,{api_host:%s,person_profiles:"identified_only",persistence:mkConsent==="da"?"localStorage+cookie":"memory",capture_pageview:true,capture_pageleave:true});
</script>""" % (json.dumps(CFG["posthog_key"]), json.dumps(CFG["posthog_host"]))


NAV = [("/", "Naslovnica", "Home"), ("/brendovi/", "Brendovi", "Brands"), ("/kategorije/favoriti/", "Favoriti", "Favourites"), ("/kategorije/flop/", "Flop", "Flops"),
       ("/kategorije/njega-lica/", "Njega", "Skincare"), ("/kategorije/sminka/", "Šminka", "Make-up"), ("/o-meni/", "O meni", "About")]


def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{e(T(n, en))}</a>' for h, n, en in NAV[1:])
    return f"""<header class="site-header"><div class="wrap">
<a class="brand" href="/" aria-label="{e(CFG['site_name'])}, {T('naslovnica', 'home')}">{mark()}<span class="brand__name">{e(CFG['site_name'])}</span></a>
<nav class="nav" aria-label="{T('Glavna navigacija', 'Main navigation')}">{links}<!--LANGSW--></nav>
</div></header>
<main id="sadrzaj">"""


def footer():
    cats = "".join(f'<li><a href="/kategorije/{c["slug"]}/">{e(c["name"])}</a></li>' for c in CATEGORIES)
    return f"""</main>
<footer class="site-footer"><div class="wrap">
<div><a class="brand" href="/">{mark()}<span class="brand__name">{e(CFG['site_name'])}</span></a>
<p class="note">{e(CFG['tagline'])}. {T('Sadržaj je informativan i ne zamjenjuje savjet dermatologa.', 'Content is for information only and does not replace advice from a dermatologist.')}</p></div>
<div><h2>{T('Kategorije', 'Categories')}</h2><ul>{cats}</ul></div>
<div><h2>{T('Portal', 'Site')}</h2><ul><li><a href="/o-meni/">{T('O meni', 'About me')}</a></li><li><a href="/kontakt/">{T('Kontakt', 'Contact')}</a></li>
<li><a href="/politika-privatnosti/">{T('Privatnost i kolačići', 'Privacy and cookies')}</a></li><li><button type="button" class="btn-link" id="mk-consent-open">{T('Postavke kolačića', 'Cookie settings')}</button></li>{'<li><a href="/brand/identitet.html">Vizualni identitet (pregled)</a></li>' if PREVIEW else ''}</ul></div>
</div><div class="wrap"><p>© {date.today().year} {e(CFG['site_name'])}</p></div></footer>
<div class="consent" id="mk-consent" hidden role="dialog" aria-label="{T('Kolačići', 'Cookies')}"><div class="consent__in">
<p>{T('Koristimo kolačiće za analitiku posjeta i prikaz oglasa. Nužni rade uvijek, ostale uključujemo samo uz vaš pristanak.', 'We use cookies for visitor analytics and ads. Essential ones always run; we only switch on the others with your consent.')} <a href="/politika-privatnosti/">{T('Više o tome', 'Learn more')}</a></p>
<div class="consent__btns"><button type="button" class="no" id="mk-consent-no">{T('Samo nužni', 'Essential only')}</button><button type="button" class="yes" id="mk-consent-yes">{T('Prihvaćam', 'Accept')}</button></div>
</div></div>
<script>
(function(){{var b=document.getElementById("mk-consent"),v=null;try{{v=localStorage.getItem("mk-consent")}}catch(_){{}}
if(!v)b.hidden=false;
function set(x){{try{{localStorage.setItem("mk-consent",x)}}catch(_){{}}b.hidden=true;
if(window.gtag){{var g=x==="da"?"granted":"denied";gtag("consent","update",{{ad_storage:g,ad_user_data:g,ad_personalization:g,analytics_storage:g}})}}
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
        return (f'<div class="ad"><p class="ad__label">{T('Oglas', 'Advertisement')}</p><ins class="adsbygoogle" style="display:block;text-align:center" '
                f'data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="{e(CFG["adsense_client"])}" '
                f'data-ad-slot="{e(CFG["adsense_slot_in_article"])}"></ins></div>')
    if CFG["show_ad_placeholders"]:
        return f'<div class="ad ad--placeholder" aria-hidden="true">{T("Mjesto za AdSense oglas", "AdSense ad space")}</div>'
    return ""


def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>' for h, n in items)
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": BASE + h} if h else {})} for i, (h, n) in enumerate(items)]}
    return f'<nav class="crumbs wrap read" aria-label="{T('Putanja', 'Breadcrumb')}"><ol>{lis}</ol></nav>', ld


def post_row(a, feature=False):
    img = (f'<a class="post__img" href="/clanci/{a["slug"]}/" tabindex="-1" aria-hidden="true">{picture(a["slug"], a["h1"], 1200, 750)}</a>'
           if has_image(a["slug"]) else "")
    return f"""<article class="post{' post--feature' if feature else ''}{' post--img' if img else ''}">{img}
<div><div class="post__meta"><span class="eyebrow">{e(a['kicker'])}</span><time datetime="{a['date']}">{hr_date(a['date'])}</time><span>{reading_time(a['body'])} {T('min čitanja', 'min read')}</span></div>
<h3><a href="/clanci/{a['slug']}/">{e(a['h1'])}</a></h3>{('<p class="post__stars">' + stars(a['review']['rating']) + '</p>') if a.get('review') else ''}<p>{e(a['excerpt'])}</p>
<div class="tags">{''.join(f'<a class="tag" href="/kategorije/{s}/"><span class="dot hue-{CAT[s]["hue"]}"></span>{e(CAT[s]["name"])}</a>' for s in a['categories'])}</div></div>
</article>"""


# ---------- stranice ----------

def page_home():
    def tiles(group):
        return "".join(f"""<a class="cat hue-{c['hue']}" href="/kategorije/{c['slug']}/"><span class="cat__dot"></span>
<h3>{e(c['name'])}</h3><p>{e(c['short'])}</p><span class="cat__count">{plural(sum(c['slug'] in a['categories'] for a in ARTICLES))} →</span></a>""" for c in CATEGORIES if c["group"] == group)
    posts = "".join(post_row(a, i == 0) for i, a in enumerate(ARTICLES))
    return head(T(f"{CFG['site_name']} – iskrene beauty recenzije na hrvatskom", f"{CFG['site_name']} – honest beauty reviews for sensitive skin"),
                T("Beauty recenzije na hrvatskom: njega, šminka i SPF, od Rhode i Chanela do ljekarničke kozmetike. Testirano na osjetljivoj koži, bez plaćenih recenzija.",
                  "Honest beauty reviews from Europe: skincare, make-up and SPF, from Rhode and Chanel to pharmacy brands. Tested on sensitive skin with rosacea, no paid reviews."),
                "/", full_title=False) + header("/") + f"""
<section class="hero"><div class="wrap">
<div><p class="eyebrow">{T('Beauty bilješke na hrvatskom', 'Beauty notes from Croatia')}</p>
<h1>{T('Beauty recenzije <em>bez filtera</em>, od Rhode do Chanela.', 'Beauty reviews <em>without a filter</em>, from Rhode to Chanel.')}</h1>
<p class="lede">{T(f"Hej, ja sam <strong>{e(CFG['author'])}</strong>. Isprobavam hit proizvode, luksuzne klasike i ljekarničku kozmetiku na svojoj osjetljivoj koži s rozaceom i pišem što je vrijedilo, a što je završilo u smeću.",
                   f"Hi, I'm <strong>{e(CFG['author'])}</strong>. I test viral products, luxury classics and pharmacy skincare on my sensitive skin with rosacea, and write about what was worth it and what ended up in the bin.")}</p>
<a class="btn" href="/o-meni/">{T('Upoznaj me', 'Meet me')}</a></div>
<div class="hero__panel">{picture("foto-naslovnica", T("Kozmetika na roza podlozi: bočica s pumpicom, serum, krema, SPF tuba i ruž", "Beauty products on a pink background: pump bottle, serum, cream, SPF tube and lipstick"), 1000, 1000, "hero__img", eager=True)}<span class="hero__sticker">{T('Testirano na osjetljivoj koži', 'Tested on sensitive skin')}</span><span class="hero__sticker hero__sticker--b">{T('Bez plaćenih recenzija', 'No paid reviews')}</span></div>
</div></section>
<div class="stripes" aria-hidden="true"></div>
<section class="section"><div class="wrap">
<div class="section__head"><h2>{T('Recenzije po kategoriji', 'Reviews by category')}</h2></div>
<div class="cats cats--3">{tiles("proizvod")}</div>
<div class="section__head" style="margin-top:56px"><h2>{T('Po tipu kože', 'By skin type')}</h2><p class="eyebrow">{T('Moja specijalnost', 'My speciality')}</p></div>
<div class="cats">{tiles("koza")}</div>
<div class="section__head" style="margin-top:56px"><h2>{T('Favoriti i flopovi', 'Favourites and flops')}</h2><p class="eyebrow">{T('Iskreno, bez uljepšavanja', 'Honest, no sugar-coating')}</p></div>
<div class="cats cats--2">{tiles("presuda")}</div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
<div class="section__head"><h2>{T('Najnovije recenzije', 'Latest reviews')}</h2></div>
<div class="posts">{posts}</div>
</div></section>
<section class="section principles"><div class="wrap">
<div class="section__head"><h2>{T('Kako recenziram', 'How I review')}</h2></div>
<ul>
<li><h3>{T('Na vlastitoj koži', 'On my own skin')}</h3><p>{T('Pišem samo o proizvodima koje sam koristila tjednima, na osjetljivoj koži sklonoj crvenilu.', 'I only write about products I have used for weeks, on sensitive skin prone to redness.')}</p></li>
<li><h3>{T('I ono što ne valja', 'The bad bits too')}</h3><p>{T('Promašaji su jednako važni kao favoriti. Ako je nešto peklo ili curilo, to piše.', 'Flops matter as much as favourites. If something stung or leaked, I say so.')}</p></li>
<li><h3>{T('Bez plaćenih recenzija', 'No paid reviews')}</h3><p>{T('Portal se financira oglasima. Brendovi ne plaćaju ocjene niti čitaju tekstove prije objave.', 'The site is funded by ads. Brands don\'t pay for ratings or read reviews before they go live.')}</p></li>
</ul></div></section>
""" + footer()


def brand_chips(a):
    bs = [x for x in BRANDS if a in x["articles"]]
    if not bs:
        return ""
    return '<div class="brands-in"><p class="eyebrow">' + T("Brendovi u ovom članku", "Brands in this article") + '</p><div class="tags">' + "".join(
        f'<a class="tag" href="/brendovi/{x["slug"]}/">{e(x["name"])}</a>' for x in bs) + "</div></div>"


def page_brands():
    path = "/brendovi/"
    cr, cr_ld = crumbs([("/", T("Naslovnica", "Home")), (None, T("Brendovi", "Brands"))])
    cr = cr.replace("wrap read", "wrap")
    groups = {}
    for x in BRANDS:
        groups.setdefault(x["name"][0].upper(), []).append(x)
    body = "".join(f'''<section class="az"><h2 class="az__letter">{L}</h2><ul class="brand-list">{"".join(
        f'<li><a class="brand-tile{" brand-tile--soon" if not x["articles"] else ""}" href="/brendovi/{x["slug"]}/"><span class="brand-tile__name">{e(x["name"])}</span>'
        f'<span class="brand-tile__count">{plural(len(x["articles"])) if x["articles"] else T("recenzija uskoro", "review coming soon")}</span></a></li>' for x in xs)}</ul></section>'''
        for L, xs in groups.items())
    ld = [cr_ld, {"@type": "CollectionPage", "name": T("Brendovi", "Brands"), "url": BASE + path,
                  "hasPart": [{"@type": "WebPage", "name": x["name"], "url": f"{BASE}/brendovi/{x['slug']}/"} for x in BRANDS if x["articles"]]}]
    return head(T("Brendovi – beauty recenzije od A do Ž", "Brands – beauty reviews from A to Z"),
                T(f"Popis svih brendova na {CFG['site_name']}: od Avène i Babé do Chanela, Kiehl's i Rhode. Kliknite brend za sve recenzije.",
                  f"All brands reviewed on {CFG['site_name']}: from Avène and Babé to Chanel, Kiehl's and Rhode. Click a brand for every review."), path, extra_ld=ld) + header(path) + f"""
{cr}<div class="wrap"><header class="page-head"><p class="eyebrow">{T('Od A do Ž', 'From A to Z')}</p><h1>{T('Brendovi', 'Brands')}</h1>
<p class="page-sub">{T('Svi brendovi koje sam isprobala. Kliknite brend za recenzije i spominjanja u člancima.', 'Every brand I have tried. Click a brand for reviews and mentions in articles.')}</p></header>
<div class="az-wrap">{body}</div></div>
""" + footer()


def page_brand(x):
    path = f"/brendovi/{x['slug']}/"
    cr, cr_ld = crumbs([("/", T("Naslovnica", "Home")), ("/brendovi/", T("Brendovi", "Brands")), (None, x["name"])])
    arts = x["articles"]
    if arts:
        intro = T(f"<p>Sve što sam napisala o proizvodima brenda {e(x['name'])}: recenzije, favoriti i promašaji, testirano na mojoj osjetljivoj koži.</p>",
                  f"<p>Everything I have written about {e(x['name'])} products: reviews, favourites and flops, tested on my sensitive skin.</p>")
        lst = f'<div class="posts">{"".join(post_row(a) for a in arts)}</div>'
    else:
        intro = T(f"<p>Detaljna recenzija proizvoda brenda {e(x['name'])} stiže uskoro. Pratite portal ili mi javite koji vas proizvod najviše zanima.</p>",
                  f"<p>A detailed {e(x['name'])} review is coming soon. Follow the site or tell me which product interests you most.</p>")
        lst = ""
    desc = T(f"{x['name']} recenzije na hrvatskom: iskrena iskustva s proizvodima brenda {x['name']} na osjetljivoj koži sklonoj crvenilu.",
             f"{x['name']} reviews: honest experiences with {x['name']} products on sensitive skin prone to redness.")
    ld = [cr_ld, {"@type": "CollectionPage", "name": T(f"{x['name']} recenzije", f"{x['name']} reviews"), "url": BASE + path, "about": {"@type": "Brand", "name": x["name"]}}]
    return head(T(f"{x['name']} recenzije i iskustva", f"{x['name']} reviews and experiences"), desc, path, extra_ld=ld, noindex=not arts) + header("/brendovi/") + f"""
{cr}<div class="wrap read"><header class="page-head"><p class="eyebrow">{T('Brend', 'Brand')}</p><h1>{e(x['name'])}</h1></header>
<div class="page-intro prose">{x.get('intro') or intro}</div></div>
<section class="section" style="padding-top:24px"><div class="wrap read">{lst}<p style="margin-top:28px"><a href="/brendovi/">← {T('Svi brendovi', 'All brands')}</a></p></div></section>
""" + footer()


# AI tražilice (ChatGPT, Perplexity, Claude, Gemini, Copilot) smiju čitati i citirati stranicu.
AI_BOTS = ["OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot",
           "Claude-User", "Google-Extended", "Applebot-Extended", "Bingbot", "DuckAssistBot", "MistralAI-User"]


def plain(html):
    t = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    t = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", t)
    t = re.sub(r"<li[^>]*>", "- ", t)
    t = re.sub(r"</t[dh]>\s*(?=<t[dh])", " | ", t)
    t = re.sub(r"</(p|li|tr|h3)>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t).replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\n\s*\n+", "\n\n", "\n".join(l.strip() for l in t.splitlines())).strip()


def llms_txt(full=False):
    out = [f"# {CFG['site_name']}", "", f"> {CFG['tagline']}", "",
           T(f"Iskrene beauty recenzije na hrvatskom jeziku. Autorica {CFG['author']} piše iz osobnog iskustva s osjetljivom, reaktivnom kožom sklonom rozacei. "
             "Proizvodi su stvarno korišteni tjednima prije ocjene. Tekstovi ne zamjenjuju savjet dermatologa.",
             f"Honest beauty reviews in English (also available in Croatian). The author, {CFG['author']}, writes from personal experience with sensitive, reactive skin prone to rosacea. "
             "Products are genuinely used for weeks before being rated. The texts do not replace advice from a dermatologist."), ""] + ([] if full else [T("## Članci", "## Articles"), ""])
    for a in ARTICLES:
        url = f"{BASE}/clanci/{a['slug']}/"
        if not full:
            out.append(f"- [{a['title']}]({url}): {a['description']}")
            continue
        out += [f"# {a['h1']}", "", f"URL: {url}", T(f"Autorica: {CFG['author']} · Objavljeno: {a['date']} · Ažurirano: {a.get('updated', a['date'])}",
                                                      f"Author: {CFG['author']} · Published: {a['date']} · Updated: {a.get('updated', a['date'])}"), "",
                f"{T('Presuda', 'Verdict')}: {a['verdict']}", "", plain(a["body"]), ""]
        if a.get("faq"):
            out += [T("## Česta pitanja", "## FAQ"), ""] + [f"**{q}**\n{ans}\n" for q, ans in a["faq"]]
        out.append("")
    if not full:
        out += ["", T("## Kategorije", "## Categories"), ""] + [f"- [{c['name']}]({BASE}/kategorije/{c['slug']}/): {c['description']}" for c in CATEGORIES]
        out += ["", T("## Ostalo", "## Other"), "", T(f"- [Brendovi]({BASE}/brendovi/): popis brendova o kojima pišem", f"- [Brands]({BASE}/brendovi/): all brands I write about"),
                T(f"- [O meni]({BASE}/o-meni/): tko piše i kako nastaju recenzije", f"- [About]({BASE}/o-meni/): who writes and how reviews are made"),
                T(f"- [Svi tekstovi u jednoj datoteci]({BASE}/llms-full.txt)", f"- [All texts in one file]({BASE}/llms-full.txt)"),
                T(f"- [English version]({BASE}/en/llms.txt)", f"- [Hrvatska verzija (Croatian)]({BASE}/llms.txt)")]
    return "\n".join(out) + "\n"


def fmt_rating(n):
    return f"{n:g}" if LANG == "en" else (f"{n:g}").replace(".", ",")


def stars(n, cls="stars"):
    return (f'<span class="{cls}" role="img" aria-label="{T('Ocjena', 'Rated')} {fmt_rating(n)} {T('od', 'out of')} 5"><span aria-hidden="true">★★★★★</span>'
            f'<span class="stars__on" aria-hidden="true" style="width:{n / 5 * 100:g}%">★★★★★</span></span>')


def review_block(r):
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
    return f"""<section class="topflop" aria-labelledby="top-i-flop"><h2 id="top-i-flop">{T('Top i flop', 'Tops and flops')}</h2>
<div class="topflop__grid"><div class="topflop__col topflop__col--top"><h3>Top</h3><ul>{li(r['pros'])}</ul></div>
<div class="topflop__col topflop__col--flop"><h3>Flop</h3><ul>{li(r['cons'])}</ul></div></div></section>
<section class="rating" aria-labelledby="ocjena"><h2 id="ocjena">{T('Ocjena', 'Rating')}</h2>
<p class="rating__row">{stars(r['rating'], 'stars stars--big')}<strong>{fmt_rating(r['rating'])}/5</strong></p><p class="rating__name">{e(r['product'])}</p></section>"""


def comments_block(a):
    cs = KOMENTARI.get(a["slug"], [])
    lst = "".join(f'<li class="comment"><p class="comment__meta"><strong>{e(c["ime"])}</strong> <time datetime="{c["datum"]}">{hr_date(c["datum"])}</time></p><p>{e(c["tekst"])}</p>'
                  + (f'<p class="comment__reply"><strong>{e(CFG["author"])}:</strong> {e(c["odgovor"])}</p>' if c.get("odgovor") else "") + "</li>" for c in cs)
    return f"""<section class="comments" aria-labelledby="komentari"><h2 id="komentari">{T('Komentari', 'Comments')}{f' ({len(cs)})' if cs else ''}</h2>
{f'<ol class="comment-list">{lst}</ol>' if cs else T('<p>Još nema komentara. Budi prva koja će podijeliti svoje iskustvo!</p>', '<p>No comments yet. Be the first to share your experience!</p>')}
<form class="comment-form" name="komentari" method="POST" action="/hvala-na-komentaru/" data-netlify="true" netlify-honeypot="web-stranica">
<input type="hidden" name="form-name" value="komentari"><input type="hidden" name="clanak" value="{T('', 'EN ')}{a['slug']}">
<p class="hp" hidden><label>{T('Ne ispunjavaj', 'Leave empty')}: <input name="web-stranica"></label></p>
<div class="comment-form__row"><label>{T('Ime ili nadimak', 'Name or nickname')}<input name="ime" required maxlength="60" autocomplete="nickname"></label>
<label>E-mail <span>({T('ne objavljuje se', 'not published')})</span><input type="email" name="email" maxlength="120" autocomplete="email"></label></div>
<label>{T('Komentar', 'Comment')}<textarea name="komentar" required rows="5" maxlength="3000"></textarea></label>
<p class="comment-form__note">{T('Komentari se objavljuju nakon odobrenja. Slanjem prihvaćaš <a href="/politika-privatnosti/">politiku privatnosti</a>.', 'Comments are published after approval. By sending you accept the <a href="/politika-privatnosti/">privacy policy</a>.')}</p>
<button class="btn" type="submit">{T('Pošalji komentar', 'Post comment')}</button></form></section>"""


def page_article(a):
    path = f"/clanci/{a['slug']}/"
    c = CAT[a["categories"][0]]
    cr, cr_ld = crumbs([("/", T("Naslovnica", "Home")), (f"/kategorije/{c['slug']}/", c["name"]), (None, a["h1"])])
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a["body"])
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads)
    body = re.sub(r"<!--IMG:([\w-]+)\|([^|]*)\|([^>]*)-->", lambda m: f'<figure class="inline-fig{" inline-fig--sm" if m.group(1).startswith("foto-spf-") else ""}">{picture(m.group(1), m.group(2), 1200, 900 if m.group(1).startswith("foto-spf-") else 750)}<figcaption>{m.group(3)}</figcaption></figure>', a["body"])
    body = body.replace("<!--AD-->", ad_slot())
    ld = [cr_ld, {
        "@type": "BlogPosting", "headline": a["title"], "description": a["description"], "inLanguage": lang_tag(),
        "datePublished": a["date"], "dateModified": a.get("updated", a["date"]),
        "mainEntityOfPage": BASE + path, "image": BASE + (f"/slike/{a['slug']}.jpg" if has_image(a["slug"]) else "/brand/og-image.png"),
        "author": person(), "publisher": {"@id": BASE + "/#org"},
        "articleSection": [CAT[s]["name"] for s in a["categories"]],
        "wordCount": len(re.sub(r"<[^>]+>", " ", a["body"]).split())}]
    if a.get("itemlist"):
        ld.append({"@type": "ItemList", "name": a["h1"], "itemListOrder": "https://schema.org/ItemListOrderAscending",
                   "numberOfItems": len(a["itemlist"]),
                   "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(a["itemlist"])]})
    r = a.get("review")
    if r:
        img = BASE + f"/slike/{a['slug']}.jpg"
        ld.append({"@type": "Review", "name": a["title"], "author": person(), "datePublished": a["date"], "inLanguage": lang_tag(),
                   "publisher": {"@id": BASE + "/#org"}, "url": BASE + path,
                   "itemReviewed": {"@type": "Product", "name": r["product"], "image": img, "brand": {"@type": "Brand", "name": r["brand"]}},
                   "reviewRating": {"@type": "Rating", "ratingValue": r["rating"], "bestRating": 5, "worstRating": 1},
                   "positiveNotes": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x} for i, x in enumerate(r["pros"])]},
                   "negativeNotes": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x} for i, x in enumerate(r["cons"])]}})
        toc += f'<li><a href="#top-i-flop">{T("Top i flop", "Tops and flops")}</a></li><li><a href="#ocjena">{T("Ocjena", "Rating")}</a></li>'
    if a.get("faq"):
        ld.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]})
        toc += f'<li><a href="#cesta-pitanja">{T("Česta pitanja", "FAQ")}</a></li>'
    faq = (f'<section class="faq" aria-labelledby="cesta-pitanja"><h2 id="cesta-pitanja">{T("Česta pitanja", "Frequently asked questions")}</h2>'
           + "".join(f"<h3>{e(q)}</h3><p>{e(ans)}</p>" for q, ans in a["faq"]) + "</section>") if a.get("faq") else ""
    related = sorted((x for x in ARTICLES if x is not a), key=lambda x: -len(set(x["categories"]) & set(a["categories"])))[:2]
    upd = f'<span>{T("Ažurirano", "Updated")} <time datetime="{a["updated"]}">{hr_date(a["updated"])}</time></span>' if a.get("updated") and a["updated"] != a["date"] else ""
    return head(a["title"], a["description"], path, "article", ld, image=f"/slike/{a['slug']}.jpg" if has_image(a["slug"]) else None) + header(None) + f"""
{cr}
<article class="wrap read">
<header class="article-head">
<p class="eyebrow">{e(a['kicker'])}</p>
<h1>{e(a['h1'])}</h1>
<div class="byline"><span>{T('Piše', 'By')} <a href="/o-meni/">{e(CFG['author'])}</a></span><time datetime="{a['date']}">{hr_date(a['date'])}</time>{upd}<span>{reading_time(a['body'])} {T('min čitanja', 'min read')}</span></div>
<div class="tags">{''.join(f'<a class="tag" href="/kategorije/{s}/"><span class="dot hue-{CAT[s]["hue"]}"></span>{e(CAT[s]["name"])}</a>' for s in a['categories'])}</div>
<p class="verdict">{mark()}{e(a['verdict'])}</p>
</header>
{('<figure class="cover">' + picture(a["slug"], a.get("review", {}).get("product", a["h1"]), 1200, 900 if a.get("review") else 750, eager=True) + (f'<figcaption>{T("Ilustracija proizvoda, nije originalno pakiranje.", "Product illustration, not the original packaging.")}</figcaption>' if a.get("review") else '') + '</figure>') if has_image(a["slug"]) else ''}
<details class="toc" open><summary>{T('Sadržaj', 'Contents')}</summary><ul>{toc}</ul></details>
<div class="prose">{body}{review_block(a["review"]) if a.get("review") else ""}{faq}</div>
{ad_slot()}
{comments_block(a)}
{brand_chips(a)}
<aside class="author">{mark()}<div><strong>{e(CFG['author'])}</strong><p>{e(CFG['author_bio'])}</p></div></aside>
<p class="disclosure">{T('Proizvode sam kupila sama ili ih dobila na dar, a mišljenje je uvijek moje. Tekst opisuje osobno iskustvo i ne zamjenjuje savjet dermatologa.', 'I bought these products myself or received them as gifts, and the opinion is always my own. This text describes personal experience and does not replace advice from a dermatologist.')}</p>
</article>
<section class="section"><div class="wrap read"><div class="section__head"><h2>{T('Pročitaj i ovo', 'Read next')}</h2></div>
<div class="posts">{''.join(post_row(x) for x in related)}</div></div></section>
""" + footer()


def page_category(c):
    path = f"/kategorije/{c['slug']}/"
    arts = [a for a in ARTICLES if c["slug"] in a["categories"]]
    cr, cr_ld = crumbs([("/", T("Naslovnica", "Home")), (None, c["name"])])
    ld = [cr_ld, {"@type": "CollectionPage", "name": c["title"], "url": BASE + path, "description": c["description"],
                  "inLanguage": lang_tag(), "hasPart": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{BASE}/clanci/{a['slug']}/"} for a in arts]}]
    return head(c["title"], c["description"], path, extra_ld=ld) + header(path) + f"""
{cr}
<div class="wrap read">
<header class="page-head"><p class="eyebrow"><span class="dot hue-{c['hue']}"></span> {T('Kategorija', 'Category')}</p><h1>{e(c['name'])}</h1></header>
<div class="page-intro prose">{c['intro']}</div>
</div>
<section class="section"><div class="wrap read"><div class="section__head"><h2>{T('Recenzije i liste', 'Reviews and lists')}</h2></div>
<div class="posts">{''.join(post_row(a) for a in arts)}</div></div></section>
""" + footer()


def page_simple(slug, title, desc, h1, body, noindex=False):
    path = f"/{slug}/"
    cr, cr_ld = crumbs([("/", T("Naslovnica", "Home")), (None, h1)])
    return head(title, desc, path, extra_ld=[cr_ld], noindex=noindex) + header(path) + f"""
{cr}<div class="wrap read"><header class="page-head"><h1>{e(h1)}</h1></header><div class="prose">{body}</div></div>
""" + footer()


def about_hr():
    return f"""<figure class="inline-fig">{picture("foto-polica", "Kozmetika na svijetloplavoj podlozi: krema, serum, tonik, SPF i ruž", 1200, 750)}</figure>
<p class="lead">Bok, ja sam {e(CFG['author'])}. Imam osjetljivu, reaktivnu kožu s rozaceom i ten svijetao kao sir, kako to volim reći.</p>
<p>Godinama tražim kozmetiku koja moju kožu neće razljutiti. Usput sam potrošila previše novca na proizvode koji se “preporučuju za osjetljivu kožu”, a meni su izazvali crvenilo, peckanje ili ljuštenje. {e(CFG['site_name'])} je nastao da drugima taj put bude kraći, i da o svakom proizvodu, od Rhode do Chanela, dobijete iskreno mišljenje na hrvatskom.</p>
<h2 id="kako">Kako pišem recenzije</h2>
<ul><li>Pišem samo o proizvodima koje sam stvarno koristila, i to dovoljno dugo da znam kako se ponašaju.</li>
<li>Uz svaki proizvod navodim što brend tvrdi, a što sam iskusila.</li>
<li>Pišem i o promašajima, jer iz njih se najviše nauči.</li>
<li>Ne primam novac za recenzije. Portal se financira oglasima (Google AdSense).</li></ul>
<h2 id="napomena">Važna napomena</h2>
<p>Nisam liječnica ni dermatologinja. Sadržaj na portalu temelji se na osobnom iskustvu i informativne je naravi. Za dijagnozu i liječenje rozacee ili bilo kojeg stanja kože obratite se dermatologu.</p>"""

def contact_hr():
    return f"""<p>Imate pitanje, prijedlog proizvoda za recenziju ili ispravak? Pišite mi na <strong>{e(CFG['contact_email'])}</strong>.</p>
<p>Brendovi i PR agencije su dobrodošli poslati proizvod na testiranje, uz napomenu da ne jamčim objavu ni pozitivnu recenziju.</p>"""

def privacy_hr():
    return f"""<p class="lead">Ova stranica objašnjava koje podatke {e(CFG['site_name'])} prikuplja i zašto, u skladu s Općom uredbom o zaštiti podataka (GDPR).</p>
<h2 id="voditelj">Voditelj obrade</h2><p>{e(CFG['author'])}, {e(CFG['site_name'])}. Kontakt: {e(CFG['contact_email'])}.</p>
<h2 id="google-analytics">Analitika (Google Analytics)</h2><p>Koristimo i Google Analytics 4 s Googleovim načinom pristanka (Consent Mode). Bez vašeg pristanka Google Analytics ne sprema kolačiće, a Googleu se šalju samo anonimni signali bez identifikatora. Ako pristanete, sprema kolačiće _ga kojima mjerimo posjećenost.</p>
<h2 id="analitika">Analitika (PostHog)</h2><p>Za mjerenje posjećenosti koristimo PostHog s poslužiteljima u Europskoj uniji. Bez vašeg pristanka analitika radi bez kolačića i ne pamti vas između posjeta. Ako pristanete, PostHog sprema anonimni identifikator u kolačić i lokalnu pohranu preglednika kako bismo razumjeli koji su članci korisni.</p>
<h2 id="oglasi">Oglasi (Google AdSense)</h2><p>Portal prikazuje oglase putem usluge Google AdSense. Google i njegovi partneri mogu koristiti kolačiće za prikaz oglasa na temelju vaših prethodnih posjeta ovoj i drugim stranicama. Za posjetitelje iz EU pristanak za oglase prikuplja se putem Googleove platforme za upravljanje pristankom. Personalizirane oglase možete isključiti u <a href="https://adssettings.google.com" rel="nofollow noopener">Googleovim postavkama oglasa</a>. Više o tome kako Google koristi podatke: <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2 id="kolacici">Kolačići i lokalna pohrana</h2><ul>
<li><strong>mk-consent</strong> (lokalna pohrana, nužno): pamti vaš izbor o kolačićima.</li>
<li><strong>nf_lang</strong> (kolačić, nužno): pamti jeste li odabrali hrvatsku ili englesku verziju.</li>
<li><strong>ph_*</strong> (PostHog, analitika): samo uz pristanak.</li>
<li><strong>_ga, _ga_*</strong> (Google Analytics, analitika): samo uz pristanak.</li>
<li><strong>Google AdSense kolačići</strong> (oglašavanje): prema postavkama pristanka.</li></ul>
<p>Svoj izbor možete promijeniti bilo kad putem poveznice “Postavke kolačića” na dnu stranice.</p>
<h2 id="prava">Vaša prava</h2><p>Imate pravo na pristup, ispravak i brisanje podataka te pravo na prigovor Agenciji za zaštitu osobnih podataka (azop.hr).</p>
<p><em>Zadnja izmjena: {hr_date(date.today().isoformat())}</em></p>"""


def about_en():
    return f"""<figure class="inline-fig">{picture("foto-polica", "Beauty products on a light blue background: cream, serum, toner, SPF and lipstick", 1200, 750)}</figure>
<p class="lead">Hi, I'm {e(CFG['author'])}. I have sensitive, reactive skin with rosacea and a complexion as pale as cheese, as I like to say.</p>
<p>For years I've been looking for skincare that won't upset my skin. Along the way I've spent far too much money on products “recommended for sensitive skin” that gave me redness, stinging or peeling. {e(CFG['site_name'])} exists to make that road shorter for others, and to give you an honest opinion on every product, from Rhode to Chanel. I'm from Croatia and write in Croatian and English.</p>
<h2 id="how">How I write reviews</h2>
<ul><li>I only write about products I've actually used, and long enough to know how they behave.</li>
<li>For every product I list what the brand claims and what I experienced.</li>
<li>I write about flops too, because that's where you learn the most.</li>
<li>I don't accept money for reviews. The site is funded by ads (Google AdSense).</li></ul>
<h2 id="note">Important note</h2>
<p>I'm not a doctor or a dermatologist. The content on this site is based on personal experience and is for information only. For diagnosis and treatment of rosacea or any skin condition, see a dermatologist.</p>"""


def contact_en():
    return f"""<p>Got a question, a product suggestion for a review or a correction? Email me at <strong>{e(CFG['contact_email'])}</strong>. You can write in English or Croatian.</p>
<p>Brands and PR agencies are welcome to send products for testing, with the note that I don't guarantee publication or a positive review.</p>"""


def privacy_en():
    return f"""<p class="lead">This page explains what data {e(CFG['site_name'])} collects and why, in line with the General Data Protection Regulation (GDPR).</p>
<h2 id="controller">Data controller</h2><p>{e(CFG['author'])}, {e(CFG['site_name'])}. Contact: {e(CFG['contact_email'])}.</p>
<h2 id="google-analytics">Analytics (Google Analytics)</h2><p>We use Google Analytics 4 with Google Consent Mode. Without your consent Google Analytics stores no cookies and only anonymous signals without identifiers are sent to Google. If you consent, it stores _ga cookies that we use to measure visits.</p>
<h2 id="analytics">Analytics (PostHog)</h2><p>We use PostHog with servers in the European Union to measure visits. Without your consent, analytics runs without cookies and doesn't remember you between visits. If you consent, PostHog stores an anonymous identifier in a cookie and in your browser's local storage so we can understand which articles are useful.</p>
<h2 id="ads">Ads (Google AdSense)</h2><p>The site shows ads through Google AdSense. Google and its partners may use cookies to show ads based on your previous visits to this and other websites. For visitors from the EU, consent for ads is collected through Google's consent management platform. You can turn off personalised ads in <a href="https://adssettings.google.com" rel="nofollow noopener">Google's ad settings</a>. More on how Google uses data: <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2 id="cookies">Cookies and local storage</h2><ul>
<li><strong>mk-consent</strong> (local storage, essential): remembers your cookie choice.</li>
<li><strong>nf_lang</strong> (cookie, essential): remembers whether you chose the Croatian or English version.</li>
<li><strong>ph_*</strong> (PostHog, analytics): only with consent.</li>
<li><strong>_ga, _ga_*</strong> (Google Analytics, analytics): only with consent.</li>
<li><strong>Google AdSense cookies</strong> (advertising): according to your consent settings.</li></ul>
<p>You can change your choice at any time via the “Cookie settings” link at the bottom of the page.</p>
<h2 id="rights">Your rights</h2><p>You have the right to access, correct and delete your data, and the right to lodge a complaint with the Croatian Personal Data Protection Agency (azop.hr) or the data protection authority in your country.</p>
<p><em>Last updated: {hr_date(date.today().isoformat())}</em></p>"""


def page_404():
    return head(T("Stranica nije pronađena", "Page not found"), T("Tražena stranica ne postoji.", "The page you are looking for does not exist."), "/404.html", noindex=True) + header(None) + f"""
<div class="wrap read"><header class="page-head"><h1>{T('Ova stranica ne postoji', 'This page does not exist')}</h1></header>
<div class="prose"><p>{T('Možda je premještena. Vratite se na <a href="/">naslovnicu</a> ili odaberite kategoriju u izborniku.', 'It may have moved. Go back to the <a href="/">home page</a> or pick a category from the menu.')}</p></div></div>
""" + footer()


# ---------- pomoćne datoteke ----------

def sitemap():
    urls = [("/", max(x.get("updated", x["date"]) for x in ARTICLES), "1.0")]
    urls += [(f"/kategorije/{c['slug']}/", max(a.get("updated", a["date"]) for a in ARTICLES if c["slug"] in a["categories"]), "0.8") for c in CATEGORIES]
    urls += [(f"/clanci/{a['slug']}/", a.get("updated", a["date"]), "0.9") for a in ARTICLES]
    urls += [("/brendovi/", date.today().isoformat(), "0.7")]
    urls += [(f"/brendovi/{x['slug']}/", max(a.get("updated", a["date"]) for a in x["articles"]), "0.6") for x in BRANDS if x["articles"]]
    urls += [("/o-meni/", date.today().isoformat(), "0.4"), ("/kontakt/", date.today().isoformat(), "0.3"),
             ("/politika-privatnosti/", date.today().isoformat(), "0.2")]
    def alts(p):
        return (f'<xhtml:link rel="alternate" hreflang="hr" href="{BASE}{p}"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}{en_path(p)}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{p}"/>')
    rows = "".join(f"<url><loc>{BASE}{loc}</loc><lastmod>{d}</lastmod><priority>{pr}</priority>{alts(p)}</url>\n"
                   for p, d, pr in urls for loc in (p, en_path(p)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            f'{rows}</urlset>\n')


def rss():
    items = "".join(f"<item><title>{e(a['title'])}</title><link>{BASE}{U('/clanci/' + a['slug'] + '/')}</link><guid>{BASE}{U('/clanci/' + a['slug'] + '/')}</guid>"
                    f"<pubDate>{date.fromisoformat(a['date']).strftime('%a, %d %b %Y')} 08:00:00 +0000</pubDate><description>{e(a['excerpt'])}</description></item>"
                    for a in ARTICLES)
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{e(CFG["site_name"])}</title>'
            f'<link>{BASE}{U("/")}</link><description>{e(CFG["tagline"])}</description><language>{T("hr", "en-gb")}</language>{items}</channel></rss>')


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


# ---------- engleska verzija ----------
# Hrvatski je na korijenu, engleski pod /en/ s engleskim slugovima. Kod stranica radi s hrvatskim putanjama,
# a write() ih u engleskoj verziji prepisuje (en_path) i dodaje hreflang poveznice.

EN_SECTION = {"clanci": "articles", "kategorije": "categories", "brendovi": "brands", "o-meni": "about",
              "kontakt": "contact", "politika-privatnosti": "privacy", "hvala-na-komentaru": "thank-you"}
EN_SLUG = {k: v["slug"] for k, v in content_en.ARTICLES_EN.items()}
EN_SLUG.update({k: v["slug"] for k, v in content_en.CATEGORIES_EN.items()})
HR_PATH_RE = re.compile(r"(?<![\w/.-])(" + re.escape(BASE) + r")?(/(?:" + "|".join(map(re.escape, EN_SECTION)) + r")/(?:[a-z0-9-]+/)?)")


def en_path(p):
    if p == "/":
        return "/en/"
    m = re.fullmatch(r"/([a-z-]+)/(?:([a-z0-9-]+)/)?", p)
    if m and m.group(1) in EN_SECTION:
        sec, slug = m.groups()
        return f"/en/{EN_SECTION[sec]}/" + (f"{EN_SLUG.get(slug, slug)}/" if slug else "")
    return "/en" + p


def U(p):
    return en_path(p) if LANG == "en" else p


def to_en(doc):
    doc = HR_PATH_RE.sub(lambda m: (m.group(1) or "") + en_path(m.group(2)), doc)
    doc = doc.replace('href="/"', 'href="/en/"').replace(f'"{BASE}/"', f'"{BASE}/en/"')
    return doc


def lang_links(path):
    if path.endswith(".html") and path != "/":
        return "", ""
    hr, en = path, en_path(path)
    alt = (f'<link rel="alternate" hreflang="hr" href="{BASE}{hr}"><link rel="alternate" hreflang="en" href="{BASE}{en}">'
           f'<link rel="alternate" hreflang="x-default" href="{BASE}{hr}">')
    # nf_lang kolačić: Netlify ga poštuje umjesto jezika preglednika, pa ručni izbor jezika ostaje zapamćen.
    js = "try{document.cookie='nf_lang=%s;path=/;max-age=31536000;samesite=lax'}catch(_){}"
    sw = (f'<a class="lang" href="{hr}" hreflang="hr" lang="hr" onclick="{js % "hr"}">HR</a>' if LANG == "en" else
          f'<a class="lang" href="{en}" hreflang="en" lang="en" onclick="{js % "en"}">EN</a>')
    return alt, sw


def write(path, doc):
    hr_path = path
    if LANG == "en":
        doc = to_en(doc)
        path = en_path(path)
    if path.endswith(".html") or path.endswith("/"):
        alt, sw = lang_links(hr_path)
        doc = doc.replace("<!--ALT-->", alt, 1).replace("<!--LANGSW-->", sw, 1)
    fs = os.path.join(OUT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(fs), exist_ok=True)
    if PREVIEW and fs.endswith(".html"):
        doc = relativize(doc, path if path.endswith("/") else os.path.dirname(path) + "/")
    open(fs, "w", encoding="utf-8").write(doc)


def write_pages():
    write("/", page_home())
    for a in ARTICLES:
        write(f"/clanci/{a['slug']}/", page_article(a))
    for c in CATEGORIES:
        write(f"/kategorije/{c['slug']}/", page_category(c))
    write("/brendovi/", page_brands())
    for x in BRANDS:
        write(f"/brendovi/{x['slug']}/", page_brand(x))
    write("/o-meni/", page_simple("o-meni", T("O meni", "About me"),
                                  T(f"Tko piše {CFG['site_name']} i kako nastaju recenzije kozmetike za osjetljivu kožu i rozaceu.",
                                    f"Who writes {CFG['site_name']} and how the beauty reviews for sensitive skin and rosacea are made."),
                                  T("O meni", "About me"), T(about_hr(), about_en())))
    write("/hvala-na-komentaru/", page_simple("hvala-na-komentaru", T("Hvala na komentaru", "Thanks for your comment"),
                                              T("Komentar je poslan i objavit će se nakon odobrenja.", "Your comment has been sent and will be published after approval."),
                                              T("Hvala na komentaru!", "Thanks for your comment!"),
                                              T('<p>Tvoj komentar je stigao i objavit ću ga čim ga pročitam. Hvala što dijeliš svoje iskustvo!</p><p><a class="btn" href="/">Natrag na naslovnicu</a></p>',
                                                '<p>Your comment has arrived and I\'ll publish it as soon as I\'ve read it. Thanks for sharing your experience!</p><p><a class="btn" href="/">Back to the home page</a></p>'),
                                              noindex=True))
    write("/kontakt/", page_simple("kontakt", T("Kontakt", "Contact"), T("Kontakt za pitanja, prijedloge i suradnje.", "Contact for questions, suggestions and collaborations."),
                                   T("Kontakt", "Contact"), T(contact_hr(), contact_en())))
    write("/politika-privatnosti/", page_simple("politika-privatnosti", T("Politika privatnosti i kolačića", "Privacy and cookie policy"),
                                                T(f"Kako {CFG['site_name']} koristi kolačiće, Google Analytics, PostHog analitiku i Google AdSense oglase.",
                                                  f"How {CFG['site_name']} uses cookies, Google Analytics, PostHog analytics and Google AdSense ads."),
                                                T("Privatnost i kolačići", "Privacy and cookies"), T(privacy_hr(), privacy_en())))
    write("/404.html", page_404())
    write("/rss.xml", rss())
    write("/llms.txt", llms_txt())
    write("/llms-full.txt", llms_txt(full=True))


def switch_to_en():
    """Zamijeni sadržaj engleskim prijevodima (content_en.py); slugovi ostaju hrvatski, mijenjaju se tek u URL-u."""
    global LANG, ARTICLES, CATEGORIES, CAT
    LANG = "en"
    CFG.update(content_en.SITE_EN)
    by_slug = {}
    for a in ARTICLES:
        tr = dict(content_en.ARTICLES_EN[a["slug"]])
        tr.pop("slug")
        if a.get("review"):
            tr["review"] = {**a["review"], **tr.get("review", {})}
        by_slug[a["slug"]] = {**a, **tr}
    ARTICLES = [by_slug[a["slug"]] for a in ARTICLES]
    CATEGORIES = [{**c, **{k: v for k, v in content_en.CATEGORIES_EN[c["slug"]].items() if k != "slug"}} for c in CATEGORIES]
    CAT = {c["slug"]: c for c in CATEGORIES}
    for b in BRANDS:
        b["articles"] = [by_slug[a["slug"]] for a in b["articles"]]


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    write("/sitemap.xml", sitemap())
    write("/robots.txt", "".join(f"User-agent: {bot}\nAllow: /\n\n" for bot in AI_BOTS) + f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    if CFG["adsense_client"]:
        write("/ads.txt", f"google.com, {CFG['adsense_client'].replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    write("/site.webmanifest", json.dumps({"name": CFG["site_name"], "short_name": CFG["site_name"], "lang": "hr",
                                           "icons": [{"src": "/brand/logo-192.png", "sizes": "192x192", "type": "image/png"},
                                                     {"src": "/brand/logo-512.png", "sizes": "512x512", "type": "image/png"}],
                                           "theme_color": "#f4a7bb", "background_color": "#fffbf7", "display": "standalone"}, ensure_ascii=False))
    write_pages()
    switch_to_en()
    write_pages()
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
