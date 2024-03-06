
Clock.clear()

k1.curr_players()

from FoxDot.preset import *

mixer = instanciate("_mixer", "effects/fxstack_1_off")
duckless = instanciate("_duckless", "effects/kick_fx_1")

gone = instanciate("chan1", "pads/gone_1")
gone1 = gone
bass303 = instanciate("chan2", "bass/bass303_1")
apad = instanciate("chan3", "pads/apad_1")
apad3 = apad
marimba4 = instanciate("chan4", "mallets/marimba_1")
vibra1 = instanciate("chan5", "mallets/vibra_1")
pstrings = instanciate("chan7", "guitars_strings/pstrings_1")
pluckbass = instanciate("chan8", "bass/pluckbass_1")
lone1 = instanciate("chan9", "synth_keys/lonesine_1")
equals = instanciate("chan10", "synth_keys/equals_1")
dakeys = instanciate("chan11", "synth_keys/dakeys_1")
padarp = instanciate("chan12", "synth_keys/padarp_1")
keypong = instanciate("chan13", "synth_keys/keypong_1")
sizzle = instanciate("chan14", "synth_keys/sizzle_1")
wobble = instanciate("chan16", "bass/wobble_1")

Clock.latency = .5
Clock.midi_nudge = -.232 # latency 1024/48000

change_bpm(160)

Scale.default = Pvar([Scale.major, Scale.mixolydian, Scale.minor, Scale.dorian],15*.25)

mx >> mixer([None], sm_mix=.4, vdee_mix=0, ru_blend=0)

g1 >> gone1([0], dur=8, arp=0, pitch=0, oct=3)
g1.fadein(16, fvol=.6)

g1.stereo_routing = linvar([0,1], PRand(8,24), start=Clock.mod(4))
# b1 >> bino1(
#     [None],
#     setup_id=.32,
#     azimuth_slider=linvar([.3,.7],33),
#     elevation_slider=linvar([.2,.8],24),
# )
g1.oscillator_1_unison_voices = 0
g1.oscillator_1_unison_detune = 0
g1.oscillator_1_detune_power = 0
g1.oscillator_2_unison_voices = 0
g1.oscillator_2_unison_detune = 0
g1.oscillator_2_detune_power = 0
g1.oscillator_3_unison_voices = 0
g1.oscillator_3_unison_detune = 0
g1.oscillator_3_detune_power = 0
g1.envelope_1_attack = .5
g1.oscillator_1_pan = linvar([0,.3,1,.4,.8], PRand(4,8))
g1.oscillator_2_pan = linvar([0,.3,1,.4,.8], PRand(8,16))
g1.oscillator_3_pan = linvar([0,.3,1,.4,.8], PRand(4,24))
g1.body=.2
g1.dull=.2

g1.body = linvar([.2,0,1,.4,.8,0,.6],PRand(2,24,seed=2)[:12], start=Clock.mod(4))
g1.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=2)[:12], start=Clock.mod(4))

c1 >> play("c.c.c.cc.", amp=1, dur=1/3, rate=2, room2=1).fadein()
c1.rate=2.5
c2 >> play(".c.c.c.cc", amp=1, dur=1/3, rate=1, room2=1).fadein()
c4 >> play(".c..", amp=1, dur=1/3, rate=.75, room2=1).fadein()
c2.rate=.3
c2.amp=2.22
c3 >> play("c..", amp=1.3, dur=1/3, rate=.5, room2=1).fadein()

c_all.amplify = linvar(P[.4,1,.7,1.3,.6,1.2]*.75, PRand(8,32)[:12], start=Clock.mod(4))
hh >> play("..-.", amp=4, rate=1.5, sample=1, dur=.5)


k2.rate=linvar([.8,1.2],32)
k2.sample = PRand(0,2)
