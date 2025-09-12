from tkinter import *
import random
from tkinter.ttk import Combobox

win = Tk()
win.title('Guess the Word')
win.geometry('800x500')

word = ''
guess = []


def choose_word(e):
    global word, guess
    fruits = ['apple', 'peach', 'orange', 'coconut']
    color = ['yellow', 'green', 'gray', 'black']

    if combo.get() == 'color':
        word = random.choice(color)
    elif combo.get() == 'fruits':
        word = random.choice(fruits)
    
    guess = ['-'] * len(word)
    show_word()
    label2.config(text='You can start guessing!')


def show_word():
    label.config(text=' '.join(guess))


def check_letter():
    global guess
    letter = entry.get().lower()
    entry.delete(0, END)

    if not word:
        label2.config(text='Please select a category first!')
        return

    if len(letter) != 1:
        label2.config(text='Please enter just one letter.')
        return

    if letter in word.lower():
        for i in range(len(word)):
            if word[i].lower() == letter:
                guess[i] = word[i]  
        show_word()
        label2.config(text=f'Great guess! "{letter}" is in the word.')
    else:
        label2.config(text=f'Wrong guess! "{letter}" is not in the word.')

    if '-' not in guess:
        label2.config(text=f'You win! The word was "{word}"')


mylist = ['color', 'fruits']
combo = Combobox(win, values=mylist)
combo.pack()
combo.set('Select a category')
combo.bind('<<ComboboxSelected>>', choose_word)


label = Label(win, text='')
label.pack()

entry = Entry(win)
entry.pack()

label2 = Label(win, text=' ')
label2.pack()

button = Button(win, text='Check', command=check_letter)
button.pack()

win.mainloop()
