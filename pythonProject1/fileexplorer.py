from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Explorer")
root.config(background="white")
root.geometry("500x500")


def open():
    file = filedialog.askopenfilename(initialdir='/Desktop',
                                      title="Select a file",
                                      filetypes=(("Text files",
                                                  "*.txt*"),
                                                 ("all files",
                                                  "*.*")))
    label.configure(text="File Opened: " + file)


label = Label(root, text="Open a file\n\n", width=100, height=4,)
label.grid(row=2, column=2)
browse_file = Button(root, text="browse file", command=open)
browse_file.grid(row=5, column=2)
exit = Button(root, text="Exit", command=exit)
exit.grid(row=7, column=2)

root.mainloop()
