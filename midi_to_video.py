from synthviz import create_video
from colorsys import hsv_to_rgb
import random

def random_rgb():
    return hsv_to_rgb(
        random.random(), 
        random.uniform(0.6, 1.0), 
        random.uniform(0.6, 0.8))

def write_to_video(source_midi: str, output_file: str):
    create_video(input_midi=source_midi,
                 video_filename=output_file,
                 falling_note_color=random_rgb(),
                 vertical_speed=.5)