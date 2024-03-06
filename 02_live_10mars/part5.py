




bpm_to(160, 24)

change_bpm(160)

bb.fadeout()

d_all.fadeout()

l_all.fadeout()


k2 >> play("v..vb.v.", dur=.25, amp=2, lpf=600, hpf=60, output=12).fadeout()

hh >> play("-.-....-", dur=.25, rate=1, amp=4, sample=3)

c5 >> play(".cc.cc.c", amp=3.5, dur=.25, rate=2.5, room2=1).fadein(26)

k3 >> play("X..X..X.", dur=.25, amp=2, lpf=1000)

hh.amp=6
hh.rate=linvar([2,4],PRand(4,16, seed=2), start=Clock.mod(4))
hh.pan=linvar([-.8,.8], PRand(4,16))
c5.rate=linvar([4,7],PRand(4,16, seed=2), start=Clock.mod(4))

k2.sample=0

h2 >> play("..-.", amp=5.5, rate=(.8,1.2), sample=4, dur=.5)

c4 >> play(".c..", amp=3, dur=1/3, rate=2.5, room2=1)
c4.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=5)[:12], start=Clock.mod(4))

hh.rate=1
c3 >> play("c..", amp=2.5, dur=1/3, rate=3, room2=1)
c3.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=4)[:12], start=Clock.mod(4))

c_all.fadeout(16)

l2 >> lone1(
    chords2,
    dur=.5,
    sus=linvar([.3, 3], 16),
    oct=(4,5),
    amp=1,
    cutoff=.4,
    vol=1.6,
    # room2=1,
    pan=[-1, 0, 1],
).fadein(16, fvol=1.4)
l2.voices = linvar([0,1],32)

k2 >> play("V..V..V.", dur=.25, amp=2, lpf=900, output=12)
k3.stop()

# l2 >> vibra1(
#     chords,
#     dur=cascara*4/3,
#     sus=linvar([.3, 3], 16),
#     oct=(4,5),
#     amp=1,
#     cutoff=.4,
#     vol=1.3,
#     # room2=1,
#     pan=[-1, 0, 1],
# )

k2 >> play("<V.><X.>", dur=2/3, amp=2, lpf=900, output=12)
c5 >> play(".c.c.c.cc", amp=1.7, dur=1/3, rate=4, room2=1)
c5.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=3)[:12], start=Clock.mod(4))

c1 >> play("c.c.c.cc.", amp=4.5, dur=1/3, rate=6, room2=1)
c1.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=2)[:12], start=Clock.mod(4))

s2 >> blip(
    [0],
    dur=P[.5, .5, 1]*2/3,
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 2,
    pan=[-1,0,1,0],
    oct=P[5, 7, 6, 7]-P[0,1,0],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
s2.fadein(16, fvol=2)

s2.dur=.5

hh.fadeout(8)

Scale.default = Scale.chinese

s2.degree=chords

k2 >> play("V.", lpf=800, dur=.5, output=12, amp=1.4)

b2 >> bass303(
    chords,
    # dur=PDur(3, 8),
    dur=2*2/3,
    sus=bb.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    # cutoff=0,
    cutoff=linvar([0, 1], 32),
    reso=linvar([0, 1], 24),
    decay=linvar([0, 1], 48),
)
b2.fadein(fvol=.95)
bb >> pluckbass(
    chords,
    # dur=PDur(3, 8),
    dur=2*2/3,
    sus=bb.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
)
bb.fade(fvol=1)

k1.sample=2

c5.fadeout(24)
c3.fadeout(24)

c_all.fadeout()

bb.dur = var(P[2,.5,1/3,.25]*4/3, 8, start=Clock.mod(4))
b2.dur = var(P[2,.5,1/3,.25]*4/3, 8, start=Clock.mod(4))

Scale.default = Scale.minor

k2 >> play("V.", lpf=800, output=12, amp=1.4)
c2 >> play(".*.*.*.**", amp=2.5, dur=1/3, rate=2, room2=1).fadein()
c2.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=3)[:12], start=Clock.mod(4))

s2.degree=[0,2,0,5]+chords
l1.degree=[2,0,0,4]+chords

l1.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
s2.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)

k2 >> play("V..V..V.", dur=.25, amp=2, lpf=900, output=12)
bb.dur = var(P[2,.5,1/3,.25], 8, start=Clock.mod(4))
b2.dur = var(P[2,.5,1/3,.25], 8, start=Clock.mod(4))

l1.dur=cascara
c_all.dur=.25
s2.dur=[.5,.25,.25]

Root.default = var(PTri(12),.5)

bpm_to(260, 24)

Root.default = 0
bpm_to(30, 16)
