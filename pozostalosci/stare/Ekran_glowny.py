import customtkinter
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
    gtext_label.config(text = string, bg=_from_rgb((555, 555, 555)), fg="white") 
    gtext_label.after(1000, time)

# ekran 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

aplikacja = customtkinter.CTk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
# obraz w tle

#zkladki
tabview_1 = customtkinter.CTkTabview(master=aplikacja, width=200, height=70)
tabview_1.place(x=300,y=100)
tabview_1.add("Produkty")
tabview_1.add("Minutnik")
#zegar 
gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)

#przycisk  do minutnika
przycisk_min = customtkinter.CTkButton(master=aplikacja,text="Minutnik", width=80, height=55)
przycisk_min .place(x=323, y=220)
#przycisk do produkty
przycisk_min = customtkinter.CTkButton(master=aplikacja,text="Produkty", width=80, height=55)
przycisk_min .place(x=405, y=220)
#wyswietlanie na ekran 
time()
aplikacja.mainloop()
