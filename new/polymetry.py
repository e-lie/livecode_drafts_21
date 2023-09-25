





p1 >> sheer(var([0,5,0,2],4), reverb_mix=0)
# p1.fadein(16)
p1 + [0,5,0,6,-2]
p1 + [0,1,0,2]
p1.dur=P[.5,1,2,.5]/2
p1.dur=.5
p1.amp=[0,1]
p1.amp=[1,0]
p1.amp=1
p1.root=PRand([0,0,0,0,0,2])

b1 >> pluckbass(
    var([0,5,0,2],4),
    dur=.5,
    # amp=[0,1,1,0],
    drive=0,
    amp=[1,0,0,0],
    oct=(3,4),
)

k1 >> play("<v...><X.xx...><V.X..>", dur=.25, output=12)
hh >> play("<.--.><..(*-)><s.s..>", amp=3, dur=.25, rate=1.5)
