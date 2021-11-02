import datetime
from tkinter import *
from playsound import playsound
import time

root = Tk()
root.geometry("400x200")
root.config(bg="SlateGray3")
root.title("alarm clock")


def current(set_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == set_timer:
            print("Alarm")
            playsound("/Users/ankitpandey/Desktop/python/pythonProject1/1.mp4")
            break


def alarm():
    set_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    current(set_timer)


hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(root, textvariable=hour, bg="white", width=5).place(x=110, y=30)
Entry(root, textvariable=minute, bg="white", width=5).place(x=170, y=30)
Entry(root, textvariable=second, bg="white", width=5).place(x=230, y=30)

btn = Button(root, text="Set alaram", fg="red", width=10, relief="solid", bg="yellow", command=alarm).place(x=140, y=80)

root.mainloop()
