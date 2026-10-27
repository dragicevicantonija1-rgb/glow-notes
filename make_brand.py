# Stranica vizualnog identiteta (assets/brand/identitet.html), generira se iz logotipa.
import json
NAME = json.load(open("config.json", encoding="utf-8"))["site_name"]


def svg(f):
    return open(f"assets/brand/{f}").read().replace("<svg ", f'<svg role="img" aria-label="{NAME}" ', 1)


SW = [("Bordo", "#7A1730", "Logo, naslovi, gumbi, podnožje"), ("Toplo bijela", "#FFFBF7", "Pozadina"),
      ("Roza", "#F4A7BB", "Značka, prugice, karo uzorak"), ("Ruž", "#E8688C", "Naglašene riječi, oznake"),
      ("Blijedo roza", "#FDE6EC", "Plohe, kutija s autoricom"), ("Trešnja", "#D7263D", "Iskra u znaku, promašaji"),
      ("Nebo", "#C4E0F4", "Osjetljiva koža, blok Kako recenziram"), ("Vanilija", "#FBE7A6", "SPF, naljepnice"), ("Pistacija", "#D7EFE2", "Njega lica")]
sws = "".join(f'<li><span class="sw" style="background:{h}"></span><strong>{n}</strong><code>{h}</code><small>{u}</small></li>' for n, h, u in SW)
CATS = [("Njega lica", "#D7EFE2"), ("Šminka", "#FBD0DC"), ("SPF zaštita", "#FBE7A6"), ("Koža 30+", "#FDE0CC"),
        ("Osjetljiva koža", "#C4E0F4"), ("Rozacea", "#F8C3C8"), ("Reaktivna koža", "#FFD9C2")]
cats = "".join(f'<span class="chip" style="background:{c}">{n}</span>' for n, c in CATS)

page = f'''<!doctype html>
<html lang="hr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{NAME} identitet</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&family=Instrument+Sans:wght@400..700&display=swap">
<style>
:root{{--paper:#fffbf7;--card:#fde6ec;--ink:#7a1730;--soft:#6e4a53;--line:#f2d3db;--tomato:#e8688c;--cobalt:#2f5bea;--sun:#fbe7a6;
--display:"Fraunces","Cooper Black",Georgia,serif;--body:"Instrument Sans",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--paper:#171310;--card:#1e1915;--ink:#fbf7ef;--soft:#cfc4b8;--line:#fbf7ef;--cobalt:#8fb0ff;--tomato:#ff7a63;color-scheme:dark}}}}
:root[data-theme="dark"]{{--paper:#171310;--card:#1e1915;--ink:#fbf7ef;--soft:#cfc4b8;--line:#fbf7ef;--cobalt:#8fb0ff;--tomato:#ff7a63;color-scheme:dark}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font:400 1.075rem/1.65 var(--body)}}
.w{{max-width:1080px;margin:auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:48px}}
h1,h2{{font-family:var(--display);font-weight:900;font-variation-settings:"SOFT" 100;letter-spacing:-.01em;line-height:1.05;text-wrap:balance;margin:0}} h1{{font-size:clamp(2.1rem,5vw,3.8rem)}} h1 em{{font-style:italic;font-weight:800;color:var(--tomato)}}
h2{{font-size:1.6rem;margin:64px 0 18px}}
.lead{{font-size:1.25rem;color:var(--soft);max-width:60ch}} .eb{{font:700 .78rem/1 var(--body);letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}}
.tile{{border:1px solid #f2d3db;border-radius:24px;padding:28px;display:grid;place-items:center;min-height:200px;background:#fffbf7}}
.tile.dk{{background:#7a1730;border-color:#7a1730}} .tile.sun{{background:#ffd84d}} .tile svg{{width:100%;height:auto;max-height:130px}}
.cap{{font-size:.88rem;color:var(--soft);margin-top:10px}}
.story{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:32px;align-items:center}}
.eq{{display:flex;align-items:center;gap:12px;font-family:var(--display);font-size:1.8rem;flex-wrap:wrap}} .eq span{{width:46px;height:46px;border-radius:50%;display:inline-block}}
ul.sw-list{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:18px}}
ul.sw-list li{{display:flex;flex-direction:column;gap:2px}} .sw{{height:96px;border-radius:20px;border:1px solid #f2d3db;margin-bottom:8px}}
code{{font-size:.85rem;color:var(--soft)}} small{{color:var(--soft);line-height:1.4}}
.type{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:32px}} .spec-d{{font:900 2.8rem/1.05 var(--display);font-variation-settings:"SOFT" 100;margin:8px 0}} .spec-b{{font:600 2.4rem/1.05 var(--body);margin:8px 0}}
.do{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px}} .do>div{{background:var(--card);border:0;border-radius:24px;padding:22px}} .do ul{{padding-left:1.1em;margin:0}} .do h3{{font:900 1.3rem var(--display);margin:0 0 8px}}
.chips{{display:flex;flex-wrap:wrap;gap:10px}} .chip{{color:#7a1730;font-weight:600;border-radius:99px;padding:7px 15px}}
@media (max-width:700px){{.story,.type,.do{{grid-template-columns:minmax(0,1fr)}}}}
</style></head><body><div class="w">
<p class="eb">Vizualni identitet · v4 · retro roza</p>
<h1>{NAME}. Beauty recenzije <em>bez filtera</em>.</h1>
<p class="lead">Iskrene beauty recenzije na hrvatskom, od Rhode i Chanela do ljekarničke kozmetike, sa specijalnošću za osjetljivu kožu, rozaceu i kožu 30+.</p>

<h2>Smjer: retro slastičarnica</h2>
<p>Inspiracija su osobni lifestyle blogovi poput Lily Pebbles: bordo slova, roza tonovi, prugice kao na tendi slastičarnice i karo uzorak kao stolnjak. Puno bijelog prostora i velika, meka serif slova daju toplinu i osobnost, a mali tekst ostaje čist i moderan.</p>

<h2>Ideja znaka</h2>
<div class="story"><div class="tile" style="min-height:260px;background:#fde6ec">{svg("znak.svg")}</div>
<div><div class="eq"><span style="background:#F4A7BB"></span><span style="background:#7A1730"></span><span style="background:#D7263D"></span></div>
<p>Znak je okrugla roza značka s monogramom <strong>GN</strong>, kao naljepnica na retro pakiranju ili pečat na kutiji kolača. Isprekidani krug podsjeća na šav, a crvena iskra je glow. Radi kao favicon, profilna slika na Instagramu i oznaka presude u članku.</p>
<p><strong>{NAME}</strong> zvuči međunarodno i osobno u isto vrijeme: bilješke iz beauty dnevnika, napisane nakon tjedana stvarnog korištenja.</p></div></div>

<h2>Logo</h2>
<div class="grid"><div><div class="tile">{svg("logo.svg")}</div><p class="cap">Osnovni (logo.svg)</p></div>
<div><div class="tile dk">{svg("logo-svijetli.svg")}</div><p class="cap">Na tamnoj podlozi (logo-svijetli.svg)</p></div>
<div><div class="tile" style="background:#fde6ec">{svg("logo-okomiti.svg")}</div><p class="cap">Okomiti, za društvene mreže (logo-okomiti.svg)</p></div></div>
<p class="cap">Slova su pretvorena u krivulje, pa logo izgleda isto i bez instaliranog fonta.</p>

<h2>Boje</h2>
<ul class="sw-list">{sws}</ul>
<p class="cap">Pravilo: bordo i roza nose identitet, pastelne boje označavaju kategorije, a prugice i karo uzorak koriste se kao ukras, nikad ispod dužeg teksta. Stranica ima i tamni način rada.</p>

<h2>Kategorije</h2>
<div class="chips">{cats}</div>

<h2>Tipografija</h2>
<div class="type"><div><p class="eb">Naslovi · Fraunces Black (meki)</p><p class="spec-d">Šminka & <i style="color:var(--tomato)">SPF</i></p><p>Debeli, mekani serif s retro karakterom, u kurzivu za naglaske. Za naslove i logo.</p></div>
<div><p class="eb">Tekst · Instrument Sans</p><p class="spec-b">Đurđica 30+ čita</p><p>Čist, moderan font, odlično čitljiv na mobitelu. Oba fonta imaju sva hrvatska slova i besplatna su; na stranici se poslužuju s vlastite domene radi brzine i GDPR-a.</p></div></div>

<h2>Glas i ton</h2>
<div class="do"><div><h3>Pišemo</h3><ul><li>u prvom licu, kao prijateljica koja je sve već isprobala</li><li>konkretno: što brend tvrdi, a što se stvarno dogodilo</li><li>i o promašajima, s razlogom</li><li>s pitanjem čitateljicama na kraju</li></ul></div>
<div><h3>Ne pišemo</h3><ul><li>medicinske savjete i obećanja izlječenja</li><li>“must have” i “čudotvorno” bez pokrića</li><li>recenzije proizvoda koje nismo koristile</li><li>plaćene ocjene</li></ul></div></div>

<h2>Rezervna imena</h2>
<p>Ako domena nije slobodna: <strong>Blush Report</strong>, <strong>Beauty Verdict</strong>, <strong>Skin Edit</strong>. Znak i boje rade uz svako od njih.</p>
</div></body></html>'''
open("assets/brand/identitet.html", "w").write(page)
print("ok")
