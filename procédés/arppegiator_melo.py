d1 >> blip([0,[2,None,4],4,[5,8,None,2],3,1], dur=.25, amp=sinvar([.6,1.2],1), oct=(4,7), amplify=PWhite(.9,1))
d1.output=6

d2 >> pluck([0,[2,5,None],4,5,3,1], dur=.25, amp=sinvar([.6,1.2],.75), oct=5, amplify=PWhite(.6,.8))
d2.output=4

Scale.default = Scale.chinese

Scale.default = Scale.majorPentatonic

Root.default = linvar([0,16], 16)

w1 >> play(".(www(w[ww]))", amp=.5, rate=[1,[1,1,1,linvar([1,2],[16,0])]])
w1.rate = [1,2,4,1,2]
w1.rate = [2,4, 1, 1]

k1 >> play("V.", amp=.7, lpf=500)

hh >> play("([--]([--](.o.O)))")
