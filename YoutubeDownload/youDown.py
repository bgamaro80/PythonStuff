from pathlib import Path
from pytube import YouTube, Stream
import humanize
from moviepy.editor import *
from sys import argv

def videoResolutionScore(video):
    if not video.includes_video_track or "audio" in video.mime_type:
        return -1
    
    return video.bitrate
    
def on_progress(stream: Stream, chunk, bytes_remaining):
    percent = (stream.filesize - bytes_remaining) * 100 /  stream.filesize
    print (f"{int(percent)}%\tRemaining: {humanize.naturalsize( bytes_remaining )}", end = "\r")
        
def on_complete(stream: Stream, file_path):
    print(f"{stream.title} - {file_path} complete.")
    
#link = argv[1]
link = "https://www.youtube.com/watch?v=GgyQufB1Yic"
yt = YouTube(link)

yt.register_on_progress_callback(on_progress)
yt.register_on_complete_callback(on_complete)

print(f"Title: {yt.title}\nAuthor: {yt.author}")

allVideo = yt.streams.all()

bestVideo = max(allVideo, key=videoResolutionScore)
# bestVideo = yt.streams.get_highest_resolution()
print("Size: ", humanize.naturalsize( bestVideo.filesize ))

bestVideoFile = bestVideo.download(filename_prefix="video_", output_path="temp", )

audio = yt.streams.get_audio_only()
audioFile = audio.download(filename_prefix="audio_", output_path="temp")

# #Cargamos el fichero .mp4
# videoclip = VideoFileClip(bestVideoFile)
# audioclip = AudioFileClip(audioFile)

# new_audioclip = CompositeAudioClip([audioclip])
# videoclip.audio = new_audioclip
# videoclip.write_videofile(f"temp/new_{Path(bestVideoFile).stem}.mp4")

# #Lo escribimos como audio y `.mp3`
# #clip.audio.write_audiofile("transformado_a.mp3")