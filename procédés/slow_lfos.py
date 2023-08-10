
change_bpm(130)

Root.default = 0

Scale.default = Scale.minor
Scale.default = Scale.majorPentatonic

k1 >> play("<v...><X...>", dur=.25, sdb=1, lpf=linvar([400,900],64), rate=linvar([.9,1.2],64), sample=var([0,1,2],64), amp=2, output=12, room2=linvar([.2,.8],64))
hh >> play("-(.-)", dur=.25, sdb=1, rate=P[1.3,1.8,1]*linvar([1,2],128), sample=var([0,1,2,3]), hpf=linvar([5000,9000],128), pan=linvar([0,.9],16)*P[-.2,.6,.2,0,-.6])
cp >> play(".(...(*.))*.", dur=.25, sdb=1, rate=linvar([1.5,2.5],128), sample=var([1,2],PRand(4,16)), lpf=6000, hpf=4000, amp=2)
m1 >> pharao(P[0,None,2,1,None]+[0,[0,2],[(0,2),-2],2,0], dur=cascara, oct=P[4,5,4], sus=.7, amp=P[.3,1]*2, vol=1)
m2 >> pharao(P[None,1,None,1,0]+[0,[0,2],[(0,2),-2],2,0], dur=cascara, oct=P[4,5,4]+1, sus=.7, amp=P[.3,1], vol=1, cutoff=linvar([.2,1],128))

b1 >> wobble([0,0,2], dur=Pvar([[2,2,4],PDur(3,8)],[48,16]), oct=4, vol=1, cutoff=linvar([.4,1],64), effects=linvar([0,1],128))

hh.degree = Pvar(["-(.-)",".","(.[--]-)-","-"],[32,8,16,8])
hh.room2 = .4

m_all.stop()
