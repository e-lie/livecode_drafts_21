import mido

in_port = mido.open_input("midii", virtual=True)

def handle_midi_msg():
    print(f"MIDI: {msg}")
    with open('/tmp/foxdotcode.txt', 'w') as code_file:
        code_file.write('d1 >> blip(oct=4)')

in_port.callback = handle_midi_msg
