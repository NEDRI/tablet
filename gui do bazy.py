from glob import glob
from random import choice
from re import L
from tkinter import Tk, Label, Button
from tkinter import *
import tkinter as tk
import time

#ekran
aplikacja=tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")

#zmiene
liczba= 0
szp=10 #szerokosc przycisku
wp=1
#położenie obiektów
l=1
sl=2
sp=5
p=6
obraz= PhotoImage(file= r"/home/hj/Downloads/MicrosoftTeams-image.png")

aplikacja.columnconfigure(0, minsize=120)
aplikacja.rowconfigure([0, 1], minsize=50)

gtext_label = Label(aplikacja, font=36, text="Witaj w bazie twoich produktów!")
gtext_label.grid(row=0, column=3)

#1
gtext_label = Label(aplikacja, font=36, image=obraz)
gtext_label.grid(row=1, column=0)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.grid(row=1, column=2)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.grid(row=1, column=sp)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.grid(row=1, column=p)


#2
gtext_label = Label(aplikacja, font=36, text="Mleko")
gtext_label.grid(row=2, column=0)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.grid(row=2, column=2)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.grid(row=2, column=sp)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.grid(row=2, column=p)

aplikacja.mainloop()

