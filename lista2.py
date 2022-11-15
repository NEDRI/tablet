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

#zmiene
a=_from_rgb((240, 248, 255 ))
# liczba= 0
szp=7 #szerokosc przycisku
wp=1
#położenie obiektów
# l=1
# sl=2
# sp=5
# p=6
# '''obraz'''
#obraz= PhotoImage(file= r"D:\\Users\\hjakubowski356\\Desktop\\tak.png")
#baza danych
bazasfa="/home/ai/pliki/bazyd/bazasfa"

def zwieksz(nazwa_produktu):
    usun_widok()
    print("zwiekszam +1", nazwa_produktu)
    baza = sqlite3.connect(bazasfa)
    baza.execute("UPDATE Produkt SET iloscp = iloscp + 1 WHERE produkt ='" + nazwa_produktu + "'")
    baza.commit()
    zbuduj_widok()

def zmniejsz(nazwa_produktu, ilosc):
    if ilosc > 0:
        usun_widok()
        print("zmniejszam -1", nazwa_produktu)
        baza = sqlite3.connect(bazasfa)
        baza.execute("UPDATE Produkt SET iloscp = iloscp - 1 WHERE produkt ='" + nazwa_produktu + "'")
        baza.commit()
        zbuduj_widok()


def usun_widok():
    lista_elementow = aplikacja.winfo_children()
    print(lista_elementow)
    for x in lista_elementow:
        x.destroy()

def zbuduj_widok():
    baza = sqlite3.connect(bazasfa)
    dane = baza.execute('''SELECT * FROM Produkt;''').fetchall()
    print("Dane z bazy", dane)
    for x in dane:
        print("linia: ", x)
    #napis menu
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
    #lista z bazy
    poz_x_produkt=70
    poz_x_ilosc=250
    poz_x_plus=550
    poz_x_minus=630
    poz_y_poczatek=80
    poz_y_krok=30
    poz_y=1
    elementy=[]
    for wiersz_z_bazy in dane:
        print("wiersz_z_bazy: ",wiersz_z_bazy)
        produkt=wiersz_z_bazy[0]
        ilosc=wiersz_z_bazy[1]
        print("poz: ", poz_y, "produkt: ", produkt, "ilosc: ",ilosc)
        gtext_label = Label(aplikacja, font=36, text=produkt, bg=a)
        gtext_label.place(x=poz_x_produkt, y=(poz_y * poz_y_krok) + poz_y_poczatek)
        gtext_label = Label(aplikacja, font=36, text=ilosc, bg=a)
        gtext_label.place(x=poz_x_ilosc, y=(poz_y * poz_y_krok) + poz_y_poczatek)
        plus = Button(aplikacja, text="+", width=szp, height=wp, bg = a, command=lambda p=produkt: zwieksz(p))
        plus.place(x=poz_x_plus, y=(poz_y*poz_y_krok)+poz_y_poczatek)
        minus=Button(aplikacja,text="-", width=szp, height=wp, bg = a, command=lambda p=produkt, i=ilosc: zmniejsz(p,i))
        minus.place(x=poz_x_minus, y=(poz_y*poz_y_krok)+poz_y_poczatek)
        poz_y = poz_y + 1


#ekran
aplikacja=tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240,   248,   255)))

aplikacja.columnconfigure(0, minsize=120)
aplikacja.rowconfigure([0, 1], minsize=50)

zbuduj_widok()

aplikacja.mainloop()

