#!/usr/bin/env python3
"""
Banner v12 - jako v11, ale text zuzeny o vnitrni okraj.

Bezpecna zona zmerena z DOM zustava jako HRANICE (x 43,5-80,0 %).
Uvnitr ni je jeste vnitrni okraj o sirce jednoho pismene, z obou stran stejne,
takze teziste bloku zustava na stejne svisle ose jako v v11.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 4200, 700
BG=(22,22,26); GOLD=(198,164,92); WHITE=(238,236,230); DIM=(160,156,148)
BASK="/System/Library/Fonts/Supplemental/Baskerville.ttc"
OUT="/Users/pavelkudrna/Downloads/personix-logo-fix/"

BX0, BX1 = int(0.435*W), int(0.800*W)   # hranice 1827 .. 3360
Y0, Y1   = int(0.21*H),  int(0.79*H)
CENTER   = (BX0+BX1)/2                   # teziste - musi zustat

T_EYE="UNCENSORABLE   ·   INCORRUPTIBLE"
T_MAIN="Decentralized Reputation Network"
T_CLAIM="Take your authority back."
T_URL="personix.org"

def f(s,i=0): return ImageFont.truetype(BASK,s,index=i)
def tw(d,t,fo,sp=0.0): return sum(d.textlength(c,font=fo) for c in t)+sp*(len(t)-1)
def tr(d,xy,t,fo,fill,sp=0.0):
    x,y=xy
    for ch in t:
        d.text((x,y),ch,font=fo,fill=fill); x+=d.textlength(ch,font=fo)+sp
def fit(d,t,mw,start,i=0,sp=0.0):
    for s in range(start,8,-2):
        fo=f(s,i)
        if tw(d,t,fo,sp)<=mw: return fo
    return f(9,i)

img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
for y in range(H):
    k=y/H
    d.line([(0,y),(W,y)],fill=(int(22+7*k),int(22+6*k),int(26+7*k)))

# vnitrni okraj = sirka jednoho pismene v nadpisu, dopocitano iterativne
box = BX1 - BX0
for _ in range(4):
    fm = fit(d, T_MAIN, box, 130)
    m  = d.textlength("n", font=fm)          # tloustka jednoho pismene
    box = (BX1 - BX0) - 2*m
X0 = CENTER - box/2
X1 = CENTER + box/2

fm = fit(d, T_MAIN, box, 130)
fe = fit(d, T_EYE,  box, 54, sp=9)
fc = fit(d, T_CLAIM, box, 72, i=1)
fu = f(44)
wm = tw(d, T_MAIN, fm)

h_total = fe.size + 26 + fm.size + 20 + 4 + 22 + fc.size
y = Y0 + max(0, (Y1-Y0-h_total-70)//2)

tr(d,(X0,y),T_EYE,fe,GOLD,9)
y += fe.size + 26
d.text((X0,y),T_MAIN,font=fm,fill=WHITE)
y += fm.size + 20
d.line([(X0,y),(X0+wm,y)],fill=GOLD,width=4)
y += 22
d.text((X0,y),T_CLAIM,font=fc,fill=WHITE)
tr(d,(X0+wm-tw(d,T_URL,fu,4),Y1-46),T_URL,fu,DIM,4)

img.save(OUT+"V12-linkedin.png", optimize=True)
print(f"hranice   {BX0/W*100:.1f}-{BX1/W*100:.1f} %  ({BX1-BX0} px)")
print(f"okraj     {m:.0f} px z kazde strany (sirka pismene n pri {fm.size} px)")
print(f"text      {X0/W*100:.1f}-{X1/W*100:.1f} %  ({box:.0f} px)")
print(f"tezisto   {CENTER/W*100:.2f} % - stejne jako v11")
print(f"nadpis    {fm.size} px = {fm.size*191/700:.0f} px na obrazovce")
print(f"{os.path.getsize(OUT+'V12-linkedin.png')/1024:.0f} kB")
