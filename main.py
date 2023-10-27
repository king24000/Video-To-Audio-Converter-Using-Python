#pip install  MoviePy
#python code to convert video to audio
import moviepy.editor as mp 
#inser video file
clip = mp.VideoFileClip(r"j.mp4")
#insert audio file path
clip.audio.write_audiofile(r"audio.mp3")