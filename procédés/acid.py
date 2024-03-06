


from FoxDot.preset import *

mixer = instanciate("_mixer", "effects/fxstack_1_off")
duckless = instanciate("_duckless", "effects/kick_fx_1")

bass303 = instanciate("chan2", "bass/bass303_2")
acidbb = instanciate("chan3", "bass/acidbb_1")
bass303_2 = instanciate("chan4", "bass/bass303_2")
acidbb_2 = instanciate("chan5", "bass/acidbb_1")

tb303 = instanciate("chan6", "bass/tb303_1")

Clock.latency = .5
Clock.midi_nudge = -.232 # latency 2048/48000

Scale.default = Scale.minor

change_bpm(110)

Clock.bpm=130

b1 >> bass303(
    [[0,0,2],5,4,2,[5,4],4,[0,7],7],
    dur=P[1,.25,.5,.25],
    sus=b1.dur-P[.02,.0,.02,0],
    oct=[5,[4,5],5,[5,6]],
)

print(b1.cutoff)
print(b1.reso)
print(b1.envmod)
print(b1.decay)
print(b1.keytrack)
print(b1.reverb)
print(b1.phaser)
print(b1.surfilter)

b1.surfilter = 0

k1 >> play("x.", output=12, lpf=800, sample=2, amp=2)

hh >> play("..(----.)(...-)", output=12, sample=1, rate=.8, amp=2, dur=.25)

b1 >> tb303(
    [0,0,0,4,0,8],
    dur=[.25],
    sus=b1.dur-P[.02, .02, .02, -.02, .02, .02],
    oct=3,
    cutoff=linvar([.2,.8], 13),
    resonance=linvar([0,.8], 17),
    accent=linvar([0,.8], 17),
    formant_x=linvar([.2,.8],13),
    formant_y=linvar([.2,.8],7),
)

b1 >> MidiOut(var([0,5,4,0]), dur=[.25], sus=.49, channel=0, amp=[1,0], oct=5.5, amplify=linvar([.6,1]))
b2 >> MidiOut(var([0,5,4,0]), dur=[.25], sus=.49, channel=1, amp=[0,1], oct=5.5, amplify=linvar([.6,1]))

b1 + [0,1,0,4]
b2 + [0,1,0,4,0]

d1 >> play("X.", lpf=600)
cp >> play("..(OOOO)(...[.O])", sample=1, rate=linvar([.7,1.2],16), amp=1, hpf=300, lpf=3000)
hh >> play("[--]-(..--)(...-)", sample=4, rate=1.3)
