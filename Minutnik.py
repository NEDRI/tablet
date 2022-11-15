from distutils.cmd import Command
from glob import glob
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
		global liczba
		text_label['text']= liczba
	
	print('koniec czasu')

def Minutnik2():
	global liczba
	global czydzialal
	czydzialal = True
	if czydzialal == True:
		if liczba >= 0:
			mins, secs = divmod(liczba, 60)
			minutniktext = '{:02d}:{:02d}'.format(mins, secs)
			liczba -=1
			text_label['text']= minutniktext
			text_label.after (1000,Minutnik2)
		else:
			czydzialal=False
			liczba = 0
	


def ustawczas(t):
	global liczba
	liczba+=t
	print(liczba)
	mins, secs = divmod(liczba, 60)
	minutniktext = '{:02d}:{:02d}'.format(mins, secs)
	text_label['text']= minutniktext

def zero():
	global liczba
	liczba = liczba * 10
	print(liczba)
	mins, secs = divmod(liczba, 60)
	minutniktext = '{:02d}:{:02d}'.format(mins, secs)
	text_label['text']= minutniktext

def zerozero():
	global liczba
	liczba = liczba * 60
	print(liczba)
	mins, secs = divmod(liczba, 60)
	minutniktext = '{:02d}:{:02d}'.format(mins, secs)
	text_label['text']= minutniktext

def liczbadel():
	global liczba
	liczba = 0
	print(liczba)
	mins, secs = divmod(liczba, 60)
	minutniktext = '{:02d}:{:02d}'.format(mins, secs)
	text_label['text']= minutniktext


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
czas=liczba
czydzialal = False

aplikacja.columnconfigure(0, minsize=225)
aplikacja.rowconfigure([0, 1], minsize=100)

'''obraz w tle'''
#bg = PhotoImage(file = "/home/ai/Downloads/bgi.png")

#label1 = Label( aplikacja, image = bg)
#label1.place(x = 0, y = 0)

gtext_label = Label(aplikacja, font=36, text="Wybierz czas:")
gtext_label.grid(row=0, column=srodek)

#tu ma byc czas wyswietlany
text_label = Label(aplikacja, font=60, text=czas)
text_label.grid(row=1, column=srodek)

Przycisk1= Button(aplikacja, text="1", font=40, width=szerokosc, height=3, command=lambda: ustawczas(1))
Przycisk1.grid(row=2, column=lewo)

Przycisk2= Button(aplikacja, text="2", font=40, width=szerokosc, height=3, command=lambda: ustawczas(2))
Przycisk2.grid(row=2, column=srodek)

Przycisk3= Button(aplikacja, text="3", font=40, width=szerokosc, height=3, command=lambda: ustawczas(3))
Przycisk3.grid(row=2, column=prawo)

Przycisk4= Button(aplikacja, text="4", font=40, width=szerokosc, height=3, command=lambda: ustawczas(4))
Przycisk4.grid(row=3, column=lewo)

Przycisk5= Button(aplikacja, text="5", font=40, width=szerokosc, height=3, command=lambda: ustawczas(5))
Przycisk5.grid(row=3, column=srodek)

Przycisk6= Button(aplikacja, text="6", font=40, width=szerokosc, height=3, command=lambda: ustawczas(6))
Przycisk6.grid(row=3, column=prawo)

Przycisk7= Button(aplikacja, text="7", font=40, width=szerokosc, height=3, command=lambda: ustawczas(7))
Przycisk7.grid(row=4, column=lewo)

Przycisk8= Button(aplikacja, text="8", font=40, width=szerokosc, height=3, command=lambda: ustawczas(8))
Przycisk8.grid(row=4, column=srodek)

Przycisk9= Button(aplikacja, text="9", font=40, width=szerokosc, height=3, command=lambda: ustawczas(9))
Przycisk9.grid(row=4, column=prawo)

Przycisk00= Button(aplikacja, text="00s", font=40, width=szerokosc, height=3, command=zerozero)
Przycisk00.grid(row=5, column=lewo)

Przycisk0= Button(aplikacja, text="0", font=40, width=szerokosc, height=3, command=zero)
Przycisk0.grid(row=5, column=srodek)

PrzyciskBack= Button(aplikacja, text="del", font=40, width=szerokosc, height=3, command=liczbadel)
PrzyciskBack.grid(row=5, column=prawo)

PMinutnik= Button(aplikacja, text="start", font=40, width=szerokosc, height=3, command=Minutnik2)
PMinutnik.grid(row=5, column=10)

aplikacja.mainloop()
