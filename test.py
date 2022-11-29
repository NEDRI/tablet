import tkinter as tk
import time
from tkinter import Label, Button
import tkinter as tk
import sqlite3
from tkinter import *
from time import strftime 
import tkinter.ttk as ttk

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

aplikacja = tk.Tk()
aplikacja.title(" SFA ")
aplikacja.geometry('800x480')
aplikacja.configure(bg=_from_rgb((0, 0, 0)))



gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)



tabGeneral = ttk.Notebook(aplikacja)
tab3_info = ttk.Frame(aplikacja)
tabGeneral.add(tab3_info, text='minutnik')
tabGeneral.insert(0, tab3_info, text='Główny') 
tabGeneral.pack(expand=1, fill="both")
tabGeneral.place(x=300, y=450)
def time(): 

    string = strftime('%H:%M:%S') 

    gtext_label.config(text = string, bg="black", fg="white") 

    gtext_label.after(1000, time)

gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)

gtext_label = Label(aplikacja, font= 36)
gtext_label.place(x= 370, y=30)

tab1_log = ttk.Frame(aplikacja)
tabGeneral.add(tab1_log, text='minutnik')

tab2_gra = ttk.Frame(aplikacja)
tabGeneral.add(tab2_gra, text='produkty')


time()
aplikacja.mainloop()