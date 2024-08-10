from tkinter import *
import requests

root = Tk()
root.title("Pokedex by Carlo")

frame = Frame(root)
frame.pack()

def Search_Pokemon(_):
    print('searching')


root.bind('<Return>', Search_Pokemon)

search_bar = Entry(frame, width=41)
search_bar.pack()

root.mainloop()