

change_bpm(130)
change_bpm(100)

m1 >> sheer(
    var([0,1,2,3],1) + PRand([0,1,2], seed=17)[:16],
    # var([0,4,0,2],1) + PRand([0,1,2], seed=17)[:16],
    # var([0,1,2,3],1) + PRand([0,1,2], seed=13)[:32],
    # dur=var([.25,.25,.5],1),
    # dur=.25,
    # dur=[.5,.25,.25],
    dur=[.4,.3,.3],
    # amp=[0,1,0,1],
    amplify=[1,1,0,1,1],
    amp=PWhite(.7,1.2),
    # oct=var([4,5,4,6],.25),
    oct=(3,4),
    # vol=1.2,
    vol=.9,
)

d1 >> play("<s..><...(cc*)>", rate=2, amp=1.5, dur=.25)

k1 >> play("x.", output=12)

d2 >> play("s", dur=[.4,.3,.3], amp=2, rate=1.3)

b2 >> wobble([0,2], dur=2, oct=3, fm_tone=expvar(P[.1,.4,.3,.2].stutter(2),.5), mod_shape=expvar([.1,.3,.4,.2]))
