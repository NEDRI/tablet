import time
from tkinter import Label, Button
import tkinter as tk
import sqlite3
from tkinter import *
from time import strftime 

# funkcja do koloru tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
# wyswietlanie czasu
def time(): 

    string = strftime('%H:%M:%S') 

    gtext_label.config(text = string, bg="black", fg="white") 

    gtext_label.after(1000, time)

# ekran 
aplikacja = tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240, 248, 255)))
# obraz w tle
bg= PhotoImage(file="/home/hj/programowanie/SFA/grafiki/tło_głowne")
# tlo wyswietlanie 
label1= Label(aplikacja, image = bg)
label1.place(x=0, y=0)
#zegar 
gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)
#przycisk  do minutnika
Przycisk_minutnik=Button(aplikacja, text="Minutnik", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_minutnik.place(x=300, y=200)
#przycisk do produkty
Przycisk_baza=Button(aplikacja, text="produkty", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_baza.place(x=400, y=200)
#wyswietlanie na ekran 
time()
aplikacja.mainloop()
