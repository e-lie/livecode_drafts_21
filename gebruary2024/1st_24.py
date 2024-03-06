from FoxDot.preset import *

Clock.latency = .5
Clock.midi_nudge = -.232
# vital/ium <3
abbysun = instanciate("chan3", "pads/abbysun_1")
lone1 = instanciate("chan9", "synth_keys/lonesine_1")
mixer = instanciate("_mixer", "effects/fxstack_1_off")

change_bpm(100)

#osc(12,0,[0,.5].smooth())
#.mult(osc().rotate(1.5), .2)
#.modulateScale(voronoi().modulate(noise(500),.4), .3)
#.modulate(noise([.4,2].smooth()),.6)
#.mult(solid(.1,.1,.2), [.5,1.2].smooth())
#.out()
#speed=.1
mx >> mixer(
    vdee_mix=linvar([0,0,.4], PRand(16,24), start=Clock.mod(4)),
)

Root.default = var([0,1,3,5], [4,8,16])

h1 >> play("s", dur=1/3, pan=[-.7,0,.7], amp=2, rate=P(1,2), spack=1).fadein()

a1 >> abbysun([0, 4], amp=1, dur=4, sus=3.9, oct=(3,6)).fadein(128, fvol=.8)

b1 >> blip([None, 0, None], dur=[.4,.3,.3], oct=4, lpf=600, pan=PWhite(-.3,.3)).fadein(32)
b1.pause(4,16)

b3 >> lone1([0, None], dur=1/3, hpf=0, oct=2, pan=PWhite(-.7, .7), amp=4, room2=1, lpf=300).fadein()

r1 >> charm([0, 4], amp=1, dur=4, room2=1, sus=6, oct=(3,6)).fadein(32)

b1.degree = [0, 0, None]

b1.degree = [0, 4, None]

b2 >> lone1([0, None], dur=[.4,.3,.3], lpf=1200, oct=6, pan=PWhite(-.7, .7))

r1.fadeout(32)

b2.degree = [0, [0, None]]
b2.pause(16,64)

h1.fade(fvol=3)

Root.default = var([0,4,7,0,2,9], 1/3)

h1.degree="<{s.}><{=.}>"

h1.sample = PRand(0,6)

h1.rate = linvar([1,4],[16, inf], start=Clock.mod(4))

a1.fadeout()
