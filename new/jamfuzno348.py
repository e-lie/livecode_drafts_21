


b1 >> bbass(oct=3)

notes = var([0,3,0,5], [2,4])

b2 >> blip(
    notes + [0,1,2,3,0,-2,4],
    dur=[.25,.5,.25,1],
    sus=var([.2,.7],2),
    amp=linvar([1,5],[2,8])+PWhite(.2,.8),
    oct=var([4,5,4,6])
)

b2 + P*(0,2)

b3 >> bbass(
    notes + [0,1,2,3,0,-2,4],
    dur=1,
    sus=var([.2,.7],2),
    amp=linvar([1,5],[2,8])+PWhite(.2,.8),
    oct=3,
)
