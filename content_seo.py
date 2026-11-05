# SEO naslovi (<title>) i meta opisi za Google, odvojeno od H1 i naslova na stranici.
# Google prikazuje ~60 znakova naslova i ~155 znakova opisa; duži se režu usred rečenice.
# Ključ je hrvatski slug članka, vrijednost (HR, EN). Ako članak nema unos, build.py ga automatski skraćuje.

SEO_TITLES = {
    "jane-iredale-hydropure-tinted-serum-recenzija": ("jane iredale HydroPure Tinted Serum recenzija i iskustvo", "jane iredale HydroPure Tinted Serum review"),
    "jane-iredale-hydropure-color-correcting-serum-recenzija": ("jane iredale HydroPure Color Correcting Serum recenzija", "jane iredale HydroPure Color Correcting Serum review"),
    "la-roche-posay-cicaplast-baume-b5-recenzija": ("La Roche-Posay Cicaplast Baume B5+ recenzija za rozaceu", "La Roche-Posay Cicaplast Baume B5+ review for rosacea"),
    "moj-glow-up-rutina-rozacea": ("Rutina za rozaceu: Omnilux LED maska, Soolantra, Skinoren", "Rosacea routine: Omnilux LED mask, Soolantra, Skinoren"),
    "babe-mineralni-spf-50-recenzija": ("Babé mineralni SPF 50 recenzija za osjetljivu kožu", "Babé Mineral SPF 50 review for sensitive skin"),
    "chanel-water-fresh-tint-recenzija": ("Chanel Water-Fresh Tint recenzija: nijansa Medium", "Chanel Water-Fresh Tint review: shade Medium"),
    "babe-lip-cheek-spf-50-mocca-recenzija": ("Babé Lip & Cheek SPF 50 Mocca recenzija", "Babé Lip & Cheek SPF 50 Mocca review"),
    "bioderma-sensibio-h2o-micelarna-voda-recenzija": ("Bioderma Sensibio H2O recenzija: micelarna voda", "Bioderma Sensibio H2O review for sensitive skin"),
    "bioderma-photoderm-ar-spf-50-recenzija": ("Bioderma Photoderm AR SPF 50+ recenzija za rozaceu", "Bioderma Photoderm AR SPF 50+ review for rosacea"),
    "avene-b-protect-spf-50-recenzija": ("Avène B-Protect SPF 50+ recenzija: tonirani SPF", "Avène B-Protect SPF 50+ review: tinted sunscreen"),
    "avene-termalna-voda-rozacea-recenzija": ("Avène termalna voda i rozacea: recenzija", "Avène Thermal Spring Water and rosacea: review"),
    "avene-couvrance-tekuci-puder-recenzija": ("Avène Couvrance tekući puder recenzija i iskustvo", "Avène Couvrance liquid foundation review"),
    "avene-cicalfate-serum-recenzija": ("Avène Cicalfate+ serum recenzija: crvenilo i hidratacija", "Avène Cicalfate+ serum review: redness and hydration"),
    "biologique-recherche-p50w-recenzija": ("Biologique Recherche P50W recenzija: osjetljiva koža", "Biologique Recherche P50W review for sensitive skin"),
    "erborian-cc-red-correct-recenzija": ("Erborian CC Red Correct recenzija na koži s rozaceom", "Erborian CC Red Correct review on rosacea skin"),
    "rhode-pocket-blush-tan-line-recenzija": ("Rhode Pocket Blush Tan Line recenzija i iskustvo", "Rhode Pocket Blush Tan Line review"),
    "rhode-peptide-lip-shape-recenzija": ("Rhode Peptide Lip Shape recenzija i jeftinija alternativa", "Rhode Peptide Lip Shape review and a cheaper dupe"),
    "mineralni-spf-recenzije-poredak": ("Najbolji mineralni SPF za osjetljivu kožu: 6 testiranih", "Best mineral SPF for sensitive skin: 6 tested, ranked"),
    "proizvodi-koji-nisu-odgovarali-rozacea": ("12 proizvoda za osjetljivu kožu koji mi nisu odgovarali", "12 popular products that failed my rosacea skin"),
    "proizvodi-koje-cu-ponovno-kupiti": ("Proizvodi koje ću ponovno kupiti: moji beauty favoriti", "Products I'll buy again: my beauty favourites"),
}

SEO_DESCRIPTIONS = {
    "jane-iredale-hydropure-tinted-serum-recenzija": (
        "Recenzija jane iredale HydroPure Tinted Seruma na osjetljivoj koži s rozaceom: prekrivanje, sastav, reakcija kože i usporedba s Chanelom. Ocjena 2,5/5.",
        "jane iredale HydroPure Tinted Serum on rosacea-prone skin: coverage, ingredients, how my skin reacted and how it compares to Chanel. Rating 2.5/5."),
    "jane-iredale-hydropure-color-correcting-serum-recenzija": (
        "Recenzija jane iredale Color Correcting Seruma na koži s rozaceom: koliko zeleni ton prikriva crvenilo i usporedba s Erborian CC Red Correct. Ocjena 3,5/5.",
        "jane iredale Color Correcting Serum on rosacea skin: how well the green tint hides redness and how it compares to Erborian CC Red Correct. Rating 3.5/5."),
    "la-roche-posay-cicaplast-baume-b5-recenzija": (
        "Recenzija Cicaplast Baume B5+ na koži s rozaceom: umirivanje, korištenje kao krema ujutro i navečer i kome je preteška. Ocjena 4,5/5.",
        "Cicaplast Baume B5+ on rosacea skin: instant soothing, using it as a moisturiser morning and night, and who may find it too heavy. Rating 4.5/5."),
    "moj-glow-up-rutina-rozacea": (
        "Moja rutina za rozaceu korak po korak: Omnilux LED maska, Soolantra navečer, Skinoren ujutro, Bioderma Sensibio i Cicaplast. Što mi je smirilo kožu.",
        "My rosacea routine step by step: Omnilux LED mask, Soolantra at night, Skinoren in the morning, Bioderma Sensibio and Cicaplast. What calmed my skin."),
    "babe-mineralni-spf-50-recenzija": (
        "Recenzija Babé mineralnog SPF-a 50, toniranog i netoniranog, na osjetljivoj koži s rozaceom: bijeli trag, ponovno nanošenje i sastav. Ocjena 4/5.",
        "Babé Mineral SPF 50, tinted and untinted, on sensitive skin with rosacea: white cast, reapplication, nano titanium dioxide and packaging. Rating 4/5."),
    "chanel-water-fresh-tint-recenzija": (
        "Recenzija Chanel Les Beiges Water-Fresh Tint u nijansi Medium: lagano prekrivanje, prirodni sjaj, suhoća tijekom dana i za koga je. Ocjena 4,5/5.",
        "Chanel Les Beiges Water-Fresh Tint in Medium: light coverage, plump skin, a natural glow, dryness during the day and who it suits. Rating 4.5/5."),
    "bioderma-sensibio-h2o-micelarna-voda-recenzija": (None,
        "Bioderma Sensibio H2O micellar water on sensitive skin and rosacea: my long-time favourite for removing make-up without rinsing. Rating 5/5."),
    "avene-termalna-voda-rozacea-recenzija": (None,
        "Avène Thermal Spring Water on rosacea and sensitive skin: it calms redness for many people, but long-term it made mine worse. Rating 2/5."),
    "biologique-recherche-p50w-recenzija": (
        "Recenzija Biologique Recherche P50W na reaktivnoj koži s rozaceom: sastav, kiseline i zašto mi kultni piling tonik nije odgovarao. Ocjena 2/5.",
        "Biologique Recherche Lotion P50W on reactive skin with rosacea: ingredients, acids and why the cult exfoliating toner didn't suit me. Rating 2/5."),
    "erborian-cc-red-correct-recenzija": (
        "Erborian CC Red Correct na koži s rozaceom: zelena CC krema lijepo prikriva crvenilo, ali kemijski SPF mi je izazvao papule. Ocjena 2,5/5.",
        "Erborian CC Red Correct on rosacea skin: the green CC cream hides redness beautifully, but its chemical SPF gave me papules. Rating 2.5/5."),
    "rhode-pocket-blush-tan-line-recenzija": (
        "Recenzija Rhode Pocket Blush Tan Line: kremasto rumenilo koje se lako razmazuje, izgleda kao prirodno rumenilo od sunca i ne iritira kožu. Ocjena 5/5.",
        "Rhode Pocket Blush in Tan Line: a cream blush that blends easily, looks like a natural sun flush and doesn't irritate sensitive skin. Rating 5/5."),
    "rhode-peptide-lip-shape-recenzija": (
        "Rhode Peptide Lip Shape: lako se razmazuje, ali nije precizna olovka, a nijanse su pretamne za svijetlu put. Jeftinija alternativa je Catrice. 3/5.",
        "Rhode Peptide Lip Shape: it blends nicely but isn't precise, and the shades are too dark for fair skin. A cheaper, better dupe is Catrice. 3/5."),
    "mineralni-spf-recenzije-poredak": (
        "6 mineralnih SPF-ova testiranih na svijetloj, osjetljivoj koži (Babé, Paula's Choice, Bioderma, Avène): koji ne ostavlja bijeli trag, a koji je promašaj.",
        "6 mineral sunscreens tested on fair, sensitive skin (Babé, Paula's Choice, Bioderma, Avène): which leaves no white cast and which ended up in the bin."),
    "proizvodi-koji-nisu-odgovarali-rozacea": (
        "CeraVe, Kiehl's, Paula's Choice, P50W i drugi: 12 često preporučenih proizvoda koji nisu odgovarali mojoj osjetljivoj, reaktivnoj koži s rozaceom.",
        None),
}
