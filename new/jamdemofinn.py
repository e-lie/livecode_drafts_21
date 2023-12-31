FoxDot
renardo.org

demoplayer = Player()

Scale.default = Scale.major

g3 >> bellmod(P[0,1,2]*3, dur=PTri(8)/8, atk=.1).stop()

g4 >> bbass(P[0,1,2]*3, dur=1, oct=3, amp=2)

j2 >> play("x", dur=.5, sample=2, lpf=4000, rate=linvar([1,3], PRand(2,8)))

hh >> play(".c-", dur=.25, sample=2, lpf=4000, amp=4).fadeout()
