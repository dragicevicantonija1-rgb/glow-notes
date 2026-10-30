"""Kratki SEO opisi brendova: kako brend odgovara osjetljivoj koži i rozacei.

Ključ je ime brenda iz content.BRANDS. Svako polje je par (hr, en):
  desc  -> meta description stranice brenda (do ~155 znakova)
  about -> odlomci "O brendu" na stranici brenda (HTML)
"""

BRAND_INFO = {
    "Avène": {
        "desc": ("Avène i osjetljiva koža: termalna voda, Cicalfate, Couvrance i SPF iz ljekarne, iskreno testirani na koži s rozaceom i crvenilom.",
                 "Avène for sensitive skin: thermal water, Cicalfate, Couvrance and pharmacy SPF, honestly tested on skin with rosacea and redness."),
        "about": ("""<p>Avène je francuski dermokozmetički brend grupe Pierre Fabre, nastao oko termalnog izvora u istoimenom mjestu. Gotovo cijela ponuda namijenjena je osjetljivoj i reaktivnoj koži, a za crvenilo i rozaceu postoji posebna linija Antirougeurs. Većina formula je bez parfema i s kratkim popisom sastojaka.</p>
<p>Moje iskustvo s Avèneom je mješovito: Cicalfate serum i mineralni fluid mi pomažu nakon tretmana, ali termalna voda, tonirani SPF i Couvrance puder nisu prošli test na mojoj koži s rozaceom. Dobar brend za početak, samo svaki proizvod isprobajte zasebno.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Avène ima patentiranu tehnologiju sterilne kozmetike (Cosmétique Stérile) u liniji Tolérance, koja omogućuje formule bez konzervansa. Za termalnu vodu navodi više od 150 kliničkih i znanstvenih studija, ali bez objavljenog broja ispitanika. Krema Antirougeurs Rosamed u studiji na 41 osobi smanjila je intenzitet crvenila za 48&nbsp;% nakon mjesec dana korištenja dvaput dnevno.</p>""",
                  """<p>Avène is a French dermocosmetic brand from the Pierre Fabre group, built around the thermal spring in the village of the same name. Almost the entire range is made for sensitive and reactive skin, and there is a dedicated Antirougeurs line for redness and rosacea. Most formulas are fragrance-free with short ingredient lists.</p>
<p>My experience with Avène is mixed: the Cicalfate serum and the mineral fluid help after treatments, but the thermal water, the tinted SPF and Couvrance foundation did not pass the test on my rosacea-prone skin. A good brand to start with, just test each product on its own.</p>
<p><strong>Patents and testing (according to the brand):</strong> Avène holds a patent on its sterile cosmetics technology (Cosmétique Stérile) used in the Tolérance line, which allows preservative-free formulas. It cites more than 150 clinical and scientific studies on its thermal water, without publishing subject numbers. In a study on 41 people, Antirougeurs Rosamed cream reduced redness intensity by 48% after a month of twice-daily use.</p>"""),
    },
    "Babé": {
        "desc": ("Babé (Laboratorios Babé) recenzije: mineralni SPF 50 i SPF za usne i obraze, testirani na osjetljivoj koži s rozaceom. Moj broj jedan SPF.",
                 "Babé (Laboratorios Babé) reviews: mineral SPF 50 and lip & cheek SPF tested on sensitive skin with rosacea. My number one SPF."),
        "about": ("""<p>Laboratorios Babé je španjolski ljekarnički brend poznat po pristupačnoj dermokozmetici i zaštiti od sunca. Za osjetljivu kožu i rozaceu najzanimljiviji su njihovi 100&nbsp;% mineralni SPF-ovi, jer mnogim reaktivnim kožama upravo kemijski UV filteri izazivaju crvenilo i peckanje.</p>
<p>Babé Super Fluid Color SPF 50 je moj sveti gral među mineralnim SPF-ovima: lako se razmazuje, ne ostavlja bijeli trag na svijetloj koži i ne crveni me. Za mene je to brend kojem se uvijek vraćam.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Babé na stranici proizvoda ne navodi patente ni kliničke testove. Formula je 100&nbsp;% mineralna (cinkov oksid i titanov dioksid) i namijenjena koži koja ne podnosi kemijske filtere.</p>""",
                  """<p>Laboratorios Babé is a Spanish pharmacy brand known for affordable dermocosmetics and sun care. For sensitive skin and rosacea the most interesting products are their 100% mineral sunscreens, because chemical UV filters are a common trigger of redness and stinging on reactive skin.</p>
<p>Babé Super Fluid Color SPF 50 is my holy grail mineral SPF: it spreads easily, leaves no white cast on fair skin and doesn't make me flush. It's a brand I keep coming back to.</p>
<p><strong>Patents and testing (according to the brand):</strong> Babé doesn't cite patents or clinical tests on the product page. The formula is 100% mineral (zinc oxide and titanium dioxide) and is made for skin that doesn't tolerate chemical filters.</p>"""),
    },
    "Bioderma": {
        "desc": ("Bioderma i osjetljiva koža: Sensibio H2O micelarna voda i Photoderm AR SPF protiv crvenila, iskreno testirani na koži s rozaceom.",
                 "Bioderma for sensitive skin: Sensibio H2O micellar water and Photoderm AR anti-redness SPF, honestly tested on skin with rosacea."),
        "about": ("""<p>Bioderma je francuski dermokozmetički brend (NAOS) i jedan od najprodavanijih ljekarničkih brendova u Europi. Za osjetljivu kožu ključna je linija Sensibio, za crvenilo i rozaceu Sensibio AR, a u liniji Photoderm postoje SPF-ovi s laganim tonom koji prikriva crvenilo.</p>
<p>Sensibio H2O je moj dugogodišnji favorit i prvi korak čišćenja svake večeri. S njihovim SPF-ovima sam manje sretna: Photoderm AR je okej, a mineralni Photoderm mi je završio na dnu poretka.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Bioderma ima patentirani kompleks D.A.F. (Dermatological Advanced Formulation), koji podiže prag tolerancije kože, i patent za micelarno čišćenje bez ispiranja. Linije za crvenilo (Sensibio AR, Photoderm AR) koriste patent Rosactiv. Za Sensibio H2O navodi opservacijsku studiju na 400 osoba: nakon 28 dana 90&nbsp;% ih je prijavilo manje neugodnih osjećaja na koži. Za Sensibio AR navodi 73&nbsp;% manje crvenila, ali bez broja ispitanika.</p>""",
                  """<p>Bioderma is a French dermocosmetic brand (NAOS) and one of the best-selling pharmacy brands in Europe. The Sensibio line is the go-to for sensitive skin, Sensibio AR targets redness and rosacea, and the Photoderm range includes lightly tinted sunscreens that tone down redness.</p>
<p>Sensibio H2O has been my favourite for years and is the first cleansing step every evening. I'm less happy with their sunscreens: Photoderm AR is fine, while the mineral Photoderm ended up at the bottom of my ranking.</p>
<p><strong>Patents and testing (according to the brand):</strong> Bioderma holds a patent on its D.A.F. complex (Dermatological Advanced Formulation), which raises the skin's tolerance threshold, and on its no-rinse micellar cleansing. Its redness lines (Sensibio AR, Photoderm AR) use the patented Rosactiv. For Sensibio H2O it cites an observational study on 400 people: after 28 days, 90% reported fewer unpleasant skin sensations. For Sensibio AR it claims 73% less redness, without giving the number of subjects.</p>"""),
    },
    "Biologique Recherche": {
        "desc": ("Biologique Recherche i rozacea: iskustvo s kultnim piling tonikom Lotion P50W na reaktivnoj, osjetljivoj koži sklonoj crvenilu.",
                 "Biologique Recherche and rosacea: my experience with the cult exfoliating toner Lotion P50W on reactive, sensitive skin prone to redness."),
        "about": ("""<p>Biologique Recherche je francuski luksuzni brend koji se prodaje uglavnom preko salona i kozmetičara. Najpoznatiji je po Lotion P50, eksfoliirajućem toniku s kiselinama, a verzija P50W predstavlja se kao blaža, za osjetljivu kožu.</p>
<p>Kod rozacee i reaktivne kože svaki svakodnevni piling s kiselinama je rizik. Meni P50W nije odgovarao ni u blažoj verziji, pa ga preporučujem samo koži koja kiseline već dobro podnosi.</p>""",
                  """<p>Biologique Recherche is a French luxury brand sold mainly through salons and facialists. It is best known for Lotion P50, an exfoliating toner with acids, and the P50W version is marketed as the gentler option for sensitive skin.</p>
<p>With rosacea and reactive skin, any daily acid toner is a risk. P50W didn't suit me even in its gentler form, so I only recommend it to skin that already tolerates acids well.</p>"""),
    },
    "Catrice": {
        "desc": ("Catrice recenzije: pristupačna drogerijska šminka, olovke za obrve i usne, iz perspektive svijetle, osjetljive kože sklone crvenilu.",
                 "Catrice reviews: affordable drugstore make-up, brow and lip pencils, from the point of view of fair, sensitive skin prone to redness."),
        "about": ("""<p>Catrice je njemački drogerijski brend šminke (cosnova) s vrlo pristupačnim cijenama i brzim izmjenama kolekcija. Kod osjetljive kože i rozacee najsigurnije su olovke za obrve i usne, maskare i puderi u prahu, dok tekuće podloge i proizvode za lice uvijek najprije testiram na manjem dijelu kože.</p>
<p>Catriceina olovka za obrve je u mojoj stalnoj rutini, a njihova mekana olovka za usne je moja jeftinija preporuka umjesto Rhodeove.</p>""",
                  """<p>Catrice is a German drugstore make-up brand (cosnova) with very affordable prices and fast-changing collections. With sensitive skin and rosacea the safest picks are brow and lip pencils, mascaras and powders, while liquid bases and face products are always patch-tested first.</p>
<p>The Catrice brow pencil is a permanent part of my routine, and their soft lip liner is my cheaper recommendation instead of the Rhode one.</p>"""),
    },
    "CeraVe": {
        "desc": ("CeraVe i osjetljiva koža: iskustvo s umivalicama, kremom za lice i SA kremom za tijelo na koži s rozaceom. Što mi je odgovaralo, a što nije.",
                 "CeraVe for sensitive skin: my experience with the cleansers, face cream and SA body cream on rosacea-prone skin. What worked and what didn't."),
        "about": ("""<p>CeraVe je američki brend razvijen s dermatolozima, danas dio grupe L'Oréal. Prepoznatljiv je po ceramidima za obnovu kožne barijere i formulama bez parfema, pa je često prva preporuka za osjetljivu kožu.</p>
<p>Kod rozacee to ipak nije pravilo: CeraVe umivalice i krema za lice mojoj koži nisu odgovarale. S druge strane, SA kremu za tijelo kupujem iznova. Dobar dokaz da isti brend može biti odličan za tijelo, a ne sjesti na reaktivno lice.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> CeraVe koristi MVE tehnologiju (multivezikularnu emulziju) koja postupno otpušta ceramide tijekom dana, a za koju navodi raniji američki patent br. 6,709,663. Broj ispitanika u studijama za proizvode za lice na stranici brenda nije naveden.</p>""",
                  """<p>CeraVe is an American brand developed with dermatologists and now part of L'Oréal. It is known for ceramides that support the skin barrier and fragrance-free formulas, which makes it a frequent first recommendation for sensitive skin.</p>
<p>With rosacea that isn't a rule, though: CeraVe cleansers and face cream didn't suit my skin. On the other hand, I keep repurchasing the SA body cream. Proof that the same brand can be great for the body and still not agree with a reactive face.</p>
<p><strong>Patents and testing (according to the brand):</strong> CeraVe uses MVE technology (multivesicular emulsion), which releases ceramides gradually through the day, and cites a former US patent no. 6,709,663. The brand's site doesn't give subject numbers for its face product studies.</p>"""),
    },
    "Chanel": {
        "desc": ("Chanel recenzije: Les Beiges Water-Fresh Tint i luksuzna šminka testirana na osjetljivoj koži 30+ sklonoj crvenilu. Vrijedi li cijene?",
                 "Chanel reviews: Les Beiges Water-Fresh Tint and luxury make-up tested on sensitive 30+ skin prone to redness. Is it worth the price?"),
        "about": ("""<p>Chanel je francuska luksuzna kuća čija linija Les Beiges nudi lagane podloge za prirodan, svjež ten. Kod osjetljive kože i rozacee luksuzna šminka nije automatski nježna: mnoge formule sadrže parfem, pa uvijek provjerite sastav i testirajte proizvod prije nego što ga nanesete na cijelo lice.</p>
<p>Water-Fresh Tint je iznimka koja me oduševila: lagano ujednačava ten, koža izgleda punije i svježije, a moja ga koža s rozaceom dobro podnosi.</p>""",
                  """<p>Chanel is a French luxury house whose Les Beiges line offers light bases for a natural, fresh complexion. With sensitive skin and rosacea, luxury make-up isn't automatically gentle: many formulas contain fragrance, so always check the ingredients and test before applying to the whole face.</p>
<p>Water-Fresh Tint is the exception that won me over: it evens out the skin lightly, leaves it looking plumper and fresher, and my rosacea-prone skin tolerates it well.</p>"""),
    },
    "Clinique": {
        "desc": ("Clinique i osjetljiva koža: alergološki testirane formule bez parfema i krema Smart Clinical Repair testirana na koži 30+ sklonoj rozacei.",
                 "Clinique for sensitive skin: allergy-tested, fragrance-free formulas and Smart Clinical Repair cream tested on 30+ skin prone to rosacea."),
        "about": ("""<p>Clinique je američki brend grupe Estée Lauder, od početka razvijan s dermatolozima. Proizvodi su alergološki testirani i bez parfema, što ga čini jednim od sigurnijih luksuznih izbora za osjetljivu kožu. Za crvenilo postoji i linija Redness Solutions.</p>
<p>Na mojoj koži 30+ s rozaceom najbolje se pokazala krema Smart Clinical Repair Wrinkle Correcting Cream, koju kupujem ponovno.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Clinique ne navodi patent za osjetljivu kožu, ali navodi gotovo 6 milijuna testnih aplikacija u alergološkim testovima od osnutka, a svi proizvodi su dermatološki testirani i 100&nbsp;% bez parfema.</p>""",
                  """<p>Clinique is an American brand from the Estée Lauder group, developed with dermatologists from the start. Its products are allergy-tested and fragrance-free, which makes it one of the safer luxury choices for sensitive skin. There is also a Redness Solutions line for redness.</p>
<p>On my 30+ skin with rosacea the Smart Clinical Repair Wrinkle Correcting Cream has worked best, and I keep buying it again.</p>
<p><strong>Patents and testing (according to the brand):</strong> Clinique doesn't claim a sensitive-skin patent, but cites nearly 6 million test applications in allergy testing since its launch, and all products are dermatologist tested and 100% fragrance-free.</p>"""),
    },
    "Dior": {
        "desc": ("Dior recenzije: luksuzna šminka i njega iz perspektive osjetljive kože sklone rozacei. Na što paziti prije kupnje.",
                 "Dior reviews: luxury make-up and skincare from the point of view of sensitive skin prone to rosacea. What to check before you buy."),
        "about": ("""<p>Dior je francuska luksuzna kuća (LVMH) poznata po podlogama Forever, ružu Addict i proizvodima za usne. Kod osjetljive kože i rozacee kod luksuznih brendova najviše treba paziti na parfem i alkohol u formulama, jer upravo oni najčešće izazivaju crvenilo i peckanje.</p>
<p>Detaljna recenzija Diora tek stiže, a ovdje ću skupljati sve što isprobam.</p>""",
                  """<p>Dior is a French luxury house (LVMH) known for its Forever foundations, Addict lipsticks and lip products. With sensitive skin and rosacea, the main things to watch for in luxury brands are fragrance and alcohol in the formulas, since they are the most common triggers of redness and stinging.</p>
<p>A detailed Dior review is still on its way, and this is where I'll collect everything I try.</p>"""),
    },
    "Erborian": {
        "desc": ("Erborian i rozacea: iskustvo sa zelenom CC Red Correct kremom za crvenilo na osjetljivoj, reaktivnoj koži. Zašto mi nije odgovarala.",
                 "Erborian and rosacea: my experience with the green CC Red Correct cream for redness on sensitive, reactive skin, and why it didn't suit me."),
        "about": ("""<p>Erborian je korejsko-francuski brend koji spaja korejske formule i biljne sastojke poput centelle. Najpoznatiji je po CC kremama, a zelena CC Red Correct namijenjena je baš prikrivanju crvenila, pa se često preporučuje kod rozacee.</p>
<p>Zeleni pigment crvenilo neutralizira odlično, ali kemijski SPF u kremi mojoj je koži izazvao još više crvenila i papula. Ako vaša rozacea reagira na kemijske filtere, preskočite ga ili ga koristite samo za kratke izlaske.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Za CC Red Correct brend ne navodi patent. U testu na 33 osobe vidljivo crvenilo (bez šminke) smanjilo se za 30&nbsp;% nakon 28 dana, a svi su odmah nakon nanošenja vidjeli neutralizirano crvenilo.</p>""",
                  """<p>Erborian is a Korean-French brand that combines Korean formulas with botanical ingredients such as centella. It is best known for its CC creams, and the green CC Red Correct is designed specifically to hide redness, so it's often recommended for rosacea.</p>
<p>The green pigment neutralises redness beautifully, but the chemical SPF in the cream gave my skin even more redness and bumps. If your rosacea reacts to chemical filters, skip it or keep it for short outings.</p>
<p><strong>Patents and testing (according to the brand):</strong> Erborian doesn't claim a patent for CC Red Correct. In a test on 33 people, visible redness on bare skin dropped by 30% after 28 days, and all of them saw redness neutralised right after application.</p>"""),
    },
    "IT Cosmetics": {
        "desc": ("IT Cosmetics recenzije: CC krema s visokim prekrivanjem i SPF-om na osjetljivoj koži 30+ sklonoj crvenilu i rozacei.",
                 "IT Cosmetics reviews: high-coverage CC cream with SPF on sensitive 30+ skin prone to redness and rosacea."),
        "about": ("""<p>IT Cosmetics je američki brend (danas L'Oréal) poznat po CC+ kremi, toniranoj kremi s visokim prekrivanjem, njegujućim sastojcima i SPF-om. Za kožu s rozaceom zanimljiva je jer jednim slojem prekriva crvenilo i neravnine, bez potrebe za korektorom.</p>
<p>Originalna CC krema mi je jedan od proizvoda koje kupujem ponovno. Ako vam smetaju kemijski filteri, prije kupnje provjerite sastav verzije koja se prodaje kod nas.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Za CC+ kremu brend ne navodi patent ni tvrdnje za osjetljivu kožu, nego samo potrošačke testove (npr. 98&nbsp;% kaže da brzo prikriva tragove akni), bez broja ispitanika.</p>""",
                  """<p>IT Cosmetics is an American brand (now L'Oréal) known for its CC+ Cream, a high-coverage tinted cream with skincare ingredients and SPF. For rosacea-prone skin it is interesting because a single layer covers redness and texture without needing concealer.</p>
<p>The original CC cream is one of my repurchases. If chemical filters bother your skin, check the ingredient list of the version sold in your country before buying.</p>
<p><strong>Patents and testing (according to the brand):</strong> IT Cosmetics doesn't claim a patent or sensitive-skin benefits for CC+ Cream, only consumer tests (e.g. 98% say it quickly covers acne marks), without giving the number of people.</p>"""),
    },
    "Kérastase": {
        "desc": ("Kérastase recenzije: luksuzna njega kose i maska Nutritive Masquintense iz perspektive osjetljive kože lica i vlasišta.",
                 "Kérastase reviews: luxury hair care and the Nutritive Masquintense mask from the point of view of sensitive facial skin and scalp."),
        "about": ("""<p>Kérastase je luksuzni brend za njegu kose iz grupe L'Oréal, prodaje se uglavnom u frizerskim salonima. Proizvodi za kosu često imaju intenzivan miris, pa kod osjetljive kože i rozacee pazim da ne dolaze u dodir s licem i linijom kose, a kosu ispiram prije umivanja lica.</p>
<p>Nutritive Masquintense je moja maska za suhu kosu kojoj se stalno vraćam.</p>""",
                  """<p>Kérastase is a luxury hair care brand from the L'Oréal group, sold mainly through hair salons. Hair products are often strongly fragranced, so with sensitive skin and rosacea I make sure they don't touch my face and hairline, and I rinse my hair before washing my face.</p>
<p>Nutritive Masquintense is the dry-hair mask I keep coming back to.</p>"""),
    },
    "Kiehl's": {
        "desc": ("Kiehl's i osjetljiva koža: Ultra Facial Cream, krema oko očiju s avokadom i serumi testirani na koži s rozaceom. Favoriti i promašaji.",
                 "Kiehl's for sensitive skin: Ultra Facial Cream, avocado eye cream and serums tested on rosacea-prone skin. Favourites and flops."),
        "about": ("""<p>Kiehl's je brend nastao 1851. u njujorškoj ljekarni, danas dio grupe L'Oréal. Ponuda je široka: od jednostavnih hidratantnih krema do seruma s aktivnim sastojcima, pa se kod osjetljive kože i rozacee isplati čitati sastav proizvod po proizvod.</p>
<p>Ultra Facial Cream i krema oko očiju s avokadom su mi stalni favoriti. Vitamin C serum i Skin Strengthening Super Serum s jakim mirisom alkohola mojoj reaktivnoj koži nisu odgovarali.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Za Ultra Facial Cream Kiehl's ne navodi patent, ali navodi 132&nbsp;% više hidratacije i trenutno manje suhoće kod 97&nbsp;% ispitanika, bez broja ispitanika. Krema je bez parfema i ima oznaku američkog udruženja National Eczema Association.</p>""",
                  """<p>Kiehl's started in a New York apothecary in 1851 and is now part of L'Oréal. The range is wide, from simple moisturisers to serums with strong actives, so with sensitive skin and rosacea it pays to read the ingredients product by product.</p>
<p>Ultra Facial Cream and the avocado eye cream are long-time favourites. The vitamin C serum and the Skin Strengthening Super Serum, with its strong alcohol smell, didn't suit my reactive skin.</p>
<p><strong>Patents and testing (according to the brand):</strong> Kiehl's doesn't claim a patent for Ultra Facial Cream, but cites a 132% hydration boost and immediately less dryness in 97% of subjects, without giving the number of subjects. The cream is fragrance-free and carries the US National Eczema Association seal.</p>"""),
    },
    "L'Occitane": {
        "desc": ("L'Occitane i osjetljiva koža: iskustvo s njegom lica na koži sklonoj rozacei i na što paziti kod mirisnih formula s eteričnim uljima.",
                 "L'Occitane for sensitive skin: my experience with its skincare on rosacea-prone skin and what to watch for in fragranced formulas."),
        "about": ("""<p>L'Occitane en Provence je francuski brend poznat po shea maslacu, smilju i biljnim sastojcima iz Provanse. Mnoge formule imaju izražen miris i eterična ulja, koja su kod rozacee i reaktivne kože čest okidač crvenila.</p>
<p>Njihov booster za lice mojoj koži nije odgovarao. Kreme za ruke i tijelo su sigurniji izbor nego njega lica ako imate osjetljivo lice.</p>""",
                  """<p>L'Occitane en Provence is a French brand known for shea butter, immortelle and botanical ingredients from Provence. Many formulas are noticeably scented and contain essential oils, which are a common redness trigger for rosacea and reactive skin.</p>
<p>Their face booster didn't suit my skin. Hand and body creams are a safer choice than facial skincare if your face is sensitive.</p>"""),
    },
    "La Roche-Posay": {
        "desc": ("La Roche-Posay i rozacea: Cicaplast Baume B5+ i njega za osjetljivu kožu iz ljekarne, iskreno testirani na koži sklonoj crvenilu.",
                 "La Roche-Posay and rosacea: Cicaplast Baume B5+ and pharmacy skincare for sensitive skin, honestly tested on skin prone to redness."),
        "about": ("""<p>La Roche-Posay je francuski dermokozmetički brend grupe L'Oréal, nastao uz termalni izvor bogat selenom. Za osjetljivu kožu tu su linije Toleriane i Cicaplast, za crvenilo i rozaceu Rosaliac, a Anthelios je jedan od najpoznatijih ljekarničkih SPF-ova.</p>
<p>Cicaplast Baume B5+ je moj sigurni izbor kad je koža nadražena: odmah je smiri i ne peče. Za kožu s rozaceom ovo je jedan od brendova kojima najviše vjerujem.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Za Cicaplast Baume B5+ brend ne navodi patent (Tribioma opisuje kao ekskluzivni prebiotik), ali navodi testove na 14 stanja kože. Na 52 bebe (4 do 34 mjeseca) nakon 4 tjedna kod svih je koža bila smirena. Na 42 odrasle osobe nakon lasera 97&nbsp;% je osjetilo veću ugodu, a kod 60&nbsp;% crvenilo je brže nestalo. Studija o Rosaliac AR kod rozacee objavljena je u časopisu Journal of Drugs in Dermatology 2013.</p>""",
                  """<p>La Roche-Posay is a French dermocosmetic brand from the L'Oréal group, built around a selenium-rich thermal spring. Toleriane and Cicaplast are its lines for sensitive skin, Rosaliac targets redness and rosacea, and Anthelios is one of the best-known pharmacy sunscreens.</p>
<p>Cicaplast Baume B5+ is my safe choice when my skin is irritated: it calms it instantly and doesn't sting. For rosacea-prone skin, this is one of the brands I trust most.</p>
<p><strong>Patents and testing (according to the brand):</strong> La Roche-Posay doesn't claim a patent for Cicaplast Baume B5+ (it calls Tribioma an exclusive prebiotic), but says it was tested on 14 skin conditions. In 52 babies (4 to 34 months), every participant's skin was soothed after 4 weeks. In 42 adults after laser treatment, 97% felt more comfortable and redness faded faster in 60%. A study of Rosaliac AR on rosacea-prone skin was published in the Journal of Drugs in Dermatology in 2013.</p>"""),
    },
    "Ladria": {
        "desc": ("Ladria recenzije: jastučići za područje oko očiju testirani na osjetljivoj koži 30+. Iskreno iskustvo i ocjena.",
                 "Ladria reviews: under-eye pads tested on sensitive 30+ skin. An honest experience and rating."),
        "about": ("""<p>Ladria je brend njege čiji su jastučići za područje oko očiju postali dio moje rutine. Koža oko očiju je najtanja i najosjetljivija na licu, pa kod reaktivne kože biram proizvode bez jakog mirisa koji ne peku i ne zamagljuju oči.</p>
<p>Ladria jastučiće kupujem ponovno, a detaljna recenzija stiže uskoro.</p>""",
                  """<p>Ladria is a skincare brand whose under-eye pads have become part of my routine. The skin around the eyes is the thinnest and most sensitive on the face, so with reactive skin I choose products without strong fragrance that don't sting or blur my vision.</p>
<p>I repurchase the Ladria pads, and a detailed review is coming soon.</p>"""),
    },
    "NARS": {
        "desc": ("NARS recenzije: kultni bronzer Laguna i šminka za svijetlu, osjetljivu kožu sklonu crvenilu. Iskreno iskustvo.",
                 "NARS reviews: the cult Laguna bronzer and make-up for fair, sensitive skin prone to redness. An honest experience."),
        "about": ("""<p>NARS je američki brend šminke koji je osnovao vizažist François Nars, danas dio grupe Shiseido. Poznat je po rumenilima, bronzerima i podlogama. Kod kože s rozaceom bronzer i rumenilo pomažu da crvenilo izgleda kao prirodan ten, ali birajte nijanse bez previše narančastog i šljokica.</p>
<p>Bronzer u nijansi Laguna je moj stalni favorit.</p>""",
                  """<p>NARS is an American make-up brand founded by make-up artist François Nars and now part of Shiseido. It is known for its blushes, bronzers and foundations. On rosacea-prone skin, bronzer and blush help redness read as a natural flush, but choose shades without too much orange or glitter.</p>
<p>The Laguna bronzer is a permanent favourite of mine.</p>"""),
    },
    "Olaplex": {
        "desc": ("Olaplex recenzije: No. 3 Hair Perfector za oštećenu kosu, iz perspektive osjetljive kože lica i vlasišta.",
                 "Olaplex reviews: No. 3 Hair Perfector for damaged hair, from the point of view of sensitive facial skin and scalp."),
        "about": ("""<p>Olaplex je američki brend za njegu kose poznat po tehnologiji koja obnavlja veze u oštećenoj kosi. Kod osjetljive kože lica i rozacee kod proizvoda za kosu pazim da ne dolaze na lice i liniju kose, pa ih ispiram prije umivanja.</p>
<p>Olaplex No. 3 je proizvod koji kupujem iznova.</p>""",
                  """<p>Olaplex is an American hair care brand known for technology that repairs broken bonds in damaged hair. With sensitive facial skin and rosacea I make sure hair products don't reach my face and hairline, and I rinse them off before washing my face.</p>
<p>Olaplex No. 3 is a product I keep repurchasing.</p>"""),
    },
    "Olival": {
        "desc": ("Olival i rozacea: hrvatska prirodna kozmetika testirana na osjetljivoj koži. Amino gel i hidrator u spreju, ali i što mi nije odgovaralo.",
                 "Olival and rosacea: Croatian natural skincare tested on sensitive skin. The amino gel and hydrating mist, plus what didn't suit me."),
        "about": ("""<p>Olival je hrvatski brend prirodne kozmetike s maslinovim uljem, smiljem i drugim biljnim sastojcima, a Professional linija nudi i blaže formule za osjetljivu kožu. Prirodno nije automatski nježno: eterična ulja i biljni ekstrakti kod rozacee mogu izazvati crvenilo.</p>
<p>Olival Professional amino gel je dio moje večernje rutine, a hidrator u spreju kupujem ponovno. Krema od smilja i Olival SPF 30 mojoj koži nisu odgovarali.</p>""",
                  """<p>Olival is a Croatian natural skincare brand built on olive oil, immortelle and other botanicals, and its Professional line offers gentler formulas for sensitive skin. Natural isn't automatically gentle, though: essential oils and plant extracts can trigger redness in rosacea.</p>
<p>The Olival Professional amino gel is part of my evening routine and I repurchase the hydrating mist. The immortelle cream and Olival SPF 30 didn't suit my skin.</p>"""),
    },
    "Omnilux": {
        "desc": ("Omnilux Contour Face LED maska i rozacea: crveno i blisko infracrveno svjetlo u kućnoj rutini za osjetljivu kožu 30+. Iskustvo i specifikacije.",
                 "Omnilux Contour Face LED mask and rosacea: red and near-infrared light in an at-home routine for sensitive 30+ skin. Experience and specs."),
        "about": ("""<p>Omnilux je brend LED uređaja s crvenim i bliskim infracrvenim svjetlom, a Contour Face je fleksibilna maska za kućnu upotrebu. LED terapija ne koristi aktivne sastojke na koži, pa je zanimljiva opcija za reaktivnu kožu koja teško podnosi kiseline i retinoide.</p>
<p>Maska je najveća investicija u mojoj rutini za rozaceu. Ako imate rozaceu ili uzimate lijekove koji povećavaju osjetljivost na svjetlo, LED terapiju prvo dogovorite s dermatologom.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Contour Face je odobren od američke FDA (FDA cleared) i koristi crveno svjetlo od 633&nbsp;nm i blisko infracrveno od 830&nbsp;nm iz 132 LED diode. Proizvođač navodi studiju na 25 sudionika (3 tretmana tjedno, 4 tjedna), ali rezultate su procjenjivali sami sudionici i studija nije objavljena.</p>""",
                  """<p>Omnilux makes LED devices with red and near-infrared light, and Contour Face is its flexible mask for home use. LED therapy puts no actives on the skin, which makes it an interesting option for reactive skin that struggles with acids and retinoids.</p>
<p>The mask is the biggest investment in my rosacea routine. If you have rosacea or take medication that increases light sensitivity, talk to your dermatologist before starting LED therapy.</p>
<p><strong>Patents and testing (according to the brand):</strong> Contour Face is FDA cleared and uses 633&nbsp;nm red and 830&nbsp;nm near-infrared light from 132 LEDs. The brand cites a study on 25 participants (3 treatments a week for 4 weeks), but results were self-reported and the study isn't published.</p>"""),
    },
    "Paula's Choice": {
        "desc": ("Paula's Choice i rozacea: SPF bez parfema, 2% BHA i azelaic booster testirani na osjetljivoj koži. Što je prošlo, a što ne.",
                 "Paula's Choice and rosacea: fragrance-free SPF, 2% BHA and azelaic booster tested on sensitive skin. What passed and what didn't."),
        "about": ("""<p>Paula's Choice je američki brend koji je osnovala Paula Begoun, poznat po formulama bez parfema i proizvodima s kiselinama, posebno 2% BHA tekućem pilingu. Za crvenilo postoji linija Calm, a azelaična kiselina se često preporučuje kod rozacee.</p>
<p>Super-Light Daily Wrinkle Defense SPF 30 mi je drugi u poretku mineralnih SPF-ova. Salicilna kiselina, i u 2% BHA i u Azelaic Acid Boosteru, mojoj koži s rozaceom nije odgovarala.</p>""",
                  """<p>Paula's Choice is an American brand founded by Paula Begoun, known for fragrance-free formulas and acid products, especially the 2% BHA liquid exfoliant. The Calm line is aimed at redness, and azelaic acid is often recommended for rosacea.</p>
<p>Super-Light Daily Wrinkle Defense SPF 30 is second in my mineral SPF ranking. Salicylic acid, in both the 2% BHA and the Azelaic Acid Booster, didn't suit my rosacea-prone skin.</p>"""),
    },
    "Revox": {
        "desc": ("Revox recenzije: pristupačna njega lica testirana na osjetljivoj koži sklonoj rozacei. Iskreno iskustvo s hidratantnom kremom.",
                 "Revox reviews: affordable skincare tested on sensitive skin prone to rosacea. An honest experience with the moisturiser."),
        "about": ("""<p>Revox je pristupačan brend njege lica poznat po jednostavnim formulama s istaknutim aktivnim sastojkom na pakiranju. Niska cijena čini ga zanimljivim za isprobavanje, ali kod osjetljive kože i rozacee uvijek provjerite sastav i postotak aktivnih sastojaka.</p>
<p>Njihova hidratantna krema mojoj koži nije odgovarala.</p>""",
                  """<p>Revox is an affordable skincare brand known for simple formulas with the key active ingredient printed on the pack. The low price makes it tempting to try, but with sensitive skin and rosacea always check the ingredient list and the percentage of actives.</p>
<p>Their moisturiser didn't suit my skin.</p>"""),
    },
    "Rhode": {
        "desc": ("Rhode recenzije: Pocket Blush i Peptide Lip Shape brenda Hailey Bieber testirani na osjetljivoj koži sklonoj crvenilu. Vrijedi li hype?",
                 "Rhode reviews: Hailey Bieber's Pocket Blush and Peptide Lip Shape tested on sensitive skin prone to redness. Is it worth the hype?"),
        "about": ("""<p>Rhode je brend Hailey Bieber, poznat po minimalističkom pakiranju, peptidnim proizvodima za usne i glow izgledu. Kremasti proizvodi poput Pocket Blusha dobro sjedaju na osjetljivu kožu jer se nanose prstima, bez trljanja kistom.</p>
<p>Pocket Blush u nijansi Tan Line me potpuno osvojio i ne iritira mi kožu. Peptide Lip Shape olovka me razočarala, a nijanse su pretamne za svijetlu put.</p>""",
                  """<p>Rhode is Hailey Bieber's brand, known for minimalist packaging, peptide lip products and a glowy look. Cream products like Pocket Blush suit sensitive skin well because you apply them with your fingers, without rubbing a brush over the skin.</p>
<p>Pocket Blush in Tan Line won me over completely and doesn't irritate my skin. The Peptide Lip Shape pencil disappointed me, and the shades are too dark for fair skin.</p>"""),
    },
    "Skintegra": {
        "desc": ("Skintegra Ros/Ac i rozacea: hrvatska dermokozmetika za kožu sklonu crvenilu i nečistoćama, testirana na osjetljivoj koži.",
                 "Skintegra Ros/Ac and rosacea: Croatian dermocosmetics for skin prone to redness and breakouts, tested on sensitive skin."),
        "about": ("""<p>Skintegra je hrvatski dermokozmetički brend usmjeren na problematičnu i osjetljivu kožu. Za kožu s rozaceom i nečistoćama najzanimljiviji je proizvod Ros/Ac, namijenjen smirivanju crvenila i upaljenih promjena.</p>
<p>Skintegra Ros/Ac je među proizvodima koje kupujem ponovno, a detaljna recenzija stiže uskoro.</p>""",
                  """<p>Skintegra is a Croatian dermocosmetic brand focused on problem-prone and sensitive skin. For skin with rosacea and breakouts its most interesting product is Ros/Ac, designed to calm redness and inflamed spots.</p>
<p>Skintegra Ros/Ac is one of my repurchases, and a detailed review is coming soon.</p>"""),
    },
    "Sweed": {
        "desc": ("Sweed recenzije: Lash Serum i maskara testirani na osjetljivim očima i koži sklonoj crvenilu. Iskreno iskustvo.",
                 "Sweed reviews: Lash Serum and mascara tested on sensitive eyes and skin prone to redness. An honest experience."),
        "about": ("""<p>Sweed je švedski brend proizvoda za trepavice i obrve, poznat po serumu za rast trepavica i maskarama. Kod osjetljive kože i očiju serume za trepavice nanosite samo uz liniju trepavica i prekinite korištenje ako se pojavi crvenilo ili peckanje.</p>
<p>Sweed Lash Serum i Sweed maskara su mi među proizvodima koje kupujem iznova.</p>""",
                  """<p>Sweed is a Swedish lash and brow brand known for its lash growth serum and mascaras. With sensitive skin and eyes, apply lash serums only along the lash line and stop if you notice redness or stinging.</p>
<p>Sweed Lash Serum and Sweed mascara are among my repurchases.</p>"""),
    },
    "Vichy": {
        "desc": ("Vichy i osjetljiva koža: Minéral serum s vulkanskom vodom testiran na koži 30+ sklonoj rozacei. Iskreno iskustvo iz ljekarne.",
                 "Vichy for sensitive skin: Minéral serum with volcanic water tested on 30+ skin prone to rosacea. An honest pharmacy experience."),
        "about": ("""<p>Vichy je francuski dermokozmetički brend grupe L'Oréal, nastao oko vulkanske termalne vode iz Vichyja. Linija Minéral 89 s hijaluronskom kiselinom je kratka i jednostavna, pa je dobar izbor za osjetljivu kožu koja treba hidrataciju bez puno sastojaka.</p>
<p>Vichy Minéral serum je u mojoj rutini i kupujem ga ponovno.</p>
<p><strong>Patenti i testiranja (prema proizvođaču):</strong> Minéral 89 testiran je u studiji na 1.630 osoba s kožnim problemima ili nakon estetskih tretmana. Nakon 4 tjedna crvenilo je nestalo ili se smanjilo kod 68 do 72&nbsp;% sudionika, a peckanje se smanjilo kod oko 85&nbsp;%. Patent za osjetljivu kožu brend ne navodi.</p>""",
                  """<p>Vichy is a French dermocosmetic brand from the L'Oréal group, built around volcanic thermal water from Vichy. The Minéral 89 line with hyaluronic acid is short and simple, which makes it a good choice for sensitive skin that needs hydration without a long ingredient list.</p>
<p>Vichy Minéral serum is part of my routine and I keep buying it again.</p>
<p><strong>Patents and testing (according to the brand):</strong> Minéral 89 was tested in a study on 1,630 people with skin conditions or after aesthetic procedures. After 4 weeks, redness cleared or improved in 68 to 72% of participants and stinging decreased in about 85%. The brand doesn't claim a sensitive-skin patent.</p>"""),
    },
}
