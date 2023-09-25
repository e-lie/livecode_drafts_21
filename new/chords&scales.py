
## Repiquer des accords !!
### Ok le truc c'est de comprendre les modes je crois


Root.default = var([-1,-1,-1,])
Root.default = -1
Scale.default = Scale.minor

chords = var([0,0,0,4,6,6,5,3],2)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.major], [6,6,2,2])

t1 >> mmarimba(chords+[0,2,4,0,1,3,4], dur=[.25,.5,.25,.25,.5], oct=4)
t2 >> mmarimba(chords+[0,2,4,0,1,3,4], dur=[.25,.5], oct=3)

t_all.amp = linvar([.5,1],[4,8,2,3,5]) + PWhite(0,.3)

k1 >> play("X.", lpf=400, amplify=1, output=12)
hh >> play(".-", sample=4, rate=1.3).fadein(16)
