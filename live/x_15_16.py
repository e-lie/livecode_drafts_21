
change_bpm(120)

Scale.default = Scale.major

mmelody = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5], .25)
mmelody2 = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0], .25)

m1 >> vibra1(mmelody, dur=.25, release=.5, decay=.7, attack=0)
m1.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
m1.fadein(30, fvol=1.2)
b1 >> bino1(
    [None],
    setup_id=.32,
    azimuth_slider=linvar([.3,.7],128),
    elevation_slider=linvar([.2,.8],77),
)
m1.release = .6
m1.decay = .8
a4.fade(30, fvol=.7)

m1.release = linvar([.5, .8], [16,inf], start=Clock.mod(4))
m1.decay = linvar([.7, .3], [16,inf], start=Clock.mod(4))

m1.oct = [5, None, None, None, 5]

m1.oct = [5, None, None, None, 6]

m1.oct = [5, 4, None, None, 6]

ff >> play("b", dur=.125, rate=linvar([3,8],16), amp=.1, sample=5)
ff.faderand()

m1.fade(fvol=1.3)

m1.oct = [5, 4, 6, None, 6]

m1.amp=linvar([1, .45], 2*15*.25, start=Clock.mod(4))

Scale.default = Scale.aeolian

m2 >> marimba4(mmelody, dur=.25, release=.5, decay=.7, attack=0)
m2.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
m2.fadein(8, fvol=1.1)
Scale.default = Scale.dorian
m2.oct = [None, 4, None, None, None]
b2 >> bino4(
    [None],
    azimuth_slider=linvar([.3,.7],17),
    elevation_slider=linvar([.2,.8],27),
)

m1.fade(fvol=1)

m2.oct = [None, 4, None, 4, 7]

m2.release = linvar([.5, .8], [16], start=Clock.mod(4))
m2.decay = linvar([.7, .3], [16], start=Clock.mod(4))

m2.attack = linvar([0, .3], [24], start=Clock.mod(4))

m1.degree = mmelody + (0,2)

Scale.default = Scale.aeolian

m2.degree = mmelody + (0,4)

ff.fadeout()

l1 >> lone1(mmelody, dur=.25, reverb_mix=0, delay_mix=0)
l1.fadein(fvol=1)
l1.oct=m1.oct
b3 >> bino3(
    azimuth_slider=linvar([.3,.7],177),
    elevation_slider=linvar([.2,.8],277),
)

l1.fade(fvol=1.2)

m1.degree=mmelody2
l1.degree=mmelody2

l1.voices = linvar([0,.8],17) # to debug
l1.tones = linvar([0,.8],13)

l1.degree = 0
l1.oct = 4
l1.voices = 1

l1.degree=mmelody2

l1.oct = (4,5)

l1.degree = -2

l1.degree = 2

l1.degree=mmelody2
l1.oct = (4,5,6)

l1.oct = (4,5)
l1.fade(fvol=.1)

l1.faderand()

Scale.default = Pvar([Scale.major, Scale.mixolydian, Scale.minor, Scale.dorian],15*.25)

kk >> play("x..............", dur=.25, amp=1, lpf=300, sample=1, sdb=2, output=12)
kk.fadein(15)
kk.rate=(1,1.8)

k2 >> play("x...............", dur=.25, amp=1, lpf=300, sample=1, sdb=2, output=12)

kk.degree="x.(..x).."

hh >> play(".-", rate=.3, room2=0, sdb=2, sample=3)

b4 >> bino4(
    [None],
    setup_id=.32,
    azimuth_slider=linvar([.3,.7],4),
    elevation_slider=linvar([.2,.8],7),
)

hh.degree = ".[--]"
hh.pan=[-1,0,1]

hh.degree = ".[--...]"

hh.degree = ".[---..]"

hh.degree = ".[----.]"

hh.room2 = 0
hh.room2 = linvar([0,1], [8,inf], start=Clock.mod(4))

d2 >> play("X...", dur=.25, amp=.8, lpf=200, sample=1, sdb=2, output=12)
d2.fadein(7.5)

hh.degree = ".[-----]"

hh.degree = "-[-----]"

hh.rate = linvar([.3,2], [30, inf], start=Clock.mod(4))

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
d3 >> play("V(..(xv))", output=12, lpf=600, amp=.8).fadein()

m1.fadeout(32)

d3.pause(8,32)

d2.degree = "([XXX]X)(...X)"

d3.sample = 2

d4 >> play("<c>", dur=[1/3,2/3], rate=4, lpf=600, amp=2)
d2.degree = "X..X."
d2.sample=6

d4.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])

d4.rate=P(3,1)

d4.rate=P(3,1,6)

d4.rate=P(6,3,12)
d4.amp=3

d4.rate=P*(3,1,6,9,15)

d4.dur=[1/3,2/3]

d4.rate=4
d4.fade(fvol=1)

d5 >> play("s.", dur=[.4,.3,.3], rate=[1,1.2,1], amp=2, sample=0)
d5.rate = linvar([1,4], 32)
d4.pan = [-1, 0, 0, 1]

d5.degree = "s"
d5.room2=.6

d5.fadeout(16)

k_all.fadeout(15)

d_all.fadeout(15)

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
