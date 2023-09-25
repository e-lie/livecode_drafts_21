change_bpm(130)

line = var([0,1,0,2], PDur(3,8))


k1 >> play("<(v.).><(xX).>", output=12, amp=1.5, sample=2)
hh >> play("-")
hh.sample = 3
sn >> play("..o.")
cp >> play("((.[**].[.*])...)(.[.*])", rate=2, amp=4, pan=[-.5,.5,0])

b1 >> acidbass(degree=P[None,1,None,1]*line, curve=linvar([-1,1], 8), dur=PDur(3,8), oct=3, sus=.2, amp=1, lagtime=linvar([0,.3],16), frange=linvar([0,7],8), pan=[-.5,.5])
b2 >> pluckbass(degree=P[1,None,1,1]*line, dur=PDur(3,8), oct=3, sus=.2, amp=1)
m1 >> blip(line+[0,8,3], dur=.25, sus=.4, oct=[5,6,7,8])

# regular mode
tol = 32
brl = 8

k_all.pause(brl,tol,tol-brl)
b_all.pause(brl,tol,tol-brl-1)
m1.pause(brl,tol/2,tol/2-brl*2)
# p_all.
hh.degree = Pvar([".-", "-", "[--]", "[---]", None], [tol/2,tol/2-brl,brl/2,brl/4,brl/4])
hh.pan = Pvar([[-.2,.2],[-.6,.6]], [tol*3/4,tol/4])

# triggered mode
tol = 128
brl = 8

k_all.pause(brl,tol,tol-brl)
b_all.pause(brl,tol,tol-brl-2)
m1.pause(brl,tol/2,tol/2-brl*2)
# p_all.
hh.degree = Pvar([".-", "-", "[--]", "[---]", None], [tol/2,tol/2-brl,brl/2,brl/4,brl/4])
hh.pan = Pvar([[-.2,.2],[-.6,.6]], [tol*3/4,tol/4])
