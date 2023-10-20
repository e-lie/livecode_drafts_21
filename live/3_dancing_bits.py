Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 8, start=Clock.mod(4))
Root.default = var(PTri(12), 16, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

Root.default = 0
chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])
Clock.meter = (4,4)
Root.default = 0

Scale.default = Scale.chinese

d6 >> play("<x.*...*.>", dur=.5, sample=1, rate=(1.2,1.6), amp=2, room2=2)
d6.fadein()

change_bpm(140)

bb >> pluckbass(
    [0],
    # chords,
    # chords2,
    # chords3,
    dur=PDur(3, 8),
    # dur=cascara,
    oct=(3,4),
    amp=2.5,
    room2=1,
    # sus=1,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
    vol=1,
    # sus=linvar([.5,2], 32),
    # pan=var([-.5, 0, .5], 4)
)#.pause(8, 32)
# bb.mpan(3)
d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=2.5)
# d8.mpan(PRand(0,3))

k5 >> kicker(
    "V.......",
    dur=.5,
    # sample=var([0, 1, 2], 32),
    sample=2,
    # rate=linvar([.8, 1.2], 16),
    lpf=700,
    rate=1,
    amp=1,
    output=12
).fadein()
bb.pause(8,32)


l1 >> blip(
    chords + P(0,2),
    # chords3,
    dur=clave23,
    # dur=.25,
    # dur=PDur(5,8),
    # dur=Pvar([.5, .25, 1/3, PDur(5,8)], 8),
    sus=linvar([.4, 6], 16),
    oct=6,
    # room2=3,
    amp=1.2,
    # pan=[-1, 0, 0, 1, 1, 0],
    # pan=var([-1, 0, 1, 0])
).fadein()

Root.default = 0

l1.fade(fvol=1.4)

d6.solo()

change_bpm(140)

d6.solo(0)
l1.degree = chords + P(0,2)
bb.degree = chords

l1.pause(4, 16)

k5.degree = "V...vV.."
k5.amp=1.6
s1.fadeout(32, ivol=1.2)

l2 >> pluck(
    chords,
    dur=cascara,
    sus=linvar([.3, 3], 16),
    oct=(4,6),
    amp=1.5,
    cutoff=.4,
    vol=1.1,
    # room2=1,
    pan=[-1, 0, 1],
)
l2.pause(4, 16, 8)

l2.degree = chords + P[0, 2, 0, P(0, 2)]
l2.dur=var([1,.5])

k5.degree = "V.v.VVv."
d6.degree = "..(iii{[IIIIIIII]*})...(i[ii])."
d6.amp=2
d6.pan=[-1,0,1]

Scale.default = Scale.aeolian

e3 >> play(
    "*",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 1.5),
    amp=1,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
# e3.mpan(mrot(6))
e3.pause(4, 16, 12)

l2.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.amp=3

bb.degree = chords3
l1.degree = chords3 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.degree = chords3 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
Scale.default = Scale.minor

a1 >> apad(
    chords + P(0,12),
    dur=PRand(2, 8),
    sus=PRand(4, 12),
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
    vol=1.1,
)
a1.fadein(fvol=1.3)

Scale.default = Scale.chromatic

l2.stop() # wait for the pause

Root.default = var(PTri(6), .5)

Scale.default = Scale.minor
Root.default = var(PTri(8), 2)

Root.default = 0
k5.degree = "V......."

bb.fadeout()
e3.stop()

somegroup = Group(l1, l2, a1)
somegroup.only()

l2 >> pluck(
    chords,
    dur=cascara,
    sus=linvar([.3, 3], 16),
    oct=(4,6),
    amp=1.5,
    cutoff=.4,
    vol=1.1,
    # room2=1,
    pan=[-1, 0, 1],
)
l2.dur=var([1,.5,.25],[20,8,4])
l2.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.pause(4, 16, 8)


bb >> bass303(
    chords2,
    # dur=PDur(3, 8),
    dur=2,
    sus=bb.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    # cutoff=0,
    cutoff=linvar([0, 1], 32),
    reso=linvar([0, 1], 24),
    decay=linvar([0, 1], 48),
)
bb.fadein(fvol=.95)
b2 >> pluckbass(
    chords2,
    # dur=PDur(3, 8),
    dur=2,
    sus=bb.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
)
b2.fadein(fvol=.95)

l1.fade(24, fvol=.8)

bb.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))
b2.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))

a1.fade(24, fvol=.7)

k5 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amp=1.6,
    output=12
)

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32, fvol=.9)
# a4.span(srot(32), .5)
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
k5.pause(8,32)

l1 >> pluck(
    chords2 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2),
    dur=Pvar([.5, .25, 1/3, PDur(5,8)], 8),
    sus=linvar([.4, 1], 16),
    oct=6,
    room2=3,
    amp=1.5,
    # pan=[-1, 0, 0, 1, 1, 0],
    pan=var([-1, 0, 1, 0])
)
# l1.mpan(PRand(0,3)[:17].stutter(8))
l1.pause(4, 16)
a1.stop()


k6 >> kicker(
    "<(VVV(V[.V]V[VV]))(...V)>",
    # "<V...>",
    # "<V(x.)(.x).>",
    # "<V(x.)(.x)X>",
    dur=.5,
    amp=1.4,
    crush=8,
    bits=linvar([6, 2], 24, start=Clock.mod(4)),
    output=12,
)

Scale.default = Scale.minor
Root.default = var(PTri(6), [16]*6+[inf], start=Clock.mod(4))

# Root.default = var(PTri(12), .25, start=Clock.mod(4))
Root.default = var(PTri(12), 1, start=Clock.mod(4))

bb.fadeout(64)
b2.fadeout(64)

Root.default = 0
k5.ampfadeout()

bb.stop()
b2.stop()
s1.stop()

s1 >> pstrings(
    [0],
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    # cutoff=linvar([.06,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
    cutoff=linvar([.2, .5], [15 * .25 * 15], start=Clock.mod(15 * .25)),
) + P(0, 2)
# s1.span(srot(64),.4)
s1.fadein()

k6.fadeout(32)

l1.fade(32, fvol=.5)
l2.fade(32, fvol=.5)

n1 >> padarp(
    chords3 + P(0, 2),
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    # cutoff=linvar([.06,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
    cutoff=linvar([.2, .5], [15 * .25 * 15], start=Clock.mod(15 * .25)),
) + P(0, 2)
n1.pause(4, 16)
n1.fadein()

a4.fadeout(32)

n2 >> dakeys(
    chords3,
    dur=PDur(5, 8),
    sus=linvar([.3, 3], 16),
    oct=(4, 5),
    room2=1,
    pan=[-1, 0, 1]
)#.pause(4, 16, 8)

k4 >> play(
    ".VxV",
    lpf=500,
    sample=4,
    amp=1,
    sdb=1,
    dur=1 / 4,
    room2=10,
    output=12,
    cut=.9
).fadein(16)

e3 >> play(
    # "iii[ii]",
    "<(aqscxsqkscdjs)(esdfqio)(sofjldfm)[(qqsdfqds)(sqsefq)]><*..[**]>",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 3.5),
    amp=2,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
e3.fadein(16)
e3.pause(4, 16, 12)

k4.fade(16, fvol=1.2)

Scale.default = Scale.minor
k7 >> play('<X.><v.>', dur=1 / 2, sdb=1, sample=1, amp=5, output=12, lpf=800)
k4.ampfadeout(64, iamp=1.5, famp=.7)

k7.fade(32, fvol=1)

l1.stop()

l1 >> blip(
    chords3 + P(0,2),
    dur=clave23,
    sus=linvar([.4, 6], 16),
    oct=6,
    amp=1.6,
    pan=var([-1, 0, 1, 0])
)
# l1.mpan(mrot(128))
l1.pause(4, 16)

k4.fadeout()
Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
e3.rate = linvar([1,3],32)

e3.fade(fvol=.8)

n2.fadeout(32)

k7.fadeout(32)

l1.fadeout(16)
e3.fadeout(32)
cp.fadeout()

s1.only()
