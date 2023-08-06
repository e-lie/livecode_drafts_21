

change_bpm(130)

Clock.meter = (4,4)

k1 >> play("X...", dur=.25, sdb=1, lpf=500)
hh >> play("-(.-)", dur=.25, sdb=1, rate=[1.3,1.8,1])
cp >> play(".(...(*.))*.", dur=.25, sdb=1, rate=1.5)
m1 >> blip([0,0,2,1], dur=.25, oct=[4,5,6])

k1.degree = "X.(X.)."

k1.degree = "X.X..."

k1.degree = "X..."
k1.dur=3/8
Clock.meter = (6,4)

m1.degree = [0,0,0,2,1,2]
m1.oct=[3,4,5,6,5]

hh.dur=3/8

cp.stop()

cp >> play(".(...(*.))*.", dur=3/8, sdb=1, rate=2.5)
hh.dur = 3/8
hh.pan = Pvar([-.6,.6,P[-.4,.4].stutter(2)], 2)
hh.rate = var([1,2,1.5],2)
k1.degree = "V..."

m1.sus=1
m1.dur=3/8
m1.degree = [0,0,2,1]
m1.oct=[4,5,6]

# cp.degree = ".*"

sn >> play("<..i.><..o.>", dur=3/8, sdb=1, lpf=20000, rate=1.3, sample=3, amp=2)
hh >> play("-", dur=.25, sdb=1, sample=0, rate=1.6, amp=2.5, room2=5)

k2 >> play(
    Pvar(vessel_kicks, 4),
    # vessel_kicks[1],
    dur=3/8,
    sdb=1,
    lpf=500,
    sample=4,
    # rate=1.2,
    rate=1,
    amp=2.8,
    output=12,
)
# k1.every(16,"stutter") # TODO fix that !!
k2.amp=2

sn.dur = 3/8
sn.rate = 1.5
sn.rate = linvar([1.5, 3], [16, inf], start=Clock.mod(4))

k2.dur=.25
sn.dur=.25
sn.rate=3

k1.dur=.25
k1.sample=3

p1 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
p1.fadein(32, fvol=.6)

##############################


k1 >> play("X...", dur=.25, sdb=1, lpf=500)
hh >> play("-(.-)", dur=.25, sdb=1, rate=[1.3,1.8,1])
cp >> play(".(...(*.))*.", dur=.25, sdb=1, rate=1.5)
m1 >> blip([0,0,2,1], dur=.25, oct=[4,5,6])

k1.degree = "X..X."
hh.degree = ".-..-"

m1.dur = 2/5
