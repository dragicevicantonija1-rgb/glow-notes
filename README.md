# Glow Notes – beauty portal

Statična web stranica (čisti HTML, bez baze i bez WordPressa): brza, sigurna i besplatna za hosting.

## Struktura

| Datoteka / mapa | Što je |
|---|---|
| `config.json` | Ime, domena, autorica, e-mail i **svi ključevi** (PostHog, Search Console, AdSense) |
| `content.py` | Kategorije i članci. Novi članak = novi blok u `ARTICLES` |
| `assets/site.css` | Izgled stranice (boje, fontovi) |
| `assets/brand/` | Logo (SVG, PNG), slika za dijeljenje, stranica vizualnog identiteta |
| `assets/slike/` | Ilustracije za naslovnicu i članke (`make_images.py`). Slika se automatski prikazuje ako se zove kao članak, npr. `mineralni-spf-recenzije-poredak.jpg` |
| Brendovi | Popis u `content.py` (`BRANDS`). Stranica brenda sama skuplja članke u kojima se brend spominje; brend bez članaka ima `noindex` dok ne dobije recenziju |
| `build.py` | Generira gotovu stranicu u mapu `dist/` |
| `dist/` | **Gotova stranica za objavu** |

Pokretanje: `python3 build.py` (treba samo Python 3, bez dodatnih paketa).

## Prije objave: što treba upisati u `config.json`

1. **Domena** – `base_url`, sada `https://glownotes.eu` (kupuje se na Porkbunu, nameserveri na Netlify).
2. **E-mail** – `contact_email` (sad je privremeno `info@glownotes.eu`, sandučić tek treba otvoriti).
3. **PostHog** – na eu.posthog.com napraviti projekt (EU poslužitelji, zbog GDPR-a), kopirati *Project API key* (`phc_...`) u `posthog_key`.
4. **Google Search Console** – dodati svojstvo, odabrati *HTML tag*, kopirati samo vrijednost `content="..."` u `google_site_verification`. (Još bolje: verifikacija preko DNS-a za cijelu domenu.) Nakon verifikacije poslati `https://DOMENA/sitemap.xml`.
5. **AdSense** – nakon prijave upisati `ca-pub-...` u `adsense_client`; nakon odobrenja napraviti *In-article* oglasnu jedinicu i njen broj upisati u `adsense_slot_in_article`. `ads.txt` se generira sam. U AdSenseu uključiti **Privacy & messaging → GDPR poruku** (Googleov certificirani CMP, obavezan za EU).
6. Postaviti `show_ad_placeholders` na `false` (makne isprekidane okvire "Mjesto za AdSense oglas").
7. Ponovno pokrenuti `python3 build.py` i objaviti mapu `dist/`.

## Hosting: GitHub + Netlify (automatska objava)

1. Kod je u GitHub repozitoriju. `netlify.toml` već kaže Netlifyju što da radi (`python3 build.py`, objavljuje mapu `dist/`).
2. Na app.netlify.com: **Add new site → Import an existing project → GitHub** → odabrati repozitorij → **Deploy**. Postavke builda se same učitaju iz `netlify.toml`.
3. U Netlifyju: **Domain management → Add a domain** i upisati svoju domenu; HTTPS se uključi sam.
4. Od tada svaka promjena na GitHubu (novi članak, ključ u `config.json`) automatski se objavi za minutu-dvije.

## SEO koji je već ugrađen

- jedinstveni `title`, `meta description` i `canonical` na svakoj stranici, `lang="hr"`
- schema.org: Organization, WebSite, BlogPosting (autorica, datumi), BreadcrumbList, ItemList (poredak proizvoda), CollectionPage
- Open Graph i Twitter kartice sa slikom za dijeljenje (1200×630)
- `sitemap.xml`, `robots.txt`, RSS (`rss.xml`), `site.webmanifest`, favicon u svim veličinama
- čisti URL-ovi (`/clanci/mineralni-spf-recenzije-poredak/`), sadržaj članka s sidrima, interne poveznice među člancima
- fontovi s vlastite domene (brže i GDPR), CSS ugrađen u stranicu, bez teških skripti
- tamni način rada, prilagodba mobitelu, pristupačnost (preskoči na sadržaj, fokus)

## Napomena o AdSense odobrenju

Google obično traži više originalnog sadržaja prije odobrenja: realno 15–25 kvalitetnih članaka, plus stranice O meni, Kontakt i Politika privatnosti (već postoje).

## SEO za ChatGPT, Perplexity, Gemini i Claude
- `robots.txt` izričito dopušta AI tražilicama (OAI-SearchBot, ChatGPT-User, GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot i dr.) čitanje stranice.
- `/llms.txt` je kratki vodič kroz portal za AI modele, a `/llms-full.txt` sadrži sve članke kao čisti tekst. Oba se generiraju sama pri svakom buildu.
- Svaki članak ima sekciju **Česta pitanja** s FAQPage shemom: kratki, izravni odgovori koje AI asistenti najlakše citiraju. Novi članak dobiva je kroz polje `"faq"` u `content.py`.
- Autorica ima Person shemu (opis i teme), pa AI zna tko stoji iza recenzija.
- **Bing Webmaster Tools** (bing.com/webmasters): ChatGPT pretraživanje se oslanja na Bingov indeks. Dodaj stranicu, upiši kod u `bing_site_verification` u `config.json` i pošalji `sitemap.xml`. Najbrže je uvesti stranicu izravno iz Google Search Consolea.

## Google Analytics 4
1. Na analytics.google.com: **Admin → Create → Property** (vremenska zona Hrvatska, valuta EUR) → **Web stream** s adresom stranice.
2. Kopiraj **Measurement ID** (oblik `G-XXXXXXXXXX`) i upiši ga u `ga4_id` u `config.json` (ili ga pošalji Claudeu).
3. GA se učitava s Googleovim Consent Modeom: bez pristanka nema kolačića, nakon klika "Prihvaćam" mjeri normalno.

### Dnevni izvještaj u 8:00 na e-mail
U GA4: **Reports → Reports snapshot** (ili Realtime/Acquisition) → ikona **Share this report → Schedule email** → Frequency: **Daily**, vrijeme 8:00, primatelj tvoj e-mail.

## Komentari
- Svaki članak ima obrazac za komentare (Netlify Forms, obrazac "komentari"). Netlify ga prepozna sam nakon prvog deploya.
- U Netlifyju: **Site configuration → Forms → Form notifications → Add notification → Email** da ti svaki novi komentar stigne na mail.
- Komentari se ne objavljuju automatski (zaštita od spama). Odobrene upiši u `komentari.py` (ili ih pošalji Claudeu) i objave se na članku, s mogućnošću tvog odgovora.

## Engleska verzija (EN)

- Hrvatska verzija je na `glownotes.eu/`, engleska na `glownotes.eu/en/` s engleskim adresama (npr. `/en/articles/babe-mineral-spf-50-review/`).
- Prijevodi su u `content_en.py` (ključ je hrvatski slug). **Novi članak = dodaj ga i u `content_en.py`**, inače build javlja grešku.
- Svaka stranica ima hreflang poveznice (hr, en, x-default) i sitemap s obje verzije, pa Google zna koju verziju pokazati kome.
- Gumb HR/EN u izborniku vodi na isti članak na drugom jeziku i pamti izbor (kolačić `nf_lang`).
- Automatski jezik (u `netlify.toml`): posjetitelji iz Hrvatske, BiH, Srbije i Crne Gore ostaju na hrvatskom; ostali s engleskim ili drugim europskim jezikom preglednika idu na `/en/`.
- Engleski komentari stižu u isti Netlify obrazac "komentari", a polje "clanak" počinje s `EN `.

## Pravilo rada

Promjene ostaju lokalno i u pregledu. Na GitHub (i time na Netlify) idu tek kad Antonija kaže da ide live.
