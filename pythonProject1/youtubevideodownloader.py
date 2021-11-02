from pytube import YouTube


link = input("enter the link : ")
yt = YouTube(link)

print("title : ", yt.title)
print("views : ", yt.views)
print('description : ', yt.description)
print("length : ", yt.length)
print("rating : ", yt.rating)
print("author : ", yt.author)

ys = yt.streams.get_audio_only()
print("downloading")
ys.download()
print("downloaded")

