#!/usr/bin/env python3
"""og.png 1200x630 — Brick & Basil — roast-ink poster with a staggered brick course.
Burnt-brick sienna, plaster cream, basil green, gold rules. Shop identity only."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

INK = (36, 28, 24); BRICK = (141, 55, 40); CREAM = (247, 239, 224); SAND = (216, 203, 182)
GOLD = (201, 138, 46); BASIL = (78, 107, 58)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style.ttc", "Palatino.ttc", "Georgia.ttf", "Times New Roman.ttf"], s)
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "HelveticaNeue.ttc", "Arial.ttf"], s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# staggered brick course along the bottom third
BH, GAP = 34, 8
y0 = H - 2*BH - GAP - 64
row_colors = [BRICK, (120, 46, 33)]
for r in range(2):
    y = y0 + r*(BH+GAP)
    offset = 0 if r == 0 else 78
    x = -offset
    i = 0
    while x < W:
        bw = 150 if i % 3 else 88
        d.rectangle([x, y, x+bw-6, y+BH], fill=row_colors[i % 2])
        x += bw + GAP
        i += 1

def center(text, f, y, fill, tracking=0):
    if tracking:
        widths = [d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text]
        tw = sum(widths) + tracking*(len(text)-1)
        x = (W-tw)/2
        for ch,w in zip(text,widths):
            bb = d.textbbox((0,0), ch, font=f)
            d.text((x - bb[0], y), ch, font=f, fill=fill)
            x += w + tracking
        return tw
    bb = d.textbbox((0,0), text, font=f)
    d.text(((W-(bb[2]-bb[0]))/2 - bb[0], y), text, font=f, fill=fill)
    return bb[2]-bb[0]

center("OPENING EARLY 2027  ·  THE BALLAST ON SALEM  ·  APEX, NORTH CAROLINA", sans(23), 44, GOLD, tracking=5)
center("Brick & Basil", serif(126), 96, CREAM)
d.rectangle([W/2-150, 262, W/2+150, 265], fill=GOLD)
d.rectangle([W/2-150, 271, W/2+150, 274], fill=GOLD)
center("Handmade pasta.  Detroit-style deep dish.", serif(46), 300, CREAM)
center("Focaccia sandwiches, off the same dough.", serif(38), 368, (233, 196, 106))
center("50 indoor seats · 35-seat patio · a glass pasta room you can watch", sans(24), 432, SAND)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
