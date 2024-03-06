from FoxDot.preset import *

# OMG j'ai découvert le paramètre bpm de chaque synth_keys

k1 >> play("X.", bpm=120)
hh >> play("-", dur=cascara, bpm=120)
k2 >> play(".{....c}c{...c}", dur=.25, bpm=120, rate=[1,1.1])

k2 >> play("c{.c}c{c}", dur=.5, bpm=90)

hh >> play(".-", dur=cascara/2, bpm=linvar([120, 90], [8,inf], start=Clock.mod(4)))

k1.bpm=90

hh.degree = "-"

# Exemple 4 : 150 -> 120 elaboré

bassline = var([0,0,0,-1,5], 4)

change_bpm(150)
k1 >> play("v{.x}", dur=1/2)
hh >> play("{..-}{--[--]}", sdb=1, sample=(3,5), dur=cascara)
b1 >> pluckbass(bassline+[0,2], dur=2, sus=3.5, oct=[3,4])
b1.dur = [2,1]

k2 >> play("X", dur=5/4, output=12).fadein()

bassline2 = var([0,0,0,-1,5], 2*5/4)

b2 >> blip(bassline2, dur=P[.5]*5/4, sus=2, oct=4).fadein()

# Besoin de pouvoir créer plusieur Clocks et switcher la clock par défaut pour pas avoir a faire change_bpm
# OMG

# Exemple 3 : switcher de 150 à 120 => 4/5

change_bpm(150)
d1 >> play("X-")
b1 >> bbass([0,2,-2,5,2], dur=[1/2,1], oct=3)

d2 >> play("X", dur=5/4).fadein()
b2 >> bbass([0], dur=P[1,1/2]*5/4, oct=3).fadein()

b1.fadeout()

d1.stop()
b2.dur = [1,.5]
d2.dur = 1
change_bpm(120)

d3 >> play("-[--]", dur=1/2)

# Exemple 2 ?

change_bpm(130)

Clock.meter = (4,4)

k1 >> play("X...", dur=.25, sdb=1, lpf=500)
hh >> play("-(.-)", dur=.25, sdb=1, rate=[1.3,1.8,1])
cp >> play(".(...(*.))*.", dur=.25, sdb=1, rate=1.5)
m1 >> blip([0,0,2,1], dur=.25, oct=[4,5,6])

k1.degree = "X.(X.)."

k1.degree = "X.X..."

k1.degree = "X..."
k1.dur=3/8
Clock.meter = (6,4)

m1.degree = [0,0,0,2,1,2]
m1.oct=[3,4,5,6,5]

hh.dur=3/8

cp.stop()

cp >> play(".(...(*.))*.", dur=3/8, sdb=1, rate=2.5)
hh.dur = 3/8
hh.pan = Pvar([-.6,.6,P[-.4,.4].stutter(2)], 2)
hh.rate = var([1,2,1.5],2)
k1.degree = "V..."

m1.sus=1
m1.dur=3/8
m1.degree = [0,0,2,1]
m1.oct=[4,5,6]

### Exemple 1 ?

# cp.degree = ".*"

sn >> play("<..i.><..o.>", dur=3/8, sdb=1, lpf=20000, rate=1.3, sample=3, amp=2)
hh >> play("-", dur=.25, sdb=1, sample=0, rate=1.6, amp=2.5, room2=5)

k2 >> play(
    Pvar(vessel_kicks, 4),
    # vessel_kicks[1],
    dur=3/8,
    sdb=1,
    lpf=500,
    sample=4,
    # rate=1.2,
    rate=1,
    amp=2.8,
    output=12,
)
# k1.every(16,"stutter") # TODO fix that !!
k2.amp=2

sn.dur = 3/8
sn.rate = 1.5
sn.rate = linvar([1.5, 3], [16, inf], start=Clock.mod(4))

k2.dur=.25
sn.dur=.25
sn.rate=3

k1.dur=.25
k1.sample=3

p1 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
p1.fadein(32, fvol=.6)

##############################


k1 >> play("X...", dur=.25, sdb=1, lpf=500)
hh >> play("-(.-)", dur=.25, sdb=1, rate=[1.3,1.8,1])
cp >> play(".(...(*.))*.", dur=.25, sdb=1, rate=1.5)
m1 >> blip([0,0,2,1], dur=.25, oct=[4,5,6])

k1.degree = "X..X."
hh.degree = ".-..-"

m1.dur = 2/5
