from tkinter import *

root = Tk()
root.geometry('400x400')
root.config(bg='SlateGray3')
root.title("Data Flair - AddressBook")
root.resizable(0, 0)

contactlist = [
    ['Parv Maheswari', '0176738493'],
    ['David Sharma', '2684430000'],
    ['Mandish Kabra', '4338354432'],
    ['Prisha Modi', '6834552341'],
    ['Rahul kaushik', '1234852689'],
    ['Johena Shaa', '2119876543'],
]
Name = StringVar()
Number = StringVar()

# create a form
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=HORIZONTAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0])


def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()


def Edit():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()


def View():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def Delete():
    del contactlist[Selected()]
    Select_set()


def Exit():
    root.destroy()


def Reset():
    Name.set('')
    Number.set('')


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()

Label(root, text="Name", bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name).place(x=130, y=20)
Label(root, text="Phone no.", bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number).place(x=130, y=70)

Button(root, text='Add', bg='SlateGray4', command=AddContact).place(x=50, y=110)
Button(root, text='Edit', bg='SlateGray4', command=Edit).place(x=50, y=260)
Button(root, text='Delete', bg='SlateGray4', command=Delete).place(x=50, y=210)
Button(root, text='View', bg='SlateGray4', command=View).place(x=50, y=160)
Button(root, text='Exit', bg='tomato', command=Exit).place(x=300, y=320)
Button(root, text='Reset', bg='SlateGray4', command=Reset).place(x=50, y=310)

root.mainloop()
