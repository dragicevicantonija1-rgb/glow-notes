# Sadržaj portala: kategorije i članci.
# Novi članak = novi dict u ARTICLES. Tijelo je HTML; <h2 id="..."> naslovi grade sadržaj (TOC).

CATEGORIES = [
    {
        "slug": "njega-lica", "group": "proizvod", "nav": "Njega",
        "name": "Njega lica",
        "short": "Kreme, serumi i umivalice, od ljekarne do luksuza.",
        "title": "Njega lica – recenzije krema, seruma i umivalica",
        "description": "Recenzije njege lica na hrvatskom: kreme, serumi, umivalice i tonici, od ljekarničkih brendova do Rhode, Kiehl's i luksuznih klasika.",
        "intro": """<p>Kreme, serumi, umivalice i tonici koje sam isprobala, od ljekarničkih klasika do hit proizvoda s TikToka i luksuznih brendova. Uz svaki proizvod pišem što brend tvrdi i kako se stvarno ponašao na mojoj koži.</p>""",
        "hue": "mint",
    },
    {
        "slug": "sminka", "group": "proizvod", "nav": "Šminka",
        "name": "Šminka",
        "short": "Tenovi, bronzeri, maskare i obrve koje stvarno nosim.",
        "title": "Šminka – recenzije tena, bronzera i maskara",
        "description": "Recenzije šminke na hrvatskom: CC kreme, bronzeri, maskare i olovke za obrve, od drogerije do Chanela i NARS-a.",
        "intro": """<p>Šminka koju nosim svaki dan i ona koja je razočarala. Posebno pazim na tenove i tonirane proizvode, jer na svijetloj koži sklonoj crvenilu nijansa i formula odlučuju sve.</p>""",
        "hue": "pink",
    },
    {
        "slug": "spf", "group": "proizvod", "nav": "SPF",
        "name": "SPF zaštita",
        "short": "Mineralni i kemijski SPF bez bijelog traga i peckanja.",
        "title": "SPF za lice – recenzije mineralnih i kemijskih krema",
        "description": "Recenzije SPF krema za lice na hrvatskom: mineralni i tonirani SPF za svijetlu i osjetljivu kožu, bez bijelog traga.",
        "intro": """<p>Dobra zaštita od sunca je najvažniji korak njege, ali pronaći SPF koji ne ostavlja bijeli trag, ne peče oči i ne isušuje je izazov. Ovdje skupljam sve što sam isprobala.</p>""",
        "hue": "sun",
    },
    {
        "slug": "koza-30-plus", "group": "koza", "nav": "30+",
        "name": "Koža 30+",
        "short": "Prve bore, gubitak sjaja i njega koja ne iritira.",
        "title": "Njega kože 30+ – recenzije krema i seruma",
        "description": "Iskrene recenzije njege za kožu 30+: kreme protiv bora, kreme oko očiju i serumi testirani na osjetljivoj koži sklonoj crvenilu.",
        "intro": """<p>Nakon tridesete koža se mijenja. Obnavlja se sporije, brže gubi vlagu, a fine linije oko očiju više nisu samo od smijeha. Ako je pritom i osjetljiva, izbor njege postaje pravi mali projekt: puno proizvoda “protiv starenja” sadrži jake aktivne sastojke i mirise koji reaktivnu kožu brzo izbace iz ravnoteže.</p>
<p>U ovoj kategoriji skupljam kreme, serume i proizvode za područje oko očiju koje sam isprobala na svojoj koži 30+. Fokus je na onome što daje vidljiv rezultat, a da pritom ne izaziva crvenilo, peckanje ni ljuštenje.</p>""",
        "hue": "cobalt",
    },
    {
        "slug": "osjetljiva-koza", "group": "koza", "nav": "Osjetljiva",
        "name": "Osjetljiva koža",
        "short": "Peckanje, zatezanje i proizvodi koji je ne ljute.",
        "title": "Osjetljiva koža – iskustva i recenzije kozmetike",
        "description": "Recenzije kozmetike za osjetljivu kožu na hrvatskom: umivalice, kreme, serumi i mineralni SPF koji (ne) peckaju.",
        "intro": """<p>Osjetljiva koža reagira na ono što drugima ne smeta: peče nakon umivanja, zateže, crveni od parfema ili nove kreme. Najveći izazov je što se “za osjetljivu kožu” piše na gotovo svakom pakiranju, a stvarno iskustvo često je drugačije.</p>
<p>Ovdje pišem o proizvodima koje sam isprobala na vlastitoj osjetljivoj koži: što je prošlo, što je završilo kod prijateljice, a što u smeću. Bez plaćenih recenzija i bez uljepšavanja.</p>""",
        "hue": "sky",
    },
    {
        "slug": "rozacea", "group": "koza", "nav": "Rozacea",
        "name": "Rozacea",
        "short": "Crvenilo, proširene kapilare i njega koja smiruje.",
        "title": "Rozacea – njega, proizvodi i osobna iskustva",
        "description": "Osobna iskustva s njegom kože s rozaceom: koji proizvodi smiruju crvenilo, a koji su mi pogoršali stanje. Recenzije na hrvatskom.",
        "intro": """<p>Rozacea je kronično stanje kože koje se najčešće vidi kao crvenilo na obrazima, nosu i bradi, a ponekad i kao sitne upaljene točkice. Okidači su vrlo individualni: sunce, toplina, alkohol u kozmetici, mirisi, kiseline.</p>
<p>Ja nisam dermatologinja i ovdje ne dajem medicinske savjete. Dijelim ono što sam naučila kroz godine isprobavanja: koji su proizvodi mojoj koži s rozaceom pomogli, a koji su je razljutili. Ako sumnjate na rozaceu, prvi korak uvijek je pregled kod dermatologa.</p>""",
        "hue": "tomato",
    },
    {
        "slug": "reaktivna-koza", "group": "koza", "nav": "Reaktivna",
        "name": "Reaktivna koža",
        "short": "Koža koja burno reagira na nove proizvode.",
        "title": "Reaktivna koža – što joj (ne) odgovara",
        "description": "Reaktivna koža i kozmetika: iskustva s proizvodima koji izazivaju crvenilo i peckanje te alternative koje su mi se pokazale sigurnijima.",
        "intro": """<p>Reaktivna koža je ona koja na promjenu odgovara odmah: novi serum, jači vjetar ili tretman kod kozmetičarke i lice je crveno, toplo i nadraženo. Kod mene se to preklapa s rozaceom, pa sam s vremenom naučila uvoditi jedan po jedan proizvod i pažljivo čitati sastav.</p>
<p>U ovoj kategoriji su recenzije i liste proizvoda koji su mojoj reaktivnoj koži odgovarali ili nisu, uz napomenu zašto mislim da je tako.</p>""",
        "hue": "orange",
    },
]

ARTICLES = [
    {
        "slug": "mineralni-spf-recenzije-poredak",
        "title": "Mineralni SPF za svijetlu i osjetljivu kožu: 6 isprobanih, od najboljeg do promašaja",
        "h1": "Mineralni SPF-ovi koje sam probala, od svetog grala do potpunog promašaja",
        "description": "Iskrena recenzija 6 mineralnih SPF-ova za svijetlu, osjetljivu kožu: Babé, Paula's Choice, Bioderma i Avène. Koji ne ostavlja bijeli trag, a koji je završio u smeću.",
        "excerpt": "Pronaći mineralni SPF koji ne izgleda kao bijela maska i ne isušuje je stalna borba. Ovo je mojih šest, poredanih od favorita do katastrofe.",
        "categories": ["spf", "osjetljiva-koza", "rozacea"],
        "date": "2026-10-20",
        "updated": "2026-10-27",
        "kicker": "Poredak",
        "faq": [('Koji je najbolji mineralni SPF za osjetljivu kožu s rozaceom?', 'Od šest mineralnih SPF-ova koje sam probala, najbolji mi je Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineralna verzija). Lijepo se razmazuje i ne peče me za oči.'), ('Koji mineralni SPF ne ostavlja bijeli trag?', "Babé Super Fluid Sunscreen Color i Paula's Choice Super-Light Daily Wrinkle Defense SPF 30 kod mene ne ostavljaju bijeli trag. Najviše bijelog traga ostavio je Bioderma Photoderm Mineral SPF 50+, koji se uz to preslikavao na odjeću i predmete."), ('Je li tonirani Babé SPF dobar za jako svijetlu kožu?', 'Tonirana verzija je pretamna za jako svijetlu put. Zato je miješam s netoniranom verzijom iz iste linije i tako dobijem pravu nijansu.'), ('Gdje kupiti Babé SPF povoljnije?', 'Ja ga naručujem sa španjolske stranice Care to Beauty, gdje je puno jeftiniji nego u hrvatskim ljekarnama.'), ('Kada koristiti Avène Mineral Fluid SPF 50+ bez boje?', 'Ostavljam ga za razdoblje nakon jačih tretmana poput microneedlinga, kad koži treba zaštita koja ostaje na površini. Za svakodnevno nošenje ispod šminke mi je prebijel.')],
        "verdict": "Pobjednik: Babé Super Fluid Color SPF 50",
        "itemlist": [
            "Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineralna verzija)",
            "Paula's Choice Super-Light Daily Wrinkle Defense SPF 30",
            "Bioderma Photoderm Nude Touch SPF 50+ (nijansa Claire/Light)",
            "Avène Tinted Mineral Fluid SPF 50+",
            "Avène Mineral Fluid SPF 50+ (bez boje)",
            "Bioderma Photoderm Mineral SPF 50+ (bez boje)",
        ],
        "body": """
<p class="lead">Pronalazak dobrog mineralnog SPF-a, onog koji ne izgleda kao bijela maska i ne isušuje, za mene je stalna borba. Zato sam složila listu svih koje sam isprobala, poredanih od favorita do potpunog promašaja. Nadam se da će nekome sa svijetlim ili neutralnim tenom ovo uštedjeti malo novca i živaca.</p>

<div class="summary" role="note">
  <p class="summary__title">Ukratko</p>
  <div class="table-wrap">
  <table>
    <thead><tr><th scope="col">#</th><th scope="col">Proizvod</th><th scope="col">Presuda</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Babé Super Fluid Color SPF 50</td><td><span class="pill pill--good">Sveti gral</span></td></tr>
      <tr><td>2</td><td>Paula's Choice Super-Light Daily Wrinkle Defense SPF 30</td><td><span class="pill pill--ok">Elegantan, ali skup</span></td></tr>
      <tr><td>3</td><td>Bioderma Photoderm Nude Touch SPF 50+</td><td><span class="pill pill--meh">Ne stoji mi</span></td></tr>
      <tr><td>4</td><td>Avène Tinted Mineral Fluid SPF 50+</td><td><span class="pill pill--meh">Pretaman</span></td></tr>
      <tr><td>5</td><td>Avène Mineral Fluid SPF 50+ (bez boje)</td><td><span class="pill pill--meh">Samo nakon tretmana</span></td></tr>
      <tr><td>6</td><td>Bioderma Photoderm Mineral SPF 50+</td><td><span class="pill pill--bad">U smeću</span></td></tr>
    </tbody>
  </table>
  </div>
</div>


<h2 id="babe">1. Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineralna verzija)</h2>
<!--IMG:foto-spf-1|Ilustracija tube: Babé Super Fluid Sunscreen Color SPF 50|Ilustracija: Babé Super Fluid Sunscreen Color SPF 50 (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> ultralagana tekstura koja se brzo upija, obogaćena prebiotičkim sastojcima koji jačaju prirodnu barijeru i štite mikrobiom kože.</p>
<p><strong>Moje iskustvo: sveti gral.</strong> Uvjerljivo najbolji mineralni SPF koji sam probala. Jako se lijepo razmazuje i uopće me ne peče za oči, što mi je ogroman plus. Jedina mana je što tonirana verzija nije za nas jako svijetle cure. Zato je miješam s običnom, netoniranom verzijom iz iste linije i tako dobijem savršenu nijansu.</p>
<p class="tip"><strong>Savjet:</strong> naručujem ga sa španjolske stranice Care to Beauty jer je ondje puno jeftiniji nego u našim ljekarnama.</p>

<h2 id="paulas-choice">2. Paula's Choice Super-Light Daily Wrinkle Defense SPF 30</h2>
<!--IMG:foto-spf-2|Ilustracija tube: Paula's Choice Super-Light Daily Wrinkle Defense SPF 30|Ilustracija: Paula's Choice Super-Light Daily Wrinkle Defense SPF 30 (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> tonirana hidratantna krema s cinkovim oksidom koja ostavlja mat finiš i smiruje crvenilo.</p>
<p><strong>Moje iskustvo:</strong> kozmetički izuzetno elegantan proizvod. Fino se razmazuje i ne ostavlja klasični bijeli odsjaj, ali prekrivenost je jako, jako slaba, tek toliko da izjednači ten. Najveći minus je cijena, preskup je. Uz to mi nakon cijelog dana zna isušiti lice i nakupiti se na suhim dijelovima.</p>

<!--AD-->

<h2 id="bioderma-nude-touch">3. Bioderma Photoderm Nude Touch SPF 50+ (nijansa Claire/Light)</h2>
<!--IMG:foto-spf-3|Ilustracija tube: Bioderma Photoderm Nude Touch SPF 50+|Ilustracija: Bioderma Photoderm Nude Touch SPF 50+ (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> 100&nbsp;% mineralni filteri, kontrola sjaja do 8 sati i formula koja ujednačava ten.</p>
<p><strong>Moje iskustvo:</strong> ovaj mi nažalost nikako ne stoji. Nijansa Claire nije topla, više vuče na rozo-neutralnu. Ni tekstura mi se ne sviđa: dosta se teško razmazuje i na licu ostaje mrljasta, nejednako se prima.</p>

<h2 id="avene-tinted">4. Avène Tinted Mineral Fluid SPF 50+</h2>
<!--IMG:foto-spf-4|Ilustracija tube: Avène Tinted Mineral Fluid SPF 50+|Ilustracija: Avène Tinted Mineral Fluid SPF 50+ (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> visoka zaštita za netolerantnu kožu, sa zlatnom nijansom koja ujednačava ten.</p>
<p><strong>Moje iskustvo:</strong> puno, puno pretaman. Čak i curama koje nisu izrazito svijetle ovo će biti previše. Uz to se teško razmazuje. Za ovaj proizvod stvarno treba imati tamniju put ili već dobar ten.</p>

<h2 id="avene-bez-boje">5. Avène Mineral Fluid SPF 50+ (bez boje)</h2>
<!--IMG:foto-spf-5|Ilustracija tube: Avène Mineral Fluid SPF 50+|Ilustracija: Avène Mineral Fluid SPF 50+ (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> 100&nbsp;% mineralni filteri, fotostabilna zaštita bez kemijskih filtera i parfema.</p>
<p><strong>Moje iskustvo:</strong> doslovno bijeli kreč, bez ikakvih dodatnih njegujućih sastojaka. Zadržala sam ga samo zato što je dobar i siguran izbor nakon jačih kozmetičkih tretmana, poput microneedlinga, kad koži treba zaštita koja sjedne na površinu. Za svakodnevno nošenje ispod šminke, zaboravite.</p>

<h2 id="bioderma-mineral">6. Bioderma Photoderm Mineral SPF 50+ (bez boje)</h2>
<!--IMG:foto-spf-6|Ilustracija tube: Bioderma Photoderm Mineral SPF 50+|Ilustracija: Bioderma Photoderm Mineral SPF 50+ (nije originalno pakiranje).-->
<p class="claim"><strong>Što brend tvrdi:</strong> maksimalna učinkovitost protiv UVB i UVA zraka za kožu alergičnu na kemijske filtere.</p>
<p><strong>Moje iskustvo: totalna katastrofa.</strong> Nešto najbjelje što sam ikad stavila na sebe. Problem je što se ta bjelina užasno preslikava: sve što sam dotaknula ostalo je umrljano i više se nije dalo oprati. Sjedalo u autu, neseser za šminku, čak i vrata od kuće. Završio je u smeću. A kao šlag na tortu, pakiranje curi na sve strane.</p>

<h2 id="zakljucak">Zaključak</h2>
<p>Ako imate svijetlu, osjetljivu kožu sklonu crvenilu i tražite mineralni SPF za svaki dan, moj odgovor je Babé Super Fluid Color, po potrebi pomiješan s netoniranom verzijom. Paula's Choice je lijepa, ali skupa alternativa ako vam treba samo lagano ujednačavanje tena.</p>
<p><strong>Što vi koristite?</strong> Ako imate preporuku za dobar mineralni SPF koji ne ostavlja bijeli trag na svemu što dotaknete, javite mi se.</p>
""",
    },
    {
        "slug": "proizvodi-koji-nisu-odgovarali-rozacea",
        "title": "12 popularnih proizvoda za osjetljivu kožu koji su mojoj rozacei bili promašaj",
        "h1": "Popularni proizvodi koji su završili “u smeću”",
        "description": "CeraVe, Kiehl's, Paula's Choice, Biologique Recherche P50W i drugi: 12 često preporučenih proizvoda koji nisu odgovarali mojoj osjetljivoj, reaktivnoj koži s rozaceom.",
        "excerpt": "Ovi se proizvodi često preporučuju baš za osjetljivu kožu s rozaceom. Meni nisu odgovarali, pa možda vama uštede novac.",
        "categories": ["rozacea", "njega-lica", "reaktivna-koza", "osjetljiva-koza"],
        "date": "2026-10-13",
        "updated": "2026-10-27",
        "kicker": "Antipreporuke",
        "faq": [('Zašto CeraVe nije odgovarao mojoj koži s rozaceom?', 'Probala sam više CeraVe umivalica i njihovu hidratantnu kremu i nijedna mi nije sjela, iako su česta preporuka za osjetljivu kožu. Svaka koža je drugačija, pa nekome drugome mogu odgovarati.'), ('Koji sastojci najčešće iritiraju moju kožu s rozaceom?', 'Kod mene se ponavljaju isti okidači: salicilna kiselina (BHA), alkohol i jak miris te kemijski UV filteri.'), ('Je li azelaična kiselina dobra za rozaceu?', "Azelaična kiselina se često preporučuje kod rozacee, ali Paula's Choice Azelaic Acid Booster mi nije odgovarao, vjerojatno zato što sadrži i salicilnu kiselinu."), ('Kako uvoditi nove proizvode ako imate reaktivnu kožu?', 'Prije kupnje provjerim sastav, a nove proizvode uvodim jedan po jedan kako bih znala što točno izaziva reakciju.')],
        "verdict": "12 proizvoda koje ne bih ponovno kupila",
        "itemlist": [
            "CeraVe umivalice za lice", "CeraVe hidratantna krema", "Kiehl's vitamin C serum",
            "Kiehl's Skin Strengthening Super Serum", "Biologique Recherche P50W",
            "Paula's Choice Azelaic Acid Booster", "Paula's Choice 2% BHA", "Revox hidratantna krema",
            "Olival krema od smilja", "Olival SPF 30", "L'Occitane booster", "Erborian Red CC krema",
        ],
        "body": """
<p class="lead">Imam osjetljivu, reaktivnu kožu s rozaceom i ovo su proizvodi koji mi nisu odgovarali. Zanimljivo je da se baš mnogi od njih često preporučuju za taj tip kože, pa vam ova lista možda uštedi novac.</p>
<p>Odmah da razjasnim navodnike u naslovu: većina ovih proizvoda nije doslovno završila u smeću, nego sam ih darovala dalje. Ono što nije odgovaralo meni, nekome drugome može biti savršeno.</p>

<h2 id="umivanje-i-hidratacija">Umivanje i hidratacija</h2>
<ul class="verdicts">
  <li><strong>CeraVe umivalice za lice (bilo koja vrsta).</strong> Probala sam ih više i nijedna mi nije sjela, unatoč tome što su gotovo uvijek prva preporuka za osjetljivu kožu.</li>
  <li><strong>CeraVe hidratantna krema.</strong> Isto iskustvo kao s umivalicama.</li>
  <li><strong>Revox hidratantna krema.</strong> Nije mi odgovarala.</li>
  <li><strong>Olival krema od smilja.</strong> Smilje se često spominje kao smirujući sastojak, ali moja ga koža u ovoj formuli nije voljela.</li>
</ul>

<h2 id="serumi">Serumi i boosteri</h2>
<ul class="verdicts">
  <li><strong>Kiehl's vitamin C serum.</strong> Nije za moju kožu.</li>
  <li><strong>Kiehl's Skin Strengthening Super Serum.</strong> Ima snažan miris po alkoholu, što je za reaktivnu kožu prvi alarm.</li>
  <li><strong>L'Occitane booster.</strong> Nije mi odgovarao.</li>
</ul>

<!--AD-->

<h2 id="kiseline">Kiseline i tonici</h2>
<ul class="verdicts">
  <li><strong>Biologique Recherche P50W.</strong> Kultni tonik, ali ne za moju kožu s rozaceom.</li>
  <li><strong>Paula's Choice Azelaic Acid Booster.</strong> Azelaična kiselina se često preporučuje kod rozacee, ali ovaj booster vjerojatno nije prošao jer sadrži i salicilnu kiselinu.</li>
  <li><strong>Paula's Choice 2% BHA.</strong> Salicilna kiselina mojoj koži jednostavno ne odgovara.</li>
</ul>

<h2 id="spf-i-ten">SPF i tonirani proizvodi</h2>
<ul class="verdicts">
  <li><strong>Olival SPF 30.</strong> Nije mi odgovarao.</li>
  <li><strong>Erborian Red CC krema.</strong> Popularna je baš za prikrivanje crvenila, ali mi nije sjela, vjerojatno zbog kemijskih filtera u SPF-u. Od tada koristim isključivo <a href="/clanci/mineralni-spf-recenzije-poredak/">mineralne SPF-ove</a>.</li>
</ul>

<h2 id="sto-sam-naucila">Što sam naučila</h2>
<p>Kad pogledam ovu listu, ponavljaju se isti okidači: salicilna kiselina, alkohol i jak miris te kemijski UV filteri. Danas sastav provjerim prije kupnje i nove proizvode uvodim jedan po jedan, kako bih znala što točno izaziva reakciju.</p>
<p>Svaka koža je drugačija. Ako vama neki od ovih proizvoda odgovara, super. Ova lista samo pokazuje da “za osjetljivu kožu” na pakiranju ne znači da će odgovarati baš vašoj. Proizvode koji su se kod mene pokazali dobitnima skupila sam u članku <a href="/clanci/proizvodi-koje-cu-ponovno-kupiti/">Proizvodi koje ću ponovno kupiti</a>.</p>
""",
    },
    {
        "slug": "proizvodi-koje-cu-ponovno-kupiti",
        "title": "Proizvodi koje ću ponovno kupiti: moji ride or die favoriti za lice, kosu i tijelo",
        "h1": "Proizvodi koje ću ponovno kupiti",
        "description": "Moji ride or die proizvodi koje kupujem iznova: njega za osjetljivu kožu s rozaceom, šminka, kosa i tijelo. Kiehl's, Vichy, Babé, Skintegra, Olaplex i drugi.",
        "excerpt": "Kratka lista proizvoda koje sam kupila više puta i kupit ću ih opet: njega lica, šminka, kosa i tijelo.",
        "categories": ["njega-lica", "sminka", "koza-30-plus"],
        "date": "2026-10-06",
        "updated": "2026-10-27",
        "kicker": "Favoriti",
        "faq": [('Koje proizvode za osjetljivu kožu s rozaceom kupujem iznova?', "Za lice iznova kupujem Olival hidrator u spreju, Kiehl's Ultra Facial Cream, Vichy Minéral serum, Babé mineralni tonirani SPF 50 i Skintegra Ros/Ac, među ostalima."), ('Koji SPF koristim svaki dan?', 'Laboratorios Babé mineralni tonirani fluid SPF 50. Među mineralnim SPF-ovima koje sam probala on mi je broj jedan.'), ('Koju šminku kupujem ponovno?', 'Catrice olovku za obrve, IT Cosmetics CC kremu (Original), NARS bronzer u nijansi Laguna i Sweed Lash maskaru.'), ('Koji proizvodi za kosu i tijelo su mi favoriti?', 'Za kosu Olaplex No. 3 i Kérastase Nutritive Masquintense, a za tijelo CeraVe SA kremu, iako mi CeraVe proizvodi za lice nisu odgovarali.')],
        "verdict": "16 proizvoda koje kupujem iznova",
        "itemlist": [
            "Olival hidrator u spreju", "Kiehl's Ultra Facial Cream", "Vichy Minéral serum",
            "Laboratorios Babé mineralni tonirani fluid SPF 50", "Skintegra Ros/Ac", "Sweed Lash Serum",
            "Clinique Smart Clinical Repair Wrinkle Correcting Cream", "Kiehl's krema oko očiju s avokadom",
            "Ladria jastučići za područje oko očiju", "Catrice olovka za obrve", "IT Cosmetics CC krema (Original)",
            "NARS Laguna bronzer", "Sweed Lash maskara", "Olaplex No. 3", "Kérastase Nutritive Masquintense",
            "CeraVe SA krema za tijelo",
        ],
        "body": """
<p class="lead">Nakon <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">liste promašaja</a> red je i na proizvode koji su prošli najstroži test: kupila sam ih više puta i kupit ću ih opet. Moja koža je osjetljiva, reaktivna i sklona rozacei, pa ovo nije lista slučajnih favorita.</p>

<!--IMG:foto-polica|Krema, serum, tonik, SPF tuba i ruž na svijetloplavoj podlozi|Njega i šminka koju kupujem iznova.-->

<h2 id="njega-lica">Njega lica</h2>
<ul class="picks">
  <li><strong>Olival hidrator u spreju</strong></li>
  <li><strong>Kiehl's Ultra Facial Cream</strong></li>
  <li><strong>Vichy Minéral serum</strong></li>
  <li><strong>Laboratorios Babé mineralni tonirani fluid SPF 50</strong>, moj <a href="/clanci/mineralni-spf-recenzije-poredak/">broj jedan među mineralnim SPF-ovima</a></li>
  <li><strong>Skintegra Ros/Ac</strong></li>
  <li><strong>Sweed Lash Serum</strong></li>
  <li><strong>Clinique Smart Clinical Repair Wrinkle Correcting Cream</strong></li>
  <li><strong>Kiehl's krema oko očiju s avokadom</strong></li>
  <li><strong>Ladria jastučići za područje oko očiju</strong></li>
</ul>

<!--AD-->

<h2 id="sminka">Šminka</h2>
<ul class="picks">
  <li><strong>Catrice olovka za obrve</strong> (mislim da je nijansa Ashton)</li>
  <li><strong>IT Cosmetics CC krema (Original)</strong></li>
  <li><strong>NARS bronzer u nijansi Laguna</strong></li>
  <li><strong>Sweed Lash maskara</strong></li>
</ul>

<h2 id="kosa">Kosa</h2>
<ul class="picks">
  <li><strong>Olaplex No. 3</strong></li>
  <li><strong>Kérastase Nutritive Masquintense</strong></li>
</ul>

<h2 id="tijelo">Tijelo</h2>
<ul class="picks">
  <li><strong>CeraVe SA krema</strong>. Zanimljivo, CeraVe proizvodi za lice mi nisu odgovarali, ali SA kremu za tijelo kupujem iznova.</li>
</ul>

<h2 id="vasi-favoriti">A vaši favoriti?</h2>
<p>O većini ovih proizvoda uskoro pišem detaljne recenzije. Koji su vaši ride or die proizvodi koje ste kupile više puta? Javite mi, rado ću ih isprobati.</p>
""",
    },
]


# Brendovi: stranica brenda automatski prikuplja članke u kojima se brend spominje (po nazivu ili aliasu).
# "intro" se može dopisati kad postoji recenzija; brend bez članaka ima noindex dok ne dobije sadržaj.
BRANDS = [
    {"name": "Avène", "aliases": ["Avène", "Avene"]},
    {"name": "Babé", "aliases": ["Babé", "Babe"]},
    {"name": "Bioderma", "aliases": ["Bioderma"]},
    {"name": "Biologique Recherche", "aliases": ["Biologique Recherche"]},
    {"name": "Catrice", "aliases": ["Catrice"]},
    {"name": "CeraVe", "aliases": ["CeraVe", "Cerave"]},
    {"name": "Chanel", "aliases": ["Chanel"]},
    {"name": "Clinique", "aliases": ["Clinique"]},
    {"name": "Dior", "aliases": ["Dior"]},
    {"name": "Erborian", "aliases": ["Erborian"]},
    {"name": "IT Cosmetics", "aliases": ["IT Cosmetics"]},
    {"name": "Kérastase", "aliases": ["Kérastase", "Kerastase"]},
    {"name": "Kiehl's", "aliases": ["Kiehl's", "Kiehls"]},
    {"name": "L'Occitane", "aliases": ["L'Occitane", "Loccitane"]},
    {"name": "Ladria", "aliases": ["Ladria"]},
    {"name": "NARS", "aliases": ["NARS"]},
    {"name": "Olaplex", "aliases": ["Olaplex"]},
    {"name": "Olival", "aliases": ["Olival"]},
    {"name": "Paula's Choice", "aliases": ["Paula's Choice", "Paulas Choice"]},
    {"name": "Revox", "aliases": ["Revox"]},
    {"name": "Rhode", "aliases": ["Rhode"]},
    {"name": "Skintegra", "aliases": ["Skintegra"]},
    {"name": "Sweed", "aliases": ["Sweed"]},
    {"name": "Vichy", "aliases": ["Vichy"]},
]
