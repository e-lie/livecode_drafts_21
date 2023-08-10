Clock.clear()

from FoxDot.preset import *

fxstack, memory_leak = add_chains("effects/fxstack_1", "synth_keys/memory_leak_1")
bass303, gone = add_chains("bass/bass303_1", "pads/gone_1")
apad, marimba = add_chains("pads/apad_1", "mallets/marimba_1")
lavitar, pharao = add_chains("synth_keys/lavitar_1", "synth_keys/pharao_1")
pluckbass, equals = add_chains("bass/pluckbass_1", "synth_keys/equals_1")
dakeys, padarp = add_chains("synth_keys/dakeys_1", "synth_keys/padarp_1")
sizzle, keypong = add_chains("synth_keys/sizzle_1", "synth_keys/keypong_1")
wobble, reese = add_chains("bass/wobble_1", "bass/reese_1")

Clock.latency = .5
Clock.midi_nudge = -.235 # latency 1024/48000


change_bpm(130)
Root.default = 0
tt >> fxstack(ru_on=False, ens_on=False, vdee_on=False, sm_on=False, deda_on=False)
Scale.default = Scale.major
pitches = [0, 2, 5, 2, 0, -2, 5, 4]

a1 >> apad(
    P[0, 4, -2],
    dur=P[5,3,8]*2,
    attack=.8,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
)
# a1.span(srot(128), .8)
a1.fadein(16, fvol=.7)
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.degree = P[0,4,-2] + P(0,4,5)

k1 >> play("..(...x)(...(.X))", dur=.25, lpf=900, output=12)
k1.fadein(16)

s1 >> pharao(
    [0],
    dur=1,
    oct=4,
    amp=P[.8, .7, .8, 1.1],
    cutoff = .8,
    level=.3,
)
s1.fadein(16, fvol=1.8)
# s1.span(srot(48),.6)

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

k1.degree = "(V...).(...x)(...(.X))"

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.oct = 3
a4.fadein(32, fvol=.6)
a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Pvar([Scale.minor, Scale.major], 32, start=Clock.mod(4))

cc >> play("..(*.)(.*)", dur=.25, rate=var([3,4]), amp=2.3, room2=0, hpf=700, lpf=2000, sample=4)
cc.fadein(24)

a1.fade(16, fvol=.8)
k1.degree = "(V).(...x)(...(.X))"
k1.pause(8,64)
Scale.default = Scale.majorPentatonic

k1.sample=var([0,1,2],64)

a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.oct = 4
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

cp >> play(".(.**.)(.*..)(...(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)

cc.fadeout(24)

a4.fade(32, fvol=.4)

a1.fade(24, fvol=.3)

Scale.default = Scale.minor

s1.dur = .5
s1.level=.5
s1 + P(0,5)

pitches = [0, 2, 5, 2, 0, -2, 5, 4]

pitches = var([0, 2, 5, 2, 0, -2, 5, 4],[1,1,2,.5,.5,.5,.5,.5])
s1.degree = pitches
s1.vol=1.8
s1.level=.5
s1.dur=.5

s1.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))
s1.amp = [1,1,0,0]

cp >> play(".(.**.)(**.-)(..(O.)(.O))", dur=.25, lpf=8000, hpf=1000, amp=2, rate=2)

hh >> play("..(---(---(ib)))(.-)", sdb=1, amp=2, rate=1.2, dur=.25, sample=6)

k1 >> play(
    degree="V...",
    pdb=2,
    output=12,
    sample=8,
    room2=.1,
    lpf=400,
    amp=2,
)
k1.fadein(24, fvol=.7)

k1 >> play("V.(v)(...(.X))", dur=.25, lpf=900, output=12, amp=1.5)

k1.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))

k1.degree = "<V.x.>"

k1.degree = "<V.x.><..[(...X)X]>"

k1.degree = "<V.x.><.(..[XV])[(...X)X]>"

k1.lpf = 800

s1.fade(16, fvol=.5)

s1.fade(32, fvol=1.4)
s1.oct=(5,6)
s1.cutoff=linvar([1,.4],32, start=Clock.mod(4))

a4.pitch = 0
a4.arp = 0

Scale.default = Scale.minor

a4.fadeout(16)
s1 + (0,2)

k1.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))
k1.pause(8,48)
a4.stop()

a4.curr_players()
a1.fadeout()
k1.fadeout(ivol=None)

################################################################
############      Entrée caisse claire
################################################################

s2 >> blip(
    [0],
    dur=P[.5, .25, .25],
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 1,
    pan=[-1,0,1,0],
    oct=[5, 7, 6, 7],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
# s2.mpan(mrot(64))
s2.fadein(16, fvol=1.2)

# s1.span(srot(48))
s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

s1.fadeout(16, ivol=1.8, fvol=1)

s2.fadein(ivol=1, fvol=1.4)
k1.fadein(ivol=1, fvol=1.4)
s2.oct = Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
s2.amp = P[.8, .7, .5, 1.1, .9] * 2

s2.dur = var([.25, .5, 1/3], [10,4,2])
# s2.mpan(PRand(0,3))

a1.fadeout()

k1.degree = "<V.x.>"
a1.stop()

Scale.default = Scale.major

################################################################
############      Premiere montée
################################################################

Root.default = var(PTri(12), 8, start=Clock.mod(4))

k1.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))

k1.amp=1.2

s2.degree = pitches

s2.oct=(4,6)

Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)

Root.default = 0

################################################################
############      Premier break
################################################################

thegroup = Group(k1,s1)
thegroup.solo()
s2.stop()

thegroup = Group(k1,s1)
thegroup.solo()

s1.fadeout(24, ivol=1, fvol=.8)

################################################################
############      Deuxieme forme
################################################################

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32, fvol=.8)
# a4.span(srot(64), .4)
a4.oct = 3

a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
# a1.fadein(32)
k1.ampfadeout(16)
s1.fadeout()

s3 >> space(
    pitches,
    dur=[.5, .25, .25],
    amp=P[.8, .7, .8, 1.1] * 1.5,
    room2=.5,
    oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3]),
)
s3.pause(8,24,smooth=.3)

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

k1.stop()
s1.stop()

p2 >> padarp(
    [0, 2],
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
    filter_fx_cutoff=linvar([.2,.6],[32,inf], start=Clock.mod(4))
)
b1.fadein(4)

# p2.span(srot(12), .5)
p2.expand=linvar([0, 1], 24, start=Clock.mod(4))

p2.verb=linvar([0,1], [32], start=Clock.mod(4))

p2.delay=linvar([0,1], [64], start=Clock.mod(4))

p2.oct=[2,3,4,3]

s3.stop()
a4.fadeout(24, ivol=.8, fvol=.5)
k1 >> play(
    "X{.xXx}(X.)",
    output=12,
    sample=0,
    pdb=0,
    dur=.5,
    lpf=4000,
    pan = [-.5,0.5],
    amp=3
    # dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8)),
)
k1.fadein(16)
k1.rate = PWhite(.8,1.6)
# k1.mpan(PWhite(0,3.9))

k1.dur=Pvar([.25, PDur(5, 8)], PRand(2, 8))

k1.dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8))
k1.pause(8,32)

################################################################
############      Explosion
################################################################

k1.crush = PWhite(0,8)
k1.bits = PWhite(3,8)
a4.fadein(32, ivol=.5, fvol=.9)

Root.default = var(PTri(12), 8, start=Clock.mod(4))

Root.default = var(PTri(12), .25, start=Clock.mod(4))

Scale.default = Scale.minor

Root.default = 0
bpm_to(100, 128)

########### Cleaning

k1.ampfadeout(24)
s2.ampfadeout(24)
s3.ampfadeout(24)

a4.only()
