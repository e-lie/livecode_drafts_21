import mido
import yaml

with mido.open_input("midii", virtual=True) as in_port:
    for msg in in_port:
        try:
            if msg.type == 'note_off': # on note release
                midi_foxdotcode = None
                with open("midi_foxdotcode_mapping.yaml", "r") as mapping_file:
                    midi_foxdotcode = yaml.safe_load(mapping_file)
                code_string = midi_foxdotcode[f"note{msg.note}"]
                print(f"### {code_string}")
                with open('/tmp/foxdotcode.txt', 'w') as code_file:
                    code_file.write(code_string)
        except KeyError:
            print(f"no code for : {msg}")

    #d1 >> blip(2, oct=6)
