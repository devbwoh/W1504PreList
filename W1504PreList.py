from tkinter import *
from os import path
from glob import glob
from tkinter import messagebox

win = Tk()

win.title('파일 리스트')
win.geometry('250x200')

win.columnconfigure(0, weight=1)
win.columnconfigure(1)
win.rowconfigure(0, weight=1)

files = [f for f in glob('./*')]

listbox = Listbox()
listbox.grid(column=0, row=0,
    sticky=N+E+W+S)

scrollbar = Scrollbar()
scrollbar.grid(column=1, row=0,
    sticky=N+S)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

for file in files:
    listbox.insert('end', path.basename(file))

def onDoubleClick(e):
    global listbox, files, canvas
    index = listbox.curselection()[0]
    if (path.isdir(files[index])):
        listbox.delete(0, END)
        
        files = [f for f in glob(f'{files[index]}/*')]
        for file in files:
            listbox.insert('end', path.basename(file))
    else:
        messagebox.showinfo('File', files[index])

listbox.bind('<Double-Button>', onDoubleClick)

win.mainloop()