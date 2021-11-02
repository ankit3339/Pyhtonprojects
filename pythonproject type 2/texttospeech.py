from gtts import gTTS
from tkinter import *
from playsound import playsound

root = Tk()

root.geometry("400x400")
msg = StringVar()
entry = Entry(root, textvariable=msg, width='50')
entry.place(x=10, y=10)


def text_to_speech():
    message = entry.get()
    speech = gTTS(text=message)
    speech.save("message.mp3")
    playsound("message.mp3")


Button(root, command=text_to_speech, text="play").place(x=25, y=50)
root.mainloop()
