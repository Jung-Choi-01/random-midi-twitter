import os
from synthviz import create_video

# possible future todo's
# - randomize colors

def write_to_video(source_midi: str, output_file: str):
    create_video(input_midi=source_midi,
                 video_filename=output_file,
                 falling_note_color=[255, 255, 255],
                 vertical_speed=1)