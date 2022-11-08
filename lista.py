from glob import glob
from random import choice
from re import L
from tkinter import Tk, Label, Button
from tkinter import *
import tkinter as tk
import time
from tkinter import ttk

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
#obraz= PhotoImage(file= r"/home/hj/Downloads/MicrosoftTeams-image(1).png")

aplikacja.columnconfigure(0, minsize=120)
aplikacja.rowconfigure([0, 1], minsize=50)

#napis
gtext_label = Label(aplikacja, font=36, text="Witaj w bazie twoich produktów!")
gtext_label.place(x=280, y=0)

#1
gtext_label = Label(aplikacja, font=36, text="Mleko1")
gtext_label.place(x=70, y=80)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=80)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=80)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=80)


#2
gtext_label = Label(aplikacja, font=36, text="Mleko2")
gtext_label.place(x=70, y=110)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=110)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=110)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=110)

#3
gtext_label = Label(aplikacja, font=36, text="Mleko3")
gtext_label.place(x=70, y=140)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=140)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=140)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=140)

#4
gtext_label = Label(aplikacja, font=36, text="Mleko4")
gtext_label.place(x=70, y=170)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=170)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=170)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=170)

#5
gtext_label = Label(aplikacja, font=36, text="Mleko5")
gtext_label.place(x=70, y=200)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=200)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=200)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=200)

#6
gtext_label = Label(aplikacja, font=36, text="Mleko6")
gtext_label.place(x=70, y=230)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=230)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=230)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=230)

#7
gtext_label = Label(aplikacja, font=36, text="Mleko7")
gtext_label.place(x=70, y=260)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=260)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=260)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=260)

#8
gtext_label = Label(aplikacja, font=36, text="Mleko8")
gtext_label.place(x=70, y=290)

gtext_label = Label(aplikacja, font=36, text="dostępność:")
gtext_label.place(x=250, y=290)

usun=Button(aplikacja, text="-", width=szp, height=wp)
usun.place(x=550, y=290)

plus=Button(aplikacja,text="+", width=szp, height=wp)
plus.place(x=630, y=290)


aplikacja.mainloop()
