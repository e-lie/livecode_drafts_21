

change_bpm(110)

from FoxDot.preset import *

sc1 = instanciate("sc1", "effects/kverb1")
sc2 = instanciate("sc2", "effects/kverb1")
external = instanciate("external", "effects/kverb1")
fx11 = instanciate("fx11", "effects/kverb1")
fx12 = instanciate("fx12", "effects/kverb1")
fx21 = instanciate("fx21", "effects/dot8_1")
fx22 = instanciate("fx22", "effects/fxstack_1_off")

gone = instanciate("chan1", "pads/gone_1")
bass303 = instanciate("chan2", "bass/bass303_1")
apad = instanciate("chan3", "pads/apad_1")
marimba1 = instanciate("chan4", "mallets/marimba_1")
marimba2 = instanciate("chan5", "mallets/marimba_1")
sheer = instanciate("chan6", "synth_keys/sheer_1")
pstrings = instanciate("chan7", "guitars_strings/pstrings_1")
pluckbass = instanciate("chan8", "bass/pluckbass_1")
equals = instanciate("chan9", "synth_keys/equals_1")
dakeys = instanciate("chan10", "synth_keys/dakeys_1")
padarp = instanciate("chan11", "synth_keys/padarp_1")
keypong = instanciate("chan12", "synth_keys/keypong_1")
sizzle = instanciate("chan13", "synth_keys/sizzle_1")
wobble = instanciate("chan14", "bass/wobble_1")
reese = instanciate("chan15", "bass/reese_1")

f1 >> fx21(smix=.5)

p1 >> marimba1(
    P[0,1,None,5,None,3,5]+[0,(0,2),0,P*(0,2)],
    oct=P[4,5,5,5,5,5]+var([0,1,2],P[1,2,3,4]/2),
    dur=P[.25],
    # vol=0,
    smix=.05,
    smix1=.2,
    smix2=0,
    # smix=linvar([.2,.8],24),
    # smix1=linvar([.3,.8],17),
    # smix2=linvar([.5,1],16),
)

p1.fadein(24)

p2 >> marimba2(
    [0,0,0,0,0,3],
    oct=(2,8), dur=1,
    # vol=,
    amp=linvar([.6,1],24),
    smix=.05,
    smix1=.2,
    smix2=0,
)

b1 >> blip([0], dur=.5, amp=.6, sus=2)

sc >> sc1([0], smix=linvar([0,1]), smix1=linvar([0,1],7), smix2=linvar([0,1],7))


### Idées de procédés
# variations sur double croches [.22,.25,.28] => bof faut trouver un truc qui marche
# variation sur plusieurs kick layered => en mode gabber mais avec la saturation qui varie selon les layers
# Faire de la percussion notamment le kick avec un synthé
# faire des remix avec loop et stretch
# trouver des trucs qui "sonnent musique algorithmique"
