
change_bpm(160)

g1 >> gone1(dur=4, oct=(3,5)).fadein(32)

g1.degree =
notes=var([0,2,0,[2,5]], 8) + [0,1,0,2]
g1.dur=2

d1 >> play("c.{c[cc]}c.c.", rate=PRand([1,1.3,1.5,2]))#.fadein(16)

d1.fadeout(24)

hh >> play("(--.[--]){-[--]--.[---]}", dur=.5, rate=linvar([.2,2],7))
h2 >> play("..-.", dur=.5, rate=.8, amp=2)

k1 >> play("v.x{v..V}..", dur=.5, rate=linvar([.2,])).fadeout()

k2 >> play("{VVV..}{V}", output=12, lpf=500, amp=1.3, dur=1/3, rate=linvar([1,2]))

k2.degree =

h2.fadeout()

k2.degree = 'v...'
k2.dur=.5

Scale.default = Scale.majorPentatonic

Root.default = var(PTri(12), 4)*
Root.default = 0


b1 >> blip(notes, dur=Pvar([[.25,.25,.5],.25], 8), amp=PRand([1,1,1,.8,0]), oct=6, sus=linvar([.2,2], 16, start=Clock.mod(4)))
b2 >> blip(notes, dur=[.5,1], amp=PRand([1,1,1,.8,0])*2, oct=5, sus=linvar([.2,2], 16, start=Clock.mod(4)), )

b_all.fadeout(64)
b_all.oct=4
