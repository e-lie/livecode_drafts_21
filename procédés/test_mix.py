from FoxDot.preset import *
from functools import partials

sc2 = instanciate("_sc2", "effects/fxstack_1_off")
track2 = partial(loop, output=4)

l1 >> loop("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 146.75, dur=16)

l2 >> track2("/home/elie/Musiqqque/spotdl/feet start dancing EP/WAVs/DJ Manny - Get The Money.wav", 146.75, dur=16)
t2 >> sc2(None)

t2.fadein()





d1 >> playpack1("X-")
