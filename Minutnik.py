from glob import glob
from tkinter import Label, Button
from tkinter import *
import tkinter as tk
import time
import customtkinter

#funkcja 
# funkcja do koloru tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def Minutnik():
	global liczba
	global czydzialal
	czydzialal = True
	if czydzialal == True:
		if liczba >= 0:
			mins, secs = divmod(liczba, 60)
			minutniktext = '{:02d}:{:02d}'.format(mins, secs)
			liczba -=1
			text_label['text']= minutniktext
			text_label.after (1000,Minutnik)
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
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

aplikacja=customtkinter.CTk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")

#zmiene
liczba= 0
szerokosc=80 #szerokosc przycisku
wys=65
lewo=5
srodek=7
prawo=9
czas=liczba
czydzialal = False

#GUI
aplikacja.columnconfigure(0, minsize=225)
aplikacja.rowconfigure([0, 1], minsize=100)
#tlo



#menu
gtext_label = customtkinter.CTkLabel(aplikacja,text="Wybierz czas:")
gtext_label.place(x = 350, y = 40)

#tu ma byc czas wyswietlany
text_label = Label(aplikacja, font=100, bg=_from_rgb((555, 555, 555)), fg="white",  text=czas)
text_label.place(x = 380, y = 70)

Przycisk1= customtkinter.CTkButton(aplikacja, text="1",width=szerokosc, height=wys, command=lambda: ustawczas(1))
Przycisk1.place(x = 255, y = 200)

Przycisk2= customtkinter.CTkButton(aplikacja, text="2",width=szerokosc, height=wys, command=lambda: ustawczas(2))
Przycisk2.place(x = 350, y = 200)

Przycisk3= customtkinter.CTkButton(aplikacja, text="3",width=szerokosc, height=wys, command=lambda: ustawczas(3))
Przycisk3.place(x = 445, y = 200)

Przycisk4= customtkinter.CTkButton(aplikacja, text="4",width=szerokosc, height=wys, command=lambda: ustawczas(4))
Przycisk4.place(x = 255, y = 270)

Przycisk5= customtkinter.CTkButton(aplikacja, text="5",width=szerokosc, height=wys, command=lambda: ustawczas(5))
Przycisk5.place(x = 350, y = 270)

Przycisk6= customtkinter.CTkButton(aplikacja, text="6",width=szerokosc, height=wys, command=lambda: ustawczas(6))
Przycisk6.place(x = 445, y = 270)

Przycisk7= customtkinter.CTkButton(aplikacja, text="7",width=szerokosc, height=wys, command=lambda: ustawczas(7))
Przycisk7.place(x = 255, y = 340)

Przycisk8= customtkinter.CTkButton(aplikacja, text="8",width=szerokosc, height=wys, command=lambda: ustawczas(8))
Przycisk8.place(x = 350, y = 340)

Przycisk9= customtkinter.CTkButton(aplikacja, text="9",width=szerokosc, height=wys, command=lambda: ustawczas(9))
Przycisk9.place(x = 445, y = 340)

Przycisk00= customtkinter.CTkButton(aplikacja, text="00s",width=szerokosc, height=wys, command=zerozero)
Przycisk00.place(x = 255, y = 410)

Przycisk0= customtkinter.CTkButton(aplikacja, text="0",width=szerokosc, height=wys, command=zero)
Przycisk0.place(x = 350, y = 410)

PrzyciskBack= customtkinter.CTkButton(aplikacja, text="del",width=szerokosc, height=wys, command=liczbadel)
PrzyciskBack.place(x = 445, y = 410)

PMinutnik= customtkinter.CTkButton(aplikacja, text="start",width=szerokosc, height=wys, command=Minutnik)
PMinutnik.place(x = 540, y = 410)

PrzyciskPowrot=customtkinter.CTkButton(aplikacja, text="<-",width=50, height=40)
PrzyciskPowrot.place(x = 0, y = 0)

aplikacja.mainloop()
