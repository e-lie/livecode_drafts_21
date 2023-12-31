Clock.clear()

k1.curr_players()

from FoxDot.preset import *

mixer = instanciate("_mixer", "effects/fxstack_1_off")
duckless = instanciate("_duckless", "effects/kick_fx_1")

# bino1 = instanciate("bino1", "effects/stereo2bino_1")
# bino2 = instanciate("bino2", "effects/stereo2bino_1")
# bino3 = instanciate("bino3", "effects/stereo2bino_1")
# bino4 = instanciate("bino4", "effects/stereo2bino_1")

gone = instanciate("chan1", "pads/gone_1")
bass303 = instanciate("chan2", "bass/bass303_1")
apad = instanciate("chan3", "pads/apad_1")
marimba4 = instanciate("chan4", "mallets/marimba_1")
vibra1 = instanciate("chan5", "mallets/vibra_1")
# sheer = instanciate("chan6", "synth_keys/sheer_1")
pstrings = instanciate("chan7", "guitars_strings/pstrings_1")
pluckbass = instanciate("chan8", "bass/pluckbass_1")
lone1 = instanciate("chan9", "synth_keys/lonesine_1")
equals = instanciate("chan10", "synth_keys/equals_1")
dakeys = instanciate("chan11", "synth_keys/dakeys_1")
padarp = instanciate("chan12", "synth_keys/padarp_1")
keypong = instanciate("chan13", "synth_keys/keypong_1")
sizzle = instanciate("chan14", "synth_keys/sizzle_1")
wobble = instanciate("chan16", "bass/wobble_1")
# reese = instanciate("chan15", "bass/reese_1") # TODO debug midichannel 15

# Clock.latency = .5
# Clock.midi_nudge = -.235 # latency 1024/48000
Clock.latency = .5
Clock.midi_nudge = -.232 # latency 2048/48000

######## marimba patterns

change_bpm(120)

Scale.default = Scale.major

mx >> mixer([None], vdee_mix=0)
dl >> duckless(dot8_mix=0)

mmelody = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5], .25)
mmelody2 = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0], .25)

m1 >> vibra1(mmelody, dur=.25, release=.5, decay=.7, attack=0)
m1.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
m1.fadein(30, fvol=1)
m1.release = .6
m1.decay = .8
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
).fadein(16, fvol=.8)
m1.release = linvar([.5, .8], [16,inf], start=Clock.mod(4))
m1.decay = linvar([.7, .3], [16,inf], start=Clock.mod(4))

m1.oct = [5, None, None, None, 5]

m1.oct = [5, None, None, None, 6]

m1.oct = [5, 4, None, None, 6]

ff >> play("b", dur=.125, rate=linvar([2,4],16), amp=.1, sample=5, pan=linvar([-.8,.8], PRand(2,16)))
ff.amp =expvar([.01,.1], PRand(6,16), start=Clock.mod(4))

m1.fade(fvol=1.3)

m1.oct = [5, 4, 6, None, 6]

m1.amp=linvar([1, .45], 2*15*.25, start=Clock.mod(4))

Scale.default = Scale.aeolian

m2 >> marimba4(mmelody, dur=.25, release=.5, decay=.7, attack=0)
m2.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
m2.fadein(8, fvol=1.1)
Scale.default = Scale.dorian
m2.oct = [None, 4, None, None, None]

ff.fadeout()

m1.fade(fvol=1)

m2.oct = [None, 4, None, 4, 7]

m1.degree = mmelody + (0,2)

Scale.default = Scale.aeolian

m2.degree = mmelody + (0,4)

ff.fadeout(16)

l1 >> lone1(mmelody, dur=.25, reverb_mix=0, delay_mix=0)
l1.fadein(fvol=1)
l1.oct=m1.oct
m1.degree=mmelody2
l1.degree=mmelody2
l1.voices = linvar([0,.8],17) # to debug
l1.tones = linvar([0,.8],13)

l1.degree = 0
l1.oct = (4,5)

l1.degree=mmelody2
l1.oct = (4,5,6)

Scale.default = Pvar([Scale.major, Scale.mixolydian, Scale.minor, Scale.dorian],15*.25)
kk >> play("x..............", dur=.25, amp=1.7, lpf=300, sample=1, sdb=2, output=12)
kk.fadein(7)
kk.rate=(1,1.8)
kk.amp=3

k2 >> play("x...............", dur=.25, amp=3, lpf=300, sample=1, sdb=2, output=12)

kk.degree="x.(..x).."

hh >> play(".-", rate=.3, room2=.1, sdb=2, sample=3).fadein(16)

hh.degree = ".[--]"
hh.pan=P[-1,0,1,0,.5]*.8

hh.degree = ".[--...]"

hh.degree = ".[---..]"

hh.degree = ".[-----]"

hh.room2 = linvar([.1,1], [8,inf], start=Clock.mod(4))

d2 >> play("X...", dur=.25, amp=.8, lpf=200, sample=1, sdb=2, output=12)
d2.fadein(7.5)
d2.amp=1

hh.degree = "-[-----]"

hh.rate = linvar([.3,1.5], [30, inf], start=Clock.mod(4))

hh.degree = "[-----]"
d2.degree = "[XXX]..(.X)."

m1.oct = [5, 4, None, None, 6]
d2.degree = "X..X."
hh.amp=2
hh.pan=0
hh.room2=0
hh.degree = ".-"

dd.degree = "x..x."
dd.sample=2

d2.lpf=400
kk.lpf=400
d3 >> play("V(..(xv))", output=12, lpf=600, amp=1).fadein()

m1.fadeout(32)

d3.pause(8,32)

d2.degree = "([XXX]X)(...X)"
d3.sample = 2

d4 >> play("<c>", dur=[1/3,2/3], rate=4, lpf=600, amp=2)
d2.degree = "X..X."
d2.sample=6

d4.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])
d4.pan = linvar([0,.8,.3,-.9], PRand(8,16), start=Clock.mod(4))

d4.rate=P(3,1,6)

d4.rate=P(6,3,12)
d4.amp=3

d4.rate=P*(3,1,6,9,15)

d4.dur=[1/3,2/3]

d4.rate=4
d4.fade(fvol=.8)

d5 >> play("s.", dur=[.4,.3,.3], rate=[1,1.2,1], amp=2, sample=0)
d5.rate = linvar([1,4], 32)
d4.pan = [-1, 0, 0, 1]

d5.degree = "s"
d5.room2=.6

d5.curr_players()

l1.fadeout(16)
m2.fadeout(16)
kk.fadeout(16)
hh.fadeout(32)
bpm_to(130)

d_all.fadeout(15)
change_bpm(130)
Root.default = 0
# tt >> fxstack(ru_on=False, ens_on=False, vdee_on=False, sm_on=False, deda_on=False)
Scale.default = Scale.chromatic
pitches = [0, 2, 5, 2, 0, -2, 5, 4]
mx >> mixer([None], vdee_mix=0)
dl >> duckless(dot8_mix=.5)

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


k2 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12, amp=1.2)
k2.fadein(16)

m_all.fadeout()

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

cc >> play("..(..)(.*)", dur=.25, rate=var([3,4]), amp=2, room2=0, hpf=700, lpf=2000, sample=4, pan=[-.5,0,-.8])
cc.fadein(24)
a4.body = linvar([0, 1, .4, .8, 0, .6],PRand(2,24, seed=0), start=Clock.mod(4))

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
a4.oct = 4
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
cp >> play(".(.**.)(.*..)(...(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2, pan=var([-.5,0,.7,0],PRand(1,4)/4))
cp.sample = (3,4)
cp.sdb=2

cc.fadeout(24)
a4.fade(32, fvol=.5)
a1.fade(24, fvol=.3)

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
s1 + [(0,2), 0, 5, 2]
s1.dur = [.5,.25,.25]

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

hh >> play("..(---(b--(ib)))(.-)", sdb=1, amp=2, rate=1.2, dur=.25, sample=6)

s1.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))
mx.deda_drywet = linvar([0, .3], [32,inf], start=Clock.mod(4))
s1.fade(16, fvol=.9)

cp.sample = 2
hh.sample = 2

k3.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))
k3.degree = "<V.x.>"

k3.degree = "<V.x.><o.[(...X)X]>"

k3.degree = "<V.x.><o(..[XV])[(...X)X]>"

k1.lpf = 800
s1.cutoff=linvar([1,.4],32, start=Clock.mod(4))

mx.deda_drywet = linvar([.3, 0], [16,inf], start=Clock.mod(4))

mx.deda_on=0
a4.pitch = 0
a4.arp = 0

pitches = [0, 2, 5, 2, 0, -2, 5, 4]
s1.degree = pitches

s1.amp = .6
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
s1.vol=1

# un peu de noise
mx.ru_blend=linvar([0,.3], [64,32,inf], start=Clock.mod(4))

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

Root.default = 0
chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])
Clock.meter = (4,4)
Root.default = 0

bpm_to(140)

change_bpm(140)

bb.curr_players()

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
l2.degree = chords3 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2)
Scale.default = Scale.minor

Root.default = var(PTri(12), 16, start=Clock.mod(4))

Root.default = var(PTri(12), .25)

k3.degree = "V......."

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

somegroup = Group(l1, l2, a1)
somegroup.only()

Root.default = 0

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

k5 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amp=1.6,
    output=12
)

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

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32, fvol=1.1)
# a4.span(srot(32), .5)
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.curr_players()


bpm_to(200, 24)

bpm_to(60, 24   )                   
