import time
import sys
from tkinter import Tk, Label, Button
from tkinter import ttk, Button
import tkinter as tk
import sqlite3
from tkinter import *
import platform
from time import strftime 

# funkcja do tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def time(): 

    string = strftime('%H:%M:%S') 

    gtext_label.config(text = string, bg="black", fg="white") 

    gtext_label.after(1000, time)

'''
def zegar():
    while True:
        from datetime import datetime
        now = datetime.now()
        gtext_label = Label(aplikacja, font= 36, text= "%s:%s:%s" % (now.hour,now.minute,now.second))
        gtext_label.place(x= 370, y=30)
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
'''

aplikacja = tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240, 248, 255)))

bg= PhotoImage(file="/home/ai/Downloads/tlomenu.png")

label1= Label(aplikacja, image = bg)
label1.place(x=0, y=0)

gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)

Przycisk_minutnik=Button(aplikacja, text="Minutnik", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_minutnik.place(x=300, y=200)

Przycisk_baza=Button(aplikacja, text="produkty", bg="black", fg="white", font=36, width=7, height=2)
Przycisk_baza.place(x=400, y=200)

time()
aplikacja.mainloop()

