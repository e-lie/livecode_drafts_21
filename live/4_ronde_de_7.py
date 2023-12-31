Root.default = 0

change_bpm(140)

s1 >> pstrings(
    [0],
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    # cutoff=linvar([.06,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
    cutoff=linvar([.2, .5], [15 * .25 * 15], start=Clock.mod(4)),
    level=.3,
) + P(0, 2)
s1.fadein(ivol=1, fvol=1.2)
Scale.default = Pvar([Scale.chinese, Scale.majorPentatonic], 14)
s1.only()


p1 >> dakeys(
    # chords+P[0, 2, 5, 2, -2, 1, 4],
    # P[0, 2, 5, 2, -2, 1, 4].rotate(3),
    P[-2, 1, 4, 0, 2, 5, 2],
    # [0, 2, 4, 2, -2, 4],
    dur=.5,
    oct=(3,5,7),
    # oct=6,
    amp=.8,
    pad=0,
    modelb=0,
    pluck=1,
    space=.4,
    # vol=1.5,
    # vol=1.0,
)
p1.fadein(32, fvol=.95)

p1.pad = linvar([0, .5], 24, start=Clock.mod(4))

k5 >> play(
    degree="V...",
    # degree = "<V.xV>",
    # degree = "<V.x.><..[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    # degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],[32,16], start=Clock.mod(4)),
    pdb=2,
    output=12,
    sample=PRand(0,3),
    # room2=3,
    room2=.1,
    lpf=8000,
    amp=1.2,
    # rate=PWhite(.8,1.8),
    # cut=linvar([.1,.9], 8),
    # cut=1,
)
# k5.mpan((PRand(0,1),PRand(2,3)))
k5.fadein(16)

s1.fade(fvol=1)

s1.dur = cascara

cp >> play(".(.**.)(**.-)(..(O.)(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)
cp.fadein(16)

p1.fadeout(8, ivol=.95, fvol=.85)

p1.vol=1.2

p1.modelb = linvar([0,1],32, start=Clock.mod(4))

p1.pluck = linvar([1,0],24, start=Clock.mod(4))

p1.space = linvar([0,1],32, start=Clock.mod(4))

s1.fade(64, fvol=.8)

a3 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,p.9],
    dur=.5,
    oct=3,
    amp=1,
    vol=1,
    # expand=0,
    expand=linvar([0,1], [32,inf], start=Clock.mod(4)),
    verb=0,
    # verb=linvar([0,1], [32,inf], start=Clock.mod(4)),
    detune=1,
    delay=0,
    filter_fx_switch=0,
    # filter_fx_cutoff=linvar([.2,.5]),
)
# a2.fadein(fvol=1.2)
# a2.span(linvar([0,3.99], [2,48,8]), linvar([0,1.5], 32))

a3.dur = clave23

Scale.default = Scale.majorPentatonic

a3.expand=linvar([1,0], [16,inf], start=Clock.mod(4))
a3.verb=linvar([1,0], [16,inf], start=Clock.mod(4))

# p1.span(srot(7),linvar([.3,1], 24, start=Clock.mod(4)))

a3.oct=Pvar(P[(4,5), 3, (3,4,5)]+2, P[2,4,3,3]+2)

a3.detune = 0

a3.delay=linvar([0,.6,0], [64,16,inf], start=Clock.mod(4))

k5.degree = "<V.xV><.(..[XV])[(...X)X]>"
k5.amp=1

Scale.default = Pvar([Scale.majorPentatonic, Scale.major, Scale.minor, Scale.major], 14, start=Clock.mod(4))

a2.verb = 0
a2.expand = 0
a2.oct = (3,6)

Root.default = var(PTri(12), 14, start=Clock.mod(14))
# Scale.default = Scale.minor
p1.fadein(64, ivol=1, fvol=1.3)

Root.default = var(PTri(12), 1)

Root.default = var(PTri(12), 4)

e3 >> play(
    "iii[**]",
    dur=.5,
    # sample=P[0, 1, 2].stutter(4),
    sample=1,
    rate=PWhite(1.2, 1.5),
    amp=1.3,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
# e3.mpan(PWhite(0,3.9)[:17].stutter(3))
e3.pause(4, 16, 12)

Root.default = var(PTri(12), .25)

e3 >> play(
    # "iii[ii]",
    "<(aqscxsqkscdjs)(esdfqio)(sofjldfm)[(qqsdfqds)(sqsefq)]><*..[**]>",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 3.5),
    amp=1.5,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4),
    lpf=3000,
    hpf=2000,
)
e3.faderand(16)
# e3.mpan(PWhite(0,3.9)[:17].stutter(3))
e3.pause(4, 16, 12)

l_all.stop()

cp.fadeout(24)

e3.fadeout(64)

Root.default = 0

s1 >> pstrings(
    [0],
    # mmelody,
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    # cutoff=.06,
    cutoff=linvar([.1,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
) + P(0, 2)
s1.fadein(32, ivol=.8, fvol=1.5)

a2.fadeout()
Scale.default = Scale.minor
Root.default = 0

k5.degree = "<V.><v.><X.>"

p1.oct = (6,7)

mx.ru_blend=linvar([0,.8], [32,64,inf], start=Clock.mod(4))

bpm_to(260, 32)

bpm_to(60, 16)

change_bpm(120)
