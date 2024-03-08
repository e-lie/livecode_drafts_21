
vibra = Player()
liblip = Player()
marimba = Player()
lonesynth = Player()
kick1 = Player()
kick2 = Player()
kick3 = Player()
kick4 = Player()
clave = Player()
shaker = Player()
kicks = Group(kick1, kick2, kick3, kick4)
percus = Group(kick1, kick2, kick3, kick4, clave, shaker, hh)

change_bpm(110)

Scale.default = Scale.major

mmelody = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5], .25)
mmelody2 = var(P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0], .25)

vibra >> vibra1(mmelody, dur=.25, release=.5, decay=.7, attack=0)
vibra.amp=linvar([.75, .45], 15*.25)
vibra.fadein(30, fvol=1)
vibra.release = .6
vibra.decay = .8
vibra.span(srot(32), .2)

vibra.release = linvar([.5, .8], [16,inf], start=Clock.mod(4))
vibra.decay = linvar([.7, .3], [16,inf], start=Clock.mod(4))

vibra.oct = [5, None, None, None, 5]

vibra.oct = [5, None, None, None, 6]

vibra.oct = [5, 4, None, None, 6]

liblip >> play("b", dur=.125, rate=linvar([3,8],16), amp=.1, sample=5)
liblip.faderand()
liblip.mpan(mrot(256))

vibra.fade(fvol=1.3)

vibra.oct = [5, 4, 6, None, 6]

vibra.amp=linvar([1, .45], 2*15*.25)

Scale.default = Scale.aeolian

marimba >> marimba4(mmelody, dur=.25, release=.5, decay=.7, attack=0)
marimba.amp=linvar([.75, .45], 15*.25, start=Clock.mod(4))
marimba.fadein(8, fvol=1.1)
Scale.default = Scale.dorian
marimba.oct = [None, 4, None, None, None]
marimba.span(srot(48),.5)

vibra.fade(fvol=1)

liblip.mpan(mrot(16))
marimba.oct = [None, 4, None, 4, 7]

marimba.release = linvar([.5, .8], [16], start=Clock.mod(4))
marimba.decay = linvar([.7, .3], [16], start=Clock.mod(4))
marimba.attack = linvar([0, .3], [24], start=Clock.mod(4))

vibra.degree = mmelody + (0,2)

Scale.default = Scale.aeolian

liblip.fade(fvol=.2)
bpm_to(120, 32)
marimba.degree = mmelody + (0,4)

liblip.mpan(mrot(256))
lonesynth >> lone1(mmelody, dur=.25, reverb_mix=0, delay_mix=0)
lonesynth.fadein(fvol=1)
lonesynth.voices = linvar([0,1],32)
lonesynth.oct=vibra.oct
lonesynth.span(srot(4), linvar([0,.2,0,.8], 16))

lonesynth.fade(fvol=1.2)

vibra.degree=mmelody2
lonesynth.degree=mmelody2

lonesynth.voices = linvar([0,.8],17)
lonesynth.tones = linvar([0,.8],13)

lonesynth.degree = 0
lonesynth.oct = 4
lonesynth.voices = 1

lonesynth.degree=mmelody2

lonesynth.degree = 0
lonesynth.oct = (4,5)

lonesynth.degree = -2

lonesynth.degree = 2

lonesynth.degree=mmelody2
lonesynth.oct = (4,5,6)

lonesynth.degree = -2

lonesynth.degree=mmelody2

lonesynth.oct = (4,5)
lonesynth.fade(fvol=.1)
lonesynth.amp=1.8

lonesynth.faderand()

Scale.default = Pvar([Scale.major, Scale.mixolydian, Scale.minor, Scale.dorian],15*.25)

kick1 >> play("x"+14*'.', dur=.25, amp=1.2, lpf=300, sample=1, sdb=0, output=12)
kick1.fadein(15)
kick1.rate=(1,1.8)
liblip.fadep("rate", dur=48, fvalue=.1)
liblip.fade(fvol=1)

kick1.degree="x.(x..).."

kick2 >> play("V"+15*'.', dur=.25, amp=1, lpf=300, sample=1, sdb=0, output=12)

hh >> play(".-", rate=.3, room2=0, sdb=0, sample=3, pan=linvar([-.8,.8], 48))

hh.degree = ".[--]"

hh.pan=P[-1,0,1,0,.5]*.8
hh.mpan(mrot(8))

hh.degree = ".[--...]"
bpm_to(130, 128)
liblip.fadeout(32)

hh.degree = ".[---..]"

hh.degree = ".[----.]"

hh.room2 = 0
hh.room2 = linvar([0,1], [8,inf], start=Clock.mod(4))

kick3 >> play("X...", dur=.25, amp=.8, lpf=200, sample=1, sdb=0, output=12)
kick3.fadein(7.5)
kick3.amp=1.2

hh.degree = ".[-----]"

hh.degree = "-[-----]"

hh.rate = linvar([.3,2], [45, inf], start=Clock.mod(4))

hh.degree = "[-----]"

vibra.oct = [5, 4, None, None, 6]

kick3.degree = "X..X."
hh.amp=3
hh.pan=0
hh.room2=0
hh.degree = ".-"

kick3.lpf=400
kick1.lpf=400
kick4 >> play("V(..(xv))", output=12, lpf=600, amp=.8).fadein()
kick1.fadeout()

vibra.fadeout(32)

kick4.pause(8,32)

kick4.sample = 2

clave >> play("c", dur=[1/3,2/3], rate=4, lpf=600, amp=2)
kick3.degree = "X..X."
kick3.amp=.8
kick3.sample=6

Scale.default = Pvar([Scale.chromatic, Scale.majorPentatonic, Scale.minor],8)

clave.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])

clave.rate=P(3,1)

clave.rate=P(3,1,6)

clave.rate=P(6,3,12)
clave.amp=3

clave.rate=P*(3,1,6,9,15)

clave.rate=P(6,3,12)

clave.dur=[1/3,2/3]

clave.rate=P(3,1,6)

clave.curr_players()
kick1.fadeout()

clave.rate=4
clave.fade(fvol=.8)

shaker >> play("s..", dur=[.4,.3,.3], rate=[1,1.2,1], amp=3, sample=0)
shaker.rate = linvar([1,4], 32)
shaker.room2=.6

shaker.degree = "s."
clave.amp=2.5

shaker.degree = "s"
clave.amp=4

clave.dur=Pvar([[1/3,2/3],1/3,[1/6,1/6,2/3]], [16,8,8])

Root.default = 0

Scale.default = Scale.chinese

clave.degree = "c{c.}"

shaker.degree = "s"
shaker.room2=.6

shaker.curr_players()

liblip.fadeout(32)

shaker.degree = "s{s.}"

lonesynth.fadeout(16)
marimba.fadeout(16)
kick1.fadeout(16)
clave.fadeout(64)
shaker.fadeout(72)
hh.fadeout(32)
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
kicks.fadeout(15)
