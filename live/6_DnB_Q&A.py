Clock.clear()

# Idee: faire de la dnb avec des alternances partie avec martin

### 2 Step basic
### variations
kicks = []
basic_kicks = []
basic_kicks.append("x....x..")
basic_kicks.append("x..x....")
# basic_kicks.append("x..[.x]....")
# basic_kicks.append("x...[.x]...")
### double end or beginning kick
double_end_kicks = []
double_end_kicks.append("x....x.x")
double_end_kicks.append("x..x...x")
# kicks.append("x..[.x]...x")
double_end_kicks.append("x...[.x]..x")
double_beg_kicks = []
double_beg_kicks.append("xx...x..")
double_beg_kicks.append("xx.x....")
# kicks.append("xx.[.x]....")
double_beg_kicks.append("xx..[.x]...")
### 2 step only on 4th bar
fourbar_kicks = []
fourbar_kicks.append("x....(...x)..")
### vessel pattern
vessel_kicks = []
vessel_kicks.append("(x.)(.x)...x..")
vessel_kicks.append("(x.)(.x)...x.(...x)") # 4 bar accented kick
vessel_kicks.append("(x.)((x.)x)...x.(...x)") # 4 bar accented kick bis
### 2 step with 3 kicks
triple_kicks = []
triple_kicks.append("x..x.x..")
triple_kicks.append("x..[.x].x..") # the bounce pattern !
triple_kicks.append("x..[.x][.x]...") # the bounce pattern bis !
triple_kicks.append("x..x[.x]...") # the bounce pattern ter !
triple_kicks.append("x...xx..")
kicks = basic_kicks + double_end_kicks + double_beg_kicks + fourbar_kicks + vessel_kicks + triple_kicks
### ghost kicks (neurodnb?)
gkicks = []
gkicks.append(".[.x]......")
gkicks.append(".[.x]..")
gkicks.append(".[.x].(.[.x])")
### ghost snares
gsnares = []
gsnares.append(".")
gsnares.append("...[.o][.o]...")
gsnares.append("...[.o][.o]..[.o]")

change_bpm(160)

#######


Root.default = 0
Scale.default = Scale.minor

ke >> sizzle([var([0,2],4),None,4,None], dur=.25, oct=5, vol=1.3, sus=.24, fx=0)
ke.fadein()
ke.stop()

b3 >> wobble([0,0,0,2], oct=3, dur=4).fadein(fvol=1.3)
b3.effects=0
b3.fm_tone=0
b3.mod_shape=0

b3.mod_shape=linvar([0,.3], [4])

b3.effects=linvar([0,1],24, start=Clock.mod(4))

b3.cutoff=1


k2 >> play("v(.)", dur=1, amp=1.5)
k2 >> play("<v(.)><X.>", dur=.5, amp=2.5, output=12, rate=1)

k_all.stop()


k2.dur =.125

k2.dur =.25
k2.rate = linvar([1,3],16, start=Clock.mod(4))
k2.stop(5)

# b3.fm_tone=linvar([0,.4],32)
# b3.mod_shape=.2
b3.cutoff=.1

hh >> play("-", dur=.5, sdb=1, sample=0, rate=1.6, amp=2.5, room2=5)
hh.fadein(16)
sn >> play("<..i.><..o.>", dur=.5, sdb=1, lpf=20000, rate=1.3, sample=3, amp=4)
# sn >> play("..o.", dur=.5, sdb=1, lpf=20000, rate=1.5, sample=4, amp=3, room2=0)
sn.sample=2
sn.sample=[2,3,4,5]
sn.fadein(16)


sn.dur=var([.25,.5], [4,12])
hh.dur=.25

sn.stop()
hh.stop()


ke.oct=[3,5,7]

ke.degree="efgh"

hh.dur=.5
hh.dur=var([.5,.25],PRand(2,8))
hh.sample=PRand(0,4)
hh.pan=[-1,0,1,-1,0]
hh.room2=0
hh.room2=.2
hh.room2=.5
hh.room2=1
hh.rate=PWhite(.8,2)

sn >> play("<..i.><..o.>", dur=.5, sdb=1, lpf=20000, rate=1.3, sample=3, amp=4)
# sn >> play("..o.", dur=.5, sdb=1, lpf=20000, rate=1.5, sample=4, amp=3, room2=0)
sn.sample=2
sn.sample=[2,3,4,5]
hh >> play("-", dur=.5, sdb=1, sample=0, rate=1.6, amp=2.5, room2=5)
k1 >> play(
    Pvar(kicks, 4),
    # vessel_kicks[1],
    dur=.5,
    sdb=1,
    lpf=500,
    sample=4,
    # rate=1.2,
    rate=1,
    amp=2.8,
    output=12,
    )
# k1.every(16,"stutter") # TODO fix that !!
k1.amp=4


k1.pause(16,32,0)
sn.pause(16,32,0)
hh.pause(16,32,16)
# hh.pause(16,32,16)

k1.pause(0,32,0)
sn.pause(0,32,0)
hh.pause(0,32,16)

kk.pause(32,32,0)
sn.pause(32,32,0)
hh.pause(32,32,16)

bb >> pluckbass(
    [0,1,2,0,1],
    # chords,
    # chords2,
    # chords3,
    dur=.5,
    # dur=cascara,
    oct=P[4,5,6,7]-var([0,2,0,1],),
    # oct=P[2,3,4,5],
    amp=2,
    room2=1,
    sus=bb.dur-.3,
    vol=.8,
    # sus=linvar([.5,2], 32),
    # pan=var([-.5, 0, .5], 4)
)#.pause(8, 32)
# bb.mpan(3)
bb.drive=linvar([0,1],16)
bb.width=linvar([0,1],32)
bb.reverb=linvar([0,1],24)
bb.buzz=linvar([0,1],28)
d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=2.5)

bb.dur = PDur(3,8)
bb.dur = .5

bb.dur=[.5,1,1,.5,.5,1]
bb.amp=[0,1,1,1,1]
bb.amp=[0,1,1]
bb.amp=[.5,1,2,1,.2]

k2 >> play(
    Pvar(gkicks,8),
    amp=2.5,
    sdb=1,
    sample=1,
    rate=1.2,
    lpf=500,
    output=12
)

gn >> play(
    Pvar(gsnares, 16),
    sdb=1,
    sample=3,
    rate=2,
    amp=1.8
).pause(16,48)



kk.stop()

### DNB bass from video to continue

bb >> pluckbass([None,0], oct=4, dur=PRand(1,2), sus=5, vol=2)
bb >> pluckbass([0], oct=3, dur=[.5,7.5], amp=[0,1])
bb >> pluckbass([0], oct=3, dur=[1,7], amp=[0,1])
bb >> pluckbass([0,0,1], oct=3, dur=[1,6,1], amp=[0,1,1])
bb >> pluckbass([0,0,1], oct=3, dur=[1,5.5,1.5], amp=[0,1,1], sus=bb.dur+1)
bb >> pluckbass([0], oct=3, dur=[1.5,1.5,2], amp=1, sus=bb.dur+1)
bb >> bbass(0, oct=P[3,4,3].stutter(2), dur=.25, amp=[0,1,1], sus=bb.dur+.2) + (chords + P[0,2,0,1].stutter(2))

ft >> pharao("pokpk", dur=.5, amp=PWhite(.7,.95), vol=1.4, root=0, scale=Scale.chromatic)
ft.stop()

b4 >> reese([0,0,2], oct=4, dur=4)
b4.detune1=.3
b4.detune2=.25
b4.cutoff=.15
b4.drive=.5

b4.detune1=linvar([0,1],16)
b4.detune2=linvar([0,1],24)
b4.cutoff=linvar([1,0],24)
b4.cutoff=linvar([.3,0],24)
b4.drive=linvar([1,0],32)

b4.dur=PDur(3,8)
b4.sus=b4.dur-.2

Scale.default = Pvar([Scale.major, Scale.minor, Scale.chromatic, Scale.majorPentatonic],16)
b4.oct=[4,4,4,[5,6,4,5],4,4]
