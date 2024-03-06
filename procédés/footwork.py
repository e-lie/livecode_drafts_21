
change_bpm(160)

cc >> play("c.c.c.cc.", amp=2, dur=1/3, rate=2, room2=1)
c2 >> play(".c.c.c.cc", amp=2, dur=1/3, rate=1, room2=1)
c4 >> play(".c..", amp=2, dur=1/3, rate=.75, room2=1)
c3 >> play("c..", amp=2, dur=1/3, rate=.5, room2=1)
h2 >> play("..-.", amp=2, rate=.8, sample=4, dur=.5)

k1.curr_players()

hh.fadeout()

c1.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=2)[:12], start=Clock.mod(4))
c2.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=3)[:12], start=Clock.mod(4))
c3.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=4)[:12], start=Clock.mod(4))
c4.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=5)[:12], start=Clock.mod(4))

c_all.dur = 1/3

h2.dur = cascara

h2.degree = ".-"

h2.degree = "-"

c_all.amp=.7
h2.amp=.4

bb >> pluckbass(chords, dur=2, vol=1, oct=4).fadein()

bb.cutoff = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32,seed=5)[:12], start=Clock.mod(4))
bb.dur = clave23
bb.oct = 4

b3 >> pluckbass(chords, dur=2/3, vol=1, oct=5)

k1 >> play("V.", lpf=800, vol=1.2, output=12)

c_all.only()

bb.fadeout()

bb.fadeout()

g1.fadeout(32)

###############################################"""""

l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 16.75, dur=8)
l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 114.75, dur=16)

l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 146.75, dur=16)

l1.amp = 3

l1.only()

l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 178.75, dur=32, lpf=800)
l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 178.75, dur=64, lpf=800)
l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 178.75, dur=16, hpf=500, lpf=1500)

l1.stop()

l1.fadein()

l1.stop()

hh >> play("-", dur=1/3, amp=3)
hh >> play("-{.-}", dur=1/3, rate=linvar([.6,1.2], PRand(4,16)))
hh >> play("{---[--][----]}", dur=2/3)

Clock.bpm = 160

k2 >> play("v..v..v.", dur=.25, output=12, amp=1.2)

### COMMENT garder le rythme tout en passant à l'arrière plan de Jules
### Travailler des points de breaks pour jouer ensemble
### Comment travailler sur un support logique mais fixé

k2 >> play("v..v..v.", dur=.25, amp=.8)
k2 >> play("X..X..V.", dur=.25, output=12, lpf=linvar([400,900],32))
k2 >> play("<X..X..V.><v..v..v.>", dur=.25, output=12, lpf=linvar([200,900],32))

k2 >> play("v", dur=2/3, output=12)

k1.stop()

k_all.stop()


k2 >> play("v..v.v..".replace("v", "x"), dur=.25, output=12, amp=1.3)
k2 >> play("v.v..v..", dur=.25, output=12)

k2.lpf = 100

k2.fadeout()

k2 >> play("{vx}..{vvx}{..x}.v.", dur=.25)
k3 >> play("{v}{.v..x}", dur=1/3, output=12)
k2 >> play("{v}{.v..x}", dur=1/3, output=12, rate=1.2)

k5 >> play("V.", output=12)

c_all.fadeout()

k3.fadeout()

hh >> play("-.--.---", dur=.25, rate=3, amp=2)
hh >> play("-.-..-.[---]", dur=.25, rate=3, amp=2)
cp >> play("..(...*).(***.)...", dur=.25, sample=[0,0,0,2], amp=[1,2,1,3]).fadeout()
c2 >> play(".{*.}..{..*}..{..*}", dur=.25, rate=2)

c_all.fadeout()


h2 >> play("-.--.---.--.", dur=.25)
h2.fadeout()

k4 >> play(".x..x...x..x".replace('x', 'V'), output=12, rate=linvar([1,2],16), amp=2)
k4.stop()

k_all.fadeout()

# base 4
cc >> play("c.c.c.cc.", amp=2, dur=1/3, rate=2, room2=1)
cc >> play("c.c.c.cc.", amp=2, dur=1/3, rate=2, room2=1)
c2 >> play(".c.c.c.cc", amp=2, dur=1/3, rate=1, room2=1)
#c_all.fadeout()
c4 >> play(".c..", amp=2, dur=1/3, rate=.75, room2=1)
c3 >> play("c..", amp=2, dur=1/3, rate=.5, room2=1)


h2 >> play("..-.", amp=2, rate=.8, sample=4)


hh.fadeout()

k2.fadeout()

cc.fadeout()

hh >> play("{----[---]}{-----...[--]}", dur=.25)
hh >> play("{--..[---]}{-----...[--]}", dur=.25, sample=6, rate=linvar([.7,1.2],16))

hh.rate = 1

b3 >> pstrings([0,1.5,0,[3,1.5]], oct=6, dur=1).fade(fvol=.5)

b3 >> pstrings(chords+[0,2], oct=6, dur=2)


Root.default = -6

Scale.default = Scale.minor
Scale.default = Scale.major
Scale.default = Scale.chinese

chords = var([0,3,-2,2,0], [4,4,4,2,2])
variations = Pvar([[0,2,0,3], [0,3,2,3], [0,2,0,3], [0,1,2,0]])

hh.sample = 0

l1 >> lone1(chords+variations,
    dur=1,
    amp=1,
    oct=(5,6),
    vol=1.5,
    tone=linvar([0,1],16),
    voices=linvar([0,1],16))

l1.dur = Pvar([[2/3,4/3],1], 32)
l1.oct = Pvar([(4,7),(5,6)],32)

l1.fadeout()

b1 >> apad(chords, oct=4, dur=[4,4,4,2,2], attack=0)

k2.degree = "V..{x.}"
k2 >> play("V..{x.}")

b3.oct=(4,5)

h2 >> play("{-....}{......-}-.", amp=2, rate=.8, sample=4)
h2 >> play("..-.", amp=2, rate=.8, sample=4)

h2.fadeout(16)

# base 5
ss >> play("s{.s}", dur=P[.4,.3,.3], rate=.8, amp=2).fadein()

ss.fade(fvol=3)

ss.rate = linvar([.4, 3], 32, start=Clock.mod(4))
h2.rate = linvar([.4, 3], 32, start=Clock.mod(4))

ss.fadeout()

b3 >> padarp(chords+variations, oct=5, dur=[1.6,1.2,1.2], vol=1.5).fadein()
b3.dur=[.8,.6,.6]
b3.amplify=PRand([1,0,1])

k_all.fadeout(16)

h2.curr_players()
cp.fadeout()

b3.oct=3

##########################################""""

chords = var([0,4,-2,2], 4)

b2 >> lone1(chords, dur=4, oct=(4,3), vol=1.5)

m1 >> dakeys(chords+[0,1,0,5], dur=[.4,.6,.5,.5], oct=5).fadein(16, fvol=.7)
m2 >> dakeys(chords+P[0,1,0,5]+4, dur=[.4,.3,.3,.5,.5], oct=5).fadein(16, fvol=.7)

k1 >> play("v", dur=[1,2/3,2/3,7/6]).stop()

#

hh >> play("{.-}{--[--][.-].}", dur=cascara)
k2 >> play("V.", dur=cascara, output=12)

k2.lpf=400

k1 >> play("{vvv[vv]}{..v}", output=12, amp=.8, hpf=60)

k2.sample = 2

k2.degree = ".V"

k2.fadeout(16)

k2.sample = 3
k2.degree = "V."

k2.dur = clave23
k2.degree = "V"

k2.degree = "V{V.[VV]}"

hh.pan = linvar([-.3,.3], PRand(1,4))
k1.pan = linvar([-.3,.3], PRand(1,4))
k2.pan = linvar([-.3,.3], PRand(1,4))
k1.rate = PRand([1,1.2,1,1.4])
k2.rate = PRand([1,1.2,1,1.4])
