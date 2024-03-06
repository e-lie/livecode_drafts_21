# change_bpm(120)

Scale.default = Scale.major

mmelody = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5], .25)
mmelody2 = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0], .25)

m1 >> vibra1(mmelody, dur=.25, release=.5, decay=.7, attack=0, vibra_pan=.5)
m1.amp=linvar([.75, .45], 15*.25)
m1.fadein(30, fvol=1)
m1.release = .6
m1.decay = .8

m1.release = linvar([.5, .8], [16,inf], start=Clock.mod(4))
m1.decay = linvar([.7, .3], [16,inf], start=Clock.mod(4))

m1.oct = [5, None, None, None, 5]

m1.oct = [5, None, None, None, 6]

m1.oct = [5, 4, None, None, 6]

ff >> play("b", dur=.125, rate=linvar([3,8],16), amp=.1, sample=5)
ff.faderand()

m1.fade(fvol=1.3)


m1.oct = [5, 4, 6, None, 6]

m1.amp=linvar([1, .45], 2*15*.25)

Scale.default = Scale.aeolian

m2 >> marimba4(mmelody, dur=.25, release=.5, decay=.7, attack=0)
m2.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
m2.fadein(8, fvol=1.1)
Scale.default = Scale.dorian
m2.oct = [None, 4, None, None, None]

m1.fade(fvol=1)

m2.oct = [None, 4, None, 4, 7]

m2.release = linvar([.5, .8], [16], start=Clock.mod(4))
m2.decay = linvar([.7, .3], [16], start=Clock.mod(4))
m2.attack = linvar([0, .3], [24], start=Clock.mod(4))

m1.degree = mmelody + (0,2)

Scale.default = Scale.aeolian

m2.degree = mmelody + (0,4)


m1.degree=mmelody2
l3.degree=mmelody2

l3.voices = linvar([0,.8],17)
l3.tones = linvar([0,.8],13)

l3.degree = 0
l3.oct = 4
l3.voices = 1

l3.degree=mmelody2

l3.degree = 0
l3.oct = (4,5)

l3.degree = -2

l3.degree = 2

l3.degree=mmelody2
l3.oct = (4,5,6)

l3.degree = -2

l3.degree=mmelody2

l3.oct = (4,5)
l3.fade(fvol=.1)
l3.amp=1.8

l3.faderand()

Scale.default = Pvar([Scale.major, Scale.mixolydian, Scale.minor, Scale.dorian],15*.25)

kk >> play("x"+14*'.', dur=.25, amp=1.2, lpf=300, sample=1, sdb=0, output=12)
kk.fadein(15)
kk.rate=(1,1.8)

k2 >> play("V"+15*'.', dur=.25, amp=1, lpf=300, sample=1, sdb=0, output=12)

kk.degree="x.(..x).."

bpm_to(130, 16)

change_bpm(130)

hh >> play(".-", rate=.3, room2=0, sdb=0, sample=3, pan=linvar([-.8,.8], 48))

hh.degree = ".[--]"
hh.pan=P[-1,0,1,0,.5]*.8

hh.degree = ".[--...]"

hh.degree = ".[----.]"

hh.room2 = 0
hh.room2 = linvar([0,1], [8,inf], start=Clock.mod(4))

d2 >> play("X...", dur=.25, amp=.8, lpf=200, sample=1, sdb=0, output=12)
d2.fadein(7.5)
d2.amp=1.2

hh.degree = ".[-----]"

hh.degree = "-[-----]"

hh.rate = linvar([.3,2], [45, inf], start=Clock.mod(4))

hh.degree = "[-----]"

d2.degree = "X..X."
hh.amp=3
hh.pan=0
hh.room2=0
hh.degree = ".-"

dd.degree = "x..x."

dd.sample=2

d3 >> play("V(..(xv))", output=12, lpf=600, amp=.8).fadein()

m1.fadeout(32)

d3.pause(8,32)

d2.degree = "([XXX]X)(...X)"

d3.sample = 2
d2.amp = .8

d4 >> play("c", dur=[1/3,2/3], rate=4, lpf=600, amp=2)
d2.degree = "X..X."
d2.sample=6

Scale.default = Pvar([Scale.chromatic, Scale.majorPentatonic, Scale.minor],8)

d4.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])

d4.rate=P(3,1)

d4.rate=P(3,1,6)

d4.rate=P(6,3,12)
d4.amp=3

d4.rate=P*(3,1,6,9,15)

d4.rate=P(6,3,12)

d4.dur=[1/3,2/3]

d4.rate=P(3,1,6)

d4.curr_players()
k1.fadeout()

d4.rate=4
d4.fade(fvol=.8)

d5 >> play("s.", dur=[.4,.3,.3], rate=[1,1.2,1], amp=3, sample=0)
d5.rate = linvar([1,4], 32)
d5.room2=.6
d4.amp=2.5


d5.degree = "s"
d4.amp=4

d4.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])

Clock.meter = (4,4)
Root.default = 0

Scale.default = Scale.chinese

d4.degree = "c{c.}"

d5.degree = "s"
d5.room2=.6

d5.curr_players()

ff.fadeout(32)

d5.degree = "s{s.}"

k2 >> play("v..vb.v.", dur=.25, amp=1, lpf=600, hpf=60, output=12)

k_all.sample=var([0,3,2,1],16)

k2.curr_players()

l1.fadeout(16)
m2.fadeout(16)
kk.fadeout(16)
hh.fadeout(32)

Clock.bpm = var([120,140,160,120,160,200,120,260,360], PRand(2,5)[:8]|P[inf], start=Clock.mod(4))
mx >> mixer(None, ru_blend=linvar([0,.5], [32,inf], start=Clock.mod(4)))























k5 >> play("<V.......>", dur=.5, sample=1, rate=(1.2,1.6), amp=1, room2=0)
d6 >> play("<..*...*.>", dur=.5, sample=1, rate=(1.2,1.6), amp=1, room2=0)
d6.fadein()
k5.fadein()

bb >> pluckbass(
    [0],
    # chords,
    # chords2,
    # chords3,
    dur=PDur(3, 8),
    # dur=cascara,
    oct=(3,4),
    amp=2.5,
    room2=1,
    # sus=1,
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
    vol=1,
    # sus=linvar([.5,2], 32),
    # pan=var([-.5, 0, .5], 4)
)#.pause(8, 32)
# bb.mpan(3)
bb.fadein(16)
d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=2.5)

hh.fadeout()
m1.degree=mmelody2
l1.degree=mmelody2

d5.fadeout(32)
m1.fadeout(32)

d3.fadeout()

dd.fadeout()

l1.fadeout()
m2.fadeout()
kk.fadeout()



Clock.bpm=260


#########################################


change_bpm(120)


k1 >> play("x..............", dur=.25, amp=1.6, lpf=300, sample=1, sdb=0, output=12)

k2 >> play("V...............", dur=.25, amp=1.2, lpf=300, sample=1, sdb=0, output=12)

hh >> play("..-.", rate=.3, room2=0, sdb=0, sample=3, pan=linvar([-.8,.8], 48))

b1 >> blip([[None, [0, P*(0,0)]],P*(0,3)], dur=.5, oct=6)

b1.degree = P[None, 0] + [0,3,5,0,1]
b1.degree = P[[2,P*(0,2)], None] + [0,3,5,0,1]
b1.sus=[1,.5,2]
b1.oct=[5,6,4,3,7]
b2 + [0,2,0,3,5,1,0]
b1.pan = P[-.8,.8,.5,0,-.4].stutter(2)

k1.degree="x.(..x).."

k2 >> play("v..vb.v.", dur=.25, amp=2, lpf=600, hpf=60, output=12)

k_all.sample=0

k3 >> play("X...", dur=.25, amp=.8, lpf=200, sample=1, sdb=0, output=12)
k3.fadein(7.5)
k3.amp=1.2

Scale.default = Scale.minor

c3 >> play("c", dur=[1/3,2/3], rate=4, lpf=600, amp=2)
c3.degree = "c{c.}"

k2.sample=0

b3 >> marimba4([0,2,3,4], dur=[1/3,2/3], oct=5, amp=[1,PRand([0,1])], vol=.8)
