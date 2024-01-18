from tkinter import *
from game import jatek
def click():
    jatek('Kő!')

def click2():
    jatek('Papír!')

def click3():
    jatek('Olló!')

def gui_exit():
    exit("Szelya!")
def open_gui():
    window.eval('tk::PlaceWindow . center')
    window.mainloop()

window = Tk()
window.title("Rock,Paper,Scissors")
gomb1 = Button(window)
gomb1.config(command=click)
kep = PhotoImage(file="rock.png")
gomb1.config(image=kep)
gomb1.grid(row=0, column=0, padx=10, pady=10)

gomb2 = Button(window)
gomb2.config(command=click2)
kep1 = PhotoImage(file="paper.png")
gomb2.config(image=kep1)
gomb2.grid(row=0, column=1, padx=10, pady=10)

gomb3 = Button(window)
gomb3.config(command=click3)
kep2 = PhotoImage(file="scissors.png")
gomb3.config(image=kep2)
gomb3.grid(row=0, column=2, padx=10, pady=10)

gomb_e = Button(window, text='Exit')
gomb_e.config(command=gui_exit)
gomb_e.grid(row=1, column=1, padx=10, pady=10)
window.resizable(False, False)
open_gui()
