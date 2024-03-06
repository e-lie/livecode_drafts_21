
Scale.default = Scale.major

Root.default = 0
chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])
Clock.meter = (4,4)
Root.default = 0

bpm_to(140, 16)

change_bpm(140)

bb.curr_players()

a1.fadeout()

# Wait for the right moment
hh.fadeout()

cp.fadeout(32)

Scale.default = Scale.minor
bb >> pluckbass(
    [0],
    dur=PDur(3, 8),
    oct=(3,4),
    amp=2.5,
    room2=1,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
    vol=1,
)#.pause(8, 32)
d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=2.5)

s1.fadeout(32)

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
l1.degree = chords + P(0,2)
bb.degree = chords

k3.degree = "V...vV.."
s2.fadeout(32)

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

l2.dur = var([1,.5,.25],[20,8,4])
l2.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.pause(4, 16, 8)

l2.degree = chords + P[0, 2, 0, P(0, 2)]
l2.dur=var([1,.5])

k3.degree = "V.v.VVv."

e3 >> play(
    "b",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 1.5),
    amp=1,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
e3.mpan(mrot(6))
e3.pause(4, 16, 12)

l2.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.amp=3

e3.degree = "<*><b.>"
bb.degree = chords3
l1.degree = chords3 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
l2.degree = chords3+ P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
Scale.default = Scale.minorPentatonic

Root.default = 0

Root.default = var([0,1,2,3], [16,16,16,inf], start=Clock.mod(4))

Root.default = var(PTri(12), .5)

k3.degree = "V......."
k2.stop()

somegroup = Group(l1, l2, a1)
somegroup = Group(bb, l2, a1)
somegroup.only()

b2 >> bass303(
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
b2.fadein(fvol=.95)
bb >> pluckbass(
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
bb.fadein(fvol=.95)

Root.default = 0
l1.fade(24, fvol=.8)

bb.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))
b2.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))

k5 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amp=1.6,
    output=12
)

dl >> duckless(dot8_mix=linvar([0,.5], [16, inf], start=Clock.mod(4)))

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

dl >> duckless(dot8_on=0)
k6 >> kicker(
    "<(VVV(V[.V]V[VV]))(...V)>",
    # "<V...>",
    # "<V(x.)(.x).>",
    # "<V(x.)(.x)X>",
    dur=.5,
    amp=1.4,
    crush=8,
    bits=linvar([6, 2], [24,48], start=Clock.mod(4)),
    output=12,
)

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32, fvol=.8)
# a4.span(srot(32), .5)
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Scale.minorPentatonic

k_all.fadeout()

b2.fadeout()

l_all.fadeout(64)
