


midi = MidiIn()

# Display midi messages for debug...
midi.print_message(True)

# List midi devices
print(midi.device.get_ports())

# Select midi device with the list index from preceding list
apc = MidiIn(1)

def update_notes_and_velocity():
    var.note = var([apc.get_note()],1)
    var.velocity = var([apc.get_velocity()],1)
    Clock.future(1, update_notes_and_velocity)
update_notes_and_velocity()

f1 >> filthysaw(miditofreq(var.note)+P[10,20,30,10,20], dur=.25, sus=.4, scale=Scale.freq, amp=var.velocity)

# You can kinda control the note playing


from renardo_lib.Scale import miditofreq

def miditofreq(midinote):
    """ Converts a midi number to frequency """
    return 440 * (2 ** ((midinote - 69.0)/12.0))

######################### MIDI

apc.print_message(True)

def update_cc():
    var.lpf = var([apc.get_ctrl(51)], .1)
    Clock.future(.1, update_cc)
update_cc()


bd >> play("V.", lpf=0)
hh >> play(".-", amp=3, lpf=0)
sn >> play("[.o]", lpf=0)

grppp = Group(bd, hh, sn)
grppp.amplify=.2
grppp.hpf = var.lpf * 20

#ça marche pas trop
