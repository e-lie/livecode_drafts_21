b1 >> blip(dur=.25, output=2)
dd >> play("v[-]", output=2, rate=1, amp=3, sample=0)
k1 >> play("[xx]", output=2, rate=linvar([1,2], 16, start=Clock.mod(4)))
k1 >> play("v.", output=2, rate=1)
b2 >> bass303([0], dur=2)
g 2 >> gone([0], dur=2, oct=6)

change_bpm(130)



bb >> pl
