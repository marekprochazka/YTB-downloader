from pytube import YouTube
from tkinter.filedialog import askdirectory

print("Vlož link:")
link = input()

yt = YouTube(link)


result = yt.streams.get_highest_resolution()

dr = askdirectory()

result.download(dr)

print("Staženo")
