import mido
import csv
import os

def extract_midi_data(midi_path = "test.mid"):
    output_path = os.path.splitext(os.path.basename(midi_path))[0] + ".csv"

    mid = mido.MidiFile(midi_path)#
    # incase the filepath already exists
    # we can ask the user if they want to overwrite it or not
    if (os.path.exists(f"songdata/{output_path}")):
        user_input = input(f"{output_path} already exists. Do you want to overwrite it? (y/n): ")
        if user_input.lower() != 'y':
            os.remove(f"songdata/{output_path}")
        elif user_input.lower() == 'n':
            print("Exiting without overwriting the file.")
            return None

    for track in mid.tracks:
        tick = 0
        for msg in track:
            if msg.type in ["note_on", "note_off"]:
                tick += msg.time
                # we can store note_off as note_on with velocity 0, 
                # we can just check for note_on and note_off just as a extra measure of safety
                if msg.type == "note_on" and msg.velocity > 0:
                    with open(f"songdata/{output_path}", 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([tick, "note_on", msg.note,msg.velocity])
                elif msg.velocity == 0:
                    with open(f"songdata/{output_path}", 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        
                        writer.writerow([tick, "note_off", msg.note,msg.velocity]) #hardcode note type for safety

    print(f"MIDI data extracted and saved to songdata/{output_path}")
    return output_path



extract_midi_data()