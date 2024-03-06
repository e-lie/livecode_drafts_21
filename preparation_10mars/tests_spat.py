from FoxDot.preset import *
Clock.latency = .5
Clock.midi_nudge = -.220 # latency 2048/48000
Clock.midi_nudge = -.232 # latency 2048/48000
# mixer = instanciate("_mixer", "spat/stereooctocube")
# mixer = instanciate("_mixer", "spat/eq3octocube")
mixer = instanciate("_spat", "spat/eq3s10m")
gone = instanciate("chan1", "pads/gone_1")
vibra = instanciate("chan2", "mallets/vibra_1")

d1 >> blip([0,2], dur=.5, sus=2, amp=.2)

@player_method
def fadep(self, param_name, fvalue=1, dur=8, ivalue=None):
    if ivalue == None:
        ivalue = float(self.__getattr__(param_name))
    self.__setattr__(param_name, linvar([ivalue, fvalue], [dur, inf], start=Clock.mod(4)))
    @nextBar(dur+1)
    def static_final_value():
        self.__setattr__(param_name, fvalue)
    return self


v1 >> vibra([0,2,0,3,1], dur=[.5,.25])


v1.on=0
v1.vibra_on=1

##### stereooctocube

mx.fadep("eq3s10m_in_1_x", fvalue=1)
mx.fadep("eq3s10m_in_1_y", fvalue=.5)
mx.fadep("eq3s10m_in_1_z", fvalue=1)

x_diff_1 = (xvar([0,360],[16,0])/2+1)/2
y_diff_1 = (yvar([0,360],[16,0])/2+1)/2
z_diff_1 = linvar([0,1],16)
x_diff_2 = (xvar([0,360],[32,0])/2+1)/2
y_diff_2 = (yvar([0,360],[32,0])/2+1)/2
z_diff_2 = linvar([0,1],32)
mx >> mixer(
    [None],
    eq3s10m_in_1_x=x_diff_1,
    eq3s10m_in_1_y=y_diff_1,
    eq3s10m_in_1_z=z_diff_1,
    eq3s10m_in_2_x=x_diff_2,
    eq3s10m_in_2_y=y_diff_2,
    eq3s10m_in_2_z=z_diff_2,
)

mx >> mixer(
    [None],
    eq3s10m_in_1_x=linvar([0,1], 13),
    eq3s10m_in_1_y=linvar([0,1], 7),
    eq3s10m_in_1_z=linvar([0,1], 17),
)


######### eq3octocube

hspeed = .3
hsdiff = 1
mspeed = .5
msdiff = .3
lspeed = .3
lsdiff = 1

x_diff_1_highs = (xvar([0,360],[16/hspeed-hsdiff,0])/2+1)/2
y_diff_1_highs = (yvar([0,360],[16/hspeed-hsdiff,0])/2+1)/2
z_diff_1_highs = linvar([0,1],16/hspeed-hsdiff)
x_diff_2_highs = (xvar([0,360],[16/hspeed+hsdiff,0])/2+1)/2
y_diff_2_highs = (yvar([0,360],[16/hspeed+hsdiff,0])/2+1)/2
z_diff_2_highs = linvar([0,1],16/hspeed+hsdiff)

x_diff_1_mids = (xvar([0,360],[16/mspeed-msdiff,0])/2+1)/2
y_diff_1_mids = (yvar([0,360],[16/mspeed-msdiff,0])/2+1)/2
z_diff_1_mids = linvar([0,1],16/mspeed-msdiff)
x_diff_2_mids = (xvar([0,360],[16/mspeed+msdiff,0])/2+1)/2
y_diff_2_mids = (yvar([0,360],[16/mspeed+msdiff,0])/2+1)/2
z_diff_2_mids = linvar([0,1],16/mspeed+msdiff)

x_diff_1_lows = (xvar([0,360],[16/lspeed-lsdiff,0])/2+1)/2
y_diff_1_lows = (yvar([0,360],[16/lspeed-lsdiff,0])/2+1)/2
z_diff_1_lows = linvar([0,1],16/lspeed-lsdiff)
x_diff_2_lows = (xvar([0,360],[16/lspeed+lsdiff,0])/2+1)/2
y_diff_2_lows = (yvar([0,360],[16/lspeed+lsdiff,0])/2+1)/2
z_diff_2_lows = linvar([0,1],16/lspeed+lsdiff)

d1 >> blip(amp=.2, oct=(4,5,6))

mx >> mixer(
    [None],
    eq3s10m_in_1_x=x_diff_1_highs,
    eq3s10m_in_1_y=y_diff_1_highs,
    eq3s10m_in_1_z=z_diff_1_highs,
    eq3s10m_in_2_x=x_diff_2_highs,
    eq3s10m_in_2_y=x_diff_2_highs,
    eq3s10m_in_2_z=z_diff_2_highs,
    eq3s10m_in_3_x=x_diff_1_mids,
    eq3s10m_in_3_y=y_diff_1_mids,
    eq3s10m_in_3_z=z_diff_1_mids,
    eq3s10m_in_4_x=x_diff_2_mids,
    eq3s10m_in_4_y=y_diff_2_mids,
    eq3s10m_in_4_z=z_diff_2_mids,
    eq3s10m_in_5_x=x_diff_1_lows,
    eq3s10m_in_5_y=y_diff_1_lows,
    eq3s10m_in_5_z=z_diff_1_lows,
    eq3s10m_in_6_x=x_diff_2_lows,
    eq3s10m_in_6_y=y_diff_2_lows,
    eq3s10m_in_6_z=z_diff_2_lows,
)

####### interpolations

x1h = 0
y1h = 0
z1h = 0
x2h = 0
y2h = 0
z2h = 0
x1m = 0
y1m = 0
z1m = 0
x2m = 0
y2m = 0
z2m = 0
x1l = 0
y1l = 0
z1l = 0
x2l = 0
y2l = 0
z2l = 0

mx.eq3s10m_in_1_divergence = 0

divergence_dur = 8

mx.fadep("eq3s10m_in_2_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_1_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_3_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_4_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_5_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_6_divergence", dur=divergence_dur, fvalue=0)
mx.fadep("eq3s10m_in_1_gain", dur=divergence_dur, fvalue=.25)
mx.fadep("eq3s10m_in_2_gain", dur=divergence_dur, fvalue=.25)
mx.fadep("eq3s10m_in_3_gain", dur=divergence_dur, fvalue=.25)
mx.fadep("eq3s10m_in_4_gain", dur=divergence_dur, fvalue=.25)
mx.fadep("eq3s10m_in_5_gain", dur=divergence_dur, fvalue=.25)
mx.fadep("eq3s10m_in_6_gain", dur=divergence_dur, fvalue=.25)

mx.fadep("eq3s10m_in_2_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_1_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_3_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_4_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_5_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_6_divergence", dur=divergence_dur, fvalue=1)
mx.fadep("eq3s10m_in_1_gain", dur=divergence_dur, fvalue=.6)
mx.fadep("eq3s10m_in_2_gain", dur=divergence_dur, fvalue=.6)
mx.fadep("eq3s10m_in_3_gain", dur=divergence_dur, fvalue=.6)
mx.fadep("eq3s10m_in_4_gain", dur=divergence_dur, fvalue=.6)
mx.fadep("eq3s10m_in_5_gain", dur=divergence_dur, fvalue=.6)
mx.fadep("eq3s10m_in_6_gain", dur=divergence_dur, fvalue=.6)

value1 = random()
value2 = random()
value3 = random()
value4 = random()
value5 = random()
value6 = random()
mx.fadep("eq3s10m_in_2_divergence", dur=divergence_dur, fvalue=value1)
mx.fadep("eq3s10m_in_1_divergence", dur=divergence_dur, fvalue=value2)
mx.fadep("eq3s10m_in_3_divergence", dur=divergence_dur, fvalue=value3)
mx.fadep("eq3s10m_in_4_divergence", dur=divergence_dur, fvalue=value4)
mx.fadep("eq3s10m_in_5_divergence", dur=divergence_dur, fvalue=value5)
mx.fadep("eq3s10m_in_6_divergence", dur=divergence_dur, fvalue=value6)
mx.fadep("eq3s10m_in_1_gain", dur=divergence_dur, fvalue=.25+(value1*.35))
mx.fadep("eq3s10m_in_2_gain", dur=divergence_dur, fvalue=.25+(value2*.35))
mx.fadep("eq3s10m_in_3_gain", dur=divergence_dur, fvalue=.25+(value3*.35))
mx.fadep("eq3s10m_in_4_gain", dur=divergence_dur, fvalue=.25+(value4*.35))
mx.fadep("eq3s10m_in_5_gain", dur=divergence_dur, fvalue=.25+(value5*.35))
mx.fadep("eq3s10m_in_6_gain", dur=divergence_dur, fvalue=.25+(value6*.35))

mx >> mixer(
    [None],
    eq3s10m_in_1_x=x1h,
    eq3s10m_in_1_y=y1h,
    eq3s10m_in_1_z=z1h,
    eq3s10m_in_2_x=x2h,
    eq3s10m_in_2_y=x2h,
    eq3s10m_in_2_z=z2h,
    eq3s10m_in_3_x=x1m,
    eq3s10m_in_3_y=y1m,
    eq3s10m_in_3_z=z1m,
    eq3s10m_in_4_x=x2m,
    eq3s10m_in_4_y=y2m,
    eq3s10m_in_4_z=z2m,
    eq3s10m_in_5_x=x1l,
    eq3s10m_in_5_y=y1l,
    eq3s10m_in_5_z=z1l,
    eq3s10m_in_6_x=x2l,
    eq3s10m_in_6_y=y2l,
    eq3s10m_in_6_z=z2l,
)

from random import random

transi_dur = 16

mx.fadep("eq3s10m_in_1_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_1_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_1_z", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_2_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_2_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_2_z", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_3_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_3_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_3_z", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_4_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_4_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_4_z", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_5_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_5_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_5_z", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_6_x", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_6_y", dur=transi_dur, fvalue=random())
mx.fadep("eq3s10m_in_6_z", dur=transi_dur, fvalue=random())
