from musicpy import *
import random

# possible future todo's
# 1. implement proper note durations for their interval
# - implement swing
# - implement multiple octaves
# - implement different instruments

tonics = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']
tonalities = ['major', 'minor']
melody_length = 30
bpm_range = [80, 200]
# note_range = [str(degree) for degree in range(1, 8)] + [str(degree) + ".1" for degree in range(1,8)] # two octaves
note_range = range(1,8)
note_lengths = [1/16, 1/8, 1/4, 1/2]

def random_melody():
    scale = S(f"{random.choice(tonics)} {random.choice(tonalities)}")
    C1 = chord(notes=[scale[random.choice(note_range)] for _ in range(melody_length)],
               interval=random.choices(note_lengths, k=melody_length))

    return piece(tracks=[C1],
        instruments=['Acoustic Grand Piano'],
        bpm=random.randrange(bpm_range[0], bpm_range[1]),
        start_times=[.5],
        track_names=['piano'],
        channels=[0])

def write_random_melody_to_file(output_path: str):
    write(random_melody(), name=output_path)