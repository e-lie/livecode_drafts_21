from FoxDot.preset import *

vital1 = instanciate("chan1", "vital")
vital2 = instanciate("chan2", "vital")
vital3 = instanciate("chan3", "vital")
vital4 = instanciate("chan4", "vital")


v1 >> vital1([0,1,1.5,1,2], oct=P*(3,4,5), dur=[1,.5,.25,.25])
v2 >> vital2([0,2,5,2], oct=P*(3,4,5), dur=[1,.5,.25,.25])

d1 >> play("v.", amp=2, rate=[2,1,1.5])

Scale.default = Scale.

b1 >> blip(P[0,1,2]+var([0,2,3]))

d1 >> play("x-[---]", amp=5, dur=.5)
