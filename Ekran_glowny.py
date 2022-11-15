from tkinter import Tk, Label, Button
from tkinter import ttk, Button
import tkinter as tk
import sqlite3
from tkinter import *

# funkcja do tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

aplikacja = tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240, 248, 255)))

bg= PhotoImage(file="/home/hj/Downloads/tło.png")

label1= Label(aplikacja, image = bg)
label1.place(x=0, y=0)

gtext_label = Label(aplikacja, font= 36, text= "zegar")
gtext_label.place(x= 370, y=30)

Przycisk_minutnik=Button(aplikacja, text="Minutnik", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_minutnik.place(x=300, y=200)

Przycisk_baza=Button(aplikacja, text="produkty", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_baza.place(x=400, y=200)
aplikacja.mainloop()
