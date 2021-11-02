from tkinter import *

root = Tk()
root.config(bg='SlateGray3')
root.title("Calculator")

e = Entry(root, bg='white', width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=30, pady=10, )

list_of_numbers = []


def input(number):
    current_val = e.get()
    e.delete(0, END)
    e.insert(0, str(current_val) + str(number))


def cls():
    list_of_numbers.clear()
    e.delete(0, END)


def sum_val():
    num1 = e.get()
    list_of_numbers.append(num1)
    e.delete(0, END)


def equals():
    num1 = e.get()
    list_of_numbers.append(str(num1))
    e.delete(0, END)

    SUM = 0
    for values in list_of_numbers:
        SUM += int(values)

    e.insert(0, SUM)


btn9 = Button(root, text='9', bg='white', padx=30, pady=10, command=lambda: input(9)).grid(row=1, column=0)
btn8 = Button(root, text='8', bg='white', padx=30, pady=10, command=lambda: input(8)).grid(row=1, column=1)
btn7 = Button(root, text='7', bg='white', padx=30, pady=10, command=lambda: input(7)).grid(row=1, column=2)

btn6 = Button(root, text='6', bg='white', padx=30, pady=10, command=lambda: input(6)).grid(row=2, column=0)
btn5 = Button(root, text='5', bg='white', padx=30, pady=10, command=lambda: input(5)).grid(row=2, column=1)
btn4 = Button(root, text='4', bg='white', padx=30, pady=10, command=lambda: input(4)).grid(row=2, column=2)

btn3 = Button(root, text='3', bg='white', padx=30, pady=10, command=lambda: input(3)).grid(row=3, column=0)
btn2 = Button(root, text='2', bg='white', padx=30, pady=10, command=lambda: input(2)).grid(row=3, column=1)
btn1 = Button(root, text='1', bg='white', padx=30, pady=10, command=lambda: input(1)).grid(row=3, column=2)

btn0 = Button(root, text='0', bg='white', width=41, pady=10, command=lambda: input(0)).grid(row=4, column=0,
                                                                                            columnspan=3)

add = Button(root, text='+', bg='white', padx=30, pady=10, command=sum_val).grid(row=5, column=0)
cls = Button(root, text='cls', bg='white', padx=30, pady=10, command=cls).grid(row=5, column=1)
btn_eql = Button(root, text="=",bg='white',padx = 30,  pady=10, command=equals).grid(row=5, column=2)

root.mainloop()
