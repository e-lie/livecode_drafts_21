
from renardo_lib.preset import *
gone = instanciate("chan1", "pads/gone_1")


g1 >> gone([0,2,4], body=linvar([0,1],8), dull=linvar([0,1],7), oct=4)


d1 >> play("X(.*)", lpf=2500)
b1 >> blip([0,1,2,0,None], dur=.25, sus=.9, oct=[4,5,3,6], lpf=1500)
b2 >> blip([0,1,None], dur=.5, sus=.9, oct=P[4,5,3,6]+1, lpf=1500)

Clock.bpm=140

Root.default = var(PTri(12), .5)
Root.default = 0

d1 >> blip([0,2], dur=[.25, .25, .5], sus=1, oct=P[3,4,5,6]+1)
d2 >> pluck([0,2], dur=1/3, sus=1, oct=P[3,4,5], amp=2)
b1 >> play("aeRF*=uhal", dur=1/3, rate=linvar([.2,2]), amp=.5)
k1 >> play("X.*.", amp=2)

print(SynthDefs)
