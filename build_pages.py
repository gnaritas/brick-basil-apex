#!/usr/bin/env python3
"""Brick & Basil — Apex NC (The Ballast on Salem). Template-v2 multi-page site build.
Every claim traced in evidence.json. Unknowns (hours, opening day, prices, menu items)
omitted — never guessed. Zero JS. Hand-rolled HTML/CSS. noindex on demo host.
Built 2026-11-24 by the websites desk."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://brick-basil-apex-demo.up.railway.app'
BRAND = 'Brick &amp; Basil'
BRAND_PLAIN = 'Brick & Basil'
CITY = 'Apex, NC'
STREET = '1801 Chatham Flats Dr Suite 4'
FULL_ADDR = '1801 Chatham Flats Dr Suite 4, Apex, NC 27502'
PLAZA = 'The Ballast on Salem'
PHONE = '+19193464742'
PHONE_TXT = '(919) 346-4742'
EMAIL = 'info@brickandbasilnc.com'
FB = 'https://www.facebook.com/profile.php?id=61571583961194'
IG = 'https://www.instagram.com/brickandbasil.nc/'
MAPQ = 'https://www.google.com/maps?q=1801%20Chatham%20Flats%20Dr%2C%20Apex%2C%20NC%2027502'
LAT, LON = 35.71645, -78.87553  # Nominatim centroid for Chatham Flats Dr, Apex — approximation, see evidence.json
SOCIALS = [FB, IG]

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND_PLAIN}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com">
</head>
<body>'''

def nav():
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">Brick&nbsp;&amp;&nbsp;Basil <span>Apex,&nbsp;NC</span></a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/detroit-deep-dish">Deep&nbsp;Dish</a>
    <a href="/catering">Catering</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact&nbsp;Us</a>
  </nav>
</header>'''

def footer():
    return f'''<footer class="site">
  <div class="footgrid">
    <div class="footnap">
      <p class="fbrand">Brick&nbsp;&amp;&nbsp;Basil</p>
      <address>{PLAZA}<br>{STREET.replace(' Suite 4', ' <span>Suite&nbsp;4</span>')}<br>{CITY} 27502</address>
      <p class="fcontact"><a href="tel:{PHONE}">{PHONE_TXT}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="footcta">
      <p class="basilrule" aria-hidden="true"></p>
      <p class="fline">Handmade pasta. Detroit-style deep dish.<br>Focaccia sandwiches.</p>
      <p class="fsocial"><a href="{FB}" rel="noopener">Facebook</a> &nbsp;·&nbsp; <a href="{IG}" rel="noopener">Instagram</a></p>
      <p class="fline2">Opening early 2027 at {PLAZA} — updates posted there first.</p>
    </div>
  </div>
  <p class="footline">&copy; 2026 Brick&nbsp;&amp;&nbsp;Basil · {CITY}</p>
</footer>
<!-- BUILT-2026-11-24 -->'''

def breadcrumbs(name, path):
    items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'}]
    if path != '/':
        items.append({'@type': 'ListItem', 'position': 2, 'name': name, 'item': ORIGIN + path})
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}, ensure_ascii=False)

def ld_restaurant():
    obj = {
        '@context': 'https://schema.org', '@type': 'Restaurant',
        'name': BRAND_PLAIN,
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'servesCuisine': ['Italian', 'Pizza', 'Handmade pasta'],
        'email': EMAIL,
        'telephone': PHONE,
        'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Apex', 'addressRegion': 'NC', 'postalCode': '27502', 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'sameAs': SOCIALS,
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_service(name, path, desc, area):
    obj = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': name, 'description': desc,
        'url': ORIGIN + path,
        'serviceType': name,
        'areaServed': area,
        'provider': {'@type': 'Restaurant', 'name': BRAND_PLAIN, 'email': EMAIL, 'telephone': PHONE,
                     'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Apex', 'addressRegion': 'NC', 'postalCode': '27502', 'addressCountry': 'US'}},
    }
    return json.dumps(obj, ensure_ascii=False)

CTA = f'''<p class="cta">
  <a class="btn btn-big" href="tel:{PHONE}">Call&nbsp;{PHONE_TXT}</a>
  <a class="btn btn-ghost btn-big" href="/contact">Email&nbsp;the&nbsp;shop</a>
</p>'''

PAGES = {}

# ---------- HOME ----------
PAGES['index.html'] = (head(
    f'{BRAND_PLAIN} — Italian Restaurant Coming to Apex, NC — Opening Early 2027',
    'Brick &amp; Basil is an authentic Italian restaurant from chef and caterer Scott Harvey (Rolling Deep food truck) — handmade pasta, Detroit-style deep dish and focaccia sandwiches at The Ballast on Salem, Apex, NC. Opening early 2027.',
    '/'), f'''{nav()}
<section class="hero">
  <div class="bricks" aria-hidden="true"><span></span><span></span><span></span></div>
  <p class="kicker">Opening Early 2027 · {PLAZA} · Apex, North Carolina</p>
  <h1 class="brandword">Brick <em>&amp;</em> Basil</h1>
  <p class="standfirst">An authentic Italian concept with food-truck roots — the forever home of the Rolling Deep kitchen. Handmade pasta, Detroit-style deep dish and focaccia sandwiches, made from scratch in a glass pasta room you can watch.</p>
  {CTA}
</section>
<main id="main">
<section class="features">
  <h2 class="sr-only">What&rsquo;s coming</h2>
  <a class="feature" href="/handmade-pasta">
    <span class="fnum">01</span>
    <span class="fpic pic-pasta" aria-hidden="true"></span>
    <h3>Handmade pasta</h3>
    <p>The menu is centered on fresh, handmade pasta — rolled and cut in the glass pasta room at the front of the dining room.</p>
    <span class="more">Inside the pasta room →</span>
  </a>
  <a class="feature" href="/detroit-deep-dish">
    <span class="fnum">02</span>
    <span class="fpic pic-dish" aria-hidden="true"></span>
    <h3>Detroit-style deep dish</h3>
    <p>Crispy golden edges, buttery crust, layers of cheese and sauce — the pies the Rolling Deep truck built its line on.</p>
    <span class="more">The deep dish story →</span>
  </a>
  <a class="feature" href="/focaccia-sandwiches">
    <span class="fnum">03</span>
    <span class="fpic pic-focc" aria-hidden="true"></span>
    <h3>Focaccia sandwiches</h3>
    <p>Focaccia sandwiches and other Italian dishes — made from scratch, like everything else this kitchen turns out.</p>
    <span class="more">More of the menu →</span>
  </a>
</section>
<section class="facts" aria-label="The room and the plan">
  <p><b>50 seats</b> inside, <b>35 more</b> on a newly built patio</p>
  <p><b>Pasta room in glass</b> — the dough and the pasta get made in view of your table</p>
  <p><b>Your call on service</b> — seat yourself and order by QR code, or take full table service</p>
  <p><b>Most ingredients imported from Italy</b>, the rest from North Carolina organic farms and local growers</p>
</section>
<section class="strip">
  <p class="stripk">From the truck to a forever home</p>
  <p class="stript">Chef Scott Harvey grew up in the restaurant business, worked upstate New York kitchens and restaurant consulting, then built <b>Rolling Deep</b> — the Detroit-style deep dish and fusion egg roll truck. Brick &amp; Basil is its forever home: the truck is on hiatus while the buildout happens, and the catering kitchen keeps booking.</p>
  <p class="cta"><a class="btn btn-brick" href="/our-story">Read the story</a> <a class="btn btn-ghost" href="/catering">Book catering</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_restaurant()}</script>
<script type="application/ld+json">{breadcrumbs('Home', '/')}</script>
</body>
</html>''')

# ---------- MENU HUB ----------
PAGES['menu.html'] = (head(
    f'Menu — What&rsquo;s Coming at {BRAND_PLAIN}, Apex NC',
    'What the menu at Brick &amp; Basil in Apex, NC will cover: handmade pasta, Detroit-style deep dish pizza, focaccia sandwiches and other Italian plates — scratch-made, preservative-free. Full items and prices land closer to opening.',
    '/menu'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Menu</p>
  <h1>Written the way the kitchen works</h1>
  <p class="lead">Everything starts from scratch — organic-milled flour, mozzarella stretched on site, dough made in the glass pasta room. Most ingredients are imported from Italy; the rest come from North Carolina organic farms and area growers. Menu items and prices will be announced as the opening gets closer.</p>
</section>
<div class="edrow">
  <div class="ednum" aria-hidden="true">01</div>
  <div class="edpic pic-pasta" aria-hidden="true"></div>
  <div class="edtext">
    <h2><a href="/handmade-pasta">Handmade pasta</a></h2>
    <p>A chef-driven pasta program — noodles rolled and cut by hand in view of the dining room. Gluten-free options are part of the plan at opening.</p>
  </div>
</div>
<div class="edrow alt">
  <div class="ednum" aria-hidden="true">02</div>
  <div class="edpic pic-dish" aria-hidden="true"></div>
  <div class="edtext">
    <h2><a href="/detroit-deep-dish">Detroit-style deep dish</a></h2>
    <p>The square pan, the crispy cheese edges, the layers. This is the food the Rolling Deep truck was known for — now with dining-room tables under it.</p>
  </div>
</div>
<div class="edrow">
  <div class="ednum" aria-hidden="true">03</div>
  <div class="edpic pic-focc" aria-hidden="true"></div>
  <div class="edtext">
    <h2><a href="/focaccia-sandwiches">Focaccia sandwiches &amp; other Italian plates</a></h2>
    <p>Focaccia sandwiches and other Italian dishes round out the menu — the full lineup is coming with the opening announcement.</p>
  </div>
</div>
<section class="smallprint">
  <h2>The small stuff, decided early</h2>
  <ul class="checks">
    <li>Mozzarella stretched on site</li>
    <li>Organically milled flour</li>
    <li>Scratch-made, no preservatives</li>
    <li>Gluten-free options planned for opening</li>
    <li>Filtered tap water on every table</li>
  </ul>
  {CTA}
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Menu at Brick & Basil', '/menu', 'Handmade pasta, Detroit-style deep dish, focaccia sandwiches and other Italian plates in Apex, NC.', 'Apex (NC), Cary (NC), Morrisville (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Menu', '/menu')}</script>
</body>
</html>''')

# ---------- HANDMADE PASTA ----------
PAGES['handmade-pasta.html'] = (head(
    f'Handmade Pasta — {BRAND_PLAIN}, Apex NC',
    'Handmade pasta in Apex, NC: a chef-driven pasta lineup rolled and cut by hand in Brick & Basil&rsquo;s glass-enclosed pasta room, from organically milled flour. Opening early 2027 at The Ballast on Salem.',
    '/handmade-pasta'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">01 · In View Of Your Table</p>
  <h1>The pasta happens in a glass room</h1>
  <p class="lead">At the front of the dining room sits a pasta room enclosed in glass. Staff prepare pasta, pizza dough and other items right there — you can watch the whole thing while you wait for your pie.</p>
</section>
<div class="panel">
  <div class="window" aria-hidden="true"><span class="windowpane"></span><span class="windowlabel">PASTA ROOM</span></div>
  <div class="panelflow">
    <h2>What to expect</h2>
    <ul class="checks">
      <li>A chef-driven pasta lineup — made by hand, every service</li>
      <li>Noodles rolled and cut by hand, from organically milled flour</li>
      <li>Mozzarella stretched on site, the same morning it gets used</li>
      <li>Gluten-free options planned for opening</li>
    </ul>
    <p class="notefine">Menu items and prices will be announced closer to opening.</p>
    <p class="cta"><a class="btn btn-big" href="tel:{PHONE}">Call&nbsp;{PHONE_TXT}</a> <a class="btn btn-ghost btn-big" href="/menu">Back&nbsp;to&nbsp;the&nbsp;menu</a></p>
  </div>
</div>
<section class="strip">
  <p class="stripk">Watch it happen</p>
  <p class="stript">The room is built for volume — state-of-the-art equipment behind glass, so the scratch cooking never slows the dining room down.</p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Handmade Pasta', '/handmade-pasta', 'Handmade pasta, rolled and cut in view of the dining room at Brick & Basil, Apex, NC.', 'Apex (NC), Cary (NC), Morrisville (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Handmade Pasta', '/handmade-pasta')}</script>
</body>
</html>''')

# ---------- DETROIT DEEP DISH ----------
PAGES['detroit-deep-dish.html'] = (head(
    f'Detroit-Style Deep Dish — {BRAND_PLAIN}, Apex NC',
    'Detroit-style deep dish pizza in Apex, NC: crispy golden edges, buttery crust, layers of cheese and sauce — from Rolling Deep&rsquo;s truck pies to dining tables at Brick & Basil, opening early 2027.',
    '/detroit-deep-dish'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">02 · The Pie The Truck Was Built On</p>
  <h1>Detroit-style deep dish, the way the truck made it</h1>
  <p class="lead">The crispy golden edges. The buttery crust. The layers of cheese and sauce. This is the pizza the Rolling Deep food truck specialized in — the reason the truck was a fixture around Wake County, now with a dining room under it.</p>
</section>
<div class="panwrap">
  <figure class="panfig">
    <svg class="pan" viewBox="0 0 640 420" role="img" aria-label="Illustration of a Detroit-style square pan pizza with cheese, sauce stripes and toppings">
      <rect x="20" y="20" width="600" height="380" rx="26" fill="#2a211c" />
      <rect x="44" y="44" width="552" height="332" rx="14" fill="#8d3728" />
      <rect x="60" y="60" width="520" height="300" rx="10" fill="#e9c46a" />
      <g fill="#c1493a"><circle cx="150" cy="130" r="24"/><circle cx="320" cy="105" r="21"/><circle cx="480" cy="140" r="24"/><circle cx="220" cy="220" r="22"/><circle cx="400" cy="235" r="24"/><circle cx="130" cy="310" r="21"/><circle cx="310" cy="330" r="24"/><circle cx="500" cy="300" r="22"/><circle cx="540" cy="200" r="18"/><circle cx="100" cy="215" r="16"/></g>
      <g stroke="#a34131" stroke-width="7"><line x1="80" y1="170" x2="560" y2="150"/><line x1="80" y1="270" x2="560" y2="262"/></g>
      <rect x="44" y="44" width="552" height="332" rx="14" fill="none" stroke="#f4e9d8" stroke-width="10" />
    </svg>
    <figcaption>The square pan: cheese to the edges, sauce in stripes, out of the pan onto the table.</figcaption>
  </figure>
  <div class="panflow">
    <h2>Why Detroit-style</h2>
    <p>Chef Scott Harvey&rsquo;s truck specialized in deep dish pizza — the perceived gap in the market for a properly-made scratch pie is exactly what pushed the truck toward a permanent home at {PLAZA}.</p>
    <ul class="checks">
      <li>Baked in a rectangular pan, not round — the edges get crispy and golden</li>
      <li>Layers of cheese and sauce, built the Detroit way</li>
      <li>Dough made in the glass pasta room next door</li>
      <li>The pizza Rolling Deep specialized in — served at a table</li>
    </ul>
    <p class="cta"><a class="btn btn-big" href="tel:{PHONE}">Call&nbsp;{PHONE_TXT}</a> <a class="btn btn-ghost btn-big" href="/visit">See&nbsp;the&nbsp;map</a></p>
  </div>
</div>
<section class="strip">
  <p class="stripk">&ldquo;From four wheels to four walls&rdquo;</p>
  <p class="stript">— the page&rsquo;s own words, as the buildout plans went in with the city of Apex. Construction is next.</p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Detroit-Style Deep Dish Pizza', '/detroit-deep-dish', 'Detroit-style deep dish pizza baked in rectangular pans at Brick & Basil, Apex, NC.', 'Apex (NC), Cary (NC), Raleigh (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Detroit-Style Deep Dish', '/detroit-deep-dish')}</script>
</body>
</html>''')

# ---------- FOCACIA ----------
PAGES['focaccia-sandwiches.html'] = (head(
    f'Focaccia &amp; Sandwiches — {BRAND_PLAIN}, Apex NC',
    'Focaccia sandwiches and other Italian plates at Brick & Basil in Apex, NC — made the same scratch-made way as the pasta and pizza. Opening early 2027 at The Ballast on Salem.',
    '/focaccia-sandwiches'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">03 · Off The Same Dough</p>
  <h1>Focaccia sandwiches &amp; the rest of the table</h1>
  <p class="lead">Scratch-made and preservative-free is the rule for everything this kitchen turns out — the pasta, the pizza dough and the focaccia alike. Sandwiches and other Italian dishes come off that same standard.</p>
</section>
<div class="edrow">
  <div class="ednum" aria-hidden="true">A</div>
  <div class="edpic pic-focc" aria-hidden="true"></div>
  <div class="edtext">
    <h2>Focaccia sandwiches</h2>
    <p>Focaccia sandwiches are on the menu from day one. Fillings and names land with the opening announcement — what&rsquo;s certain is that they&rsquo;re made from scratch.</p>
  </div>
</div>
<div class="edrow alt">
  <div class="ednum" aria-hidden="true">B</div>
  <div class="edpic pic-plates" aria-hidden="true"></div>
  <div class="edtext">
    <h2>Other Italian plates</h2>
    <p>The menu goes beyond pasta, pie and sandwiches into other Italian dishes — the full lineup is coming with opening. The kitchen&rsquo;s rules of the house don&rsquo;t change: imported Italian staples, organic North Carolina produce and area farms, nothing with a preservative list.</p>
  </div>
</div>
{CTA}
</main>
{footer()}
<script type="application/ld+json">{ld_service('Focaccia Sandwiches', '/focaccia-sandwiches', 'Focaccia sandwiches and other Italian plates at Brick & Basil, Apex, NC.', 'Apex (NC), Cary (NC), Morrisville (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Focaccia & Sandwiches', '/focaccia-sandwiches')}</script>
</body>
</html>''')

# ---------- CATERING ----------
PAGES['catering.html'] = (head(
    f'Catering &amp; Events — {BRAND_PLAIN} / Harvey Hospitality, Apex NC',
    'Catering and private-event bookings from Harvey Hospitality Catering — the kitchen behind Brick & Basil, catering in Apex and the Triangle for about four years, still booking while the dining room is built out.',
    '/catering'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Already In The Event Business</p>
  <h1>The kitchen is catering your event right now</h1>
  <p class="lead">Chef Harvey has run <b>Harvey Hospitality Catering</b> for about four years — catering and private events across the Apex and Triangle area. While the Brick &amp; Basil buildout happens, the catering side keeps booking.</p>
</section>
<div class="cateringgrid">
  <div class="ccard">
    <h2>What gets booked</h2>
    <ul class="checks">
      <li>Catering for private events and gatherings</li>
      <li>Bookings across Apex and the Triangle</li>
      <li>Dates while the dining room is built out</li>
    </ul>
  </div>
  <div class="ccard">
    <h2>How it gets served</h2>
    <ul class="checks">
      <li>Send the date, headcount and the plan</li>
      <li>Use the form below or call the shop line</li>
      <li>The catering kitchen answers directly</li>
    </ul>
  </div>
</div>
<section class="strip">
  <p class="stripk">Book ahead</p>
  <p class="stript">Send the date, headcount and what you&rsquo;re celebrating — the form below lands in the shop inbox and the catering side answers it.</p>
  <p class="cta"><a class="btn btn-big" href="/contact">Start&nbsp;a&nbsp;catering&nbsp;inquiry</a> <a class="btn btn-brick btn-big" href="tel:{PHONE}">Call&nbsp;{PHONE_TXT}</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Catering &amp; Events', '/catering', 'Catering and private-event bookings from Harvey Hospitality Catering, the kitchen behind Brick & Basil, Apex, NC.', 'Raleigh–Durham–Cary (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Catering & Events', '/catering')}</script>
</body>
</html>''')

# ---------- OUR STORY ----------
PAGES['our-story.html'] = (head(
    f'Our Story — Chef Scott Harvey, {BRAND_PLAIN}, Apex NC',
    'The story of Brick & Basil: chef Scott Harvey — upstate New York kitchens, restaurant consulting, the Rolling Deep food truck — opens an authentic Italian restaurant at The Ballast on Salem, Apex, NC, early 2027.',
    '/our-story'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Our Story</p>
  <h1>From food truck roots to a forever home</h1>
  <p class="lead">Brick &amp; Basil is an authentic Italian concept with food-truck roots — the next chapter of a kitchen that has been building toward a dining room for years.</p>
</section>
<ol class="timeline">
  <li>
    <p class="tdate">Raised In It</p>
    <h2>A restaurant childhood, upstate New York</h2>
    <p>Scott Harvey grew up in the restaurant business — his father was a chef. He worked high-end kitchens in upstate New York before moving into restaurant consulting, helping other owners open rooms, fix operations and plan buildouts.</p>
  </li>
  <li>
    <p class="tdate">The Truck Era</p>
    <h2>Harvey Hospitality Catering + Rolling Deep</h2>
    <p>Around four years ago he started his own catering company and launched <b>Rolling Deep</b>, a food truck built on Detroit-style deep dish pizzas and fusion egg rolls. The truck&rsquo;s success — and a gap he saw in the market for high-quality deep dish pizza — pointed toward four walls.</p>
  </li>
  <li>
    <p class="tdate">Now</p>
    <h2>Brick &amp; Basil, at The Ballast on Salem</h2>
    <p>Plans for Brick &amp; Basil are filed with the city of Apex and the buildout is next: 50 seats inside, 35 on a new patio, and a glass-enclosed pasta room at the front of the house. Opening early 2027. The truck is on hiatus while the forever home comes together — catering stays open for business.</p>
  </li>
</ol>
<blockquote class="bigquote">
  <p>&ldquo;My grandfather was a butcher, and I didn&rsquo;t even see a grocery store till I was 16.&rdquo;</p>
  <cite>Scott Harvey, on the farm childhood behind the kitchen&rsquo;s sourcing rules</cite>
</blockquote>
<section class="strip">
  <p class="stripk">The rules of the house</p>
  <p class="stript">Clean food, trusted sourcing, everything made from scratch without preservatives. Most ingredients imported from Italy; the rest from North Carolina organic products and area farmers — organic-milled flour, mozzarella stretched in house, filtered tap water on the table.</p>
  {CTA}
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('About Chef Scott Harvey', '/our-story', 'Chef Scott Harvey — Rolling Deep food truck, Harvey Hospitality Catering — opening an authentic Italian restaurant, Brick & Basil, in Apex, NC.', 'Apex (NC), Cary (NC), Raleigh (NC)')}</script>
<script type="application/ld+json">{breadcrumbs('Our Story', '/our-story')}</script>
</body>
</html>''')

# ---------- VISIT ----------
FAQ_ITEMS = [
    ('When does Brick & Basil open?', 'Opening early 2027 at The Ballast on Salem in Apex, NC. Plans have been submitted to the city of Apex and construction is next. Facebook is the main source of progress updates.'),
    ('Where exactly is it?', '1801 Chatham Flats Dr Suite 4, Apex, NC 27502 — at The Ballast on Salem.'),
    ('How does seating work?', 'About 50 seats inside and 35 on a newly built patio. You&rsquo;ll be able to seat yourself and order from your phone by QR code, or opt for full table service.'),
]
def ld_faq():
    obj = {'@context': 'https://schema.org', '@type': 'FAQPage',
           'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ_ITEMS]}
    return json.dumps(obj, ensure_ascii=False)

PAGES['visit.html'] = (head(
    f'Visit — {BRAND_PLAIN} at The Ballast on Salem, Apex NC',
    f'Visiting Brick & Basil: {FULL_ADDR} — {PLAZA}, Apex, NC. 50 indoor seats plus a 35-seat patio, QR self-ordering or full service. Opening early 2027.',
    '/visit'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Visit</p>
  <h1>{PLAZA}, Apex</h1>
  <p class="lead">Brick &amp; Basil is going in at {STREET}, Apex, NC 27502 — <b>opening early 2027</b>. The exact opening day and hours will be announced once the buildout sets them.</p>
</section>
<div class="visitgrid">
  <section class="mapbox">
    <iframe title="Map to Brick &amp; Basil, {STREET}, {CITY} 27502" width="100%" height="380" frameborder="0" style="border:0;display:block"
      src="https://www.google.com/maps?q=1801%20Chatham%20Flats%20Dr%2C%20Apex%2C%20NC%2027502&output=embed" loading="eager" referrerpolicy="no-referrer-when-downgrade"></iframe>
    <p class="fineprint">Map not loading? <a href="{MAPQ}" rel="noopener">Open it in Google Maps</a> or <a href="mailto:{EMAIL}">email us</a>.</p>
  </section>
  <aside class="visitinfo">
    <h2>The details</h2>
    <p class="clabel">Address</p>
    <address class="bigaddr">{PLAZA}<br>{STREET}<br>{CITY} 27502</address>
    <p class="clabel">Phone</p>
    <p class="cbig"><a href="tel:{PHONE}">{PHONE_TXT}</a></p>
    <p class="clabel">Email</p>
    <p class="cbig"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="clabel">The room</p>
    <p class="roomline">50 seats inside · 35-seat patio · glass pasta room</p>
    <p class="clabel">Service style</p>
    <p class="roomline">Seat yourself and order by QR code, or take full table service</p>
    <p class="clabel">Opening</p>
    <p class="roomline">Early 2027 — day and hours to be announced</p>
  </aside>
</div>
<section class="faq">
  <h2>Before anyone asks</h2>
  <details>
    <summary>When does Brick &amp; Basil open?</summary>
    <p>Opening early 2027 at {PLAZA} in Apex, NC. Plans have been submitted to the city of Apex and construction is next. Facebook is the main source of progress updates.</p>
  </details>
  <details>
    <summary>Where exactly is it?</summary>
    <p>{STREET}, Apex, NC 27502 — at {PLAZA}.</p>
  </details>
  <details>
    <summary>How does seating work?</summary>
    <p>About 50 seats inside and 35 on a newly built patio. You&rsquo;ll be able to seat yourself and order from your phone by QR code, or opt for full table service.</p>
  </details>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Visit Brick & Basil', '/visit', 'Dining room opening early 2027 at The Ballast on Salem, 1801 Chatham Flats Dr Suite 4, Apex, NC 27502.', 'Apex (NC), Cary (NC), Morrisville (NC)')}</script>
<script type="application/ld+json">{ld_faq()}</script>
<script type="application/ld+json">{breadcrumbs('Visit', '/visit')}</script>
</body>
</html>''')

# ---------- CONTACT ----------
PAGES['contact.html'] = (head(
    f'Contact — {BRAND_PLAIN}, Apex NC',
    f'Contact Brick & Basil in Apex, NC: phone {PHONE_TXT}, info email, catering bookings and opening updates — The Ballast on Salem, {FULL_ADDR}.',
    '/contact'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Talk To The Shop</p>
  <h1>Contact Brick &amp; Basil</h1>
  <p class="lead">Opening questions, catering bookings, or press about the buildout — email, call, or use the form. It lands straight in the shop&rsquo;s inbox.</p>
</section>
<div class="contactgrid">
  <form class="cform" method="post" action="/contact">
    <h2>Send a message</h2>
    <p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" required maxlength="120" autocomplete="name"></p>
    <p><label for="f-phone">Phone <span>(optional)</span></label><input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel"></p>
    <p><label for="f-email">Email</label><input id="f-email" name="email" type="email" required maxlength="160" autocomplete="email"></p>
    <p><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" required maxlength="4000"></textarea></p>
    <p><button class="btn btn-brick btn-big" type="submit">Send Message</button></p>
    <p class="fineprint">This form emails the shop directly. We never share your details.</p>
  </form>
  <section class="cinfo">
    <h2>Direct lines</h2>
    <p class="clabel">Phone</p>
    <p class="cbig"><a href="tel:{PHONE}">{PHONE_TXT}</a></p>
    <p class="clabel">Email</p>
    <p class="cbig"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="clabel">The corner that&rsquo;s coming</p>
    <address class="bigaddr">{PLAZA}<br>{STREET}<br>{CITY} 27502</address>
    <p class="clabel">Progress updates land on</p>
    <p class="cbig"><a href="{FB}" rel="noopener">Facebook</a> · <a href="{IG}" rel="noopener">Instagram</a></p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Contact', '/contact')}</script>
</body>
</html>''')

# ---------- PRIVACY ----------
PAGES['privacy.html'] = (head(
    f'Privacy Policy — {BRAND_PLAIN}, Apex NC',
    'Privacy policy for the Brick &amp; Basil website: how the contact form works, and the fact that there are no trackers and no cookies.',
    '/privacy'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Privacy</p>
  <h1>Short, like the menu will be honest</h1>
</section>
<section class="prose">
  <h2>What this site collects</h2>
  <p>This site has no advertising trackers, no analytics scripts and no cookies. The only information it takes is what you choose to send through the contact form: your name, an optional phone number, your email and your message.</p>
  <h2>Where it goes</h2>
  <p>The contact form delivers your message directly to Brick &amp; Basil&rsquo;s inbox so the shop can answer you — for opening questions, catering bookings and event inquiries. It isn&rsquo;t sold, rented or added to any third-party list.</p>
  <h2>Hosting and mail delivery</h2>
  <p>The site is static HTML hosted on Railway, and form messages are relayed by Brevo, an email-delivery provider, purely to reach the shop&rsquo;s inbox. Standard web-request logs (IP address, browser type, requested page) exist for uptime and abuse checks and aren&rsquo;t used for profiling.</p>
  <h2>Questions</h2>
  <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE_TXT} and ask about anything on this page. This site currently carries a <em>noindex</em> marker because the restaurant is pre-opening; search-indexing settings may change at opening, and this page will say so.</p>
</section>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Privacy', '/privacy')}</script>
</body>
</html>''')

# ---------- 404 ----------
PAGES['404.html'] = (head(
    f'Page not found — {BRAND_PLAIN}',
    'Page not found at the Brick & Basil site. Back to the main page, or straight to what&rsquo;s coming on the menu.',
    '/404'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">404</p>
  <h1>That one&rsquo;s still in the kitchen.</h1>
  <p class="lead">This page doesn&rsquo;t exist yet — the restaurant itself is opening early 2027. Meanwhile the menu and the map are one click away.</p>
  <p class="cta"><a class="btn btn-brick btn-big" href="/">Back to Home</a> <a class="btn btn-ghost btn-big" href="/menu">See What&rsquo;s Coming</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

# ---------- THANKS ----------
PAGES['thanks.html'] = (head(
    f'Message sent — {BRAND_PLAIN}',
    'Thanks for reaching out to Brick & Basil — the shop will get back to you.',
    '/thanks'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">Received</p>
  <h1>Your message is in.</h1>
  <p class="lead">Thank you — the shop will get back to you personally. Meanwhile, the pasta room, the pies and the map are all one click away.</p>
  <p class="cta"><a class="btn btn-brick btn-big" href="/menu">See What&rsquo;s Coming</a> <a class="btn btn-ghost btn-big" href="/visit">Plan your future visit</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

for fname, (h, body) in PAGES.items():
    with open(os.path.join(PUB, fname), 'w', encoding='utf-8') as f:
        f.write(h + '\n' + body)
    print('wrote', fname, len(h + body), 'bytes')

# ---------- sitemap / robots / favicon ----------
pages_order = ['/', '/menu', '/handmade-pasta', '/detroit-deep-dish', '/focaccia-sandwiches', '/catering', '/our-story', '/visit', '/contact', '/privacy']
today = '2026-11-24'
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages_order) + '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
''')
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#241c18"/><rect x="10" y="24" width="44" height="28" rx="7" fill="#8d3728"/><path d="M32 6 C42 14 40 24 32 27 C24 24 22 14 32 6 Z" fill="#4e6b3a"/><line x1="32" y1="20" x2="32" y2="52" stroke="#f4e9d8" stroke-width="3"/></svg>
'''
open(os.path.join(PUB, 'favicon.svg'), 'w').write(favicon)
print('wrote sitemap.xml robots.txt favicon.svg')
print('PAGES:', len([f for f in PAGES if f.endswith('.html')]))
