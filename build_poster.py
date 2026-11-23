#!/usr/bin/env python3
"""Draw the 23 Nov 2026 world-news poster (1024x1024 PNG).
Deterministic: fixed text, colours, fonts, layout; no network, no time, no randomness.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BG = (250, 247, 240)
INK = (18, 24, 38)
RED = (178, 34, 34)
NAVY = (16, 42, 90)
TEAL = (0, 110, 110)
GOLD = (176, 124, 0)
SLATE = (70, 78, 92)

def font(name, size):
    paths = {
        "serif_b": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "sans_b": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "sans": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    }
    return ImageFont.truetype(paths[name], size)

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Header band
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((48, 22), "THE WORLD TODAY", font=font("serif_b", 48), fill=(255, 255, 255))
d.text((48, 92), "MONDAY  23  NOVEMBER  2026", font=font("sans_b", 28), fill=(255, 214, 90))
d.text((780, 30), "ONE IMAGE", font=font("sans_b", 24), fill=(255, 255, 255))
d.text((780, 62), "SIX STORIES", font=font("sans_b", 24), fill=(255, 255, 255))
d.text((780, 98), "23 NOV 2026", font=font("sans", 22), fill=(200, 215, 240))

# Lead story: Hormuz
d.rectangle([32, 168, 992, 388], fill=(255, 255, 255), outline=(200, 200, 190), width=2)
d.rectangle([32, 168, 992, 208], fill=RED)
d.text((52, 174), "LEAD  •  WAR AT SEA", font=font("sans_b", 24), fill=(255, 255, 255))
d.text((52, 222), "STRAIT OF HORMUZ", font=font("serif_b", 44), fill=INK)
lines = wrap(d, "Tankers struck and mines hit shipping in and near the strait; Iran's navy said two more tankers caught fire on Sunday. Attacks on shipping are at their highest since the war began.", font("sans", 26), 900)
y = 282
for ln in lines:
    d.text((52, y), ln, font=font("sans", 26), fill=INK)
    y += 34

stories = [
    ("COP31 FAILS", TEAL, "Climate talks in Turkey end with no deal — the final draft left out fossil fuels, and the EU, UK and about 130 parties rejected it."),
    ("UKRAINE", RED, "A Russian drone hit a five-storey flat in Dymer, north of Kyiv: 2 people killed, 11 missing, including two children."),
    ("LIBYA", NAVY, "Suspected sea drones hit the Russian corvette Merkury at Benghazi naval base. The ship was badly damaged and capsized; 10 hurt."),
    ("MERCURY", GOLD, "After an eight-year journey, Europe-Japan's BepiColombo entered orbit around Mercury — only the second mission ever to do so."),
    ("INDONESIA", TEAL, "Rescuers recovered 24 body bags from the candy-factory fire in Cikande, Banten, on Sunday."),
    ("SUDAN", RED, "Drone strikes hit Khartoum early on Sunday, damaging a UN facility while staff were inside; 3 killed in Omdurman."),
]
# 2 columns x 3 rows
x0s, y0 = 32, 408
cw, ch, gap = 468, 158, 24
for i, (tag, col, body) in enumerate(stories):
    x = x0s + (i % 2) * (cw + gap)
    yy = y0 + (i // 2) * (ch + 16)
    d.rectangle([x, yy, x + cw, yy + ch], fill=(255, 255, 255), outline=(200, 200, 190), width=2)
    d.rectangle([x, yy, x + 10, yy + ch], fill=col)
    d.text((x + 26, yy + 12), tag, font=font("sans_b", 26), fill=col)
    ls = wrap(d, body, font("sans", 21), cw - 44)
    y2 = yy + 48
    for ln in ls[:4]:
        d.text((x + 26, y2), ln, font=font("sans", 21), fill=INK)
        y2 += 26

# Bottom strip: sport & briefs
d.rectangle([32, 922, 992, 992], fill=NAVY)
d.text((52, 936), "ALSO:  Alcaraz wins ATP Finals  •  Liverpool beat Man Utd  •  UK hosts 2035 Women's WC",
       font=font("sans_b", 18), fill=(255, 255, 255))
d.text((52, 962), "Sources: AP • Reuters • BBC • Al Jazeera • AFP  —  reported 23 November 2026",
       font=font("sans", 17), fill=(200, 215, 240))

img.save("/home/hatch/workspace/news-image-20261123-reveriefayre/entry.png", format="PNG", optimize=True)
print("saved")
