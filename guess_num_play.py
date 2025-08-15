from tkinter import *
import random
win=Tk()
win.title('guess the number')
win.geometry('800x500')
sc=random.randrange(1,100)
print(sc)
def guess():
    a=int(entry.get())
    if a==sc:
        label.config(text='you win')
    elif a<sc:
        label.config(text='guess higher')
    else:
        label.config(text='guess lower')



label=Label(master=win, text='enter num')
label.pack()

entry=Entry(master=win)
entry.pack()

button=Button(master=win, text='check answer', command=guess)
button.pack()

win.mainloop()
