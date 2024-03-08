
pad1 = Player()
pad2 = Player()
kick1 = Player()
kick2 = Player()
kick3 = Player()
kick4 = Player()
plucked = Player()
blipmelo = Player()
percu1 = Player()
percu2 = Player()

kicks = Group(kick1, kick2, kick3, kick4)
percus = Group(kick1, kick2, kick3, kick4, hh, percu1, percu2)

change_bpm(130)
Root.default = 0
pitches = [0, 2, 5, 2, 0, -2, 5, 4]
mx >> mixer([None], vdee_mix=0)
dl >> duckless(dot8_mix=linvar([0,.5], [16, inf], start=Clock.mod(4)))

pad1 >> apad(
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
pad1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
pad1.degree = P[0,4,-2] + P(0,4)
pad1.span(srot(32), .7)
mx.deda_drywet = linvar([0, .4], [16,inf], start=Clock.mod(4))
kicks.fadeout(15)
Scale.default = Scale.major

kick1 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12, amp=1.2)
kick1.fadein(16)

pad1.degree = P[0,4,-2] + P(0,4,5)
mx.ru_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))

plucked >> pstrings(
    # [0, 5, 4, 0, 4, 3],
    [0],
    # dur=1,
    dur=[2, 1, 2, 3],
    oct=4,
    amp=P[.3, .7, .8, 1.1],
    # cutoff=.5,
    cutoff=linvar([.4,.6],32),
    timbre=linvar([.3,.6],64),
    verb=linvar([.1,.3],64),
)
plucked.span(srot(64),.4)
plucked.fadein(16, fvol=1)
mx.deda_drywet = linvar([.4, 0], [64,inf], start=Clock.mod(4))
pad1.space = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
plucked.degree = [0, 5, 4, 0, 4, 3]
kick1.degree = "(V...).(...x)(...(.X))"

pad2 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3)
pad2.fadein(16, fvol=1)
pad2.span(srot(32), .4)
pad2.dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Pvar([Scale.minor, Scale.major], 32, start=Clock.mod(4))

percu1 >> play("..(*.)(...*)", dur=.25, rate=var([3,4]), amp=2, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])
percu1.fadein(24)
percu1.mpan(mrot(7))
pad2.body = linvar([0, 1, .4, .8, 0, .6],PRand(2,24, seed=0), start=Clock.mod(4))

pad1.fade(16, fvol=.8)
kick1.degree = "(V).(...x)(...(.X))"

pad2.fade(32, fvol=.6)

Scale.default = Scale.majorPentatonic
kick1.pause(8,64)

Scale.default = Scale.minor
percu1 >> play("..(c.)(.*)", dur=.25, rate=var([3,4]), amp=2.3, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])

# Attendre la pause
kick1.sample=var([0,1,2,3], 64)
dl >> duckless(dot8_mix=var([0,.5],64))
pad2.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24, seed=2), start=Clock.mod(4))

mx.vdee_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))
pad2.oct = 4
pad2.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
percu2 >> play(
    ".(.**.)(.*..)(...(.O))",
    dur=.25,
    lpf=8000,
    hpf=1000,
    amp=2,
    rate=2,
    pan=var([-.5,0,.7,0],PRand(1,4)/4)
)
percu2.mpan(mrot(13))
percu2.sample = (3,4)
pad2.stop()

percu1.fadeout(24)
pad2.fade(32, fvol=.5)
pad1.fade(24, fvol=.3)

# cut delay
mx.vdee_mix = 0

plucked.dur = .5
plucked.sus = .45
# plucked.level=.5
plucked + P(0,5)
plucked.amp = [0,1,0,0,1,0]
percu2.fade(12, fvol=.1)

plucked.degree = var([0,5,2,3],[8,4,2,2], start=Clock.mod(4)) + (0,5)
# pitches = var([0, 2, 5, 2, 0, -2, 5, 4],[1,1,2,.5,.5,.5,.5,.5])
# plucked.degree = pitches

percu2.fadeout()
Scale.default = Scale.minor
plucked.level=.5
plucked.dur=.5
kick1.fadeout(16)
pad2.fade(16,fvol=1)
pad2.oct=2
plucked + (0,2)
plucked + [(0,2), 0, 5, 2]
plucked.dur = [.5,.25,.25]

mx.vdee_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))
plucked.amp = [0,1,0,0,1,1]

hh >> play("..-.", sdb=1, amp=2, rate=1.2, dur=.25, sample=6, pan=linvar([-.5,.5],16))
hh.mpan(mrot(5))

plucked.amp = [1,1,0,0,1,1]

plucked.amp = [1,1,1,0,1,1]

percu2 >> play(".(.**.)(**.-)(..(O.)(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)
percu2.mpan(mrot(23))
percu2.fadein(16)

kick2 >> play(
    degree="V...",
    pdb=2,
    output=12,
    sample=8,
    room2=.1,
    lpf=200,
    amp=1.5,
)
kick2.fadein(16, fvol=1)

hh >> play("..(---(b--(ib)))(.-)", sdb=1, amp=2, rate=1.2, dur=.25, sample=6)

plucked.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))
mx.deda_drywet = linvar([0, .3], [32,inf], start=Clock.mod(4))
plucked.fade(16, fvol=.9)

percu2.sample = 2
hh.sample = 2
kick2.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))
kick2.degree = "<V.x.>"
mx.vdee_mix = linvar([.2,0], [16,inf], start=Clock.mod(4))
kick2.amp=2

Scale.default = Scale.chinese
kick2.degree = "<V.x.><o.[(...X)X]>"

kick2.degree = "<V.x.><o(..[XV])[(...X)X]>"

kick2.sample = 0

k1.lpf = 800
Root.default = var(PTri(12), 2)
plucked.cutoff=linvar([1,.4],32, start=Clock.mod(4))

Scale.default = Scale.minor
mx.deda_drywet = linvar([.3, 0], [16,inf], start=Clock.mod(4))

mx.deda_on = 0
pad2.pitch = 0
pad2.arp = 0

pitches = [0, 2, 5, 2, 0, -2, 5, 4]
plucked.degree = pitches

plucked.vol=1.3
plucked + [(0,2), 0, 5, 2]
Root.default = 0

mx.sm_mix = linvar([0, .1], 16, start=Clock.mod(4))

kick2.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))
# kick2.pause(8,32)

blipmelo >> blip(
    [0,3,2],
    dur=P[.5, .25, .25],
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 1,
    pan=[-1,0,1,0],
    oct=[5, 7, 6, 7],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
blipmelo.mpan(mrot(16))
blipmelo.fadein(16, fvol=1.2)

plucked.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]
plucked.vol=1

# un peu de noise
mx.ru_blend=linvar([0,.3], [32,64,inf], start=Clock.mod(4))

Scale.default = Scale.minorPentatonic

plucked.fade(16, fvol=.8)
plucked.pause(8,24)
blipmelo.fade(fvol=1.4)
kick2.fade(ivol=1, fvol=1.4)
blipmelo.oct = Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
blipmelo.amp = P[.8, .7, .5, 1.1, .9] * 2
mx.vdee_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))

blipmelo.dur = var([.25, .5, 1/3], [10,4,2])
mx.ru_on = 0

kick2.degree = "<V.x.>"
