
d1 >> blip([0], dur=.25).fadeout()

d1 >> play("ax", sample=PTri(0,14), spack=1, amp=.4)

chords = var([0,5,4,0,2],4)

b4 >> bbass(
    chords + P[0,[None,(3,5),5],[5,2,4,None],4],
    dur=[.4,.3,.3], oct=3,
    amp=linvar([.3,1],2),
    amplify=PWhite(.9,1.1),
    sus=.8,
    pan=0,
    room2=.5,
    lpf=1000,
)

Clock.bpm = 100

tt >> MidiOut(chords+[0,3,[5,100]], channel=0, dur=.25, sus=.2)

Root.default =

b2 >> blip(
    chords + P[0,[3,None,(2,5)],[5,None,4,2],[4,None]],
    dur=[.4,.3,.3], oct=5,
    amp=linvar([.3,1],2),
    amplify=PWhite(.9,1.1),
    sus=.8,
    hpf=1000,
)

b3 >> blip([0,0,[0,2]]+chords, dur=[.25,.125,.125], amp=.4, oct=[5,6], room2=1).fadein(16)

PRand()
PWhite()

Scale.default = Scale.major

d1 >> play(P["x(xo.[ii])"], dur=.5, amp=.2)
b2 >> blip([0,[0,2,None,P+(4,4)]], dur=.5, amp=.4)

b3 >> blip(P[2,4,6,3], dur=.5)

Root.default = 0 #var([0,2,4],.)

b4 >> blip(linvar(P[0,2,4], P[4,2,inf], start=Clock.mod(4)), dur=.25, oct=5)

@nextBar(8)
def mafunc():
    b4.oct=6

k1 >> play("<x.><i>", amp=.6, lpf=600, room2=1)#.fadein(16,fvol=.4)

hh >> play("bbb[bbb]", amp=.5, rate=linvar([1,2],8), pan=linvar([-.5,.5],PRand(1,4)), room2=1)
