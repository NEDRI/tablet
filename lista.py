from glob import glob
from random import choice
from re import L
from tkinter import Tk, Label, Button
from tkinter import *
import tkinter as tk
import time
from tkinter import ttk
import sqlite3

#funkcja do tła
def _from_rgb(rgb):

    return "#%02x%02x%02x" % rgb 

#baza danych
baza = sqlite3.connect("/home/ai/pliki/bazyd/bazasfa")
dane = baza.execute('''SELECT * FROM Produkt;''').fetchall()
print ("Produkt:","   ","ilosc produktu:")
wiersz1=dane[0]
wiersz2=dane[1]
# nazwa produktu
produkt1 = wiersz1[0]
ilosc1 = wiersz1[1]
#ilosc produktu
produkt2 = wiersz2[0]
ilosc2 = wiersz2[1]
#wypisanie 
print(produkt1,ilosc1)
print(produkt2,ilosc2)

#ekran
aplikacja=tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240,   248,   255)))

#zmiene
a=_from_rgb((240, 248, 255 ))
liczba= 0
szp=10 #szerokosc przycisku
wp=1
#położenie obiektów
l=1
sl=2
sp=5
p=6
'''obraz'''
#obraz= PhotoImage(file= r"D:\\Users\\hjakubowski356\\Desktop\\tak.png")

aplikacja.columnconfigure(0, minsize=120)
aplikacja.rowconfigure([0, 1], minsize=50)

#napis
gtext_label = Label(aplikacja, font=36, text="Witaj w bazie twoich produktów!", bg = a)
gtext_label.place(x=280, y=0)

gtext_label = Label(aplikacja, font=36, text="Ilość produktu:", bg = a)
gtext_label.place(x=240, y=40)

gtext_label = Label(aplikacja, font=36, text="Nazwa produktu:", bg = a)
gtext_label.place(x=60, y=40)

gtext_label = Label(aplikacja, font=36, text="dodaj:", bg = a)
gtext_label.place(x=570, y=40)

gtext_label = Label(aplikacja, font=36, text="usuń:", bg = a)
gtext_label.place(x=650, y=40)

#1
gtext_label = Label(aplikacja, font=36, text="Mleko1", bg = a)
gtext_label.place(x=70, y=80)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=80)

usun=Button(aplikacja, text="+", width=szp, height=wp, bg = a)
usun.place(x=550, y=80)

plus=Button(aplikacja,text="-", width=szp, height=wp, bg = a)
plus.place(x=630, y=80)


#2
gtext_label = Label(aplikacja, font=36, text="Mleko2", bg = a)
gtext_label.place(x=70, y=110)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=110)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=110)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=110)

#3
gtext_label = Label(aplikacja, font=36, text="Mleko3", bg = a)
gtext_label.place(x=70, y=140)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=140)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=140)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=140)

#4
gtext_label = Label(aplikacja, font=36, text="Mleko4", bg = a)
gtext_label.place(x=70, y=170)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=170)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=170)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=170)

#5
gtext_label = Label(aplikacja, font=36, text="Mleko5", bg = a)
gtext_label.place(x=70, y=200)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=200)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=200)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=200)

#6
gtext_label = Label(aplikacja, font=36, text="Mleko6", bg = a)
gtext_label.place(x=70, y=230)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=230)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=230)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=230)

#7
gtext_label = Label(aplikacja, font=36, text="Mleko7", bg = a)
gtext_label.place(x=70, y=260)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=260)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=260)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=260)

#8
gtext_label = Label(aplikacja, font=36, text="Mleko8", bg = a)
gtext_label.place(x=70, y=290)

gtext_label = Label(aplikacja, font=36, text="dostępność:", bg = a)
gtext_label.place(x=250, y=290)

usun=Button(aplikacja, text="-", width=szp, height=wp, bg = a)
usun.place(x=550, y=290)

plus=Button(aplikacja,text="+", width=szp, height=wp, bg = a)
plus.place(x=630, y=290)

dodajnowy=Button(aplikacja, text="dodaj nowy produkt", width=szp, height=wp, bg = a)
dodajnowy.place(x=630, y=320)


aplikacja.mainloop()
