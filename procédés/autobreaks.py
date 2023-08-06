change_bpm(180)

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
total_len = 32
break_len = 8

k_all.pause(break_len,total_len,total_len-break_len)
b_all.pause(break_len,total_len,total_len-break_len-1)
m1.pause(break_len,total_len/2,total_len/2-break_len*2)
# p_all.
hh.degree = Pvar([".-", "-", "[--]", "[---]", None], [total_len/2,total_len/2-break_len,break_len/2,break_len/4,break_len/4])
hh.pan = Pvar([[-.2,.2],[-.6,.6]], [total_len*3/4,total_len/4])

# triggered mode
total_len = 128
break_len = 8

k_all.pause(break_len,total_len,total_len-break_len)
b_all.pause(break_len,total_len,total_len-break_len-2)
m1.pause(break_len,total_len/2,total_len/2-break_len*2)
# p_all.
hh.degree = Pvar([".-", "-", "[--]", "[---]", None], [total_len/2,total_len/2-break_len,break_len/2,break_len/4,break_len/4])
hh.pan = Pvar([[-.2,.2],[-.6,.6]], [total_len*3/4,total_len/4])
