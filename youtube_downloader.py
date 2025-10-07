import moviepy.editor
import pytubefix as pytube
import pytubefix.streams
import moviepy


subs = pytube.Channel("enter URL")

print(subs.channel_id)

link = pytube.YouTube("https://www.youtube.com/watch?v=x7X9w_GIm1s&ab_channel=Fireship")


#mp4 not working us webm yuck
video = link.streams.filter(subtype = "webm", res ="1080p").first()
sound = link.streams.filter(only_audio=True).first()

video.download()
sound.download()

#final_clip = video.







