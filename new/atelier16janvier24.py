

Scale.default = Scale.minorPentatonic

Root.default = var([0,1,2,3,4], 2) # transposer sauvagement l'ensemble tous les 2 temps

b1 >> blip(chords+P[0,2,7,8], amp=P[.5,.8,1,.5]*2, dur=[.25], oct=4, lpf=[700,3000]).fadein(16)
b2 >> blip(chords+P[0,2,5], amp=P[.5,.8,1,0]*2, dur=[.25], oct=5, lpf=[700,3000,1200]).fadein(8)

g1 >> play("v.", lpf=400, amp=.3, output=12,  rate=linvar([.8,1.3], 8))
g2 >> play(".(...(x[.V]))", lpf=800, amp=.2, output=12,  rate=linvar([.8,1.3], 8))

monkick . bd

ss >> play("s{s.}", dur=[.4,.3,.3], amp=1,  rate=linvar([.8,1.3], 8))
hh >> play(".-", dur=.5, amp=2, rate=linvar([.8,1.3], 8))

def mesaccords(param1="value1", param2="value2"): # fonction generatrice appelée dans le bloc pluckbass
    # ici on pourrait ajouter une logique puissante qui sait comment retourner une progression bebop ou whatever
    chords = var([0,2,0,5],4)
    return chords

bb >> pluckbass(
    mesaccords(),
    # dur=1,
    dur=P[0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25],
    drive=linvar([.2,1],16, start=Clock.mod(4)),
    width=linvar([.2,1],32, start=Clock.mod(4)),
    reverb=linvar([0,1],24, start=Clock.mod(4)),
    buzz=linvar([.3,.7],28, start=Clock.mod(4)),
    vol=1,
    oct=P(3),
)

bb.fadeout()
b1.fadeout()
