
change_bpm(130)
Root.default = 0
# tt >> fxstack(ru_on=False, ens_on=False, vdee_on=False, sm_on=False, deda_on=False)

Scale.default = Scale.chromatic
pitches = [0, 2, 5, 2, 0, -2, 5, 4]

z1 >> bino1([None]).span(srot(48), linvar([.1,.2,0,.5,0.1], 32, start=Clock.mod(4)))
z2 >> bino2([None]).span(srot(32), linvar([.1,1,0,.5,0,.7,0], 24, start=Clock.mod(4)))
z3 >> bino3([None]).span(srot(64), linvar([.1,.3,0,.5,0,.4], 48, start=Clock.mod(4)))
z4 >> bino4([None]).span(srot(40), linvar([.1,.2,0,.5,0], 16, start=Clock.mod(4)))

mx >> mixer([None], vdee_mix=0, vdee2_mix=0)
dl >> duckless([None], dot8_mix=.5)

a1 >> apad(
    P[0, 4, -2],
    dur=P[5,3,8]*2,
    attack=.8,
    space=0,
    detail=0,
    thick_thin=0,
    oct=4,
    vol=1,
    amplify=1,
)
a1.fadein(16, fvol=1)
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
# o3 >> bino3(
#     [None],
#     setup_id=.32,
#     azimuth_slider=linvar([.3,.7],48),
#     elevation_slider=linvar([.2,.8],77),
# )

a1.only()

z3 >> bino3([None]).span(srot(16), .2)

a1.degree = P[0,4,-2] + P(0,4)

mx.deda_drywet = linvar([0, .4], [16,inf], start=Clock.mod(4))
mx.deda2_drywet = linvar([0, .4], [16,inf], start=Clock.mod(4))

Scale.default = Scale.major

k2 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12, amp=1.2)
k2.fadein(16)

# delay
a1.degree = P[0,4,-2] + P(0,4,5)

mx.ru_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))
mx.ru2_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))

s1 >> pstrings(
    # [0, 5, 4, 0, 4, 3],
    [0],
    # dur=1,
    dur=[2, 1, 2, 3],
    sus=P[2, 1, 2, 3]-.1,
    oct=4,
    amp=P[.3, .7, .8, 1.1],
    # cutoff=.5,
    cutoff=linvar([.4,.6],32),
    timbre=linvar([.3,.6],64),
    verb=linvar([.1,.3],64),
)
s1.fadein(16, fvol=1)
mx.deda_drywet = linvar([.4, 0], [64,inf], start=Clock.mod(4))
mx.deda2_drywet = linvar([.4, 0], [64,inf], start=Clock.mod(4))

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

s1.degree = [0, 5, 4, 3]

mx.deda_on = 0
s1.degree = [0, 5, 4, 0, 4, 3]
k2.degree = "(V...).(...x)(...(.X))"

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3)
a4.fadein(16, fvol=1)
a4.dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Pvar([Scale.minor, Scale.major], 32, start=Clock.mod(4))
# o1 >> bino1(
#     [None],
#     setup_id=.32,
#     azimuth_slider=linvar([.3,.7],128),
#     elevation_slider=linvar([.2,.8],77),
# )

s1.amplify = PRand([1,1,0], seed=2)[:16]

cc >> play("..(..)(.*)", dur=.25, rate=var([3,4]), amp=2, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])
cc.fadein(24)

a4.body = linvar([0, 1, .4, .8, 0, .6],PRand(2,24, seed=0), start=Clock.mod(4))

s1.amplify = 1
s1.degree = 2

a1.fade(16, fvol=.8)
k2.degree = "(V).(...x)(...(.X))"
Scale.default = Scale.majorPentatonic

k2.pause(8,64)

Scale.default = Scale.minor
cc >> play("..(c.)(.*)", dur=.25, rate=var([3,4]), amp=2.3, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])

# Attendre la pause
k2.sample=var([0,1,2,3], 64)
dl >> duckless(dot8_mix=var([0,.5],64))

a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24, seed=2), start=Clock.mod(4))

mx.vdee_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))
mx.vdee2_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))
a4.oct = 4

a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

cp >> play(".(.**.)(.*..)(...(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2, pan=var([-.5,0,.7,0],PRand(1,4)/4))

cc.fadeout(24)

a4.fade(32, fvol=.5)

a1.fade(24, fvol=.3)

g1 >> blip(var([4,2,5], [2,4,1]), dur=[.25,.25,.5], oct=7, sus=2, amp=1, room2=1)
g1 + [0,2,6,5]

g1.fadeout(16)

# cut delay
mx.vdee_mix = 0
mx.vdee2_mix = 0

s1.dur = .5
s1.sus = .45
# s1.level=.5
s1 + P(0,5)
s1.amp = [0,1,0,0,1,0]

# pitches = var([0, 2, 5, 2, 0, -2, 5, 4],[1,1,2,.5,.5,.5,.5,.5])
# s1.degree = pitches
Scale.default = Scale.minor
s1.degree = var([0,5,2,3],[8,4,2,2])
s1.level=.5
s1.dur=.5
k2.fadeout(16)
a4.fade(16,fvol=1)
a4.oct=2
s1 + (0,2)

s1.amp = [0,1,0,0,1,1]

hh >> play("..-.", sdb=1, amp=2, rate=1.2, dur=.25, sample=6, pan=linvar([-.5,.5],16))

s1.amp = [0,1,1,0,1,1]


s1.amp = [1,1,1,0,1,1]

s1 + [(0,2), 0, 5, 2]
s1.dur = [.5,.25,.25]

cp >> play(".(.**.)(**.-)(..(O.)(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)
cp.fadein(16)

hh.degree =

k3 >> play(
    degree="V...",
    pdb=2,
    output=12,
    sample=8,
    room2=.1,
    lpf=200,
    amp=1.5,
)
k3.fadein(16, fvol=1)


hh >> play("..(---(b--(ib)))(.-)", sdb=1, amp=2, rate=1.2, dur=.25, sample=6)

hh.mpan(mrot(8))

s1.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))

mx.deda_drywet = linvar([0, .3], [16,inf], start=Clock.mod(4))
mx.deda2_drywet = linvar([0, .3], [16,inf], start=Clock.mod(4))

s1.fade(16, fvol=.7)

cp.sample = 2
hh.sample = 2

k3.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))
k3.degree = "<V.x.>"

k3.degree = "<V.x.><o.[(...X)X]>"

k3.degree = "<V.x.><o(..[XV])[(...X)X]>"

k1.lpf = 800

s1.fade(32, fvol=1)

s1.oct=(5,6)
s1.cutoff=linvar([1,.4],32, start=Clock.mod(4))

mx.deda_drywet = linvar([.3, 0], [16,inf], start=Clock.mod(4))
mx.deda2_drywet = linvar([.3, 0], [16,inf], start=Clock.mod(4))

mx.deda_on=0
mx.deda2_on=0

a4.pitch = 0
a4.arp = 0

pitches = [0, 2, 5, 2, 0, -2, 5, 4]
s1.degree = pitches

s1 + [(0,2), 0, 5, 2]

k3.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))
# k3.pause(8,32)

s2 >> blip(
    [0],
    dur=P[.5, .25, .25],
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 1,
    pan=[-1,0,1,0],
    oct=[5, 7, 6, 7],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
s2.fadein(16, fvol=1.2)

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]
s1.amp=1

# un peu de noise
mx.ru_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))
mx.ru2_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))

Scale.default = Scale.minorPentatonic

s1.fade(16, fvol=.8)

s1.pause(8,24)

s2.fade(fvol=1.4)
k1.fade(ivol=1, fvol=1.4)
s2.oct = Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
s2.amp = P[.8, .7, .5, 1.1, .9] * 2

s2.dur = var([.25, .5, 1/3], [10,4,2])

k3.degree = "<V.x.>"

Scale.default = Scale.major

# s2.fade(16, fvol=1)
s2.degree = pitches

k3.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))

Root.default = var(PTri(12), 8, start=Clock.mod(4))
s2.oct=(4,5)

Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
k3 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12)

k3.degree = "(V).(...x)(...(.X))"

k3.pause(8,64)

Root.default = 0

# s2.sfadeout(32)

hh.fadeout()
s1.fadeout(64)
s2.fadeout(64)

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(16, fvol=1)
# a4.span(srot(64), .4)
a4.oct = 3

a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

s3 >> space(
    pitches + [0,2,0,1],
    dur=[.5, .25, .25],
    amp=P[.8, .7, .8, 1.1] * 1.5,
    room2=.5,
    oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3]),
)
s3.pause(8,24,smooth=.3)

s2.fadeout(16)

s2 >> blip(
    [0,2],
    dur=P[.5, .25, .25],
    amp=P[.8, .7, .8, 1.1] * 2,
    pan=PWhite(-1,1)[:17],
    # oct=[5, 7, 6],
    fx=0,
    oct=[5, 7, 6, 7, 5, 6],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
s2.fadein(16)
s2.pause(8,24,8,smooth=.3)

s3.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

Scale.default = Scale.chinese

p2 >> padarp(
    [0, 2, 3, 2],
    dur=[1,.5],
    oct=3,
    amp=.8,
    verb=0,
    delay=0,
    # detune=sinvar([0,1], PWhite(.2,3)[:16], start=Clock.mod(4)),
    detune=0,
    expand=0,
    vol=1.2,
    filter_fx_switch=1,
    # filter_fx_cutoff=0,
    filter_fx_cutoff=linvar([.2,.9],[32,inf], start=Clock.mod(4))
)
p2.oct=[2,3,4,3]
p2.fadein(4, fvol=1.4)

p2.expand=linvar([0, 1], 24, start=Clock.mod(4))

p2.verb=linvar([0,1], [32], start=Clock.mod(4))

p2.delay=linvar([0,1], [64], start=Clock.mod(4))

# kick delay on

a4.fade(24, fvol=.5)
k4 >> play(
    "X{.xXx}(X.)",
    output=12,
    sample=0,
    pdb=0,
    dur=.5,
    lpf=4000,
    pan = [-.5,0.5],
    amp=2
    # dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8)),
)
k4.fadein(16)
k4.rate = PWhite(.8,1.6)
# k1.mpan(PWhite(0,3.9))
k3.fadeout(32)

k4.amplify=1
dl >> duckless(dot8_mix=0)

k4.dur=Pvar([.25, PDur(5, 8)], PRand(2, 8))

k4.dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8))
k4.pause(8,32)

s2.fadeout(64)

# attendre la pause

k4.crush = PWhite(0,8)
k4.bits = PWhite(3,8)

k4.fade(32, fvol=1)

a4.vol=1

Root.default = var(PTri(12), .25, start=Clock.mod(4))

Scale.default = Scale.minor

k3.curr_players()

k4.fadeout(32)

k3.fadeout()

s2.fadeout()
s3.fadeout()
p2.fadeout()

Root.default = 0

bpm_to(60, 32)

a4.fade(32,fvol=.6)

a4.only()
