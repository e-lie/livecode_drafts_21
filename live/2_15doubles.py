# C'est du 15/16 en profiter pour faire des basculements kick techno 4/5 ie 120/150 bpm ?? euh pas sur que ce soit 120/150
# essayer de faire de meilleures mélodies avec des var ici !!


Clock.clear()

Root.default = 0
Root.default = var(PTri(6)*2, 15*.25, start=Clock.mod(3.75))
Root.default = var(PTri(12), .25)
Root.default = var(PTri(6)*2, .75)

Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.lydian, Scale.aeolian], 15*.25)
Scale.default = Scale.minor
Scale.default = Scale.lydian
Scale.default = Scale.aeolian

mmelody = P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5]
srand_4 = sinvar(PWhite(0,4)[:17].stutter(2), [3.5,.5])

change_bpm(120)

Scale.default = Scale.majorPentatonic
Clock.meter = (15*.25,5)
Root.default = 0

m1.sfadeout()

a4.fade(16, fvol=.5)


mmelody = P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5]
m1 >> marimba(
    mmelody,
    amplify=1,
    oct=(4,7),
    amp=linvar([.75, .45], 15*.25, start=Clock.mod(4)),
    sus=.1,
    dur=.25,
)
m1.fadein(16, fvol=1.1)

m1.fade(8, fvol=1.2)

a1.fade(24,fvol=.3)

m1.degree = mmelody + P(0,2)

m1.oct=5

t1 >> equals([0,2], dur=[.25,.75], oct=[8], pan=[.8,0,.5,-.7,.1,-.8], vol=.8)
t1.fadein(8, fvol=.8)
t1.bass_pulse=.8
t1.detune=1
t1.filter_motion=0
t1.effects=1
t1.bass_pulse=linvar([0,.8],16, start=Clock.mod(4))
t1.detune=linvar([1,.5,0],32, start=Clock.mod(4))
t1.filter_motion=var([0,.5],24, start=Clock.mod(4))
t1.effects=linvar([0,1],32, start=Clock.mod(4))

m1.degree = mmelody + P(0,-2)

Scale.default = Scale.majorPentatonic

m1.fade(fvol=1.5)
m1.oct=[4,5,6,5,4]

m1.fade(fvol=1.2)

m1.degree = mmelody + P(0,2)

t1.degree = [0,2,5]

k4 >> play("<v.><(X).....>", amp=1.3, output=12)
hh >> play("-..(-..[.-])", amp=2)

a1.fadeout(16)

m3 >> blip(
    P[12,2,4,2,-2].stutter(3),
    oct=P[7,3,5,4,3],
    amp=2,
    dur=.25,
    vol=1,
    lpf=9000,
    level=1,
    reso=1,
)

m3.sus=linvar([.2,2], [15*.25*5], start=Clock.mod(15*.25))
# m3.span(srot(64), .6)
m3.amp=1.5

Scale.default = Scale.minor

k4.pause(8,48)

t1.degree = [0,2,5,4]
t1.oct = [6,7]
t1.amp = 1.3
t1.vol = expvar([1.2,0], PRand([12,16,24,32]), start=Clock.mod(15*.25))

Scale.default = Scale.chinese

m3.degree = 12

m3.oct = P[4,3,5,4,3]+2
m3.oct=[7,4,5,7,7]

m3.degree = P[12,2,4,2,-2].stutter(3)

a1 >> apad(
    [0, 4, -2],
    dur=PRand(1,3)[:15]*2.5,
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
)
a1.fadein(15*.25*9, fvol=1.2)

m1.fade(16, ivol=1, fvol=1.5)

Root.default = 0

m1.amplify = linvar([1,1,0,0], [15*.25,5*.25,10*.25,0])

t1.stop()

k4.fadeout(24)

m3.fade(16,  fvol=1.4)

m3.fadeout(24)

k4 >> play(
    # "x(x.)",
    "x{.xx+}(x.)",
    dur=var([.25, .75],[15*0.25*2]),
    output=12,
    rate=PWhite(.6,2),
    amp=2,
    room2=3,
    pan=[-1, 1, 0, 1],
    crush=PWhite(2,16),
    bits=PRand(3,5),
)
k4.fadein()

k5 >> play("v.", output=12, amp=1.5)

b1 >> padarp(
    P[0] + P[0,0,2,-2,0],
    dur=[1.25, .5, .75, .5, .75],
    oct=(3,4),
    amp=1.5,
    expand=linvar([0,1], [32,inf], start=Clock.mod(4)),
    verb=0,
    detune=1,
    delay=0,
)
b1.fadein(15*.25*3, fvol=1.3)
k4.fadeout(32)

m1.fadeout(15*.25*2)
m3.fade(15*.25*2, fvol=.7)

a1.fadeout()

s1 >> pstrings(
    [0],
    # mmelody,
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    # sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    cutoff=linvar([.1,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
) + P(0, 2)
s1.fadein(16, fvol=1.3)
# s1.span(srot(24),.3)
Scale.default = Pvar([Scale.minor, Scale.major], 14)

s1.sampfadeout(48)

k4.fadeout(16)

bpm_to(140, 24)

b1.fadeout()

s1.solo()

s1.curr_players()
