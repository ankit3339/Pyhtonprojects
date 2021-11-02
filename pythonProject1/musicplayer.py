from tkinter import *
import os
import pygame


class MusicPlayer:
    def __init__(self, window):
        # creating a window
        self.root = window
        self.root.title("itunes")
        self.root.geometry("1000x200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        # creating first frame
        trackFrame = LabelFrame(self.root, text="song track", fg="white", bg="grey", bd=5,
                                font=("times new roman", 15, "bold"), relief=GROOVE)
        trackFrame.place(x=0, y=0, width=600, height=100)

        Label(trackFrame, textvariable=self.track, fg="gold", bg="grey", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=10, pady=5)
        Label(trackFrame, textvariable=self.status, fg="gold", bg="grey", font=("times new roman", 15, "bold")).grid(
            row=0, column=1, padx=10, pady=5)

        # creating button frame
        btnFrame = LabelFrame(self.root, text="buttons", fg="white", bg="grey", bd=5,
                              font=("times new roman", 15, "bold"), relief=GROOVE)
        btnFrame.place(x=0, y=100, width=600, height=100)
        # Buttons
        Button(btnFrame, command=self.playsound, text="PLAY", fg="black", bg="grey", width=6, height=1,
               font=("times new roman", 15, "bold"),
               relief=GROOVE).grid(row=0, column=0, padx=10, pady=5)
        Button(btnFrame, command=self.pause, text="PAUSE", fg="black", bg="grey", width=6, height=1,
               font=("times new roman", 15, "bold"),
               relief=GROOVE).grid(row=0, column=1, padx=10, pady=5)
        Button(btnFrame, command=self.unpause, text="UNPASUE", fg="black", bg="grey", width=10, height=1,
               font=("times new roman", 15, "bold"),
               relief=GROOVE).grid(row=0, column=2, padx=10, pady=5)
        Button(btnFrame, command=self.stop, text="STOP", fg="black", bg="grey", width=6, height=1,
               font=("times new roman", 15, "bold"),
               relief=GROOVE).grid(row=0, column=3, padx=10, pady=5)

        # right side portion
        listFrame = LabelFrame(self.root, text="List of Songs", fg="white", bg="grey", bd=5,
                               font=("times new roman", 15, "bold"), relief=GROOVE)
        listFrame.place(x=600, y=0, width=400, height=200)
        scroll_y = Scrollbar(listFrame, orient=VERTICAL)
        self.playlist = Listbox(listFrame, yscrollcommand=scroll_y.set, selectmode=SINGLE, fg="navyblue", bg="silver",
                                bd=5,
                                font=("times new roman", 15, "bold"), relief=GROOVE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config()
        self.playlist.pack(fill=BOTH)

        os.chdir("/Users/ankitpandey/Desktop/music/Download/")
        songtrack = os.listdir()
        for track in songtrack:
            self.playlist.insert(END, track)

        # button functions

    def playsound(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def pause(self):
        self.status.set("_Pause")
        pygame.mixer.music.pause()

    def unpause(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

    def stop(self):
        self.status.set("-Stop")
        pygame.mixer.music.stop()


root = Tk()
MusicPlayer(root)
root.mainloop()
