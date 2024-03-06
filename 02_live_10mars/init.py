from FoxDot.preset import *
Clock.latency = .5
Clock.midi_nudge = -.232 # latency 2048/48000
#
mixer = instanciate("_mixer", "effects/fxstack_1_off")
duckless = instanciate("_duckless", "effects/kick_fx_1")
#
gone = instanciate("chan1", "pads/gone_1q")
bass303 = instanciate("chan2", "bass/bass303_1q")
apad = instanciate("chan3", "pads/apad_1q")
marimba4 = instanciate("chan4", "mallets/marimba_1q")
vibra1 = instanciate("chan5", "mallets/vibra_1q")
#
pstrings = instanciate("chan7", "guitars_strings/pstrings_1q")
pluckbass = instanciate("chan8", "bass/pluckbass_1q")
lone1 = instanciate("chan9", "synth_keys/lonesine_1q")
equals = instanciate("chan10", "synth_keys/equals_1q")
dakeys = instanciate("chan11", "synth_keys/dakeys_1q")
padarp = instanciate("chan12", "synth_keys/padarp_1q")
keypong = instanciate("chan13", "synth_keys/keypong_1")
sizzle = instanciate("chan14", "synth_keys/sizzle_1")
#
wobble = instanciate("chan16", "bass/wobble_1q")
#  Aliases
gone1 = gone
gone2 = gone
apad3 = apad
wobble3 = wobble
