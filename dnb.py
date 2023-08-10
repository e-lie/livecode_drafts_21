
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



Scale.default = Scale.minor

line = var([0,1,0,2], PDur(3,8))

change_bpm(140)
change_bpm(200)

b1 >> acidbass(degree=P[1,None,1,1]*line, curve=linvar([-1,1], 8), dur=PDur(3,8), oct=3, sus=.2, amp=1, lagtime=linvar([0,.3],16), frange=linvar([0,7],8), pan=[-.5,.5])
b3 >> wobble(line, oct=(3,4), dur=4).stop()
.fadein(fvol=.8)
b3.stop()


l3 >> space(degree=line, curve=linvar([-1,1], 8), dur=.25, oct=[6,7,6,5], amp=1, pan=[-.5,.5], sus=linvar([.1,1],16))
b2 >> play("<v.><(xX).>", output=12, amp=1.5, sample=2)
d2 >> play(".(*.*([**][.*][**][*****]))", output=12, amp=5, rate=[2,3,4], sample=2)
d2 >> play("[***]([**]i=.)", output=12, amp=4, rate=2, sample=2)
d2 >> play(".*", rate=2)
d2.stop()

sn >> play("<..i.><..o.>", dur=.5, sdb=1, lpf=20000, rate=1.3, sample=3, amp=4)
hh >> play("-", dur=.5, sdb=1, sample=0, rate=1.6, amp=2.5, room2=5)

k1 >> play(
    Pvar(vessel_kicks, 4),
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

b2.stop()

Clock.bpm = linvar([140, 170], 32, start=Clock.mod(4))

change_bpm(170)

k1.stop()
