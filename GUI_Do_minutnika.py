from random import choice
from tkinter import Tk, Label, Button
from tkinter import *
import tkinter as tk

aplikacja=tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")

a=10
lewo=5
srodek=7
prawo=9

text_label = Label(aplikacja, font=36, text="Wybierz czas:")
text_label.grid(row=0, column=srodek)


aplikacja.columnconfigure(0, minsize=225)
aplikacja.rowconfigure([0, 1], minsize=100)

Przycisk1= Button(aplikacja, text="1", font=40, width=a, height=3)
Przycisk1.grid(row=2, column=lewo)


Przycisk2= Button(aplikacja, text="2", font=40, width=a, height=3)
Przycisk2.grid(row=2, column=srodek)


Przycisk3= Button(aplikacja, text="3", font=40, width=a, height=3)
Przycisk3.grid(row=2, column=prawo)

Przycisk4= Button(aplikacja, text="4", font=40, width=a, height=3)
Przycisk4.grid(row=3, column=lewo)

Przycisk5= Button(aplikacja, text="5", font=40, width=a, height=3)
Przycisk5.grid(row=3, column=srodek)

Przycisk6= Button(aplikacja, text="6", font=40, width=a, height=3)
Przycisk6.grid(row=3, column=prawo)

Przycisk7= Button(aplikacja, text="7", font=40, width=a, height=3)
Przycisk7.grid(row=4, column=lewo)

Przycisk8= Button(aplikacja, text="8", font=40, width=a, height=3)
Przycisk8.grid(row=4, column=srodek)

Przycisk9= Button(aplikacja, text="9", font=40, width=a, height=3)
Przycisk9.grid(row=4, column=prawo)

Przycisk00= Button(aplikacja, text="00s", font=40, width=a, height=3)
Przycisk00.grid(row=5, column=lewo)

Przycisk0= Button(aplikacja, text="0", font=40, width=a, height=3)
Przycisk0.grid(row=5, column=srodek)

PrzyciskBack= Button(aplikacja, text="del", font=40, width=a, height=3)
PrzyciskBack.grid(row=5, column=prawo)



aplikacja.mainloop()