# from pytube import YouTube
#
#
# video = YouTube('https://www.youtube.com/watch?v=RX3Xenjc-GE')
#
# print("-------title------")
# print(video.title)
#
# print("----thumbnails---")
# print(video.thumbnail_url)
#
# my_video = video.streams.get_highest_resolution()
# print("downloading")
# my_video.download()
# print("download complete")


# -----seperate video to audio

import moviepy.editor

video = moviepy.editor.VideoFileClip("Odhani Odh Ke Nachu Lyrical Video Song  Tere Naam  Salman Khan Bhoomika Chawla.mp4")
audio = video.audio
audio.write_audiofile("1.mp3")