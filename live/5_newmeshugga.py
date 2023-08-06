Clock.clear()

change_bpm(145)

######  Idées
# changer la melodie au milieu du morceau
# faire des polyphonies qui marchent bien avec des var
# ajouter des break a bosser ensuite avec martin

Root.default = 0
Scale.default = Scale.major
chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])

bassline1 = var([P[0,0,1,3,4,1,0,0,1,3,4,1,8,8,8]], [1,1,2])
bassline2 = var([P[0,0,1,-8,-7,1,0,0,1,-8,-7,1,1,1,1]+7], [1,1,2])

Clock.meter = (4,4)
Scale.default = Scale.chromatic
Root.default = 0

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(10, fvol=.6)
# a4.span(srot(64), .4)
a4.oct = 3
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.degree=bassline1

h1 >> play(
    # "qeriofhjqeoriuhgflqiseurhfbiqdzueoueh",
    "<k.k..><-[--]>",
    dur=.5,
    amp=3,
    rate=PWhite(1,4)[:40],
)
h1.rate=var([[0.5,0.5,1,3,4,1,0.5,0.5,1,3,4,1,5,5,5]], [1,1,2])
h1.fadein(10)

b1 >> pluckbass(
    degree=0,
    dur=[4/5],
    oct=4,
    amp=1,
    vol=1,
    sus=b1.dur-.3,
)
b1.drive=linvar([.2,1],[60,20], start=Clock.mod(4))
b1.width=linvar([.2,1],[60,20], start=Clock.mod(4))
b1.reverb=linvar([0,1],[60,20], start=Clock.mod(4))
b1.buzz=linvar([.3,.7],[60,20], start=Clock.mod(4))
b2 >> reese(
    degree=0,
    root=0,
    dur=[4/5],
    sus=.8,
    oct=5,
    tremolo=0,
    amp=1.3,
    vol=.8,
)
b2.detune1=0
b2.detune2=0
b2.cutoff=0
b2.drive=0
b2.oct=4
b_all.fadein()
e2 >> play("v...[*----O-O]", dur=4, amp=2, output=12)
b_all.pause(4,20,16)

# b_all.degree=var([[0,0,1,3,4,1,0,0,1,3,4,1,8,8,8]], [1,1,2]),
b1.degree=bassline1
b2.degree=bassline2
b_all.dur=[1,1,2]
b_all.pause(0,20)
# b2.dur=.5
# b_all.dur=var([.5,1])

e2.stop()

b2.cutoff=linvar([0,.7],[60,20], start=Clock.mod(4))
b2.drive=linvar([0,.9],[60,20], start=Clock.mod(4))

b2.vol=1.3

b1.sus=.2
b1.dur=.25

l2 >> keypong(
    bassline1,
    dur=[.5,1,.5],
    oct=6,
    vol=1.1,
    fx=.7,
)
l2.fadein(20)
l2+P(0,7)

l2.dur=Pvar([[.5,1,.5],[.25],[.5,.5,1],[.5]],[8,4])
l2.sus=l2.dur-.1

b1.dur=[1,1,2]

b2.fadeout()

b1.dur=[1,1,2]

# b1.degree=Pvar([[0,0,1], [3,4,1], [0,0,1], [8,8,8]], [5])
# b1.dur = [1,1,2]

b1.vol = 1.4
b1.degree = bassline1

b1.dur=1

d2 >> equals(
    # chords+[0,2,3,5,6,0,2,3],
    # chords+[0,2,3,5,6],
    bassline2,
    # dur=var([.25,.5],20),
    # oct=var([5,6],20),
    oct=var([5,6],20),
    # sus=linvar([.8,3],32),
    amp=.8,
    sus=1,
    dur=[1,.5],
    vol=1,
).fadein(fvol=1.3)
d2.bass_pulse=linvar([0,.5],16)
d2.detune=linvar([0,.5,1],32)
d2.filter_motion=var([0,.5],24)
d2.effects=linvar([0,1],32)

Root.default = var(PTri(10), .5)

Root.default = var(PTri(10)-5, 4, start=Clock.mod(4))

Root.default = 0

Root.default = var([0,0,2,0,3], dur=4)
Root.default = var([0,0,2,0,3], dur=1)

Scale.default = Scale.chromatic

b1.fadeout(20)

b_all.dur=1

b2.detune1=linvar([0,1],16)
b2.detune2=linvar([0,1],24)
# b2.cutoff=linvar([1,0],24)
b2.cutoff=linvar([.3,0],24)
b2.drive=linvar([1,0],32)

b2.stop()
b1.vol=1.6

l2.ampfadeout()

b2.vol=1

h_all.stop()

k2 >> play("<X...>", dur=.25, amp=3, rate=1, output=12)
sn >> play("<.o*o>", dur=.25, amp=1, rate=1, output=12, pan=var([-1,1]))

sn.stop()

Scale.default = Pvar([Scale.minorPentatonic, Scale.chromatic, Scale.egyptian, Scale.chromatic], 20, start=Clock.mod(20))

k3 >> play("V", dur=var([2.5,1.25],20), amp=2, lpf=200, output=12)
k3.dur=2.5
k3.stop()

h2 >> play(".----", dur=.25, amp=8, rate=linvar([1,2],[1.25,0]), pan=[-1,0,1])

h2.pause(10,20)
h2.pause(0,20)
d3.stop()

l2.dur=cascara

l2.vol=1.3

e3.stop()


Scale.default = Scale.chromatic

l2.degree = chords + P[0, 2, 0, P(0, 2)]
l2.dur=var([1,.5])
l2.oct=7

b2.fadeout(20)
sn.ampfadeout(10)
k_all.ampfadeout(10)
l2.fadeout(40)
d2.fadeout()
b1.fadeout(10)
