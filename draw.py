#!/usr/bin/env python3
"""news-23 b88 front-page-dense: THE WORLD TODAY, Monday 23 November 2026.
Draws entry.png (1024x1024) with PIL. All 31 stories dated 23 Nov 2026.
Scenes are drawn illustrations, not photographs."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FD = "/usr/share/fonts/truetype/dejavu/"

def f_serif_b(sz):
    return ImageFont.truetype(FD + "DejaVuSerif-Bold.ttf", sz)

def f_sans_b(sz):
    return ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", sz)

def f_sans(sz):
    return ImageFont.truetype(FD + "DejaVuSans.ttf", sz)

def wrap(draw, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def chip(draw, x, y, label, fill):
    font = f_sans_b(9)
    tw = draw.textlength(label, font=font)
    w = int(tw) + 10
    draw.rounded_rectangle([x, y, x + w, y + 13], radius=2, fill=fill)
    draw.text((x + 5, y + 2), label, font=font, fill="white")
    return w

# palette
BLACK = (17, 17, 17)
RED = (176, 0, 32)
GOLD = (184, 134, 11)
CREAM = (245, 238, 218)
NAVY = (11, 30, 58)
GREEN = (13, 92, 46)
INK = (30, 30, 30)
GREY = (90, 90, 90)
LGREY = (230, 230, 230)
MAPG = (178, 214, 163)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 46], fill=BLACK)
d.text((12, 5), "THE WORLD TODAY", font=f_serif_b(32), fill="white")
d.text((W - 12 - d.textlength("MONDAY 23 NOVEMBER 2026", font=f_sans_b(16)), 14),
       "MONDAY 23 NOVEMBER 2026", font=f_sans_b(16), fill=(212, 175, 55))

# ---------- kicker ----------
d.rectangle([0, 46, W, 64], fill=RED)
d.text((12, 50), "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
       font=f_sans_b(13), fill="white")

# ---------- number strip (two rows of five) ----------
strip = [
    ("-3.3%", "KOSPI", (176, 0, 32)),
    ("5.3", "US-CHINA POWER GAP", (11, 60, 120)),
    ("11,762", "EBOLA CASES, DRC", (13, 92, 46)),
    ("10T won", "SEOUL STABILISATION FUND", (150, 110, 20)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (110, 40, 130)),
    ("$450M", "SKUBAL DEAL", (11, 60, 120)),
    ("165", "RUSSIAN MISSILES/WEEK", (176, 0, 32)),
    ("12,000", "CLEARED IN MANCHESTER", (13, 92, 46)),
    ("264 kg", "EXPLOSIVES SEIZED", (110, 40, 130)),
    ("$107.3B", "ANTHROPIC IPO", (13, 92, 46)),
]
colw = W // 5
for i, (val, lab, col) in enumerate(strip):
    row, c = divmod(i, 5)
    x = c * colw + 8
    yv = 68 + row * 30
    d.text((x, yv), val, font=f_sans_b(19), fill=col)
    d.text((x, yv + 20), lab, font=f_sans_b(8), fill=GREY)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", (11, 60, 120)), ("AMERICAS 8", (176, 0, 32)),
           ("MIDDLE EAST 6", (150, 110, 20)), ("EUROPE 5", (0, 120, 110)),
           ("AFRICA 3", (110, 40, 130)), ("WORLD 2", (40, 40, 40))]
seg = W // 6
for i, (lab, col) in enumerate(regions):
    x = i * seg
    d.rectangle([x, 128, x + seg - 1, 144], fill=col)
    tw = d.textlength(lab, font=f_sans_b(11))
    d.text((x + (seg - tw) / 2, 131), lab, font=f_sans_b(11), fill="white")

# ---------- THE DAY IN UTC ----------
d.rectangle([0, 146, W, 162], fill=(245, 245, 245))
d.text((12, 149), "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles",
       font=f_sans(11), fill=INK)
d.text((W - 12 - d.textlength("~ APPROX", font=f_sans(10)), 150), "~ APPROX", font=f_sans(10), fill=GREY)

# ---------- heroes ----------
HX = [8, 350, 692]
HW = 324
hy0 = 166          # scene top
scene_h = 94
strip_y = hy0 + scene_h          # black strip under scene
head_y = strip_y + 16
body_y = head_y + 44
src_y = body_y + 28

def hero_scene_kospi(x):
    d.rectangle([x, hy0, x + HW, hy0 + scene_h], fill=NAVY)
    # buildings with lit windows
    import random
    rnd = random.Random(7)
    bx = x + 6
    while bx < x + HW - 20:
        bw = rnd.randint(22, 40)
        bh = rnd.randint(28, 62)
        by = hy0 + scene_h - bh
        d.rectangle([bx, by, bx + bw, hy0 + scene_h], fill=(24, 48, 88))
        for wy in range(by + 5, hy0 + scene_h - 5, 10):
            for wx in range(bx + 4, bx + bw - 4, 9):
                if rnd.random() < 0.55:
                    d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 210, 90))
        bx += bw + 4
    # orange chart line
    pts = [(x + 10, hy0 + 78), (x + 70, hy0 + 60), (x + 130, hy0 + 70),
           (x + 190, hy0 + 42), (x + 250, hy0 + 52), (x + 310, hy0 + 26)]
    d.line(pts, fill=(255, 140, 40), width=3)
    for p in pts:
        d.ellipse([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill="white", outline=(255, 140, 40))
    d.text((x + 10, hy0 + 6), "-3.3%", font=f_sans_b(30), fill=(255, 90, 90))

def hero_scene_guterres(x):
    d.rectangle([x, hy0, x + HW, hy0 + scene_h], fill=GREEN)
    d.text((x + 12, hy0 + 8), "150 DELEGATES", font=f_sans_b(26), fill=(255, 215, 90))
    d.text((x + 12, hy0 + 38), "BACK A RISK", font=f_sans_b(26), fill=(255, 215, 90))
    d.text((x + 12, hy0 + 68), "FRAMEWORK", font=f_sans_b(26), fill=(255, 215, 90))
    # globe
    cx, cy, r = x + HW - 46, hy0 + 48, 38
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(190, 230, 200), outline=(255, 255, 255), width=2)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=(120, 170, 130), width=1)
    d.line([cx - r, cy, cx + r, cy], fill=(120, 170, 130), width=1)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=(120, 170, 130), width=1)

def hero_scene_power(x):
    d.rectangle([x, hy0, x + HW, hy0 + scene_h], fill=CREAM)
    d.text((x + 10, hy0 + 6), "NARROWEST SINCE 2018", font=f_sans_b(10), fill=INK)
    d.text((x + HW - 10 - d.textlength("GAP 5.3", font=f_sans_b(10)), hy0 + 6),
           "GAP 5.3", font=f_sans_b(10), fill=RED)
    bars = [("78.9", "US", NAVY, 62), ("73.6", "CHINA", RED, 57), ("40.5", "INDIA", (184, 134, 11), 32)]
    bx = x + 24
    for val, lab, col, bh in bars:
        by = hy0 + scene_h - 6 - bh
        d.rectangle([bx, by, bx + 78, hy0 + scene_h - 6], fill=col)
        vw = d.textlength(val, font=f_sans_b(15))
        vcol = "white" if col != (184, 134, 11) else (40, 40, 40)
        d.text((bx + (78 - vw) / 2, by + 4), val, font=f_sans_b(15), fill=vcol)
        lw = d.textlength(lab, font=f_sans_b(11))
        d.text((bx + (78 - lw) / 2, hy0 + scene_h - 24), lab, font=f_sans_b(11), fill="white")
        bx += 92

heroes = [
    ("KOSPI 4,708.54  \u00b7  -161 PTS", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE", hero_scene_kospi),
    ("UN  \u00b7  BRIDGETOWN", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 back a risk framework.",
     "UNITED NATIONS", hero_scene_guterres),
    ("ASIA POWER INDEX 2026", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE", hero_scene_power),
]
for (strip_txt, head, body, src, scene_fn), x in zip(heroes, HX):
    scene_fn(x)
    d.rectangle([x, strip_y, x + HW, strip_y + 16], fill=BLACK)
    d.text((x + 6, strip_y + 2), strip_txt, font=f_sans_b(10), fill="white")
    lines = wrap(d, head, f_sans_b(19), HW)
    yy = head_y
    for ln in lines[:2]:
        d.text((x, yy), ln, font=f_sans_b(19), fill=INK)
        yy += 22
    blines = wrap(d, body, f_sans(11), HW)
    yy = body_y
    for ln in blines[:2]:
        d.text((x, yy), ln, font=f_sans(11), fill=INK)
        yy += 14
    d.text((x, src_y), src, font=f_sans(10), fill=GREY)
    chip(d, x + HW - 78, src_y - 1, "REPORTED", (11, 60, 120))

# ---------- MORE OF THE DAY strip ----------
d.rectangle([0, 366, W, 384], fill=BLACK)
d.text((12, 370), "MORE OF THE DAY  \u2014  10 STORIES", font=f_sans_b(12), fill="white")

# ---------- cards ----------
cards = [
    ("AMERICAS", (176, 0, 32), "BESSESSENT: NVIDIA ANSWERS", "Treasury wants answers.", "Reuters", "REPORTED", (11, 60, 120)),
    ("FBI", (40, 40, 40), "FBI PROBES NCIC HACK", "NCIC database hacked.", "AP", "REPORTED", (11, 60, 120)),
    ("WHITE HOUSE", (150, 110, 20), "TRUMP: IRAN STRIKES MAY RESUME", "May resume in New Year.", "Reuters", "REPORTED", (11, 60, 120)),
    ("MARKETS", (0, 120, 110), "US FUTURES JUMP 3%", "Holiday rally lifts 3%.", "Bloomberg", "REPORTED", (11, 60, 120)),
    ("SPORT", (176, 0, 32), "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED", (11, 60, 120)),
    ("SPORT", (176, 0, 32), "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice.", "ESPN", "REPORTED", (11, 60, 120)),
    ("LEGAL", (110, 40, 130), "STATES SUE SPACEX", "Ten states sue over AI.", "AP", "REPORTED", (11, 60, 120)),
    ("TECH", (0, 120, 110), "ANTHROPIC IPO: $107.3B", "Raised $83; closes $97.17.", "WSJ", "REPORTED", (11, 60, 120)),
    ("EUROPE", (150, 110, 20), "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: 3 Kh-101s crossed.", "AP", "CLAIM", RED),
    ("SPACE", (110, 40, 130), "RUSSIAN NUCLEAR SATELLITE", "May carry a nuke.", "Reuters", "CLAIM", RED),
]
cw, chh, gap = 198, 84, 6
for i, (cat, catcol, head, body, src, chiplab, chipcol) in enumerate(cards):
    row, col = divmod(i, 5)
    x = 8 + col * (cw + gap)
    y = 390 + row * (chh + 6)
    d.rectangle([x, y, x + cw, y + chh], outline=(200, 200, 200), width=1)
    d.rectangle([x, y, x + cw, y + 14], fill=catcol)
    d.text((x + 5, y + 2), cat, font=f_sans_b(9), fill="white")
    num = str(i + 1)
    d.text((x + cw - 6 - d.textlength(num, font=f_sans_b(10)), y + 2), num, font=f_sans_b(10), fill="white")
    hlines = wrap(d, head, f_sans_b(12), cw - 10)
    yy = y + 18
    for ln in hlines[:2]:
        d.text((x + 5, yy), ln, font=f_sans_b(12), fill=INK)
        yy += 15
    d.text((x + 5, y + 52), body, font=f_sans(10), fill=INK)
    d.text((x + 5, y + 68), src, font=f_sans(9), fill=GREY)
    chip(d, x + cw - 76, y + 67, chiplab, chipcol)

# ---------- map + ALSO ----------
d.rectangle([0, 566, W, 584], fill=BLACK)
d.text((12, 570), "WHERE IT HAPPENED", font=f_sans_b(12), fill="white")
d.text((330, 570), "ALSO ON MONDAY", font=f_sans_b(12), fill="white")

# map box
mx0, my0, mx1, my1 = 8, 590, 316, 830
d.rectangle([mx0, my0, mx1, my1], outline=INK, width=1, fill=(250, 250, 248))
# simplified world blobs
d.polygon([(30, 640), (120, 610), (150, 660), (120, 740), (70, 770), (35, 710)], fill=MAPG)   # Americas
d.polygon([(170, 620), (230, 600), (250, 640), (215, 680), (175, 660)], fill=MAPG)           # Europe
d.polygon([(240, 700), (300, 680), (310, 740), (270, 790), (235, 750)], fill=MAPG)           # Asia/Africa-ish
d.polygon([(160, 740), (210, 730), (220, 780), (175, 800), (155, 770)], fill=MAPG)           # Africa
pins = [
    (1, 235, 700), (2, 92, 742), (3, 262, 716), (4, 78, 668), (5, 108, 652),
    (6, 205, 636), (7, 88, 700), (8, 48, 700), (9, 66, 748), (10, 92, 764),
    (11, 218, 622), (12, 192, 616), (13, 240, 624),
]
for n, px, py in pins:
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline="white", width=1)
    d.text((px - 3, py - 6), str(n), font=f_sans_b(9), fill="white")
d.text((mx0 + 6, my1 - 44), "Pins 1-13: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing", font=f_sans(9), fill=INK)
d.text((mx0 + 6, my1 - 32), "4 Washington \u00b7 5 New York \u00b7 6 Kyiv \u00b7 7 Chicago \u00b7 8 SF", font=f_sans(9), fill=INK)
d.text((mx0 + 6, my1 - 20), "9 Denver \u00b7 10 Austin \u00b7 11 Warsaw \u00b7 12 London \u00b7 13 Moscow", font=f_sans(9), fill=INK)

# ALSO list, two columns of nine
also = [
    "14. Paris: 100+ back 2% billionaire tax",
    "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week",
    "17. COP31: the day after Antalya pact rejected",
    "18. Benghazi: UN demands probe of port attacks [CLAIM]",
    "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike",
    "21. West Bank settler attacks",
    "22. Iran war: no deal in sight",
    "23. Lebanon seizes 264 kg explosives",
    "24. Bahrain: strike hits plant, 2 hurt",
    "25. Sudan: defences down drones [CLAIM]",
    "26. DRC: fighting traps Ebola teams",
    "27. Bangladesh: Hasina jailed if she returns",
    "28. Seoul minister quits in exam row",
    "29. SK Telecom -7.3% as hype cools",
    "30. China eases margin rules",
    "31. Seoul readies 10T-won fund",
]
for i, item in enumerate(also):
    col = 0 if i < 9 else 1
    row = i % 9
    x = 330 + col * 350
    y = 592 + row * 26
    if "[CLAIM]" in item:
        base, _ = item.split(" [CLAIM]")
        d.text((x, y), base, font=f_sans(11), fill=INK)
        cx = x + d.textlength(base + " ", font=f_sans(11))
        d.text((cx, y), "[CLAIM]", font=f_sans_b(11), fill=RED)
    else:
        d.text((x, y), item, font=f_sans(11), fill=INK)

# ---------- DATE CHECK ----------
d.rectangle([8, 838, W - 8, 902], outline=RED, width=2)
d.text((16, 844), "DATE CHECK", font=f_sans_b(13), fill=RED)
d.text((W - 16 - d.textlength("READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY", font=f_sans_b(10)), 846),
       "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY", font=f_sans_b(10), fill=RED)
d.text((16, 864), "LEFT OUT \u2014 NOT 23 NOV: Dems 258 seats (22 Nov) \u00b7 Sparta II fire (22 Nov) \u00b7 El Chapo (22 Nov) \u00b7 EU-Indonesia (21 Nov) \u00b7 Nigeria boat (21 Nov) \u00b7 ICJ Myanmar (19 Nov)",
       font=f_sans(10), fill=INK)
d.text((16, 882), "NOT YET \u2014 Dymer search continues (14 missing) \u00b7 4 House races uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped Ebola staff",
       font=f_sans(10), fill=INK)

# ---------- footer ----------
d.text((12, 912), "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 NYT \u00b7 ESPN \u00b7 Lowy Institute (Asia Power Index 2026).",
       font=f_sans(10), fill=GREY)
d.text((12, 928), "CHIPS: REPORTED = confirmed by wires. CLAIM = one side's claim, not independently confirmed. ONGOING = still developing.",
       font=f_sans(10), fill=GREY)
d.text((12, 944), "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.",
       font=f_sans(10), fill=GREY)
d.line([0, 966, W, 966], fill=GOLD, width=2)
ft = "THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions"
d.text(((W - d.textlength(ft, font=f_sans_b(13))) / 2, 976), ft, font=f_sans_b(13), fill=GOLD)

img.save(OUT, "PNG")
print("saved", OUT, os.path.getsize(OUT), "bytes")
