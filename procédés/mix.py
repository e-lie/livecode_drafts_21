

root="/home/elie/Musiqqque/renardo_wav_tracks/"

change_bpm(160)


d1 >> loop(root+"DJ Manny - Soul Control.wav", 120.22, dur=16, lpf=800)

d2 >> loop(root+"DJ Manny - Soul Control.wav", 168.22, dur=16, lpf=800)

########################
# 959.5 beats de long
d1 >> loop(root+"Pablo Gargano - Blow your Mind (eve 8).wav", 130.7, dur=8, lpf=20000, rate=1.03, output=4)

d1 >> loop(root+"Pablo Gargano - Blow your Mind (eve 8).wav", 130.7, dur=16, lpf=20000, rate=1.03, output=4)

d1 >> loop(root+"Pablo Gargano - Blow your Mind (eve 8).wav", 130.7, dur=16, lpf=20000, rate=1.03, output=4)

d1 >> loop(root+"Pablo Gargano - Blow your Mind (eve 8).wav", 146, dur=16, lpf=20000, rate=1.03, output=4)


d1 >> loop(root+"Pablo Gargano - Blow your Mind (eve 8).wav", 500, dur=8, lpf=20000, rate=1.03)

k1 >> play("V.", lpf=400, amp=.7)



k1 >> play("(*---).", amp=3)

Root.default = 0

Scale.defaut = Scale.minor

p1 >> blip(var([-2,4]))
