import moviepy.editor 
from tkinter.filedialog import *

vid = askopenfilename()
vid = moviepy.editor.VideoFileClip(vid)
audio = vid.audio

audio.write_audiofile("extracted_audio.mp3")
print("Extraction Complete")