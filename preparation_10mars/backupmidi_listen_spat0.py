import mido
import time
from threading import Thread

def midi_callback():
    with open('/tmp/foxdotcode.txt', 'w') as code_file:
        code_file.write('d1 >> blip(oct=4)')
        print("chouette")

def midi_input_listener():
    rtmidi = mido.Backend('mido.backends.rtmidi')
    with rtmidi.open_input("MIDIdlewareIN", virtual=True) as in_port:
        print(f"Écoute des entrées MIDI...")
        for msg in in_port:
            print(f"Message MIDI reçu: {msg}")
        # in_port.callback = midi_callback

listener_thread = Thread(target=midi_input_listener) #args=(function,args)
listener_thread.daemon = True
listener_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quitting midi listener")
