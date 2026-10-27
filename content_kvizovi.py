# Beauty kvizovi. Svaki tekst je par (hrvatski, engleski).
# Svaki odgovor daje jedan bod rezultatu (ključ); pobjeđuje rezultat s najviše bodova, kod izjednačenja onaj koji je prvi u "results".
# Poveznice u rezultatima su hrvatske putanje; build.py ih u engleskoj verziji prepisuje.

QUIZZES = [
    {
        "slug": "kviz-tip-koze",
        "short": ("Osjetljiva, reaktivna, suha ili normalna? Pet pitanja do odgovora.", "Sensitive, reactive, dry or normal? Five questions to your answer."), "en_slug": "skin-type-quiz",
        "title": ("Kviz: koji je tvoj tip kože?", "Quiz: what's your skin type?"),
        "h1": ("Koji je tvoj tip kože?", "What's your skin type?"),
        "description": ("Kratki kviz od 5 pitanja: saznaj je li tvoja koža osjetljiva, reaktivna, suha ili normalna i koji proizvodi iz mojih recenzija joj odgovaraju.",
                        "A short 5-question quiz: find out whether your skin is sensitive, reactive, dry or normal, and which products from my reviews suit it."),
        "intro": ("Pet brzih pitanja o tome kako se tvoja koža ponaša svaki dan. Na kraju dobiješ svoj tip kože i proizvode iz mojih recenzija koji mu odgovaraju.",
                  "Five quick questions about how your skin behaves day to day. At the end you get your skin type and products from my reviews that suit it."),
        "questions": [
            (("Kako se koža osjeća sat vremena nakon umivanja?", "How does your skin feel an hour after cleansing?"), [
                (("Zategnuto i suho", "Tight and dry"), "suha"),
                (("Peče ili lagano crveni", "It stings or turns slightly red"), "osjetljiva"),
                (("Crvena je i topla, kao da gori", "Red and warm, as if it's burning"), "reaktivna"),
                (("Ugodno, ili malo masno u T-zoni", "Comfortable, or a bit oily in the T-zone"), "normalna"),
            ]),
            (("Što se dogodi kad isprobaš novi proizvod?", "What happens when you try a new product?"), [
                (("Gotovo nikad ništa", "Almost never anything"), "normalna"),
                (("Ponekad zapeče pa prođe", "Sometimes it stings, then it passes"), "osjetljiva"),
                (("Crvenilo ili točkice koje traju danima", "Redness or bumps that last for days"), "reaktivna"),
                (("Koža se počne ljuštiti", "My skin starts to peel"), "suha"),
            ]),
            (("Koliko često ti obrazi i nos pocrvene?", "How often do your cheeks and nose go red?"), [
                (("Rijetko", "Rarely"), "normalna"),
                (("Nakon umivanja, vjetra ili hladnoće", "After cleansing, wind or cold"), "osjetljiva"),
                (("Često, od sunca, topline, vina ili ljute hrane", "Often, from sun, heat, wine or spicy food"), "reaktivna"),
                (("Samo zimi, kad je koža suha", "Only in winter, when my skin is dry"), "suha"),
            ]),
            (("Kako ti puder ili tonirani SPF izgleda do kraja dana?", "How does your foundation or tinted SPF look by the end of the day?"), [
                (("Nakupi se na suhim dijelovima", "It clings to dry patches"), "suha"),
                (("Izgleda dobro, eventualno malo sjaja", "It looks fine, maybe a little shine"), "normalna"),
                (("Ispod njega se pojavi crvenilo", "Redness shows through"), "reaktivna"),
                (("Dobro, ali neki me proizvodi peku", "Fine, but some products sting"), "osjetljiva"),
            ]),
            (("Što najviše želiš od njege?", "What do you want most from skincare?"), [
                (("Da me ništa ne peče", "Nothing that stings"), "osjetljiva"),
                (("Manje crvenila", "Less redness"), "reaktivna"),
                (("Više hidratacije i manje finih linija", "More hydration and fewer fine lines"), "suha"),
                (("Sjaj i lijep ten", "Glow and a nice complexion"), "normalna"),
            ]),
        ],
        "results": {
            "osjetljiva": {
                "title": ("Osjetljiva koža", "Sensitive skin"),
                "text": ("Tvoja koža reagira peckanjem i zatezanjem, ali se brzo smiri. Biraj nježno čišćenje bez mirisa i uvodi jedan novi proizvod odjednom.",
                         "Your skin reacts with stinging and tightness but calms down quickly. Choose gentle, fragrance-free cleansing and introduce one new product at a time."),
                "links": ["/kategorije/osjetljiva-koza/", "/clanci/bioderma-sensibio-h2o-micelarna-voda-recenzija/", "/clanci/babe-mineralni-spf-50-recenzija/"],
            },
            "reaktivna": {
                "title": ("Reaktivna koža sklona crvenilu", "Reactive skin prone to redness"),
                "text": ("Tvoja koža burno reagira i crvenilo se zadržava. Takva je i moja koža s rozaceom, pa ćeš u mojim recenzijama naći najviše za sebe. Ako crvenilo ne prolazi, javi se dermatologu.",
                         "Your skin reacts strongly and redness lingers. My rosacea skin is the same, so you'll find the most for you in my reviews. If redness doesn't go away, see a dermatologist."),
                "links": ["/kategorije/reaktivna-koza/", "/clanci/moj-glow-up-rutina-rozacea/", "/clanci/proizvodi-koji-nisu-odgovarali-rozacea/"],
            },
            "suha": {
                "title": ("Suha koža (i koža 30+)", "Dry skin (and skin over 30)"),
                "text": ("Tvojoj koži nedostaje vlage, a puder se nakuplja na suhim dijelovima. Traži bogatiju hidrataciju i izbjegavaj proizvode koji isušuju.",
                         "Your skin lacks moisture and foundation clings to dry patches. Look for richer hydration and avoid drying products."),
                "links": ["/kategorije/koza-30-plus/", "/clanci/proizvodi-koje-cu-ponovno-kupiti/", "/clanci/avene-cicalfate-serum-recenzija/"],
            },
            "normalna": {
                "title": ("Normalna do mješovita koža", "Normal to combination skin"),
                "text": ("Sretnice! Tvoja koža rijetko reagira, pa možeš slobodnije isprobavati. Fokusiraj se na dobar SPF i proizvode koji daju sjaj.",
                         "Lucky you! Your skin rarely reacts, so you can experiment more freely. Focus on a good SPF and products that give glow."),
                "links": ["/kategorije/favoriti/", "/clanci/chanel-water-fresh-tint-recenzija/", "/clanci/rhode-pocket-blush-tan-line-recenzija/"],
            },
        },
    },
    {
        "slug": "kviz-koji-spf",
        "short": ("Mineralni ili kemijski, tonirani ili bez boje? Nađi svoj SPF.", "Mineral or chemical, tinted or untinted? Find your SPF."), "en_slug": "which-spf-quiz",
        "title": ("Kviz: koji SPF za lice ti odgovara?", "Quiz: which face SPF suits you?"),
        "h1": ("Koji SPF za lice ti odgovara?", "Which face SPF suits you?"),
        "description": ("Kviz od 5 pitanja koji ti pomaže odabrati SPF za lice: mineralni ili kemijski, tonirani ili bez boje, uz preporuke iz mojih recenzija.",
                        "A 5-question quiz to help you choose a face SPF: mineral or chemical, tinted or untinted, with picks from my reviews."),
        "intro": ("SPF je najvažniji korak njege, ali pravi je teško naći. Odgovori na pet pitanja i dobit ćeš preporuku na temelju SPF-ova koje sam stvarno isprobala.",
                  "SPF is the most important skincare step, but the right one is hard to find. Answer five questions and get a recommendation based on the sunscreens I've actually tried."),
        "questions": [
            (("Kako ti koža reagira na kemijske UV filtere?", "How does your skin react to chemical UV filters?"), [
                (("Crveni, peče ili dobijem točkice", "It goes red, stings or I get bumps"), "mineralni"),
                (("Ne znam, nisam primijetila", "I don't know, I haven't noticed"), "tonirani"),
                (("Bez problema", "No problem at all"), "kemijski"),
            ]),
            (("Kakav ti je ten?", "What's your skin tone?"), [
                (("Jako svijetao", "Very fair"), "mineralni"),
                (("Svijetao do srednji", "Fair to medium"), "tonirani"),
                (("Srednji ili preplanuo", "Medium or tanned"), "kemijski"),
            ]),
            (("Želiš li da SPF malo prekrije crvenilo?", "Do you want your SPF to cover some redness?"), [
                (("Ne, samo zaštitu", "No, just protection"), "mineralni"),
                (("Da, lagano ujednačavanje", "Yes, a light evening-out"), "tonirani"),
                (("Da, što više prekrivanja", "Yes, as much coverage as possible"), "kemijski"),
            ]),
            (("Koliko često nanosiš SPF preko dana?", "How often do you reapply SPF during the day?"), [
                (("Više puta, i preko šminke", "Several times, even over make-up"), "mineralni"),
                (("Ujutro i možda još jednom", "In the morning and maybe once more"), "tonirani"),
                (("Samo ujutro", "Only in the morning"), "kemijski"),
            ]),
            (("Što ti najviše smeta kod SPF-a?", "What bothers you most about SPF?"), [
                (("Peckanje očiju i crvenilo", "Stinging eyes and redness"), "mineralni"),
                (("Bijeli trag", "White cast"), "tonirani"),
                (("Masan ili težak osjećaj", "A greasy or heavy feel"), "kemijski"),
            ]),
        ],
        "results": {
            "mineralni": {
                "title": ("Mineralni SPF, po potrebi miješan s toniranim", "Mineral SPF, mixed with a tinted one if needed"),
                "text": ("Tvoja koža traži isključivo mineralne filtere. Moj favorit je Babé mineralni SPF 50: lijepo se razmazuje, ne peče oči i divno se ponovno nanosi. Toniranu i netoniranu verziju miješam za svijetlu put.",
                         "Your skin needs mineral filters only. My favourite is Babé mineral SPF 50: it spreads nicely, doesn't sting the eyes and reapplies beautifully. I mix the tinted and untinted versions for fair skin."),
                "links": ["/clanci/babe-mineralni-spf-50-recenzija/", "/clanci/mineralni-spf-recenzije-poredak/", "/kategorije/spf/"],
            },
            "tonirani": {
                "title": ("Tonirani mineralni SPF s laganim prekrivanjem", "Tinted mineral SPF with light coverage"),
                "text": ("Treba ti SPF bez bijelog traga koji lagano ujednači ten. Pogledaj tonirani Babé i Paula's Choice iz mog poretka mineralnih SPF-ova, i pazi da nijansa nije pretamna.",
                         "You need an SPF without a white cast that lightly evens out your tone. Check out tinted Babé and Paula's Choice from my mineral SPF ranking, and make sure the shade isn't too dark."),
                "links": ["/clanci/mineralni-spf-recenzije-poredak/", "/clanci/babe-mineralni-spf-50-recenzija/", "/kategorije/spf/"],
            },
            "kemijski": {
                "title": ("Tonirani SPF, može i s kemijskim filterima", "Tinted SPF, chemical filters are fine"),
                "text": ("Tvoja koža dobro podnosi kemijske filtere, pa imaš veći izbor toniranih SPF-ova s više prekrivanja. Pročitaj moje iskustvo s Avène B-Protect i Bioderma Photoderm AR prije kupnje.",
                         "Your skin tolerates chemical filters well, so you have a wider choice of tinted sunscreens with more coverage. Read my experience with Avène B-Protect and Bioderma Photoderm AR before you buy."),
                "links": ["/clanci/avene-b-protect-spf-50-recenzija/", "/clanci/bioderma-photoderm-ar-spf-50-recenzija/", "/kategorije/spf/"],
            },
        },
    },
    {
        "slug": "kviz-crvenilo-rozacea",
        "short": ("Prepoznaj okidače crvenila i saznaj što tvojoj koži treba.", "Spot your redness triggers and find out what your skin needs."), "en_slug": "redness-rosacea-quiz",
        "title": ("Kviz: je li tvoja koža sklona crvenilu i rozacei?", "Quiz: is your skin prone to redness and rosacea?"),
        "h1": ("Je li tvoja koža sklona crvenilu i rozacei?", "Is your skin prone to redness and rosacea?"),
        "description": ("Kviz od 5 pitanja o crvenilu, okidačima i reakcijama kože, uz savjete i proizvode iz mojih recenzija. Nije dijagnoza, nego poticaj da bolje upoznaš svoju kožu.",
                        "A 5-question quiz about redness, triggers and skin reactions, with tips and products from my reviews. It's not a diagnosis, just a nudge to get to know your skin better."),
        "intro": ("Imam rozaceu i znam koliko je teško shvatiti što koži smeta. Ovaj kviz ne postavlja dijagnozu, nego ti pomaže prepoznati obrasce. Dijagnozu može dati samo dermatolog.",
                  "I have rosacea and I know how hard it is to work out what upsets your skin. This quiz doesn't diagnose anything, it helps you spot patterns. Only a dermatologist can give a diagnosis."),
        "questions": [
            (("Koliko dugo traje crvenilo kad se pojavi?", "How long does redness last when it appears?"), [
                (("Nekoliko minuta", "A few minutes"), "nisko"),
                (("Sat ili dva", "An hour or two"), "srednje"),
                (("Satima, ili je stalno prisutno", "For hours, or it's always there"), "visoko"),
            ]),
            (("Pojavljuju li se na obrazima ili bradi sitne upaljene točkice?", "Do small inflamed bumps appear on your cheeks or chin?"), [
                (("Ne", "No"), "nisko"),
                (("Ponekad", "Sometimes"), "srednje"),
                (("Često, i nisu kao obične bubuljice", "Often, and they're not like regular spots"), "visoko"),
            ]),
            (("Vidiš li sitne crvene kapilare na nosu ili obrazima?", "Can you see small red capillaries on your nose or cheeks?"), [
                (("Ne", "No"), "nisko"),
                (("Par njih", "A few"), "srednje"),
                (("Da, dosta", "Yes, quite a lot"), "visoko"),
            ]),
            (("Pocrveniš li od topline, vina, ljute hrane ili sunca?", "Do you go red from heat, wine, spicy food or sun?"), [
                (("Ne više od drugih", "No more than anyone else"), "nisko"),
                (("Od nekih od toga", "From some of these"), "srednje"),
                (("Da, gotovo od svega", "Yes, from almost all of them"), "visoko"),
            ]),
            (("Kako ti koža reagira na kiseline, alkohol ili parfem u kozmetici?", "How does your skin react to acids, alcohol or fragrance in skincare?"), [
                (("Dobro ih podnosi", "It tolerates them well"), "nisko"),
                (("Ponekad zapeče", "Sometimes it stings"), "srednje"),
                (("Crveni i peče", "It goes red and burns"), "visoko"),
            ]),
        ],
        "results": {
            "nisko": {
                "title": ("Malo sklonosti crvenilu", "Low tendency to redness"),
                "text": ("Tvoja koža rijetko i kratko crveni. Ipak je štiti mineralnim SPF-om, jer sunce je jedan od najčešćih okidača crvenila.",
                         "Your skin rarely goes red, and not for long. Still, protect it with a mineral SPF, because sun is one of the most common redness triggers."),
                "links": ["/clanci/babe-mineralni-spf-50-recenzija/", "/kategorije/njega-lica/", "/kategorije/favoriti/"],
            },
            "srednje": {
                "title": ("Osjetljiva koža koja povremeno crveni", "Sensitive skin that sometimes goes red"),
                "text": ("Tvoja koža ima okidače. Prati što izaziva crvenilo, biraj nježnu njegu bez mirisa i kiselina i uvodi proizvode jedan po jedan.",
                         "Your skin has triggers. Track what causes redness, choose gentle skincare without fragrance and acids, and introduce products one at a time."),
                "links": ["/kategorije/osjetljiva-koza/", "/clanci/bioderma-sensibio-h2o-micelarna-voda-recenzija/", "/clanci/proizvodi-koji-nisu-odgovarali-rozacea/"],
            },
            "visoko": {
                "title": ("Izražena sklonost crvenilu: vrijedi otići dermatologu", "Strong tendency to redness: worth seeing a dermatologist"),
                "text": ("Tvoji odgovori podsjećaju na ono što ja imam s rozaceom. Najvažniji korak je pregled kod dermatologa, jer rozacea se liječi i terapija stvarno pomaže. U međuvremenu pogledaj moju rutinu i listu proizvoda koji su mi bili promašaj.",
                         "Your answers sound a lot like my rosacea. The most important step is seeing a dermatologist, because rosacea can be treated and the treatment really helps. In the meantime, have a look at my routine and my list of products that were flops for me."),
                "links": ["/clanci/moj-glow-up-rutina-rozacea/", "/kategorije/rozacea/", "/clanci/proizvodi-koji-nisu-odgovarali-rozacea/"],
            },
        },
    },
]
