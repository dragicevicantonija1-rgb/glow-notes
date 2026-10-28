# English version (British English, for EU readers). Keys are the Croatian slugs;
# each entry overrides the text fields of the Croatian original. "slug" is the English URL slug.
# Internal links in bodies keep Croatian paths (/clanci/...), build.py maps them to /en/... URLs.

SITE_EN = {
    "tagline": "Honest beauty reviews from Rhode to Chanel, tested on sensitive skin",
    "author_bio": "I'm in my thirties, a beauty lover with sensitive, reactive skin with rosacea and a fair complexion. I've been testing skincare and make-up on my own skin for years and only write about products I've actually used.",
}

CATEGORIES_EN = {
    "njega-lica": {
        "slug": "skincare", "name": "Skincare",
        "short": "Creams, serums and cleansers, from pharmacy to luxury.",
        "title": "Skincare reviews – creams, serums and cleansers",
        "description": "Honest skincare reviews: creams, serums, cleansers and toners, from pharmacy brands to Rhode, Kiehl's and luxury classics, tested on sensitive skin.",
        "intro": """<p>Creams, serums, cleansers and toners I've tried, from pharmacy classics to TikTok hits and luxury brands. For every product I write what the brand claims and how it actually behaved on my skin.</p>""",
    },
    "sminka": {
        "slug": "makeup", "name": "Make-up",
        "short": "Skin tints, bronzers, mascaras and brows I actually wear.",
        "title": "Make-up reviews – skin tints, bronzers and mascaras",
        "description": "Honest make-up reviews: CC creams, skin tints, blushers, bronzers and lip liners, from the drugstore to Chanel, NARS and Rhode.",
        "intro": """<p>The make-up I wear every day and the make-up that let me down. I'm especially picky about base and tinted products, because on fair skin prone to redness, shade and formula decide everything.</p>""",
    },
    "spf": {
        "slug": "spf", "name": "SPF",
        "short": "Mineral and chemical SPF without white cast or stinging.",
        "title": "Face SPF reviews – mineral and chemical sunscreens",
        "description": "Honest face sunscreen reviews: mineral and tinted SPF for fair, sensitive skin and rosacea, without a white cast.",
        "intro": """<p>Good sun protection is the most important step in any routine, but finding an SPF that leaves no white cast, doesn't sting the eyes and doesn't dry the skin is a challenge. This is where I collect everything I've tried.</p>""",
    },
    "koza-30-plus": {
        "slug": "skin-30-plus", "name": "Skin 30+",
        "short": "First lines, loss of glow and care that doesn't irritate.",
        "title": "Skincare for 30+ – cream and serum reviews",
        "description": "Honest skincare reviews for skin over 30: anti-wrinkle creams, eye creams and serums tested on sensitive skin prone to redness.",
        "intro": """<p>After thirty, skin changes. It renews more slowly, loses moisture faster, and the fine lines around the eyes are no longer just from laughing. If it's sensitive too, choosing skincare becomes a small project: many “anti-ageing” products contain strong actives and fragrance that quickly throw reactive skin off balance.</p>
<p>In this category I collect the creams, serums and eye products I've tried on my 30+ skin. The focus is on what gives visible results without redness, stinging or peeling.</p>""",
    },
    "osjetljiva-koza": {
        "slug": "sensitive-skin", "name": "Sensitive skin",
        "short": "Stinging, tightness and products that don't upset it.",
        "title": "Sensitive skin – experiences and product reviews",
        "description": "Honest reviews of products for sensitive skin: cleansers, creams, serums and mineral SPF that do (or don't) sting.",
        "intro": """<p>Sensitive skin reacts to things other people never notice: it stings after cleansing, feels tight, turns red from fragrance or a new cream. The biggest challenge is that “for sensitive skin” is printed on almost every pack, while real experience is often different.</p>
<p>Here I write about products I've tried on my own sensitive skin: what worked, what went to a friend and what went in the bin. No paid reviews and no sugar-coating.</p>""",
    },
    "rozacea": {
        "slug": "rosacea", "name": "Rosacea",
        "short": "Redness, broken capillaries and care that calms.",
        "title": "Rosacea – skincare, products and personal experience",
        "description": "Personal experience with rosacea skincare: which products calm redness and which made my skin worse. Honest reviews.",
        "intro": """<p>Rosacea is a chronic skin condition that usually shows up as redness on the cheeks, nose and chin, and sometimes as small inflamed bumps. Triggers are very individual: sun, heat, alcohol in skincare, fragrance, acids.</p>
<p>I'm not a dermatologist and I don't give medical advice here. I share what I've learned over years of trial and error: which products helped my rosacea skin and which made it angry. If you suspect rosacea, the first step is always a dermatologist.</p>""",
    },
    "reaktivna-koza": {
        "slug": "reactive-skin", "name": "Reactive skin",
        "short": "Skin that reacts strongly to new products.",
        "title": "Reactive skin – what does (and doesn't) suit it",
        "description": "Reactive skin and skincare: experiences with products that cause redness and stinging, and the alternatives that turned out safer for me.",
        "intro": """<p>Reactive skin responds to change immediately: a new serum, strong wind or a facial and my face is red, hot and irritated. For me it overlaps with rosacea, so over time I learned to introduce one product at a time and read ingredient lists carefully.</p>
<p>This category holds reviews and lists of products that did or didn't suit my reactive skin, with a note on why I think that is.</p>""",
    },
    "favoriti": {
        "slug": "favourites", "name": "Favourites",
        "short": "Products I repurchase and can't live without.",
        "title": "Beauty favourites – products I repurchase",
        "description": "My beauty favourites: skincare, make-up and SPF I buy again and again, tested on sensitive skin with rosacea. Honest recommendations.",
        "intro": """<p>These are the products that passed the toughest test: I've bought them more than once and I'll buy them again. My skin is sensitive, reactive and prone to rosacea, so anything that makes it into the favourites has truly earned its place.</p>""",
    },
    "flop": {
        "slug": "flops", "name": "Flops",
        "short": "Hyped products that didn't work for me.",
        "title": "Beauty flops – products that disappointed me",
        "description": "Beauty flops: popular products for sensitive skin and rosacea that didn't suit me, with an explanation why. Honest, no sugar-coating.",
        "intro": """<p>Products that are often recommended but didn't suit me. For each one I explain why I think it failed, because “for sensitive skin” on the pack doesn't mean it will suit your skin. Maybe this list saves you some money.</p>""",
    },
}

ARTICLES_EN = {
    "mineralni-spf-recenzije-poredak": {
        "slug": "best-mineral-spf-sensitive-skin-ranked",
        "title": "Mineral SPF for fair, sensitive skin: 6 tested, ranked from best to worst",
        "h1": "The mineral sunscreens I've tried, from holy grail to total flop",
        "description": "An honest review of 6 mineral sunscreens for fair, sensitive skin: Babé, Paula's Choice, Bioderma and Avène. Which leaves no white cast and which ended up in the bin.",
        "excerpt": "Finding a mineral SPF that doesn't look like a white mask and doesn't dry you out is a constant battle. Here are my six, ranked from favourite to disaster.",
        "kicker": "Ranking",
        "verdict": "Winner: Babé Super Fluid Color SPF 50",
        "faq": [("What is the best mineral SPF for sensitive skin with rosacea?", "Of the six mineral sunscreens I've tried, my favourite is Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineral version). It spreads beautifully and doesn't sting my eyes."),
                ("Which mineral SPF leaves no white cast?", "Babé Super Fluid Sunscreen Color and Paula's Choice Super-Light Daily Wrinkle Defense SPF 30 leave no white cast on me. Bioderma Photoderm Mineral SPF 50+ left the most, and it also transferred onto clothes and objects."),
                ("Is tinted Babé SPF good for very fair skin?", "The tinted version is too dark for very fair skin. That's why I mix it with the untinted version from the same line to get the right shade."),
                ("Where can I buy Babé SPF for less?", "I order it from the Spanish pharmacy site Care to Beauty, where it's much cheaper than in Croatian pharmacies."),
                ("When should I use the untinted Avène Mineral Fluid SPF 50+?", "I keep it for after stronger treatments like microneedling, when the skin needs protection that sits on the surface. For everyday wear under make-up it's far too white.")],
        "itemlist": ["Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineral version)", "Paula's Choice Super-Light Daily Wrinkle Defense SPF 30",
                     "Bioderma Photoderm Nude Touch SPF 50+ (shade Claire/Light)", "Avène Tinted Mineral Fluid SPF 50+", "Avène Mineral Fluid SPF 50+ (untinted)",
                     "Bioderma Photoderm Mineral SPF 50+ (untinted)"],
        "body": """
<p class="lead">Finding a good mineral SPF, one that doesn't look like a white mask and doesn't dry you out, is a constant battle for me. So I put together a list of every one I've tried, ranked from favourite to total flop. I hope it saves someone with a fair or neutral complexion a bit of money and nerves.</p>

<div class="summary" role="note">
  <p class="summary__title">In short</p>
  <div class="table-wrap">
  <table>
    <thead><tr><th scope="col">#</th><th scope="col">Product</th><th scope="col">Verdict</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Babé Super Fluid Color SPF 50</td><td><span class="pill pill--good">Holy grail</span></td></tr>
      <tr><td>2</td><td>Paula's Choice Super-Light Daily Wrinkle Defense SPF 30</td><td><span class="pill pill--ok">Elegant but pricey</span></td></tr>
      <tr><td>3</td><td>Bioderma Photoderm Nude Touch SPF 50+</td><td><span class="pill pill--meh">Not for me</span></td></tr>
      <tr><td>4</td><td>Avène Tinted Mineral Fluid SPF 50+</td><td><span class="pill pill--meh">Too dark</span></td></tr>
      <tr><td>5</td><td>Avène Mineral Fluid SPF 50+ (untinted)</td><td><span class="pill pill--meh">Only after treatments</span></td></tr>
      <tr><td>6</td><td>Bioderma Photoderm Mineral SPF 50+</td><td><span class="pill pill--bad">In the bin</span></td></tr>
    </tbody>
  </table>
  </div>
</div>


<h2 id="babe">1. Laboratorios Babé Super Fluid Sunscreen Color SPF 50 (mineral version)</h2>
<!--IMG:foto-spf-1|Illustration of a tube: Babé Super Fluid Sunscreen Color SPF 50|Illustration: Babé Super Fluid Sunscreen Color SPF 50 (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> an ultra-light texture that absorbs quickly, enriched with prebiotic ingredients that strengthen the natural barrier and protect the skin microbiome.</p>
<p><strong>My experience: holy grail.</strong> By far the best mineral SPF I've tried. It spreads beautifully and doesn't sting my eyes at all, which is a huge plus for me. The only downside is that the tinted version isn't for us very fair girls. So I mix it with the regular, untinted version from the same line and get the perfect shade.</p>
<p class="tip"><strong>Tip:</strong> I order it from the Spanish site Care to Beauty because it's much cheaper there than in our pharmacies.</p>

<h2 id="paulas-choice">2. Paula's Choice Super-Light Daily Wrinkle Defense SPF 30</h2>
<!--IMG:foto-spf-2|Illustration of a tube: Paula's Choice Super-Light Daily Wrinkle Defense SPF 30|Illustration: Paula's Choice Super-Light Daily Wrinkle Defense SPF 30 (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> a tinted moisturiser with zinc oxide that leaves a matte finish and calms redness.</p>
<p><strong>My experience:</strong> a cosmetically very elegant product. It spreads nicely and leaves no classic white sheen, but the coverage is very, very light, just enough to even out the skin tone. The biggest minus is the price, it's too expensive. After a full day it can also dry out my face and cling to dry patches.</p>

<!--AD-->

<h2 id="bioderma-nude-touch">3. Bioderma Photoderm Nude Touch SPF 50+ (shade Claire/Light)</h2>
<!--IMG:foto-spf-3|Illustration of a tube: Bioderma Photoderm Nude Touch SPF 50+|Illustration: Bioderma Photoderm Nude Touch SPF 50+ (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> 100&nbsp;% mineral filters, shine control for up to 8 hours and a formula that evens out the complexion.</p>
<p><strong>My experience:</strong> sadly this one just doesn't suit me. The shade Claire isn't warm, it leans pink-neutral. I don't like the texture either: it's quite hard to spread and stays patchy on the face, applying unevenly.</p>

<h2 id="avene-tinted">4. Avène Tinted Mineral Fluid SPF 50+</h2>
<!--IMG:foto-spf-4|Illustration of a tube: Avène Tinted Mineral Fluid SPF 50+|Illustration: Avène Tinted Mineral Fluid SPF 50+ (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> high protection for intolerant skin, with a golden tint that evens out the complexion.</p>
<p><strong>My experience:</strong> far, far too dark. Even for girls who aren't especially fair this will be too much. It's also hard to spread. You really need a deeper skin tone or an existing tan for this one.</p>

<h2 id="avene-bez-boje">5. Avène Mineral Fluid SPF 50+ (untinted)</h2>
<!--IMG:foto-spf-5|Illustration of a tube: Avène Mineral Fluid SPF 50+|Illustration: Avène Mineral Fluid SPF 50+ (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> 100&nbsp;% mineral filters, photostable protection without chemical filters or fragrance.</p>
<p><strong>My experience:</strong> literally white paint, with no extra caring ingredients. I only kept it because it's a good, safe choice after stronger treatments such as microneedling, when the skin needs protection that sits on the surface. For everyday wear under make-up, forget it.</p>

<h2 id="bioderma-mineral">6. Bioderma Photoderm Mineral SPF 50+ (untinted)</h2>
<!--IMG:foto-spf-6|Illustration of a tube: Bioderma Photoderm Mineral SPF 50+|Illustration: Bioderma Photoderm Mineral SPF 50+ (not the original packaging).-->
<p class="claim"><strong>What the brand claims:</strong> maximum effectiveness against UVB and UVA rays for skin allergic to chemical filters.</p>
<p><strong>My experience: a total disaster.</strong> The whitest thing I've ever put on my face. The problem is that the white transfers horribly: everything I touched was stained and wouldn't wash off. The car seat, my make-up bag, even the front door. It went in the bin. And the cherry on top: the packaging leaks everywhere.</p>

<h2 id="zakljucak">Conclusion</h2>
<p>If you have fair, sensitive skin prone to redness and you're looking for an everyday mineral SPF, my answer is Babé Super Fluid Color, mixed with the untinted version if needed. Paula's Choice is a lovely but expensive alternative if you only need light evening-out of the skin tone.</p>
<p><strong>What do you use?</strong> If you can recommend a good mineral SPF that doesn't leave a white cast on everything you touch, let me know.</p>
""",
    },
    "proizvodi-koji-nisu-odgovarali-rozacea": {
        "slug": "products-that-failed-my-rosacea",
        "title": "12 popular products for sensitive skin that failed my rosacea",
        "h1": "Popular products that ended up “in the bin”",
        "description": "CeraVe, Kiehl's, Paula's Choice, Biologique Recherche P50W and more: 12 often recommended products that didn't suit my sensitive, reactive skin with rosacea.",
        "excerpt": "These products are often recommended for sensitive skin with rosacea. They didn't suit me, so maybe they'll save you some money.",
        "kicker": "Anti-picks",
        "verdict": "12 products I wouldn't buy again",
        "faq": [("Why didn't CeraVe suit my rosacea skin?", "I tried several CeraVe cleansers and their moisturising cream and none of them worked for me, even though they're a common recommendation for sensitive skin. Every skin is different, so they may suit someone else."),
                ("Which ingredients most often irritate my rosacea skin?", "The same triggers keep coming up for me: salicylic acid (BHA), alcohol and strong fragrance, and chemical UV filters."),
                ("Is azelaic acid good for rosacea?", "Azelaic acid is often recommended for rosacea, but Paula's Choice Azelaic Acid Booster didn't suit me, probably because it also contains salicylic acid."),
                ("How should you introduce new products if you have reactive skin?", "I check the ingredient list before buying and introduce new products one at a time, so I know exactly what causes a reaction.")],
        "itemlist": ["CeraVe facial cleansers", "CeraVe moisturising cream", "Kiehl's vitamin C serum", "Kiehl's Skin Strengthening Super Serum", "Biologique Recherche P50W",
                     "Paula's Choice Azelaic Acid Booster", "Paula's Choice 2% BHA", "Revox moisturiser", "Olival immortelle cream", "Olival SPF 30", "L'Occitane booster", "Erborian Red CC cream"],
        "body": """
<p class="lead">I have sensitive, reactive skin with rosacea and these are the products that didn't suit me. Interestingly, many of them are often recommended for exactly this skin type, so this list might save you some money.</p>
<p>Let me explain the quotation marks in the title straight away: most of these products didn't literally end up in the bin, I gave them away. What didn't suit me may be perfect for someone else.</p>

<h2 id="cleansing-and-moisturising">Cleansing and moisturising</h2>
<ul class="verdicts">
  <li><strong>CeraVe facial cleansers (any type).</strong> I tried several and none worked for me, even though they're almost always the first recommendation for sensitive skin.</li>
  <li><strong>CeraVe moisturising cream.</strong> Same experience as with the cleansers.</li>
  <li><strong>Revox moisturiser.</strong> Didn't suit me.</li>
  <li><strong>Olival immortelle cream.</strong> Immortelle is often mentioned as a soothing ingredient, but my skin didn't like it in this formula.</li>
</ul>

<h2 id="serums">Serums and boosters</h2>
<ul class="verdicts">
  <li><strong>Kiehl's vitamin C serum.</strong> Not for my skin.</li>
  <li><strong>Kiehl's Skin Strengthening Super Serum.</strong> It has a strong alcohol smell, which is the first alarm bell for reactive skin.</li>
  <li><strong>L'Occitane booster.</strong> Didn't suit me.</li>
</ul>

<!--AD-->

<h2 id="acids">Acids and toners</h2>
<ul class="verdicts">
  <li><strong>Biologique Recherche P50W.</strong> A cult toner, but not for my rosacea skin.</li>
  <li><strong>Paula's Choice Azelaic Acid Booster.</strong> Azelaic acid is often recommended for rosacea, but this booster probably failed because it also contains salicylic acid.</li>
  <li><strong>Paula's Choice 2% BHA.</strong> Salicylic acid simply doesn't suit my skin.</li>
</ul>

<h2 id="spf-and-base">SPF and tinted products</h2>
<ul class="verdicts">
  <li><strong>Olival SPF 30.</strong> Didn't suit me.</li>
  <li><strong>Erborian Red CC cream.</strong> It's popular precisely for covering redness, but it didn't work for me, probably because of the chemical filters in the SPF. Since then I only use <a href="/clanci/mineralni-spf-recenzije-poredak/">mineral sunscreens</a>.</li>
</ul>

<h2 id="what-i-learned">What I learned</h2>
<p>Looking at this list, the same triggers keep repeating: salicylic acid, alcohol and strong fragrance, and chemical UV filters. Today I check the ingredients before buying and introduce new products one at a time, so I know exactly what causes a reaction.</p>
<p>Every skin is different. If one of these products works for you, great. This list just shows that “for sensitive skin” on the pack doesn't mean it will suit yours. The products that turned out to be winners for me are in the article <a href="/clanci/proizvodi-koje-cu-ponovno-kupiti/">Products I'll buy again</a>.</p>
""",
    },
    "proizvodi-koje-cu-ponovno-kupiti": {
        "slug": "products-i-will-buy-again",
        "title": "Products I'll buy again: my ride-or-die favourites for face, hair and body",
        "h1": "Products I'll buy again",
        "description": "My ride-or-die products that I repurchase: skincare for sensitive skin with rosacea, make-up, hair and body. Kiehl's, Vichy, Babé, Skintegra, Olaplex and more.",
        "excerpt": "A short list of products I've bought more than once and will buy again: skincare, make-up, hair and body.",
        "kicker": "Favourites",
        "verdict": "16 products I repurchase",
        "faq": [("Which products for sensitive skin with rosacea do I repurchase?", "For my face I keep buying Olival hydrating spray, Kiehl's Ultra Facial Cream, Vichy Minéral serum, Babé mineral tinted SPF 50 and Skintegra Ros/Ac, among others."),
                ("Which SPF do I use every day?", "Laboratorios Babé mineral tinted fluid SPF 50. Of all the mineral sunscreens I've tried, it's my number one."),
                ("Which make-up do I repurchase?", "Catrice brow pencil, IT Cosmetics CC cream (Original), NARS bronzer in Laguna and Sweed Lash mascara."),
                ("Which hair and body products are my favourites?", "For hair Olaplex No. 3 and Kérastase Nutritive Masquintense, and for body CeraVe SA cream, even though CeraVe facial products didn't suit me.")],
        "itemlist": ["Olival hydrating spray", "Kiehl's Ultra Facial Cream", "Vichy Minéral serum", "Laboratorios Babé mineral tinted fluid SPF 50", "Skintegra Ros/Ac", "Sweed Lash Serum",
                     "Clinique Smart Clinical Repair Wrinkle Correcting Cream", "Kiehl's Avocado eye cream", "Ladria eye pads", "Catrice brow pencil", "IT Cosmetics CC cream (Original)",
                     "NARS Laguna bronzer", "Sweed Lash mascara", "Olaplex No. 3", "Kérastase Nutritive Masquintense", "CeraVe SA body cream"],
        "body": """
<p class="lead">After the <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">list of flops</a>, it's time for the products that passed the toughest test: I've bought them more than once and I'll buy them again. My skin is sensitive, reactive and prone to rosacea, so this isn't a list of random favourites.</p>

<!--IMG:foto-polica|Cream, serum, toner, SPF tube and lipstick on a light blue background|Skincare and make-up I repurchase.-->

<h2 id="skincare">Skincare</h2>
<ul class="picks">
  <li><strong>Olival hydrating spray</strong></li>
  <li><strong>Kiehl's Ultra Facial Cream</strong></li>
  <li><strong>Vichy Minéral serum</strong></li>
  <li><strong>Laboratorios Babé mineral tinted fluid SPF 50</strong>, my <a href="/clanci/mineralni-spf-recenzije-poredak/">number one among mineral sunscreens</a></li>
  <li><strong>Skintegra Ros/Ac</strong></li>
  <li><strong>Sweed Lash Serum</strong></li>
  <li><strong>Clinique Smart Clinical Repair Wrinkle Correcting Cream</strong></li>
  <li><strong>Kiehl's Avocado eye cream</strong></li>
  <li><strong>Ladria eye pads</strong></li>
</ul>

<!--AD-->

<h2 id="makeup">Make-up</h2>
<ul class="picks">
  <li><strong>Catrice brow pencil</strong> (I think the shade is Ashton)</li>
  <li><strong>IT Cosmetics CC cream (Original)</strong></li>
  <li><strong>NARS bronzer in Laguna</strong></li>
  <li><strong>Sweed Lash mascara</strong></li>
</ul>

<h2 id="hair">Hair</h2>
<ul class="picks">
  <li><strong>Olaplex No. 3</strong></li>
  <li><strong>Kérastase Nutritive Masquintense</strong></li>
</ul>

<h2 id="body">Body</h2>
<ul class="picks">
  <li><strong>CeraVe SA cream</strong>. Funnily enough, CeraVe facial products didn't suit me, but I keep repurchasing the SA body cream.</li>
</ul>

<h2 id="your-favourites">And your favourites?</h2>
<p>I'll be writing detailed reviews of most of these products soon. What are your ride-or-die products that you've bought more than once? Let me know, I'd love to try them.</p>
""",
    },
}

ARTICLES_EN.update({
    "babe-mineralni-spf-50-recenzija": {
        "slug": "babe-mineral-spf-50-review",
        "title": "Babé Mineral SPF 50 review: tinted and untinted mineral sunscreen for sensitive skin and rosacea",
        "h1": "Babé Mineral SPF 50: my current favourite",
        "description": "Review of Babé mineral SPF 50, tinted (Color) and untinted, for sensitive skin and rosacea: spreadability, reapplication, nano titanium dioxide, packaging and a 4/5 rating.",
        "excerpt": "The best of the best: they spread and reapply beautifully. The minuses are a too-dark tinted shade, leaky packaging and nano titanium.",
        "kicker": "Review",
        "verdict": "Rating 4/5: my current favourite",
        "review": {"product": "Babé Mineral Super Fluid SPF 50 (Color and untinted)",
                   "pros": ["Spreads beautifully, especially the tinted version", "Reapplies beautifully during the day", "100 % mineral filters, no chemical ones", "Doesn't sting the eyes", "Fragrance-free"],
                   "cons": ["Tinted shade is too dark for very fair skin", "Packaging can leak", "Untinted version sometimes has lumps", "Titanium dioxide in nano form"]},
        "faq": [("Does Babé mineral SPF contain nano titanium dioxide?", "Yes. On Babé's official ingredient list titanium dioxide is marked as TITANIUM DIOXIDE (NANO), while zinc oxide, the main filter, is not nano. This applies to both the tinted (Color) and the untinted mineral version."),
                ("Can Babé mineral SPF be reapplied during the day?", "Yes, and it's one of its biggest strengths. It reapplies beautifully, without pilling or building up."),
                ("Is tinted Babé SPF good for very fair skin?", "The tinted version is too dark for me. I mix it with the untinted version from the same line to get a shade for very fair skin."),
                ("Is Babé mineral SPF good for rosacea?", "It's my current favourite for sensitive skin with rosacea. The brand also recommends it for atopic skin and skin that can't tolerate chemical filters.")],
        "body": """
<p class="lead">If you've read my <a href="/clanci/mineralni-spf-recenzije-poredak/">mineral SPF ranking</a>, you know Babé came first. I use both the tinted (Color) and the untinted version, so this review covers both.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>100&nbsp;% mineral filters that reflect sunlight, with broad-spectrum (UVA and UVB) protection.</li>
  <li>Photobiome™ (1&nbsp;%), a prebiotic that supports the skin's natural defence against the sun, panthenol (1&nbsp;%) to hydrate and soothe, and carnosine (0.2&nbsp;%) as an antioxidant.</li>
  <li>Ultra-light texture; the tinted version adapts to all phototypes and instantly evens out the complexion.</li>
  <li>For sensitive, atopic skin and skin that can't tolerate chemical filters.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>The best of the best.</strong> Babé mineral sunscreens spread beautifully, which is a real rarity among mineral sunscreens, and they don't sting my eyes. What I love most is how well they reapply: I can top them up during the day without build-up and without a mask-like look.</p>
<p><strong>The tinted version (Color)</strong> spreads gorgeously. The downside is that it's dark, so on its own it isn't enough for us very fair girls.</p>
<p><strong>The untinted version</strong> sometimes has lumps, so I give it a good shake before applying. That's why I usually mix them: tinted plus untinted gives me the perfect shade.</p>
<p>I don't like the packaging, because it can leak. I always keep it in a separate pouch in my bag.</p>
<p><strong>What about nano titanium?</strong> I was almost sure Babé contains nano titanium dioxide, so I checked the official Laboratorios Babé site. And yes, the ingredient lists of both the tinted and untinted mineral versions say <em>Titanium Dioxide (nano)</em>. The main filter is zinc oxide, which isn't nano, but the titanium is. For me that's a minus.</p>
<p class="tip"><strong>Tip:</strong> I order it from the Spanish site Care to Beauty because it's much cheaper there than in our pharmacies. That's where I buy all my Babé products.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For anyone looking for a mineral face SPF that applies and reapplies nicely, with sensitive, reactive skin or rosacea. Overall, the minuses are the too-dark tinted shade and the nano titanium, so 4/5, even though it's my current favourite.</p>
""",
    },
    "chanel-water-fresh-tint-recenzija": {
        "slug": "chanel-water-fresh-tint-review",
        "title": "Chanel Les Beiges Water-Fresh Tint review: shade Medium, experience and summer vs winter",
        "h1": "Chanel Water-Fresh Tint: your skin but better",
        "description": "Review of Chanel Les Beiges Water-Fresh Tint in Medium: light coverage, plump skin and a natural glow. Who it's for, shades, dryness during the day and a 4.5/5 rating.",
        "excerpt": "A gorgeous base: light coverage, skin that looks like it drank water and a lovely glow. People told me my skin looked better. Rating 4.5/5.",
        "kicker": "Review",
        "verdict": "Rating 4.5/5: definitely buying again",
        "review": {"product": "Chanel Les Beiges Water-Fresh Tint (Medium)",
                   "pros": ["A gorgeous, ultra-light base", "Skin looks plump and hydrated, as if it drank water", "Lovely, natural glow", "Light coverage: your skin but better", "People told me my skin looked better"],
                   "cons": ["Can cause a little dryness during the day", "Medium is a bit too strong for winter", "Better for summer than winter"]},
        "faq": [("How much coverage does Chanel Water-Fresh Tint give?", "Light. It doesn't hide the skin, it enhances it: it evens out the tone and adds glow. Your skin but better."),
                ("Which shade of Chanel Water-Fresh Tint should I choose?", "I use Medium. It's perfect in summer, but a bit too strong for me in winter. If you're fair and want one shade for the whole year, consider Medium Light. The brand offers eight shades, from Light to Deep Plus."),
                ("Is Chanel Water-Fresh Tint good for dry skin?", "On the face it feels as if the skin has absorbed water, but during the day it can cause a little dryness for me. That's why I prefer it in summer."),
                ("Does Chanel Water-Fresh Tint have SPF?", "No, so I always apply SPF underneath."),
                ("How do you apply Chanel Water-Fresh Tint?", "The brand recommends putting a little product on the back of your hand and applying it to the face with the brush in circular motions, on its own or under or over foundation.")],
        "body": """
<p class="lead">Some products are good. And some are so good that other people tell you that you look better without knowing why. Chanel Les Beiges Water-Fresh Tint is the second kind.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>Ultra-light, hydrating and refreshing formula with 75&nbsp;% water.</li>
  <li>Patented microfluidic technology: pigments are enclosed in visible micro-droplets that melt into the skin on contact.</li>
  <li>A luminous bare-skin effect, an even complexion that lasts all day and a healthy glow.</li>
  <li>Up to 8 hours of hydration, with tamarind seed extract and a scent inspired by neroli blossom.</li>
  <li>Eight shades (Light, Medium Light, Medium, Medium Plus, Light Deep, Deep, Medium Deep and Deep Plus), 30 ml, with an application brush.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>A gorgeous, gorgeous base.</strong> From the first application it was clear this was something special. The texture is so light it's literally as if the skin has absorbed water, not as if I've applied foundation.</p>
<p>The coverage is completely light. It doesn't hide the skin, it enhances it: the tone is even, the skin looks plump and hydrated, and the glow is lovely, the natural, healthy kind, never greasy. If you want the definition of <em>your skin but better</em>, this is it.</p>
<p>The best proof? People told me my skin looked better while I was wearing it. Nobody asked what foundation I had on, they just noticed my skin looked good, and for me that's the biggest compliment a base product can get.</p>

<h3>Shade Medium</h3>
<p>I used the shade Medium. It's fine for summer, when I have a bit of colour, but in winter it's slightly too strong for me. If you're fair and want one shade for the whole year, consider going one shade lighter.</p>

<h3>The only downside: dryness</h3>
<p>During the day it can cause a little dryness. That's why I think it's better in summer, when the skin is naturally more hydrated; in winter it needs a richer cream underneath.</p>
<p>For sensitive skin it's also worth knowing that the formula contains fragrance. I didn't react, but if your skin can't tolerate fragrance, patch test it on a small area first.</p>
<p><strong>Definitely buying again.</strong> Only because of the dryness and the shade it's not a full five, but 4.5/5.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For anyone who wants a natural, fresh complexion with light coverage and glow, especially in summer and for 30+ skin where heavy foundations emphasise lines. If you need strong coverage or have very dry skin, this isn't the product for you, or pair it with a richer cream.</p>
""",
    },
    "babe-lip-cheek-spf-50-mocca-recenzija": {
        "slug": "babe-lip-cheek-spf-50-mocca-review",
        "title": "Babé Lip & Cheek SPF 50 review: tinted gloss for lips and cheeks in Mocca",
        "h1": "Babé SPF 50 for lips and cheeks: a lovely Mocca shade",
        "description": "Review of Babé Lip & Cheek Color Balm SPF 50 in Mocca: colour, shine, texture, the SPF taste and smell, and where to buy it for less. Rating 4/5.",
        "excerpt": "Lovely colour and lovely shine, an OK texture that's a little sticky, and a typical SPF taste and smell. I'd still buy it again.",
        "kicker": "Review",
        "verdict": "Rating 4/5: I'd buy it again",
        "review": {"product": "Babé Lip & Cheek Color Balm SPF 50 (Mocca)",
                   "pros": ["Lovely Mocca shade", "Lovely shine", "SPF 50 for lips and cheeks in one", "Good price at Care to Beauty"],
                   "cons": ["Slightly sticky texture", "Typical SPF smell and taste"]},
        "faq": [("Can Babé Lip & Cheek be used on the cheeks?", "Yes, the brand designed it for lips and cheeks, as a tinted gloss and blush with SPF 50."),
                ("Where can I buy Babé Lip & Cheek for less?", "I buy all my Babé products from the Spanish online pharmacy Care to Beauty, where they're much cheaper than in Croatian pharmacies."),
                ("Is Babé Lip & Cheek sticky?", "A little, but the colour and shine make up for it.")],
        "body": """
<p class="lead">After <a href="/clanci/babe-mineralni-spf-50-recenzija/">Babé mineral SPF</a> became my favourite for the face, I also tried their SPF for lips and cheeks in the shade Mocca.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A tinted balm for lips and cheeks with SPF 50 and protection against UVA and UVB rays, blue light and infrared radiation.</li>
  <li>Squalane and hyaluronic acid to hydrate and peptides for smoother-looking fine lines.</li>
  <li>A healthy, radiant finish with subtle colour, an easy-to-spread texture, instant volume and shine.</li>
  <li>For daily use and all skin types, including sensitive; also available in Cherry and Nude.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>Mocca is a lovely colour</strong>, a warm, natural nude that goes with any make-up, and the shine is lovely. The texture is OK, but a little sticky.</p>
<p>The smell and taste are typical of SPF, and there's no hiding that. Even so, I'd buy it again, because it's hard to find a lip product with such high protection that looks this pretty.</p>
<p class="tip"><strong>Tip:</strong> I buy all my Babé products from the Spanish online pharmacy Care to Beauty, where they're much cheaper than here.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For anyone who wants to protect their lips from the sun without giving up colour and shine. If sticky glosses or the taste of sunscreen bother you, this won't convert you.</p>
""",
    },
    "bioderma-sensibio-h2o-micelarna-voda-recenzija": {
        "slug": "bioderma-sensibio-h2o-micellar-water-review",
        "title": "Bioderma Sensibio H2O micellar water review: my favourite for sensitive skin and rosacea",
        "h1": "Bioderma Sensibio H2O: bottle number fifty and still my first step",
        "description": "Review of Bioderma Sensibio H2O micellar water for sensitive skin and rosacea: a long-time favourite for removing make-up and cleansing without rinsing. Rating 5/5.",
        "excerpt": "My long-time favourite, I must be on my fiftieth bottle. Forever my first step, and my skin is better for it.",
        "kicker": "Review",
        "verdict": "Rating 5/5: forever my first step",
        "review": {"product": "Bioderma Sensibio H2O micellar water",
                   "pros": ["My skin has been better since I started using it", "Gentle on sensitive skin with rosacea", "Removes face and eye make-up", "Fragrance-free", "Available in every pharmacy"],
                   "cons": ["Honestly, none"]},
        "faq": [("Is Bioderma Sensibio H2O good for rosacea?", "It's been my favourite for sensitive skin with rosacea for years. I must have bought my fiftieth bottle, and my skin is better for it."),
                ("Do you need to rinse off Bioderma Sensibio H2O?", "The brand says rinsing isn't necessary. I use it as the first step of my cleanse."),
                ("Does Bioderma Sensibio H2O remove eye make-up?", "Yes, the brand designed it to remove make-up from the face and eyes.")],
        "body": """
<p class="lead">There are products I try, and there are products that are part of me. Bioderma Sensibio H2O is the second kind: I must have bought my fiftieth bottle.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A micellar water that cleanses the face and removes make-up from the face and eyes, morning and evening, without rinsing.</li>
  <li>Micelles inspired by skin lipids and a pH of around 5.5, with a complex of biomimetic soothing sugars.</li>
  <li>Very well tolerated, soothes the skin and helps prevent reactions; fragrance-free.</li>
  <li>For sensitive and normal skin.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>My long-time favourite.</strong> Sensibio H2O is forever my first cleansing step and I have no plans to replace it.</p>
<p>I can honestly say my skin is better for it. My rosacea skin reacts quickly to cleansers, and this is one of the few cleansing products that has never upset it. Compare that with the <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">cleansers that were flops for me</a>.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For anyone with sensitive, reactive skin or rosacea looking for a gentle first cleansing step. If you take just one product from this site, make it this one.</p>
""",
    },
    "bioderma-photoderm-ar-spf-50-recenzija": {
        "slug": "bioderma-photoderm-ar-spf-50-review",
        "title": "Bioderma Photoderm AR SPF 50+ review: tinted anti-redness SPF for rosacea, my experience",
        "h1": "Bioderma Photoderm AR SPF 50+: some coverage, but it didn't calm my redness",
        "description": "Review of the new Bioderma Photoderm AR+ SPF 50+, a tinted anti-redness sunscreen for rosacea: spreadability, chemical filters, coverage and a 3/5 rating.",
        "excerpt": "The new tinted anti-redness SPF gives some coverage, but it doesn't spread nicely, it's chemical and it seemed to cause redness for me.",
        "kicker": "Review",
        "verdict": "Rating 3/5: some coverage, so it's OK",
        "review": {"product": "Bioderma Photoderm AR+ SPF 50+",
                   "pros": ["Covers some redness", "High SPF 50+"],
                   "cons": ["I'm not happy with how it spreads", "Chemical SPF", "It seemed to cause redness for me"]},
        "faq": [("Does Bioderma Photoderm AR help with rosacea?", "The brand designed it for skin prone to redness and rosacea and cites its own studies on reduced redness. It gave me some coverage, but it seemed to cause redness."),
                ("Is Bioderma Photoderm AR a mineral SPF?", "No, it's a chemical SPF. If you're looking for a mineral SPF for rosacea, see my mineral SPF ranking.")],
        "body": """
<p class="lead">Bioderma Photoderm AR is a tinted SPF 50+ made specifically for redness and rosacea, and it recently arrived in new packaging as Ultra-Fluid AR+. Perfect for me on paper, only OK in practice.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>Very high UVA and UVB protection (SPF 50+) with Sun Active Defense technology and antioxidants.</li>
  <li>The patented Rosactiv™ complex targets one of the causes of redness; according to its own study, the brand reports reduced visible redness in 96&nbsp;% of users.</li>
  <li>A natural tint that evens out the complexion.</li>
  <li>For sensitive skin prone to redness and rosacea; fragrance-free, non-comedogenic and water-resistant.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p>I'm not very happy with how it spreads: it doesn't glide over the skin like my favourites. It's also a chemical SPF, and chemical filters generally don't suit my rosacea skin.</p>
<p>Ironically, for an anti-redness product, it seemed to cause redness. What saves it is the coverage: it covers something, so the rating is OK.</p>
<p>For comparison, Bioderma's mineral SPF from the same line ended up at the bottom of my <a href="/clanci/mineralni-spf-recenzije-poredak/">mineral SPF ranking</a>, and my favourite remains <a href="/clanci/babe-mineralni-spf-50-recenzija/">Babé mineral SPF</a>.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For redness-prone skin that tolerates chemical filters well and wants an SPF with light coverage. If your rosacea reacts to chemical filters, skip it.</p>
""",
    },
    "avene-b-protect-spf-50-recenzija": {
        "slug": "avene-b-protect-spf-50-review",
        "title": "Avène B-Protect SPF 50+ review: tinted SPF for sensitive skin, my experience",
        "h1": "Avène B-Protect SPF 50+: good for summer, but drying",
        "description": "Review of Avène B-Protect SPF 50+: a tinted sunscreen with chemical filters for sensitive skin. Coverage, redness, build-up during the day and a 3/5 rating.",
        "excerpt": "A tinted SPF with just the right coverage for summer that slightly masks redness, but it's drying and builds up during the day.",
        "kicker": "Review",
        "verdict": "Rating 3/5: not bad",
        "review": {"product": "Avène B-Protect SPF 50+",
                   "pros": ["Just the right coverage for summer", "Slightly masks redness", "High SPF 50+"],
                   "cons": ["Dries out the skin", "Builds up during the day so you can see I'm wearing “something”", "Chemical filters", "Not for topping up during the day"]},
        "faq": [("Is Avène B-Protect a mineral SPF?", "No. It contains chemical UV filters alongside titanium dioxide, so it's not for anyone looking for purely mineral protection."),
                ("Does Avène B-Protect cover redness?", "A little. It's lightly tinted and gives me just the right coverage for summer, but it doesn't fully cover rosacea redness."),
                ("Can Avène B-Protect be reapplied during the day?", "Not for me. After the first layer it starts to cling to dry patches, so I don't top it up.")],
        "body": """
<p class="lead">Avène B-Protect is a tinted SPF 50+ that I wore all summer. It's not bad, but it's not a product I'll buy again either, and here's why.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>Optimal UVB and UVA protection thanks to the Sunsitive® filter combination.</li>
  <li>A lightly tinted formula with micro-encapsulated pigments that even out the complexion and give a radiant finish.</li>
  <li>A bare-skin feel: almost invisible, non-greasy, non-sticky and quickly absorbed.</li>
  <li>For sensitive skin on the face and neck, non-comedogenic and developed to minimise the risk of allergic reactions.</li>
</ul>
<p class="note-small">According to the French pharmacy register Vidal, this product was discontinued in May 2025, so it can now only be found while stocks last.</p>

<h2 id="my-experience">My experience</h2>
<p><strong>Not bad.</strong> It gives just the right coverage for summer: the skin looks more even and redness is slightly masked, though it doesn't disappear.</p>
<p>The problem is that it dries out my face. During the day it starts clinging to dry patches and then you can see I'm wearing “something”. Because of that I can't top it up during the day, and for a sunscreen that's a big downside.</p>
<p>It's also important to know this is a chemical SPF. The formula contains chemical filters alongside titanium dioxide, which generally doesn't suit my rosacea skin best. That's why today I choose <a href="/clanci/mineralni-spf-recenzije-poredak/">mineral sunscreens</a>.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For normal to combination skin that tolerates chemical filters well and wants a lightly tinted SPF for summer. If you have dry skin or rosacea, or need an SPF you'll reapply several times a day, look for something else.</p>
""",
    },
    "avene-termalna-voda-rozacea-recenzija": {
        "slug": "avene-thermal-water-rosacea-review",
        "title": "Avène Thermal Spring Water and rosacea: review and why it didn't suit me",
        "h1": "Avène Thermal Spring Water: refreshing, but it didn't help my rosacea",
        "description": "Review of Avène Thermal Spring Water (Eau Thermale) for rosacea and sensitive skin. It calms redness for many people, but long-term it caused redness for me. Rating 2/5.",
        "excerpt": "It suits many people with rosacea, but long-term it caused redness for me instead of calming. It refreshes nicely, and that's it.",
        "kicker": "Review",
        "verdict": "Rating 2/5: just a refresher",
        "review": {"product": "Avène Eau Thermale Thermal Spring Water",
                   "pros": ["Refreshes the skin nicely", "Pleasant on hot days"],
                   "cons": ["Long-term it caused redness for me", "It didn't calm my rosacea skin"]},
        "faq": [("Does Avène Thermal Spring Water help with rosacea?", "It suits many people with rosacea and is on the list of products with the seal of the US National Rosacea Society. For me, long-term use caused redness and it didn't calm my skin."),
                ("What is Avène Thermal Spring Water for?", "The brand describes it as a soothing and softening water for sensitive skin. For me it was only good as a quick refresher.")],
        "body": """
<p class="lead">Avène Thermal Spring Water is probably the best-known product for sensitive skin and rosacea. Almost every recommendation list mentions it, so I used it for a long time too. Unfortunately, my skin doesn't like it.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A thermal water that soothes, softens and reduces skin sensitivity.</li>
  <li>Designed for sensitive and irritated skin, for daily use.</li>
  <li>It's on the list of products with the seal of the National Rosacea Society, the US rosacea association.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p>Although it suits many people with rosacea, long-term use caused redness for me. Instead of calming, after a while my skin was redder than before.</p>
<p>I have to give it this: it's nicely refreshing, especially in summer. But from a product for sensitive skin with rosacea I expect more than a refresh, so it ended up on my <a href="/kategorije/flop/">flop list</a>.</p>
<p>It's a good example that “for sensitive skin” and “for rosacea” don't mean it will suit your skin. I've collected more examples like this in the article <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">Popular products that ended up in the bin</a>.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For people who want a quick facial refresh and don't react to thermal water. If you have rosacea, try it for a few weeks and keep an eye on your redness.</p>
""",
    },
    "avene-couvrance-tekuci-puder-recenzija": {
        "slug": "avene-couvrance-liquid-foundation-review",
        "title": "Avène Couvrance liquid foundation review: base for sensitive skin and rosacea, my experience",
        "h1": "Avène Couvrance: a pretty finish, but not for my skin",
        "description": "Review of Avène Couvrance corrective liquid foundation SPF 20 for sensitive skin and rosacea: finish, shades for fair skin, papules and pustules. Rating 3/5.",
        "excerpt": "It gives a pretty finish, but there's no shade light enough and I think it caused papules and pustules.",
        "kicker": "Review",
        "verdict": "Rating 3/5: pretty finish, bad reaction",
        "review": {"product": "Avène Couvrance corrective liquid foundation SPF 20",
                   "pros": ["Pretty, even finish", "Covers redness and imperfections"],
                   "cons": ["No shade for very fair skin", "I think it caused papules and pustules"]},
        "faq": [("Does Avène Couvrance have a shade for very fair skin?", "None was light enough for me. The lightest shade in the range is Porcelain."),
                ("Is Avène Couvrance good for rosacea?", "The brand designed it for sensitive skin, and the finish is pretty. I think it caused papules and pustules, so I stopped using it straight away.")],
        "body": """
<p class="lead">Avène Couvrance is a corrective liquid foundation from the pharmacy, made specifically for sensitive skin. Ideal for rosacea on paper, but it didn't stay in my routine.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A corrective liquid foundation that covers mild to moderate imperfections and evens out the complexion for a natural, radiant look.</li>
  <li>SPF 20 with mineral filters (zinc oxide and titanium dioxide), water- and sweat-resistant.</li>
  <li>Vitamin E to protect against light-induced skin ageing.</li>
  <li>For sensitive skin, in the shades Porcelain, Natural, Sand and Honey.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p>The finish is pretty, I have to admit: the skin looks even and redness is well covered.</p>
<p>The first problem is the shade. There's no very light shade like the one I need, so it always looked a little too dark on my face.</p>
<p>The second problem is more serious. I think it caused papules and pustules, those inflamed bumps we all want to avoid with rosacea. As soon as I noticed, I stopped using it straight away. I can't say for certain it was the culprit, but I didn't want to risk it.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For sensitive skin with a fair to medium complexion that needs redness coverage and doesn't react with inflamed bumps. If you have rosacea with papules, patch test it carefully on a small area.</p>
""",
    },
    "avene-cicalfate-serum-recenzija": {
        "slug": "avene-cicalfate-serum-review",
        "title": "Avène Cicalfate+ serum review: hydration and redness on sensitive skin",
        "h1": "Avène Cicalfate+ serum: OK hydration, nothing special for redness",
        "description": "Review of Avène Cicalfate+ intense repairing serum: hydration, rosacea redness, pump packaging and a 3/5 rating. My experience on sensitive skin.",
        "excerpt": "It hydrates OK, but I didn't notice anything special for redness. And the pump feels cheap.",
        "kicker": "Review",
        "verdict": "Rating 3/5: OK, but no effect on redness",
        "review": {"product": "Avène Cicalfate+ repairing serum",
                   "pros": ["Hydrates OK", "No alcohol, silicones or fragrance"],
                   "cons": ["I didn't notice any particular effect on redness", "The pump feels cheap"]},
        "faq": [("Does Avène Cicalfate+ serum reduce redness?", "The brand says it strengthens the skin barrier and helps with redness. I didn't notice anything special on my rosacea redness."),
                ("Does Avène Cicalfate+ serum hydrate?", "Yes, it hydrates OK. For dry or tight skin it may be enough, but don't expect miracles.")],
        "body": """
<p class="lead">Many people know the Cicalfate line from its repairing cream. The serum from the same line promises a stronger barrier and less redness, so I tried it on my rosacea skin.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>Strengthens the skin barrier and helps prevent dehydration, dryness, dullness, imperfections, redness and premature ageing.</li>
  <li>Gives instant relief and lastingly reduces feelings of tightness and discomfort.</li>
  <li>A hydrating, repairing formula for skin weakened by daily stressors, with Avène thermal spring water, glycerin and panthenol.</li>
  <li>96&nbsp;% ingredients of natural origin, no alcohol, silicones or fragrance.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p>Let's start with the packaging: I don't like the pump, it feels cheap. I know the contents matter most, but from a serum in this price range I expect nicer packaging too.</p>
<p>The serum itself hydrates OK. My skin doesn't feel tight and it's comfortable under cream. But when it comes to redness I didn't notice it doing anything special, and that was my main reason for buying it.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For sensitive skin that needs a simple hydrating serum without fragrance or alcohol. If you're looking for a serum that will visibly reduce rosacea redness, this isn't it.</p>
""",
    },
    "biologique-recherche-p50w-recenzija": {
        "slug": "biologique-recherche-p50w-review",
        "title": "Biologique Recherche P50W review: is P50W right for sensitive and reactive skin",
        "h1": "Biologique Recherche P50W: a cult toner, but too aggressive for reactive skin",
        "description": "Review of Biologique Recherche Lotion P50W on reactive skin with rosacea: why the cult exfoliating toner for sensitive skin didn't suit me. Ingredients, acids and a 2/5 rating.",
        "excerpt": "I'm not saying it's bad, but it's too aggressive for my reactive skin with rosacea.",
        "kicker": "Review",
        "verdict": "Rating 2/5: not for my skin",
        "review": {"product": "Biologique Recherche Lotion P50W",
                   "pros": ["A cult product that suits many people", "The gentlest version of the P50 toner"],
                   "cons": ["Too aggressive for reactive skin", "Didn't suit my rosacea skin"]},
        "faq": [("Is Biologique Recherche P50W good for sensitive skin?", "The brand recommends it for thin and sensitive skin as a very gentle exfoliating toner. For my reactive skin with rosacea it was too aggressive."),
                ("What does P50W contain?", "According to the ingredient list it contains acids (gluconolactone, lactic, malic and citric), niacinamide, urea and plant extracts, but also fragrance components such as limonene and linalool.")],
        "body": """
<p class="lead">P50 is one of the most famous toners in the world, and P50W is its gentlest version, meant specifically for sensitive skin. I already mentioned it on my <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">list of flops</a>, and here's why.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A very gentle exfoliating lotion for thin and/or sensitive skin and dehydrated skin.</li>
  <li>Exfoliates, purifies, mattifies, hydrates and maintains the pH balance of the skin's surface while smoothing texture.</li>
  <li>Contains acids (gluconolactone, lactic, malic and citric), niacinamide, glycerin, allantoin, urea and plant extracts.</li>
  <li>Not recommended on irritated skin; avoid sun exposure after application.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>Not for my skin.</strong> I'm not saying it's bad, and I know how many people love it, but for reactive skin it's too aggressive.</p>
<p>Although P50W is the gentlest version and is meant for sensitive skin, the combination of acids was too much for me. My rosacea skin doesn't like acids anyway, and there are several here, along with fragrance components such as limonene and linalool.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For sensitive but not reactive skin that tolerates gentle acids well. If you have rosacea or skin that reacts strongly to new products, skip it or talk to a dermatologist first.</p>
""",
    },
    "erborian-cc-red-correct-recenzija": {
        "slug": "erborian-cc-red-correct-review",
        "title": "Erborian CC Red Correct review: anti-redness CC cream and rosacea, my experience",
        "h1": "Erborian CC Red Correct: beautiful coverage, but redder skin afterwards",
        "description": "Review of Erborian CC Red Correct SPF 25 on rosacea skin: the green CC cream neutralises redness beautifully, but its chemical SPF gave me more redness, papules and pustules. Rating 2.5/5.",
        "excerpt": "It covers and neutralises redness beautifully, but after taking it off my skin was redder, with more papules and pustules.",
        "kicker": "Review",
        "verdict": "Rating 2.5/5: sadly a disappointment",
        "review": {"product": "Erborian CC Red Correct SPF 25",
                   "pros": ["Covers redness beautifully", "The green pigments really neutralise redness"],
                   "cons": ["Chemical SPF", "My skin was redder after taking it off", "More papules and pustules"]},
        "faq": [("Does Erborian CC Red Correct cover redness?", "Yes, it covers and neutralises redness beautifully. The problem was that my skin was redder after I took it off."),
                ("Is Erborian CC Red Correct good for rosacea?", "It wasn't for me. After removing it I had more redness, papules and pustules, probably because of the chemical filters in the SPF."),
                ("Does Erborian CC Red Correct have a mineral SPF?", "Not only mineral. Alongside zinc oxide and titanium dioxide it also contains chemical filters.")],
        "body": """
<p class="lead">Erborian CC Red Correct is a green CC cream recommended to everyone with redness, so it naturally made it onto my list. In the end it landed among the <a href="/clanci/proizvodi-koji-nisu-odgovarali-rozacea/">flops</a>, and for good reason.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>Green pigments correct colour and reduce the visibility of redness, and the cream adapts to the skin tone as it's applied.</li>
  <li>Centella asiatica (tiger grass) extract soothes the skin and supports firmness and elasticity.</li>
  <li>SPF 25, a light and radiant finish.</li>
  <li>For all skin types, non-comedogenic, tested under dermatological supervision.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>Sadly, a disappointment.</strong> On the face it looked great: it covers beautifully and really neutralises redness, which is why I wanted it to work so badly.</p>
<p>But after taking it off I saw that my skin was redder, with more papules and pustules. The cream was covering exactly what it was making worse.</p>
<p>It's a chemical SPF: alongside zinc oxide and titanium dioxide it also contains chemical filters. My rosacea skin reacts to them, and this product is exactly what taught me to choose only <a href="/clanci/babe-mineralni-spf-50-recenzija/">mineral sunscreens</a>.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For redness-prone skin that tolerates chemical filters well. If you have rosacea with papules and pustules, be careful and check how your skin looks after removing it, not just while the cream is on.</p>
""",
    },
    "rhode-pocket-blush-tan-line-recenzija": {
        "slug": "rhode-pocket-blush-tan-line-review",
        "title": "Rhode Pocket Blush Tan Line review: cream blush for sensitive skin, my experience",
        "h1": "Rhode Pocket Blush in Tan Line: the perfect blush",
        "description": "Review of Rhode Pocket Blush in Tan Line: Hailey Bieber's cream blush that blends easily, looks like a natural sun flush and doesn't irritate sensitive skin. Rating 5/5.",
        "excerpt": "A lovely blush that blends easily, doesn't irritate me at all and looks like a natural flush from the sun. The only minus: it runs out fast.",
        "kicker": "Review",
        "verdict": "Rating 5/5: the perfect blush",
        "review": {"product": "Rhode Pocket Blush (Tan Line)",
                   "pros": ["Blends easily with fingers", "Doesn't irritate me, even on rosacea skin", "The colour of a natural sun flush", "Lasts a long time on me", "Tiny pack fits in any pocket"],
                   "cons": ["There isn't much product and it runs out fast"]},
        "faq": [("What shade is Rhode Pocket Blush Tan Line?", "Tan Line is a pinky-bronze shade. On me it looks like a natural flush after a day in the sun."),
                ("Is Rhode Pocket Blush good for sensitive skin?", "It doesn't irritate me at all, and I have sensitive, reactive skin with rosacea."),
                ("How long does Rhode Pocket Blush last?", "On me it actually lasts quite a long time, which isn't always the case with cream blushes."),
                ("How do you apply Rhode Pocket Blush?", "Easiest with your fingers: tap lightly onto the apples of the cheeks and blend towards the temples. The brand says it can also be used on the lips.")],
        "body": """
<p class="lead">Rhode is Hailey Bieber's brand, known for its minimalist packaging and products that promise glow. Pocket Blush is a cream blush in a tiny pack that fits in any pocket, and the shade Tan Line is my perfect blush.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A cream blush that wakes up cheeks and lips with a satin, diffused flush.</li>
  <li>A radiant finish without a greasy feel.</li>
  <li>With peptides and tamanu oil, in a handy 5.3 g pack that can be applied with fingers, a brush or a sponge.</li>
  <li>Tan Line is described as a pinky tan shade.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>A lovely blush.</strong> It blends easily, literally a few taps with your fingers and you're done, no patches and no edges.</p>
<p>The most important thing for me is that it doesn't irritate me at all. With sensitive skin and rosacea every new cheek product is a small risk, and this one passed without any reaction.</p>
<p>Tan Line is the colour of a natural flush from the sun: as if you've just come back from the beach, only without the sunburn. On my fair skin it looks fresh and not at all overdone. It also lasts quite a long time on me, which isn't a given with cream blushes.</p>
<p>The only flop: there isn't much product. I didn't notice it at first, but since I use it every day, it really does run out fast.</p>
<p>If you're wondering whether Rhode is worth the hype, Pocket Blush is my answer: yes.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For anyone who loves a natural, fresh look and cream blushes, especially with sensitive skin. Tan Line is a great choice for fair to medium skin that wants a sun-kissed effect.</p>
""",
    },
    "rhode-peptide-lip-shape-recenzija": {
        "slug": "rhode-peptide-lip-shape-review",
        "title": "Rhode Peptide Lip Shape review: lip liner, shades and a cheaper alternative",
        "h1": "Rhode lip liner: OK, but nothing special",
        "description": "Review of Rhode Peptide Lip Shape lip liner: it blends nicely but isn't precise, and the shades are too dark for fair skin. A better and cheaper alternative is Catrice. Rating 3/5.",
        "excerpt": "It blends nicely, but it isn't precise and all the shades are somehow too dark for me. Catrice's soft liner is the better choice.",
        "kicker": "Review",
        "verdict": "Rating 3/5: nothing special",
        "review": {"product": "Rhode Peptide Lip Shape",
                   "pros": ["Blends nicely", "Comfortable, soft formula"],
                   "cons": ["Not precise", "All the shades are too dark for me", "Catrice has a better, cheaper liner"]},
        "faq": [("Is Rhode Peptide Lip Shape a precise lip liner?", "Not for me. It blends nicely, but it's not ideal for precise lip contouring."),
                ("Does Rhode lip liner have shades for fair skin?", "For me all the shades are somehow too dark."),
                ("What's a cheaper alternative to Rhode lip liner?", "I'd rather buy Catrice's new soft lip liner.")],
        "body": """
<p class="lead">After <a href="/clanci/rhode-pocket-blush-tan-line-recenzija/">Rhode Pocket Blush</a> won me over completely, I had high expectations for their lip liner too. Sadly, it didn't impress me.</p>

<h2 id="what-the-brand-says">What the brand says</h2>
<ul class="claims">
  <li>A dual-ended liner: a rounded tip for shaping on one end and a silicone applicator for blending and softening the line on the other.</li>
  <li>A contoured, fuller-looking lip effect without injections.</li>
  <li>Peptides smooth and soften the lips, and fenugreek extract helps with dryness.</li>
  <li>Can be used as a liner, to fill in the lips or under lipstick and gloss; 11 shades.</li>
</ul>

<h2 id="my-experience">My experience</h2>
<p><strong>OK.</strong> It blends nicely, but it isn't precise, so it's not ideal for a clean lip line.</p>
<p>The bigger problem is the shades: they're all somehow too dark for my fair skin. In the end it's a liner that isn't bad, but isn't anything special either.</p>
<p>My advice: buy Catrice's new soft lip liner instead. For much less money you'll get an equally comfortable formula.</p>

<h2 id="who-is-it-for">Who is it for</h2>
<p>For Rhode fans who like a soft, blurred lip look and have a medium to deeper skin tone. If you want a precise liner or have very fair skin, skip it.</p>
""",
    },
    "moj-glow-up-rutina-rozacea": {
        "slug": "my-glow-up-rosacea-routine",
        "title": "My glow up: rosacea routine with Omnilux LED mask, Soolantra and Skinoren",
        "h1": "My glow up: the routine that changed my skin",
        "description": "My rosacea skincare routine step by step: Omnilux Contour LED mask (specs), Soolantra at night, Skinoren gel in the morning, Bioderma Sensibio, Olival amino gel with a PMD device in the evening and La Roche-Posay Cicaplast.",
        "excerpt": "Everything I use for my rosacea skin, step by step: from the Omnilux red LED mask to Soolantra and Skinoren.",
        "kicker": "Routine",
        "verdict": "My routine in 6 steps",
        "itemlist": ["Bioderma Sensibio H2O micellar water", "Olival Professional amino cleansing gel and PMD device (evening)", "Skinoren gel in the morning", "Soolantra at night", "La Roche-Posay Cicaplast", "Omnilux Contour Face LED mask"],
        "faq": [("What are the specs of the Omnilux Contour Face LED mask?", "It has 132 LEDs that simultaneously emit red light at 633 nm and near-infrared light at 830 nm. A treatment lasts 10 minutes, and the brand recommends 3 to 5 treatments a week for 4 to 6 weeks. It's flexible, made of silicone, with a rechargeable controller, and it's FDA cleared for wrinkle treatment."),
                ("When should you use Soolantra and when Skinoren?", "I use Soolantra at night and Skinoren gel in the morning. Both are prescription medicines, so always agree the schedule and how to use them with your dermatologist."),
                ("How do I cleanse my face with rosacea?", "My first step is Bioderma Sensibio H2O micellar water, followed by Olival Professional amino cleansing gel. I use the PMD cleansing device only in the evening.")],
        "body": """
<p class="lead">The question I get most often is: what do you use on your skin? This is my rosacea routine, step by step, with all the products and devices responsible for my glow up.</p>
<p class="note-small">Soolantra and Skinoren are prescription medicines. I'm sharing my experience here, not medical advice: always agree your rosacea treatment with a dermatologist.</p>

<h2 id="cleansing">1. Cleansing: Bioderma Sensibio and Olival amino gel with PMD</h2>
<p>The first step is always <a href="/clanci/bioderma-sensibio-h2o-micelarna-voda-recenzija/">Bioderma Sensibio H2O micellar water</a>, my long-time favourite. After that I wash my face with <strong>Olival Professional amino gel</strong>, a gentle cleansing gel, and in the evening I use it with a <strong>PMD cleansing device</strong>, which cleans my face more thoroughly than hands alone. I use the PMD only in the evening.</p>

<h2 id="skinoren">2. Morning: Skinoren gel</h2>
<p>I apply <strong>Skinoren gel</strong> in the morning. It contains azelaic acid and is one of the medicines prescribed for rosacea, and it's a permanent part of my morning routine. Hydration goes on top, and always a mineral SPF, such as my <a href="/clanci/babe-mineralni-spf-50-recenzija/">Babé mineral SPF</a>.</p>

<!--IMG:foto-vecernja-rutina|Hands applying white cream from a tube by candlelight in a bathroom|AI illustration of an evening routine.-->

<h2 id="soolantra">3. Night: Soolantra</h2>
<p><strong>Soolantra</strong> is an ivermectin cream that dermatologists prescribe for rosacea with papules and pustules. I use it at night, as the last active step before bed.</p>

<h2 id="cicaplast">4. For repair: La Roche-Posay Cicaplast</h2>
<p>When my skin needs calming and barrier repair, I reach for <strong>La Roche-Posay Cicaplast</strong>. It's my safe choice when my skin is irritated or dry.</p>

<!--IMG:foto-led-maska|A woman relaxing on a sofa in the evening wearing a white LED mask glowing red|AI illustration of an LED face mask, not the original product.-->

<h2 id="omnilux">5. Omnilux Contour Face LED mask</h2>
<p>The biggest investment in my routine is the <strong>Omnilux Contour Face</strong>, an LED mask with red and near-infrared light. Here are the specs according to the manufacturer:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Spec</th><th scope="col">Omnilux Contour Face</th></tr></thead>
<tbody>
<tr><td>Number of LEDs</td><td>132 (66 bulbs with 2 diodes each)</td></tr>
<tr><td>Wavelengths</td><td>633 nm (red) and 830 nm (near-infrared), simultaneously</td></tr>
<tr><td>Treatment time</td><td>10 minutes, the mask switches itself off</td></tr>
<tr><td>Recommended frequency</td><td>3 to 5 times a week for 4 to 6 weeks, then maintenance</td></tr>
<tr><td>Material</td><td>Flexible silicone with head straps</td></tr>
<tr><td>Power</td><td>Rechargeable controller, USB-C cable</td></tr>
<tr><td>Certifications</td><td>FDA cleared for full-face wrinkle treatment, CE</td></tr>
<tr><td>Warranty</td><td>2 years</td></tr>
</tbody></table></div>
<p>What I love most is that the mask is flexible and fits snugly to the face, so the 10-minute treatment is the perfect evening break.</p>

<h2 id="conclusion">Conclusion</h2>
<p>My glow up didn't come from one miracle product, but from a routine: gentle cleansing, treatment prescribed by my dermatologist, barrier repair and an LED mask. If you have rosacea, the most important step is the first one, at the dermatologist's.</p>
<p><strong>And your routine?</strong> Tell me in the comments what helps your rosacea.</p>
""",
    },
})
