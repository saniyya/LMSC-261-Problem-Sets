# Problem 3.2


MIDI_number = int(input("Enter a MIDI note number between 0-127: "))
freq = 440*2**((MIDI_number-69)/12)

print(f"The frequency of the MIDI note number {MIDI_number} is {freq} Hz.")
