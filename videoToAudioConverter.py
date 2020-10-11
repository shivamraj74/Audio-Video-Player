import moviepy.editor as mp
clip=mp.VideoFileClip(r'sample.mp4')
clip.audio.write_audiofile(r'sample-1.mp3')
