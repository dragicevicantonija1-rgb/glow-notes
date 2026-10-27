# Instagram objave: jedna po članku. Slika se gradi iz polja ispod (make_instagram.py), opis i hashtagovi idu u opisi.md.
# naslov: *riječ* = roza kurziv. ton: top / ok / flop (boja značke). tocke: (+ ili -, tekst), najviše 3.

ZAJEDNICKI = ["#glownotes", "#beautyrecenzija", "#hrvatskabeauty", "#skincarehrvatska", "#osjetljivakoza"]

OBJAVE = [
    {
        "slug": "mineralni-spf-recenzije-poredak", "oznaka": "Poredak", "ton": "top",
        "naslov": "6 mineralnih SPF-ova, od *svetog grala* do promašaja",
        "lista": ["Babé Super Fluid Color SPF 50", "Paula's Choice Super-Light SPF 30", "Bioderma Nude Touch SPF 50+",
                  "Avène Tinted Mineral Fluid", "Avène Mineral Fluid (bez boje)", "Bioderma Photoderm Mineral"],
        "opis": """Mineralni SPF koji ne izgleda kao bijela maska i ne isušuje? Za mene je to godinama bila prava potraga 🧴

Isprobala sam šest i poredala ih od favorita do potpunog promašaja:
1️⃣ Babé Super Fluid Color SPF 50, moj sveti gral
2️⃣ Paula's Choice Super-Light SPF 30, elegantan, ali skup
3️⃣ Bioderma Nude Touch, nikako mi ne stoji
4️⃣ Avène Tinted Mineral, puno pretaman
5️⃣ Avène Mineral Fluid, samo nakon tretmana
6️⃣ Bioderma Photoderm Mineral, završio u smeću

Savjet za jako svijetle: toniranu Babé verziju miješam s netoniranom i dobijem savršenu nijansu ✨

Cijeli poredak s iskustvom za svaki je na glownotes.eu, link je u bio.
Koji je vaš mineralni SPF koji stvarno volite? 👇""",
        "hashtagovi": ["#mineralnispf", "#spfzalice", "#spf50", "#zastitaodsunca", "#rozacea", "#svijetlaput", "#sunscreen", "#mineralsunscreen", "#babe", "#bioderma", "#avene"],
    },
    {
        "slug": "proizvodi-koji-nisu-odgovarali-rozacea", "oznaka": "Flop", "ton": "flop",
        "naslov": "12 hvaljenih proizvoda koji su mojoj rozacei bili *promašaj*",
        "lista": ["CeraVe umivalice i krema", "Kiehl's vitamin C serum", "Biologique Recherche P50W",
                  "Paula's Choice 2% BHA", "Olival krema od smilja", "Erborian Red CC krema"],
        "opis": """Svi ih preporučuju baš za osjetljivu kožu i rozaceu. Meni nisu odgovarali 🙈

Na listi su CeraVe umivalice i krema, Kiehl's vitamin C serum i Super Serum, Biologique Recherche P50W, Paula's Choice Azelaic Acid Booster i 2% BHA, Revox, Olival krema od smilja i SPF 30, L'Occitane booster i Erborian Red CC krema.

Ne kažem da su loši. Svaka koža je priča za sebe, a moja je reaktivna i s rozaceom. Ako je i vaša takva, možda vam ova lista uštedi novac 💸

Za svaki proizvod sam napisala što se točno dogodilo, sve je na glownotes.eu, link u bio.
Koji hit proizvod je vama bio najveće razočaranje? 👇""",
        "hashtagovi": ["#rozacea", "#reaktivnakoza", "#beautyflop", "#antipreporuke", "#cerave", "#kiehls", "#paulaschoice", "#rosacea", "#sensitiveskin", "#skincareflop"],
    },
    {
        "slug": "proizvodi-koje-cu-ponovno-kupiti", "oznaka": "Favoriti", "ton": "top",
        "naslov": "16 proizvoda koje *kupujem iznova*",
        "lista": ["Kiehl's Ultra Facial Cream", "Babé tonirani fluid SPF 50", "Skintegra Ros/Ac",
                  "IT Cosmetics CC krema", "NARS Laguna bronzer", "Olaplex No. 3"],
        "opis": """Moji ride or die favoriti 💗 Proizvodi koje sam kupila više puta i bez razmišljanja ću ih kupiti opet.

Za lice: Olival hidrator u spreju, Kiehl's Ultra Facial Cream, Vichy Minéral serum, Babé tonirani SPF 50, Skintegra Ros/Ac, Clinique Smart Clinical Repair i Kiehl's krema oko očiju s avokadom.
Šminka: IT Cosmetics CC krema, NARS Laguna, Catrice olovka za obrve i Sweed maskara.
Kosa i tijelo: Olaplex No. 3, Kérastase Masquintense i CeraVe SA krema.

Svi su prošli test moje osjetljive kože s rozaceom ✨

Cijela lista s razlozima zašto ih volim je na glownotes.eu, link u bio.
Što je kod vas proizvod koji uvijek kupujete ponovno? 👇""",
        "hashtagovi": ["#beautyfavoriti", "#ridiordie", "#holygrail", "#kiehls", "#narslaguna", "#itcosmetics", "#olaplex", "#koza30plus", "#rozacea", "#skincareroutine"],
    },
    {
        "slug": "moj-glow-up-rutina-rozacea", "oznaka": "Rutina", "ton": "top",
        "naslov": "Moj *glow up*: rutina koja je promijenila moju kožu",
        "lista": ["Bioderma Sensibio H2O", "Olival amino gel i PMD (navečer)", "Skinoren gel ujutro",
                  "Soolantra navečer", "La Roche-Posay Cicaplast", "Omnilux LED maska"],
        "opis": """Rutina koja je stvarno promijenila moju kožu s rozaceom ✨

Korak po korak:
1. Bioderma Sensibio H2O za prvo čišćenje
2. Olival amino gel i PMD uređaj, samo navečer
3. Skinoren gel ujutro
4. Soolantra navečer
5. La Roche-Posay Cicaplast
6. Omnilux Contour Face, crvena LED maska

Skinoren i Soolantra su lijekovi, pa ih koristim uz savjet dermatologa. Ovo je moje iskustvo, ne zamjena za pregled 🩺

Sve detalje, redoslijed i iskustvo s LED maskom pročitaj na glownotes.eu, link u bio.
Koristi li netko od vas crvenu LED masku? 👇""",
        "hashtagovi": ["#rozacea", "#rosacea", "#glowup", "#rutinanjege", "#ledmaska", "#omnilux", "#soolantra", "#skinoren", "#cicaplast", "#skincareroutine", "#koza30plus"],
    },
    {
        "slug": "babe-mineralni-spf-50-recenzija", "oznaka": "Recenzija", "ton": "top", "ocjena": 4,
        "naslov": "Babé mineralni SPF 50: moj *trenutni favorit*",
        "tocke": [("+", "Divno se razmazuje i ponovno nanosi"), ("+", "100 % mineralni, ne peče oči"), ("-", "Tonirana nijansa pretamna za jako svijetlu put")],
        "opis": """Babé Mineral Super Fluid SPF 50 je moj trenutni favorit među SPF-ovima ☀️

Što volim: divno se razmazuje (posebno tonirana verzija), lako ga ponovno nanosim preko dana, filteri su 100 % mineralni, bez parfema je i ne peče me za oči.

Što ne volim: tonirana nijansa je pretamna za jako svijetlu put, pakiranje zna curiti, netonirana verzija ponekad ima grudice, a titanov dioksid je u nano obliku.

Moja ocjena: 4/5 ⭐

Cijela recenzija, s trikom kako dobijem savršenu nijansu, je na glownotes.eu, link u bio.
Jeste li probali toniranu ili netoniranu verziju? 👇""",
        "hashtagovi": ["#babe", "#laboratoriosbabe", "#mineralnispf", "#spf50", "#spfzalice", "#rozacea", "#svijetlaput", "#mineralsunscreen"],
    },
    {
        "slug": "chanel-water-fresh-tint-recenzija", "oznaka": "Recenzija", "ton": "top", "ocjena": 4.5,
        "naslov": "Chanel Water-Fresh Tint: *your skin but better*",
        "tocke": [("+", "Ultralagan, koža kao da je upila vodu"), ("+", "Divan, prirodan sjaj"), ("-", "Medium je za zimu malo prejak")],
        "opis": """Chanel Les Beiges Water-Fresh Tint u nijansi Medium. Ovo je ona podloga nakon koje mi ljudi govore da imam ljepšu kožu 🥹

Lagano prekrivanje, koža izgleda nabubrelo i hidratizirano, kao da je upila vodu, a sjaj je divan i prirodan. Pravi your skin but better.

Mane: tijekom dana zna malo isušiti, a Medium mi je zimi malo prejak. Za mene je to ljetni ten.

Moja ocjena: 4,5/5 ⭐ i definitivno kupujem opet.

Usporedbu ljeto/zima i cijelo iskustvo pročitaj na glownotes.eu, link u bio.
Imate li ga? Koju nijansu nosite? 👇""",
        "hashtagovi": ["#chanel", "#chanelbeauty", "#waterfreshtint", "#lesbeiges", "#sminka", "#podloga", "#koza30plus", "#nomakeupmakeup", "#luksuznakozmetika"],
    },
    {
        "slug": "babe-lip-cheek-spf-50-mocca-recenzija", "oznaka": "Recenzija", "ton": "top", "ocjena": 4,
        "naslov": "Babé SPF 50 za usne i obraze: divna boja *Mocca*",
        "tocke": [("+", "Divna boja i divan sjaj"), ("+", "SPF 50 za usne i obraze u jednom"), ("-", "Malo ljepljiv, okus tipičan za SPF")],
        "opis": """Mali proizvod koji radi dvije stvari: boja za usne i obraze plus SPF 50 💋

Nijansa Mocca je divna, sjaj isto, a na Care to Beauty je i povoljan. Tekstura je okej, malo ljepljiva, a miris i okus su tipični za SPF.

Unatoč tome, kupila bih ga opet. Moja ocjena: 4/5 ⭐

Cijela recenzija je na glownotes.eu, link u bio.
Nosite li SPF na usnama? 👇""",
        "hashtagovi": ["#babe", "#lipandcheek", "#spfzausne", "#spf50", "#sminka", "#rumenilo", "#mocca", "#caretobeauty"],
    },
    {
        "slug": "bioderma-sensibio-h2o-micelarna-voda-recenzija", "oznaka": "Recenzija", "ton": "top", "ocjena": 5,
        "naslov": "Bioderma Sensibio H2O: *pedeseta bočica* i dalje prvi korak",
        "tocke": [("+", "Nježna za kožu s rozaceom"), ("+", "Skida šminku s lica i očiju"), ("+", "Bez mirisa, u svakoj ljekarni")],
        "opis": """Ovo je valjda moja pedeseta bočica 😅 Bioderma Sensibio H2O je i dalje moj prvi korak, svaki dan.

Nježna je za osjetljivu kožu s rozaceom, skida šminku s lica i očiju, bez mirisa je i ima je u svakoj ljekarni. A koža mi je ljepša otkad je koristim.

Mane? Iskreno, nemam ih.

Moja ocjena: 5/5 ⭐

Cijela recenzija je na glownotes.eu, link u bio.
Je li i vama micelarna prvi korak? 👇""",
        "hashtagovi": ["#bioderma", "#sensibio", "#micelarnavoda", "#ciscenjelica", "#rozacea", "#njegalica", "#ljekarnickakozmetika", "#holygrail"],
    },
    {
        "slug": "bioderma-photoderm-ar-spf-50-recenzija", "oznaka": "Recenzija", "ton": "ok", "ocjena": 3,
        "naslov": "Bioderma Photoderm AR: prekrije, ali crvenilo *nije smirio*",
        "tocke": [("+", "Nešto prekrije crvenilo"), ("-", "Ne razmazuje se lijepo"), ("-", "Kemijski, kao da mi je izazivao crvenilo")],
        "opis": """Tonirani SPF 50+ koji obećava manje crvenila. Kod mene je priča bila malo drukčija 🤔

Nešto prekrije, visoki je SPF i to je okej. Ali ne razmazuje se lijepo, filteri su kemijski i imala sam osjećaj da mi je zapravo izazivao crvenilo.

Moja ocjena: 3/5 ⭐ Nešto prekrije, pa okej, ali ne bih ga ponovno kupila za rozaceu.

Cijelo iskustvo je na glownotes.eu, link u bio.
Koji tonirani SPF vama najbolje prikrije crvenilo? 👇""",
        "hashtagovi": ["#bioderma", "#photoderm", "#toniranispf", "#spf50", "#rozacea", "#crvenilo", "#spfzalice"],
    },
    {
        "slug": "avene-b-protect-spf-50-recenzija", "oznaka": "Recenzija", "ton": "ok", "ocjena": 3,
        "naslov": "Avène B-Protect SPF 50+: dobar za ljeto, ali *isušuje*",
        "tocke": [("+", "Taman prekrivanje za ljeto"), ("+", "Malo prikrije crvenilo"), ("-", "Isušuje i nakuplja se tijekom dana")],
        "opis": """Avène B-Protect SPF 50+, tonirani SPF za osjetljivu kožu ☀️

Ljeti daje taman prekrivanje i malo prikrije crvenilo. Ali isušuje kožu, tijekom dana se nakuplja i vidi se da nosim nešto na licu. Filteri su kemijski i nije za nadograđivanje preko dana.

Moja ocjena: 3/5 ⭐ Nije loš, ali ima i boljih.

Cijela recenzija je na glownotes.eu, link u bio.
Kako vi obnavljate SPF preko šminke? 👇""",
        "hashtagovi": ["#avene", "#bprotect", "#toniranispf", "#spf50", "#osjetljivakoza", "#rozacea", "#ljetnanjega"],
    },
    {
        "slug": "avene-termalna-voda-rozacea-recenzija", "oznaka": "Flop", "ton": "flop", "ocjena": 2,
        "naslov": "Avène termalna voda: osvježava, ali mojoj rozacei *nije pomogla*",
        "tocke": [("+", "Lijepo osvježi u vrućim danima"), ("-", "Meni je dugotrajno izazivala crvenilo"), ("-", "Nije umirila kožu s rozaceom")],
        "opis": """Termalna voda koju mnogi preporučuju za rozaceu. Meni nije pomogla 💧

Lijepo osvježi i ugodna je kad je vruće, i to je sve. Umjesto da umiruje, meni je dugotrajno izazivala crvenilo.

Mnogima s rozaceom odgovara, pa ovo shvatite kao moje iskustvo, ne kao pravilo.

Moja ocjena: 2/5 ⭐

Cijela recenzija je na glownotes.eu, link u bio.
Pomaže li vama termalna voda? 👇""",
        "hashtagovi": ["#avene", "#termalnavoda", "#rozacea", "#rosacea", "#beautyflop", "#crvenilo", "#reaktivnakoza"],
    },
    {
        "slug": "avene-couvrance-tekuci-puder-recenzija", "oznaka": "Flop", "ton": "flop", "ocjena": 3,
        "naslov": "Avène Couvrance: lijep ten, ali *ne za moju kožu*",
        "tocke": [("+", "Lijep, ujednačen ten"), ("-", "Nema dovoljno svijetlu nijansu"), ("-", "Čini mi se da je izazivao papule")],
        "opis": """Avène Couvrance, korektivni tekući puder za osjetljivu kožu 🫧

Daje lijep, ujednačen ten i prikrije crvenilo. Ali nema dovoljno svijetlu nijansu za mene, a čini mi se da mi je izazivao papule i pustule.

Moja ocjena: 3/5 ⭐ Lijep ten, loša reakcija.

Cijelo iskustvo je na glownotes.eu, link u bio.
Koji puder vašoj osjetljivoj koži stvarno odgovara? 👇""",
        "hashtagovi": ["#avene", "#couvrance", "#puder", "#tekucipuder", "#sminka", "#rozacea", "#beautyflop", "#svijetlaput"],
    },
    {
        "slug": "avene-cicalfate-serum-recenzija", "oznaka": "Recenzija", "ton": "ok", "ocjena": 3,
        "naslov": "Avène Cicalfate+ serum: okej, ali *ništa posebno* za crvenilo",
        "tocke": [("+", "Okej hidratizira"), ("+", "Bez alkohola, silikona i parfema"), ("-", "Na crvenilu nisam vidjela razliku")],
        "opis": """Avène Cicalfate+ serum za obnovu kože 🧪

Okej hidratizira i formula je čista: bez alkohola, silikona i parfema. Ali na crvenilu nisam primijetila ništa posebno, a pumpica djeluje jeftino za tu cijenu.

Moja ocjena: 3/5 ⭐

Cijela recenzija je na glownotes.eu, link u bio.
Imate li serum koji vam stvarno smiri crvenilo? 👇""",
        "hashtagovi": ["#avene", "#cicalfate", "#serum", "#njegalica", "#rozacea", "#crvenilo", "#ljekarnickakozmetika"],
    },
    {
        "slug": "biologique-recherche-p50w-recenzija", "oznaka": "Flop", "ton": "flop", "ocjena": 2,
        "naslov": "Biologique Recherche P50W: kultni tonik, ali *preagresivan*",
        "tocke": [("+", "Kultni proizvod koji mnogima odgovara"), ("-", "Preagresivan za reaktivnu kožu"), ("-", "Nije odgovarao mojoj rozacei")],
        "opis": """P50W, najblaža verzija kultnog P50 tonika. I dalje preagresivna za moju kožu 😬

Ne kažem da je loš. Mnogima odgovara i s razlogom je kultni proizvod. Ali za reaktivnu kožu s rozaceom, kakva je moja, ovo je bilo previše.

Moja ocjena: 2/5 ⭐ Nije za moju kožu.

Cijela recenzija je na glownotes.eu, link u bio.
Jeste li probali neki P50? 👇""",
        "hashtagovi": ["#biologiquerecherche", "#p50", "#p50w", "#tonik", "#reaktivnakoza", "#rozacea", "#beautyflop", "#luksuznakozmetika"],
    },
    {
        "slug": "erborian-cc-red-correct-recenzija", "oznaka": "Flop", "ton": "flop", "ocjena": 2.5,
        "naslov": "Erborian CC Red Correct: divno prekriva, ali koža je poslije *crvenija*",
        "tocke": [("+", "Zeleni pigmenti stvarno neutraliziraju crvenilo"), ("-", "Nakon skidanja koža crvenija"), ("-", "Više papula i pustula")],
        "opis": """CC krema protiv crvenila koju svi hvale 💚

Dok je na licu, divno prekriva i zeleni pigmenti stvarno neutraliziraju crvenilo. Ali nakon skidanja koža mi je bila crvenija, s više papula i pustula. Uz to je SPF kemijski.

Moja ocjena: 2,5/5 ⭐ Nažalost, razočaranje.

Cijela recenzija je na glownotes.eu, link u bio.
Koja vam CC krema odgovara uz rozaceu? 👇""",
        "hashtagovi": ["#erborian", "#cccream", "#ccredcorrect", "#rozacea", "#crvenilo", "#sminka", "#beautyflop", "#reaktivnakoza"],
    },
    {
        "slug": "rhode-pocket-blush-tan-line-recenzija", "oznaka": "Recenzija", "ton": "top", "ocjena": 5,
        "naslov": "Rhode Pocket Blush Tan Line: *savršeno* rumenilo",
        "tocke": [("+", "Lako se razmazuje prstima"), ("+", "Ništa mi ne izaziva, ni uz rozaceu"), ("+", "Kao prirodno rumenilo od sunca")],
        "opis": """Rhode Pocket Blush u nijansi Tan Line. Savršeno rumenilo, i to nije pretjerivanje 🌸

Lako se razmazuje prstima, ništa mi ne izaziva ni na koži s rozaceom, izgleda kao prirodno rumenilo od sunca i na meni dugo traje. Plus, malo je i stane u svaki džep.

Mane? Iskreno, nemam ih.

Moja ocjena: 5/5 ⭐

Cijela recenzija je na glownotes.eu, link u bio.
Koja je vaša Rhode nijansa? 👇""",
        "hashtagovi": ["#rhode", "#rhodeskin", "#pocketblush", "#tanline", "#rumenilo", "#kremastorumenilo", "#sminka", "#rozacea"],
    },
    {
        "slug": "rhode-peptide-lip-shape-recenzija", "oznaka": "Recenzija", "ton": "ok", "ocjena": 3,
        "naslov": "Rhode olovka za usne: okej, ali *ništa posebno*",
        "tocke": [("+", "Lijepo se razmazuje"), ("-", "Nije precizna, nijanse pretamne"), ("-", "Catrice ima bolju i jeftiniju")],
        "opis": """Rhode Peptide Lip Shape, olovka za usne o kojoj svi pričaju 💄

Lijepo se razmazuje i formula je mekana. Ali nije precizna, a sve su mi nijanse nekako pretamne. Catriceina mekana olovka mi je bolji izbor, i to za puno manje novca.

Moja ocjena: 3/5 ⭐ Ništa posebno.

Cijela recenzija s jeftinijom alternativom je na glownotes.eu, link u bio.
Imate li omiljenu olovku za usne? 👇""",
        "hashtagovi": ["#rhode", "#rhodeskin", "#peptidelipshape", "#olovkazausne", "#lipliner", "#catrice", "#dupe", "#sminka"],
    },
]
