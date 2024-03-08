kick1 = Player()
kick2 = Player()
kick3 = Player()
hihat1 = Player()
hihat2 = Player()
bongo1 = Player()
bongo2 = Player()
bongo3 = Player()
bongo4 = Player()
lonesynth = Player()
acidbass = Player()

mx >> mixer([None])
pad2 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
pad2.fadein(32, fvol=.8)
pad2.span(srot(32), .5)
pad2.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
Scale.default = Scale.minorPentatonic
mx.fadep("sm_mix", dur=16, fvalue=.15)
mx.fadep("vdee_mix", dur=16, fvalue=0)
mx.fadep("deda_drywet", dur=16, fvalue=0)

bpm_to(160, 24)

change_bpm(160)
pbass.fadeout()
percus.fadeout()
melos.fadeout()

## Ok le banger de l'année
acidbass >> bass303([0,2,4,3], dur=.25, oct=var([5,4,5,6],1))
acidbass.fadein(fvol=.8)
acidbass.span(srot(32), .5)
acidbass.decay = 0
acidbass.envmod = 0
acidbass.reso = 0
acidbass.cutoff = 0
acidbass.reverb_mix = 0
acidbass.reverb_switch = 1

####################""
Scale.default = Scale.minor

Root.default = var(PTri(12), 2)
Root.default = 0
############################

acidbass.envmod = linvar([0,.4,0], [8,8,16], start=Clock.mod(4))

kick1 >> play("<v..v..v.><x..x..x.>", dur=.25, amp=1.5, lpf=600, hpf=60, output=12)

hihat1 >> play("..-.....", dur=.25, rate=1, amp=2, sample=3)

acidbass.envmod = linvar([0,.4,0], [8,8,inf], start=Clock.mod(4))

hihat1 >> play("-.-....-", dur=.25, rate=1, amp=2, sample=3)

acidbass.envmod = linvar([0,.4,0], [8,8,16], start=Clock.mod(4))
acidbass.envmod = linvar([0,.7,0], [8,8,inf], start=Clock.mod(4))

acidbass.reso = linvar([0,.6], [9,7], start=Clock.mod(4))

acidbass.pause(4,16)

acidbass.fadep("cutoff", fvalue=.3, dur=16)

kick1 >> play("<v..vb.v.><x..x..x.>", dur=.25, amp=1.5, lpf=600, hpf=60, output=12)

bongo1 >> play(".c..c..c", amp=3, dur=.25, rate=8, room2=.4)#.fadein(26)

acidbass.fadep("cutoff", fvalue=.1, dur=16)

bongo2 >> play(".c.....c", amp=2, dur=.25, rate=[2.5,2.5,3], room2=.4)#.stop()#.fadein(26)

hihat1 >> play("-.---.--", dur=.25, rate=1, amp=2, sample=3)
hihat1.mpan(mrot(128))

bongo1 >> play(".c..{ccx.}{..cx}.{ccx.}", amp=3, dur=.25, rate=8, room2=.4)#.fadein(26)
bongo2 >> play(".cc.cc.c", amp=3, dur=.25, rate=7, room2=.4)#.fadein(26)
bongo2.mpan(mrot(32))

bongo1 >> blip(0, dur=.25, room2=.4, amp=P[0,1,1,0,1,1,0,1]*3, oct=7)#.fadein(26)
bongo1 >> blip([0,2,4,3], dur=.25, room2=.4, amp=P[0,1,1,0,1,1,0,1]*4, oct=7)#.fadein(26)
bongo1.oct=var(P[5,4,5,6]+1,1)

Scale.default = Pvar([Scale.chinese, Scale.minorPentatonic], [48,16])

bongo1.pause(8,32,8)
bongo2.pause(8,32,12)
kick1 >> play("V..V..V.", dur=.25, amp=2, lpf=1000)
kick1 >> play("V..V..V.", dur=.25, amp=2, lpf=1000)
kick1 >> play("V.VV..V.", dur=.25, amp=2, lpf=1000)
kick1 >> play("{VVV.}.{V..}V..V.", dur=.25, amp=2, lpf=1000)

kick1 >> play("V.VV.{...V}.V", dur=.25, amp=2, lpf=1000)

kick1.sample=2
kick1.amp=1.7
kick1.pause(32,128)

hihat1.amp=6
hihat1.rate=linvar([2,4],PRand(4,16, seed=2), start=Clock.mod(4))
# hihat1.pan=linvar([-.8,.8], PRand(4,16))
bongo1.rate=linvar([4,7],PRand(4,16, seed=2), start=Clock.mod(4))
sample
k2.sample=0

hihat2 >> play("..-.", amp=2.5, rate=(.8,1.2), sample=4, dur=.5)

bongo2 >> play(".{cccccc.}..", amp=3, dur=1/3, rate=7, room2=1)
# bongo2.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=5)[:12], start=Clock.mod(4))
Scale.default = Scale.minorPentatonic

hihat1.rate=1
bongo3 >> play("{ccccc.}..", amp=3, dur=1/3, rate=8, room2=1)
bongo3.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=4)[:12], start=Clock.mod(4))

c_all.fadeout(16)

l2 >> lone1(
    [0,2,4,3],
    dur=.25,
    sus=linvar([.3, 3], 16),
    oct=var(PRand(4,6),1),
    amp=1,
    cutoff=.4,
    vol=1.6,
    # room2=1,
    pan=[-1, 0, 1],
).fadein(16, fvol=1.4)
l2.voices = linvar([0,1],32)

kick2 >> play("V..V..V.", dur=.25, amp=1.5, lpf=900, output=12)
kick2 >> play("V...V.V.", dur=.25, amp=1.5, lpf=900, output=12).stop()

kick1.pause(32,64)
kick2.pause(16,64,16)

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

# k2 >> play("<V.><X.>", dur=2/3, amp=2, lpf=900, output=12)
k2 >> play("<V.><X.>", dur=1, amp=2, lpf=900, output=12)
bongo1 >> play(".c.c.c.cc", amp=4.7, dur=1/3, rate=8, room2=1)
bongo1.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=3)[:12], start=Clock.mod(4))

c1 >> play("c.c.c.cc.", amp=4.5, dur=1/3, rate=6, room2=1)
c1 >> play("c.{cc.}.c.{c.}c.", amp=4.5, dur=1/3, rate=6, room2=1)
c1.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=2)[:12], start=Clock.mod(4))

s2 >> blip(
    [0],
    dur=1/3,
    amp=P[.7, .8, .9, 1, 1.1, 1, .9, .8] * 2,
    pan=[-1,0,1,0],
    oct=P[5, 7, 6, 7]-P[0,1,0],
    sus=linvar([.3, 2], [48], start=Clock.mod(4)),
)
s2.fadein(16, fvol=2)

s2.dur=.5

hihat1.fadeout(8)

Scale.default = Scale.chinese

s2.degree=chords

k2 >> play("V.x.", lpf=800, dur=.5, output=12, amp=1.4)

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

bongo1.fadeout(24)
bongo3.fadeout(24)

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
