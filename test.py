import pygame
import time
import pygame.midi


pygame.midi.init()


for i in range(pygame.midi.get_count()):
    print(pygame.midi.get_device_info(i))


midi_in = pygame.midi.Input(pygame.midi.get_default_input_id())

print("Recording MIDI input. Press Ctrl+C to stop.")

notes = []


try:
    while True:
        if midi_in.poll():
            midi_events = midi_in.read(10)
            for event in midi_events:
                status, note, velocity, _ = event[0]
                timestamp = event[1]
                if status == 144:  # Note On
                    notes.append((note, velocity, timestamp))
                    print(f"Note On: {note}, Velocity: {velocity}, Timestamp: {timestamp}")
                elif status == 128:  # Note Off
                    notes.append((note, 0, timestamp))
                    print(f"Note Off: {note}, Timestamp: {timestamp}")

except KeyboardInterrupt:
    print("Recording has stopped")
    pass



midi_in.close()
pygame.midi.quit()
print("MIDI input closed and Pygame MIDI quit.")


