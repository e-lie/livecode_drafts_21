kick1 = Player()
pad1 = Player()
pad2 = Player()
lonesynth = Player()
pads = Group(pad1, pad2)
wbass = Player()

change_bpm(110)

pad1 >> gone1([0], dur=8, arp=0, pitch=0, oct=3)
pad1.fadein(16, fvol=.8)
pad1.oscillator_1_unison_voices = 0
pad1.oscillator_1_unison_detune = 0
pad1.oscillator_1_detune_power = 0
pad1.oscillator_2_unison_voices = 0
pad1.oscillator_2_unison_detune = 0
pad1.oscillator_2_detune_power = 0
pad1.oscillator_3_unison_voices = 0
pad1.oscillator_3_unison_detune = 0
pad1.oscillator_3_detune_power = 0
pad1.envelope_1_attack = .5
pad1.body=.2
pad1.dull=.2
pad1.span(srot(32), linvar([.2,.8],24))

pad1.body = linvar([0,1,.4,.8,0,.6],PRand(2,24,seed=2)[:12], start=Clock.mod(4))
pad1.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=2)[:12], start=Clock.mod(4))

# pad2 >> apad3(
pad2 >> apad3(
    [0],
    dur=8,
    sus=7.5,
    oct=4,
)
pad2.attack=.8
pad2.space=0
pad2.detail=0
pad2.thick_thin=0
# z3 >> bino3(
    # [None],
# ).span(srot(48), linvar([0,.7,0,.4],64, start=Clock.mod(4)))
pad2.fadein(16, fvol=.8)
pad2.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
pad2.span(srot(16), .2)

pad1.fade(16, fvol=.6)
pad2.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))

pad1.vol = 0.75*linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))

pad1.degree = 4

pad1.oct = (2,3)

pad1.fade(24,fvol=.4)
pad2.fade(24,fvol=.4)

pad1.oct = (2,3,6)

pad1.fade(24,fvol=.8)
pad2.fade(12,fvol=.8)

pad2.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))
pad1.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=2)[:12], start=Clock.mod(4))

pad1.oscillator_1_unison_voices = .1
pad1.oscillator_1_unison_detune = .1
pad1.oscillator_1_detune_power = .5

pad1.oscillator_1_unison_detune = .5

pad1.oscillator_1_unison_voices = .8

pad1.degree = (0,4)

pad1.oscillator_2_unison_voices = 0
pad1.oscillator_2_unison_detune = 0
pad1.oscillator_2_detune_power = 0

pad1.oscillator_2_unison_voices = .5
pad1.oscillator_3_unison_voices = .5

pad1.oscillator_2_unison_voices = 1
pad1.oscillator_3_unison_voices = 1
pad1.oscillator_3_unison_detune = .5
pad1.oscillator_3_detune_power = .5

pad1.oscillator_1_pan = linvar([0,1])
pad1.oscillator_2_pan = linvar([0,1],7)
pad1.oscillator_3_pan = linvar([0,1],5)

pad1.dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

pad1.degree = (0,4,-2)

pad1.fade(12,.4)
pad2.fade(12,.4)

pad1.vol=.4
pad2.vol=.4

pad1.fade(24,.8)
pad2.fade(12,.8)

pad1.vol=.8
pad2.vol=.8

pad2.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))
pad1.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=2)[:12], start=Clock.mod(4))

pad1.filter_fx_cutoff=1

pad1.filter_fx_resonance=.2

pad1.filter_fx_switch=1

pad1.filter_fx_cutoff=linvar([1,.6],[8,64,64,64], start=Clock.mod(4))
pad1.oct=(3,4)

pad1.pitch = 0
pad1.arp = 0

pad1.oscillator_1_unison_voices = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
pad1.oscillator_1_detune_power = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
pad1.oscillator_2_unison_voices = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
pad1.oscillator_2_detune_power = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

# g2 >> gone2([0], dur=4, body=0, arp=0, pitch=0, oct=3)
# g2.fadein(16, fvol=.8)
# b2 >> bino2(
#     [None],
#     azimuth_slider=linvar([.3,.7],27),
#     elevation_slider=linvar([.2,.8],32),
# )
# g2.dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
# g2.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
# g2.oct=(5,6)

tt >> play('{-...}', dur=.125, rate=linvar([10,20],16)).mpan(PWhite(0,1))
tt.fadein(fvol=2)

tt.degree = '{-..-}'
tt.dur=var([1,.5,.25,.125], PRand(1,16))
tt.amplify = linvar([.2,.7,.3,1], PRand(4,16))

Scale.default = Scale.minor

lonesynth >> lone1([0], oct=7, dur=[1,2,3], vol=.7)

lonesynth.degree = [0,2,None,-2, None]
lonesynth.delay_mix = 0
lonesynth.reverb_mix = 0
lonesynth.oct=7
lonesynth.fadein(fvol=1)

lonesynth.dur=3

lonesynth.oct=([6,7,8],[3,4,2,3])

lonesynth.dur=1

lonesynth >> lone1([[0,None,0,None],4,[None,5],1], oct=([6,7,8],[3,4,2,3]), dur=.25, vol=.7)
lonesynth.voices = linvar([0,1],32)
lonesynth.vol=1.3

kick1 >> play(
    "<{V.}x><v>",
    output=12,
    lpf=800,
    hpf=100,
    amp=linvar([.5,1,.4,1],PRand(8,32)),
    amplify=var([0,1],2),
    rate=PWhite(1.5,3)
)
kick1.mpan(mrot(4))
hh >> play("{[--]-.}", amp=3, rate=3, dur=.25).mpan(mrot(16))

tt.fadeout()

l1.fadeout()

hh.fadeout()

# g2.vol = linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))
lonesynth.fade(16, fvol=.7)

wbass >> wobble3([0], oct=3, dur=24, fm_tone=0)
wbass.fadein(24,fvol=.6)

pad1.fade(16, fvol=.6)
pad2.fade(16, fvol=.6)

# g2.oct= (2,3,4)

wbass.vol = 0.75*linvar([.8,1,.7,1.3,.6,1.2], PRand(8,32,seed=3)[:12], start=Clock.mod(4))

kick1.fadeout(16)

wbass.fm_tone=linvar([0,.3],16, start=Clock.mod(4))

## attendre que ce soit en bas
wbass.fm_tone=linvar([0,.4],[32,inf], start=Clock.mod(4))

wbass.cutoff=linvar([0,.8],[16], start=Clock.mod(4))

tt.fade(16, .7)

wbass.fade(16, fvol=1)

wbass.fm_tone=linvar([.4,0],PRand(1,4), start=Clock.mod(4))

wbass.fm_tone=linvar([.3,0],[32,inf], start=Clock.mod(4))

pad1.fadeout(24)
# g2.fadeout(24)
pad2.fadeout(24)

wbass.fadeout(32)

kick1.fadeout(16)
tt.fadeout()

lonesynth.fadeout(16)
