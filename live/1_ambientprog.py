Clock.clear()

from FoxDot.preset import *

fxstack, rdrum = add_chains("effects/fxstack_1", "drum/rdrum_1")
bass303, gone = add_chains("bass/bass303_1", "pads/gone_1")
apad, marimba = add_chains("pads/apad_1", "mallets/marimba_1")
lavitar, pharao = add_chains("synth_keys/lavitar_1", "synth_keys/pharao_1")
pluckbass, equals = add_chains("bass/pluckbass_1", "synth_keys/equals_1")
dakeys, padarp = add_chains("synth_keys/dakeys_1", "synth_keys/padarp_1")
sizzle, keypong = add_chains("synth_keys/sizzle_1", "synth_keys/keypong_1")
wobble, reese = add_chains("bass/wobble_1", "bass/reese_1")
# darkpass, hpluck, acidbb = add_chains("darkpass", "hpluck1")

# rdrum, bpiano = add_chains("drum/rdrum_1", "synth_keys/bpiano_1")

Clock.latency = .5
Clock.midi_nudge = -.235 # latency 1024/48000
# Clock.midi_nudge = -.212 # latency 256/48000

# def shift_clock(time, shift, factor=24):
#     time *= factor
#     shift *= factor
#     return max(time-shift,0)
# cshift = 1000
# cshift = 0

change_bpm(170)

b1 >> gone(vol=0, oct=3)

################################################################

change_bpm(130)
cc >> play("t", dur=1, rate=[1], pan=0, amp=[1], output=14)
cc.always_on = True

Root.default = 0
Scale.default = Scale.major
pitches = [0, 2, 5, 2, 0, -2, 5, 4]

################################################################
############      Intro Ambient
################################################################

s1 >> pharao(
    [0],
    dur=1,
    oct=4,
    amp=P[.8, .7, .8, 1.1],
    cutoff = .8,
    level=.3,
)
s1.fadein(16, fvol=1.8, ivol=0)
# s1.span(srot(48),.6)

a1 >> apad(
    P[0, 4, -2],
    dur=PRand(4, 8)[:16],
    vol=1,
    attack=.5,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
)
# a1.span(srot(128), .8)
a1.fadein(16)
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))

a1.degree = P[0,4,-2] + P(0,4,5)

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

Root.default = var([0,2,4], 1)

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32, fvol=.6)

a4.stop()


a1.fadeout(16, ivol=1, fvol=.8)
# a4.span(srot(64), .4)

################################################################
############      Entrée Batterie
################################################################

a4.oct = 3

Root.default = var([0,2,4], 2)

a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.fadeout(64, ivol=1, fvol=.8)

a1.oct = Pvar([5,(4,5),P*(4,6)], 2) - 2
a1.degree = Pvar([P[0, 4, -2], P[0, 4, -2]+P(0,4,5)], 16)

Root.default = 0

################################################################
############      Première forme
################################################################

a4.fadeout(16, ivol=.8, fvol=.5)

s1.dur = .5
s1.amp=1.7
s1.level=.5
s1 + P(0,5)

################################################################
############      Rythmiser les cymbales
################################################################

pitches = [0, 2, 5, 2, 0, -2, 5, 4]
s1.degree = pitches
s1.vol=1.8
s1.level=.5
s1.dur = Pvar([[.5,.25,.25],.5], 32, start=Clock.mod(4))

### Pas trop vite ici

################################################################
############      Entrée kick puis Toms batterie
################################################################

k1 >> play(
    degree="V...",
    pdb=2,
    output=12,
    sample=4,
    room2=.1,
    lpf=200,
)
k1.ampfadein(24, iamp=0, famp=.7)

k1.lpf = linvar([200,800], [32,inf], start=Clock.mod(4))
k1.degree = "<V.x.>"

k1.degree = "<V.x.><..[(...X)X]>"

# a1.span(.5)

k1.degree = "<V.x.><.(..[XV])[(...X)X]>"

s1.fadeout(16, ivol=1.7, fvol=1)

s1.fadein(32, ivol=1, fvol=1.4)
s1.oct=(5,6)
s1.cutoff=linvar([1,.4],32, start=Clock.mod(4))
# s1.level=.3
# s1.vol=.8
# s1.span(.5)

a4.pitch = 0
a4.arp = 0

Scale.default = Scale.minor

a4.fadeout(ivol=.5, dur=16)
s1 + (0,2)

k1.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))
k1.pause(8,48)
a4.stop()

################################################################
############      Entrée caisse claire
################################################################

s2 >> blip(
    [0],
    dur=P[.5, .25, .25],
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 2,
    pan=[-1,0,1,0],
    oct=[5, 7, 6, 7],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
# s2.mpan(mrot(64))
s2.fadein(16, fvol=1)

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
s2.ampfadein(16, famp=1)

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
    detune=sinvar([0,1], PWhite(.2,3)[:16], start=Clock.mod(4)),
    # detune=0,
    expand=0,
    vol=1.2,
)
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
k1.ampfadein(16)
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
