from FoxDot.preset import *

k1 >> blip(oct=[4,6,7,5], dur=[.5,.25], atk=linvar([0,.1],19), room2=1, amp=[1.2,1.4,.8,.9,1]) + var([0,4, 0,2], [3.5,.5])
k1.fadein(16)

k1.faderand()

k2 >> bbass([0,2,0,5], oct=[5], dur=[.18,.25,.32,.25], atk=linvar([0,.2],17), room2=1, amp=[.9,.9,1.1]) + var([0,4], [3.5,.5])

k2.solo(0)

k2.faderand()

k2 >> bbass(oct=[5], dur=[.18,.25,.32,.25], atk=linvar([0,.2],17), room2=1, amp=[.9,.9,1.1]) + var([0,4], [3.5,.5])
k_all.oct = [3,4,7]

Scale.default = Pvar([Scale.minorPentatonic, Scale.chinese],16)

Scale.default = Scale.chromatic

bpm_to(160, 16)

d1 >> play("{bbbb.}", rate=[1,2,1,1.2]).fadeout()
d2 >> play("<[--]><{.i}.c>", rate=[1,2,1,1.2])
k3 >> play("x{oi..[**]}", lpf=800, amp=2)

b8 >> blip([0], oct=[5,6,7], dur=.25, amp=2).fadeout()


h1 >> borgan([0,2], atk=.2, oct=3, room2=.2, lpf=linvar([400,1000],16), lpq=linvar([10,100],24), pan=linvar([-1,1]), sustain=2)
h2 >> borgan([0,2,0,4], atk=.2, oct=4, dur=.5, room2=.2, lpf=linvar([600,2000],16), lpq=linvar([10,100],24), pan=linvar([-1,1]), sustain=2)
h1.faderand()
h2.faderand()

j1 >> play("{VvX.VvX}", lpf=[100,800,200,2000])

k1 >> chipsy(oct=[4,6,7,5], dur=[.5,.25], atk=linvar([0,.1],19), room2=1, amp=[1.2,1.4,.8,.9,1]) + var([0,4, 0,2], [3.5,.5])
k2 >> chipsy(oct=[5], dur=[.18,.25,.32,.25], atk=linvar([0,.2],17), room2=1, amp=[.9,.9,1.1]) + var([0,4], [3.5,.5])

c1 >> cluster(oct=[4], pstep=linvar([0,10]))

c1 >> donk([0,4,0,5], dur=var([.5,.25], [3.5,.5]), lpf=linvar([300,2000], 12), oct=6) + [0,1,0,2,0,1,2]

c1 >> click(oct=(5.5,5.9,6), lpf=1000, dur=[.25,.25,.5], amp=PWhite(.7,1.3)) + [0,1,0,2,0,1,2]
c2 >> click(oct=(3.5,3.9,4), lpf=1000, dur=[.25,.5], amp=PWhite(.7,1.3)) + [0,1,0,2,0,1,2]

hh >> play("-[--]", sdb=2, sample=PTri(0,8), dur=.5, rate=(1,2), amp=2)

hh >> play(".-", sdb=2, sample=3, dur=.5, rate=1.5, amp=3)

hh >> play(".{-----[--]}", sdb=2, sample=5, dur=.5, rate=1.5, amp=3)
cp >> play(".{..*}", sdb=2, sample=5, dur=.5, rate=2.5, amp=2)
d1 >> play("v", sdb=2, sample=PTri(0,8), dur=[.5,.25,.25], rate=(1,2), amp=2, lpf=linvar([300,800],7))
d2 >> play("X", sdb=2, sample=PTri(0,8), dur=[1,.5,.5], rate=(1,2), amp=2, lpf=linvar([300,800]))

k1 >> play("{[-.-][---][-..]}", rate=linvar([.3,3],32), amp=linvar([0,2],32))

#  Music livecoding with FoxDot Python Library

b1 >> bellmod(degree=[0,2,1,0,5], oct=6, dur=[.25,1/2,.5,.25,.25], sus=linvar([.1,1],18)) + (0,2)
b2 >> blip(degree=[0,2,1,0,5], oct=7, dur=[.25,1/2,.5,.25], sus=linvar([.1,1],16)) + (0,2)
d1 >> play("<c-c--c><v.>", amp=6, rate=2)

Scale.default = Pvar([Scale.minor, Scale.major], 16)
