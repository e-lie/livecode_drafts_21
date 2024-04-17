pbass = Player()
acidbass = Player()
crash = Player()
kick1 = Player()
kick2 = Player()
kick3 = Player()
kick4 = Player()
blipmelo = Player()
pluckmelo = Player()
bipclap = Player()
kicks = Group(kick1, kick2, kick3, kick4)
percus = Group(kick1, kick2, kick3, kick4, bipclap, crash)
melos = Group(blipmelo, pluckmelo)

Scale.default = Scale.major
Root.default = 0
chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])

bpm_to(140, 24)

change_bpm(140)

cp.fadeout(32)

Scale.default = Scale.minor

pbass >> pluckbass(
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
pbass.span(srot(64), .2)
crash >> play("/", dur=16, pan=[-1, 0, -1], amp=2.5)
dl >> duckless(dot8_mix=0)

cuttt = Group(pbass, crash)
cuttt.only()

kick2 >> kicker(
    "V.......",
    dur=.5,
    # sample=var([0, 1, 2], 32),
    sample=2,
    # rate=linvar([.8, 1.2], 16),
    lpf=700,
    rate=1,
    amp=1.2,
    output=12
)

blipmelo >> blip(
    chords + P(0,2),
    dur=clave23,
    sus=linvar([.4, 6], 16),
    oct=6,
    amp=1.2,
).fadein()
blipmelo.mpan(mrot(.5))
blipmelo.degree = chords + P(0,2)
pbass.degree = chords

kick2.degree = "V...vV.."

pluckmelo >> pluck(
    chords,
    dur=cascara,
    sus=linvar([.3, 3], 16),
    oct=(4,6),
    amp=1.5,
    cutoff=.4,
    vol=1.1,
    # pan=[-1, 0, 1],
)
pluckmelo.mpan(mrot(1))

pluckmelo.dur = var([1,.5,.25],[20,8,4])
pluckmelo.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
pluckmelo.pause(4, 16, 8)

pluckmelo.degree = chords + P[0, 2, 0, P(0, 2)]
pluckmelo.dur=var([1,.5])

kick1.degree = "V.v.VVv."

bipclap >> play(
    "b",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 1.5),
    amp=1,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
bipclap.mpan(mrot(6))
bipclap.pause(4, 16, 12)
crash.fadeout(32)

pluckmelo.degree = chords + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
pluckmelo.amp=3

bipclap.degree = "<*><b.>"

pbass.degree = chords3
blipmelo.degree = chords3 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
pluckmelo.degree = chords3+ P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
Scale.default = Scale.minorPentatonic

Root.default = 0

Root.default = var([0,1,2,3], [16,16,16,inf], start=Clock.mod(4))

Root.default = var(PTri(12), .5)

kick2.degree = "V......."

somegroup = Group(blipmelo, pluckmelo, pad1)
somegroup = Group(pbass, pluckmelo, pad1)
somegroup.only()

acidbass >> bass303(
    chords2,
    dur=2,
    sus=pbass.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    cutoff=linvar([0, 1], 32),
    reso=linvar([0, 1], 24),
    decay=linvar([0, 1], 48),
)
acidbass.fadein(fvol=.95)
acidbass.span(srot(32), .2)
pbass >> pluckbass(
    chords2,
    # dur=PDur(3, 8),
    dur=2,
    sus=pbass.dur - .1,
    oct=4,
    amp=2,
    room2=0,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
)
pbass.fadein(fvol=.95)

Root.default = 0
blipmelo.fade(24, fvol=.8)

pbass.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))
acidbass.dur = var([2,.5,1/3,.25], 8, start=Clock.mod(4))

kick1 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amp=1.6,
    output=12
)

dl >> duckless(dot8_mix=linvar([0,.5], [16, inf], start=Clock.mod(4)))

kick1.pause(8,32)

blipmelo >> pluck(
    chords2 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2),
    dur=Pvar([.5, .25, 1/3, PDur(5,8)], 8),
    sus=linvar([.4, 1], 16),
    oct=6,
    room2=3,
    amp=1.5,
    # pan=[-1, 0, 0, 1, 1, 0],
    pan=var([-1, 0, 1, 0])
)
# blipmelo.mpan(PRand(0,3)[:17].stutter(8))
blipmelo.pause(4, 16)
pad1.stop()

dl >> duckless(dot8_on=0)
kick3 >> kicker(
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

pad2 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
pad2.fadein(32, fvol=.8)
pad2.span(srot(32), .5)
pad2.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Scale.minorPentatonic

kicks.fadeout()

acidbass.fadeout()

melos.fadeout(64)
