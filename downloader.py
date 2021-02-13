from pytube import YouTube
from tkinter.filedialog import askdirectory
from moviepy.editor import VideoFileClip
from os import remove

download_method = input("Vyber metodu stahování:\n1:mp4\n2:mp3\n3:mp3+mp4\n")

print("Vlož link:")
link = input()

yt = YouTube(link)


result = yt.streams.get_highest_resolution()



dr = askdirectory()

result.download(dr)
if download_method in ("2","3"):
    mp4 = "%s.mp4" % (dr + f"/{yt.title}")
    mp3 = "%s.mp3" % (dr + f"/{yt.title}")


    audio = VideoFileClip(mp4).audio
    audio.write_audiofile(mp3)
    if download_method =="2":
        remove(mp4)

print("Staženo")
