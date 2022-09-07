from pytube import Playlist

link = Playlist(input("Enter the link of the playlist \n"))

print(f'Downloading ... : {link.title} \n ', "Loading ....")


for video in link.videos:
    print("Loading...")
    print(list(enumerate(video.streams.all())))
    index = input("Choose and enter the index: ")
    video[index].download()
    print("Succesfull Download, Next...")

print("All videos downloaded")