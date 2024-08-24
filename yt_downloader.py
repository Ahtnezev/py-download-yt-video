from pytubefix import YouTube
from pytubefix.cli import on_progress

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Valió verga Tilín")
    print("Al 100 y pasadito!")


link = input("URL del vidio plis: ")
Download(link)

