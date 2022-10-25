from random import choice
from tkinter import Tk, Label, Button
from tkinter import *
import tkinter as tk
import time

#funkcja
def Minutnik(czas):
	
	while czas:
		mins, secs = divmod(czas, 60)
		minutnik = '{:02d}:{:02d}'.format(mins, secs)
		print(minutnik, end="\r")
		time.sleep(1)
		czas -= 1
	
	print('koniec czasu')

'''
czas = input("podaj czas w sekundach: ")
Minutnik(int(czas))
'''
#ekran
aplikacja=tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")

#zmiene
liczba= 0
szerokosc=10 #szerokosc przycisku
lewo=5
srodek=7
prawo=9


aplikacja.columnconfigure(0, minsize=225)
aplikacja.rowconfigure([0, 1], minsize=100)

bg = PhotoImage(file = "/home/ai/Downloads/bgi.png")


label1 = Label( aplikacja, image = bg)
label1.place(x = 0, y = 0)

text_label = Label(aplikacja, font=36, text="Wybierz czas:")
text_label.grid(row=0, column=srodek)

#tu ma byc czas wyswietlany
text_label = Label(aplikacja, font=60, text='00.00.00')
text_label.grid(row=1, column=srodek)

Przycisk1= Button(aplikacja, text="1", font=40, width=szerokosc, height=3)
Przycisk1.grid(row=2, column=lewo)

Przycisk2= Button(aplikacja, text="2", font=40, width=szerokosc, height=3)
Przycisk2.grid(row=2, column=srodek)

Przycisk3= Button(aplikacja, text="3", font=40, width=szerokosc, height=3)
Przycisk3.grid(row=2, column=prawo)

Przycisk4= Button(aplikacja, text="4", font=40, width=szerokosc, height=3)
Przycisk4.grid(row=3, column=lewo)

Przycisk5= Button(aplikacja, text="5", font=40, width=szerokosc, height=3)
Przycisk5.grid(row=3, column=srodek)

Przycisk6= Button(aplikacja, text="6", font=40, width=szerokosc, height=3)
Przycisk6.grid(row=3, column=prawo)

Przycisk7= Button(aplikacja, text="7", font=40, width=szerokosc, height=3)
Przycisk7.grid(row=4, column=lewo)

Przycisk8= Button(aplikacja, text="8", font=40, width=szerokosc, height=3)
Przycisk8.grid(row=4, column=srodek)

Przycisk9= Button(aplikacja, text="9", font=40, width=szerokosc, height=3)
Przycisk9.grid(row=4, column=prawo)

Przycisk00= Button(aplikacja, text="00s", font=40, width=szerokosc, height=3)
Przycisk00.grid(row=5, column=lewo)

Przycisk0= Button(aplikacja, text="0", font=40, width=szerokosc, height=3)
Przycisk0.grid(row=5, column=srodek)

PrzyciskBack= Button(aplikacja, text="del", font=40, width=szerokosc, height=3)
PrzyciskBack.grid(row=5, column=prawo)

aplikacja.mainloop()
