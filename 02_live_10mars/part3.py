

change_bpm(130)
Root.default = 0
# tt >> fxstack(ru_on=False, ens_on=False, vdee_on=False, sm_on=False, deda_on=False)
pitches = [0, 2, 5, 2, 0, -2, 5, 4]
mx >> mixer([None], vdee_mix=0)
dl >> duckless(dot8_mix=linvar([0,.5], [16, inf], start=Clock.mod(4)))

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
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.degree = P[0,4,-2] + P(0,4)
mx.deda_drywet = linvar([0, .4], [16,inf], start=Clock.mod(4))
k_all.fadeout(15)
Scale.default = Scale.major

d3.fadeout(24)

m_all.fadeout()

d_all.fadeout(15)

k2 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12, amp=2)
k2.fadein(16)


# delay
a1.degree = P[0,4,-2] + P(0,4,5)
mx.ru_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))

s1 >> pstrings(
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
s1.fadein(16, fvol=1)
mx.deda_drywet = linvar([.4, 0], [64,inf], start=Clock.mod(4))
a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
s1.degree = [0, 5, 4, 0, 4, 3]
k2.degree = "(V...).(...x)(...(.X))"

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3)
a4.fadein(16, fvol=1)
a4.dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Pvar([Scale.minor, Scale.major], 32, start=Clock.mod(4))

cc >> play("..(*.)(...*)", dur=.25, rate=var([3,4]), amp=2, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])
cc.fadein(24)
a4.body = linvar([0, 1, .4, .8, 0, .6],PRand(2,24, seed=0), start=Clock.mod(4))

a1.fade(16, fvol=.8)
k2.degree = "(V).(...x)(...(.X))"

a4.fade(fvol=.5)

ff.fadeout()

Scale.default = Scale.majorPentatonic
k2.pause(8,64)

Scale.default = Scale.minor
cc >> play("..(c.)(.*)", dur=.25, rate=var([3,4]), amp=2.3, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])

# Attendre la pause
k2.sample=var([0,1,2,3], 64)
dl >> duckless(dot8_mix=var([0,.5],64))
a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24, seed=2), start=Clock.mod(4))

mx.vdee_mix = linvar([0,.2], [16,inf], start=Clock.mod(4))
a4.oct = 4
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
cp >> play(".(.**.)(.*..)(...(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2, pan=var([-.5,0,.7,0],PRand(1,4)/4))
cp.sample = (3,4)
cp.sdb=0
a4.stop()

cc.fadeout(24)
a4.fade(32, fvol=.5)
a1.fade(24, fvol=.3)

# cut delay
mx.vdee_mix = 0

s1.dur = .5
s1.sus = .45
# s1.level=.5
s1 + P(0,5)
s1.amp = [0,1,0,0,1,0]
cp.fade(12, fvol=.1)

s1.degree = var([0,5,2,3],[8,4,2,2], start=Clock.mod(4)) + (0,5)
# pitches = var([0, 2, 5, 2, 0, -2, 5, 4],[1,1,2,.5,.5,.5,.5,.5])
# s1.degree = pitches

cp.fadeout()
Scale.default = Scale.minor
s1.level=.5
s1.dur=.5
k2.fadeout(16)
a4.fade(16,fvol=1)
a4.oct=2
s1 + (0,2)
s1 + [(0,2), 0, 5, 2]
s1.dur = [.5,.25,.25]

print(Scale.names())

s1.amp = [0,1,0,0,1,1]

hh >> play("..-.", sdb=1, amp=2, rate=1.2, dur=.25, sample=6, pan=linvar([-.5,.5],16))


s1.amp = [1,1,0,0,1,1]

s1.amp = [1,1,1,0,1,1]

cp >> play(".(.**.)(**.-)(..(O.)(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)
cp.fadein(16)

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

Root.default = var(PTri(12), .25)

Scale.default = Scale.locrian
hh >> play("..(---(b--(ib)))(.-)", sdb=1, amp=2, rate=1.2, dur=.25, sample=6)

s1.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))
mx.deda_drywet = linvar([0, .3], [32,inf], start=Clock.mod(4))
s1.fade(16, fvol=.9)

cp.sample = 2
hh.sample = 2

k3.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))
k3.degree = "<V.x.>"
k3.amp=2.5

Scale.default = Scale.chinese
k3.degree = "<V.x.><o.[(...X)X]>"

k3.degree = "<V.x.><o(..[XV])[(...X)X]>"

k3.sample = 0

k1.lpf = 800
s1.cutoff=linvar([1,.4],32, start=Clock.mod(4))

Scale.default = Scale.minor
mx.deda_drywet = linvar([.3, 0], [16,inf], start=Clock.mod(4))

mx.deda_on = 0
a4.pitch = 0
a4.arp = 0

pitches = [0, 2, 5, 2, 0, -2, 5, 4]
s1.degree = pitches

s1.vol=1.3
s1 + [(0,2), 0, 5, 2]

mx.sm_mix = linvar([0, .1], 16, start=Clock.mod(4))

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
s1.vol=1

# un peu de noise
mx.ru_blend=linvar([0,.3], [32,64,inf], start=Clock.mod(4))

Scale.default = Scale.minorPentatonic

s1.fade(16, fvol=.8)
s1.pause(8,24)
s2.fade(fvol=1.4)
k1.fade(ivol=1, fvol=1.4)
s2.oct = Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
s2.amp = P[.8, .7, .5, 1.1, .9] * 2

s2.dur = var([.25, .5, 1/3], [10,4,2])
mx.ru_on = 0

k3.degree = "<V.x.>"

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
# e3.mpan(mrot(6))
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


b1 >> play("{k.[ccc]..[***bb*]}", dur=[.25,.5], amp=2, rate=PWhite(2.5,4))#.fadeout()#d$.fadein()


kk >> play("[vvvX]", rate=linvar([.5,2.6], [32,inf], start=Clock.mod(4)))#.fadein(32)

kk.fadeout()













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
