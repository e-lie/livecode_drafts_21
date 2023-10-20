# Jouer avec les effets de delay aussi
# repetitions
# synchro entre rythme synthé et percu
# jeu de synchro désynchro
# revenir entre la techno et le broken !!
change_bpm(120)

Scale.default = Scale.minor

Root.default = 0

si >> keypong([0,2,12,17,8,17], oct=var([4,5,3,4],6), amp=var([1,.8,.8,0],6), dur=1)

k5 >> play("V.", amp=1.3, output=12, lpf=700)

si.dur = var([1,.25], [24,8])

si.dur = Pvar([
      .25,
      1/3,
      [.25,.25,.125,.125],
      [1],
    ],15*.25*3, start=Clock.mod(15*.25))

si.chorus = linvar([1,0], [15*.25,1,3])

si.oct = Pvar([(3,4),[3,6,3,5]],15*.25*4, start=Clock.mod(15*.25)),

dd >> play("X([XXXXXXXX].V[VVV])", output=12, amp=2)

e3.fadeout(64)

si >> keypong(
    Pvar(
        [[0],[1,17],[0,2,12,17,8,17]],
        15*.25*4,
        start=Clock.mod(15*.25)
    ),
    dur=Pvar([
      .25,
      1/3,
      [.25,.25,.125,.125],
      [1],
    ],15*.25*3, start=Clock.mod(15*.25)),
    fx=linvar([1,0], 15*.25),
    chorus=linvar([1,0], [15*.25,1,3]),
    # time=linvar([1,0], [15*.25,1,3]),
    # timbre=linvar([1,0], [15*.25,1,3]),
    vol=2,
    oct=Pvar([(3,4),[3,6,3,5]],15*.25*4, start=Clock.mod(15*.25)),
    amp=1,
    # amplify=var([1,0,0], [15*.25*2,0,15*.25*2], start=Clock.mod(15*.25)),
    amplify=1,
    root=Pvar([0,P[0,4,5].stutter(5),PTri(12)], 15*.25*4, start=Clock.mod(15*.25)),
    scale=Pvar([Scale.major, Scale.minor, Scale.chromatic], 15*.25*4, start=Clock.mod(15*.25)),
)

si.sfadeout(32)

dd >> play(
    Pvar(
        ["v", "c[++]c[.V]", "X[XXXXX]."],
        15*.25*4,
        start=Clock.mod15*.25)
    ),
    output=12,
    dur=Pvar([
      .25,
      1/3,
      [.25,.25,.125,.125],
      [1],
    ],15*.25*3, start=Clock.mod(15*.25)),
    # fx=linvar([1,0], 15*.25, start=Clock.mod(15*.25)),
    # reverb=linvar([1,0], [15*.25,1,3], start=Clock.mod(15*.25)),
    # time=linvar([1,0], [15*.25,1,3]),
    # timbre=linvar([1,0], [15*.25,1,3]),
    oct=Pvar([(3,4),[3,6,3,5]],15*.25*4, start=Clock.mod(15*.25)),
    amp=2,
    amplify=var([1,0,0], [15*.25*2,0,15*.25*2], start=Clock.mod(15*.25)),
    root=Pvar([0,P[0,4,5].stutter(5),PTri(12)], 15*.25*4, start=Clock.mod(15*.25)),
    scale=Pvar([Scale.major, Scale.minor, Scale.chromatic], 15*.25*4, start=Clock.mod(15*.25)),
)

si >> sizzle(
    Pvar([
      [0],
      [1,17],
      [0,2,12,17,8,17],
    ],
    15*.25*4,
    start=Clock.mod(15*.25)
    ),
    dur=Pvar([
      .25,
      1/3,
      [.25,.25,.125,.125],
      [1],
    ],15*.25*3, start=Clock.mod(15*.25)),
    fx=linvar([1,0], 15*.25, start=Clock.mod(15*.25)),
    reverb=linvar([1,0], [15*.25,1,3], start=Clock.mod(15*.25)),
    # time=linvar([1,0], [15*.25,1,3]),
    # timbre=linvar([1,0], [15*.25,1,3]),
    vol=2,
    oct=Pvar([(3,4),[3,6,3,5]],15*.25*4, start=Clock.mod(15*.25)),
    amp=1,
    amplify=1
    # amplify=var([1,0,0], [15*.25*2,0,15*.25*2], start=Clock.mod(15*.25)),
    root=Pvar([0,P[0,4,5].stutter(5),PTri(12)], 15*.25*4, start=Clock.mod(15*.25)),
    scale=Pvar([Scale.major, Scale.minor, Scale.chromatic], 15*.25*4, start=Clock.mod(15*.25)),
)

k1.fadeout(48)

dd >> play(
    Pvar(
        ["v", "c[++]c[.V]", "X[XXXXX]."],
        15*.25*4,
        start=Clock.mod(15*.25)
    ),
    output=12,
    dur=Pvar([
      .25,
      1/3,
      [.25,.25,.125,.125],
      [1],
    ],15*.25*3, start=Clock.mod(15*.25)),
    # fx=linvar([1,0], 15*.25, start=Clock.mod(15*.25)),
    # reverb=linvar([1,0], [15*.25,1,3], start=Clock.mod(15*.25)),
    # time=linvar([1,0], [15*.25,1,3]),
    # timbre=linvar([1,0], [15*.25,1,3]),
    oct=Pvar([(3,4),[3,6,3,5]],15*.25*4, start=Clock.mod(15*.25)),
    amp=2,
    # amplify=var([1,0,0], [15*.25*2,0,15*.25*2], start=Clock.mod(15*.25)),
    amplify=1,
    root=Pvar([0,P[0,4,5].stutter(5),PTri(12)], 15*.25*4, start=Clock.mod(15*.25)),
    scale=Pvar([Scale.major, Scale.minor, Scale.chromatic], 15*.25*4, start=Clock.mod(15*.25)),
)

Group(dd, si).sfadeout(32)
