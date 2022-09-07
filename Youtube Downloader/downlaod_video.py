from pytube import YouTube

link = input("Enter the link of the video \n")
yt = YouTube(link)

print("Wait ... ")

print("Title: ", yt.title)
print("Thumbnail: ",yt.thumbnail_url)

print("Loading Videos ... ")

video = yt.streams.all()
quality = list(enumerate(video))

for i in quality:
    print(i)

choose_quality = int(input("Choose and enter the index: "))
print("Downloading ... ")
video[choose_quality].download()
print("Download SuccessFull")

