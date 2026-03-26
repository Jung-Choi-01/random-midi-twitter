import midi_generation
import midi_to_video
import os
import shutil

# set up folders
root = os.path.dirname(__file__)
tmp_dir = os.path.join(root, "tmp")
shutil.rmtree(tmp_dir, ignore_errors=True)
os.makedirs(tmp_dir, exist_ok=True)

# make media
midi_path = os.path.join(tmp_dir, "output.mid")
video_path = os.path.join(root, "output.mp4")
midi_generation.write_random_melody_to_file(midi_path)
midi_to_video.write_to_video(source_midi=midi_path, output_file=video_path)

# cleanup
video_frames_dir = os.path.join(root, "video_frames")
output_audio_flie = os.path.join(root, "output.wav")
shutil.rmtree(video_frames_dir, ignore_errors=True)
shutil.rmtree(tmp_dir, ignore_errors=True)
os.remove(output_audio_flie)