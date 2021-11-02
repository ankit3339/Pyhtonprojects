from tkinter import *
import sys
import random
from timeit import default_timer as timer

root = Tk()
root.geometry("400x200")
root.title('typeSala')


def game():
    # root.destroy()

    def check_result():

        if entry.get() == word:
            end = timer()

            print(end - start)
            game()
        else:
            print("wrong input")
            game()

    words = ['programming', 'coding', 'algorithm',
             'systems', 'python', 'software']
    word = random.choice(words)

    start = timer()
    frame = Tk()
    frame.geometry("400x200")
    frame.title('typeSala')

    x2 = Label(frame, text=word, font="times 20")
    x2.place(x=150, y=10)

    x3 = Label(frame, text="Start Typing", font="times 20")
    x3.place(x=10, y=50)

    entry = Entry(frame)
    entry.place(x=200, y=55)

    b2 = Button(frame, text="Done",
                command=check_result, width=12, bg='grey')
    b2.place(x=150, y=100)

    b3 = Button(frame, text="Try Again",
                command=game, width=12, bg='grey')
    b3.place(x=250, y=100)
    frame.mainloop()


def Exit():
    sys.exit()


Label(root, text='Welcome to TypeSala').place(x=100, y=0)
Label(root, text="click on GO to play\nand EXIT to exit").place(x=10, y=115)

goBtn = Button(root, text='GO', fg='green', relief="solid", width=10, font="Times 14 bold", command=game).place(x=200,
                                                                                                                y=100)
exitBtn = Button(root, text='EXIT', fg='red', relief="solid", width=10, font="Times 14 bold", command=Exit).place(x=200,
                                                                                                                  y=150)
root.mainloop()
