import customtkinter
import tkinter as tk
from customtkinter import *
from tkinter import *
from time import strftime
from tkinter import ttk
import sqlite3

import time

def stronaglowna_do_minutnik():
    global app2
    print("stronaglowna_do_minutnik destroy")
    app1.destroy()
    app2 = None
    app2 = customtkinter.CTkFrame(root, width=800, height=480)
    app2_pokaz(app2)

def stronaglowna_do_produkty():
    global drzewo
    print("stronaglowna_do_produkty destroy")
    app1.destroy()
    app3_pokaz(root)

def minutnik_do_stronaglowna(text_label):
    global app1
    global liczba_tekst
    global liczba
    global czydziala
    global zegar_zadanie
    print("minutnik_do_stronaglowna destroy")
    if czydziala == True:
        text_label.after_cancel(zegar_zadanie)
    czydziala = False
    liczba_tekst = ''
    liczba = 0
    app2.destroy()
    app1 = None
    app1 = customtkinter.CTkFrame(root, width=800, height=480)
    app1_pokaz(app1)

def produkty_do_stronaglowna():
    global app1
    print("produkty_do_stronaglowna destroy")
    drzewo.destroy()
    przycisk_plus.destroy()
    przycisk_minus.destroy()
    przycisk_usun.destroy()
    przycisk_odswiez.destroy()
    przycisk_dodajprodukt.destroy()
    wpis.destroy()
    przycisk_dodaj.destroy()
    przycisk_Powrot.destroy()
    app1 = None
    app1 = customtkinter.CTkFrame(root, width=800, height=480)
    app1_pokaz(app1)

# funkcja do koloru tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

#APP1--------------------------------------------EKRAN GLOWNY
def app1_zegar(tekst):
    aktualnyczas = strftime('%H:%M:%S')
    print(aktualnyczas)
    tekst.config(text = aktualnyczas, bg=_from_rgb((555, 555, 555)), fg="white")
    tekst.after(1000, lambda: app1_zegar(tekst))

def app1_pokaz(ramka):
    zegar_label = Label(ramka, font=36)
    zegar_label.place(x=370, y=30)
    przycisk_1 = customtkinter.CTkButton(ramka, text="Minutnik", width=80, height=55, command=stronaglowna_do_minutnik)
    przycisk_1.place(x=323, y=220)
    przycisk_2 = customtkinter.CTkButton(ramka, text="Produkty", width=80, height=55, command=stronaglowna_do_produkty)
    przycisk_2.place(x=405, y=220)
    app1_zegar(zegar_label)
    ramka.pack()

#APP2--------------------------------------------MINUTNIK
liczba = None
liczba_tekst = ''
czydziala = False
zegar_zadanie = None

def czas_na_sekundy(czas):
    total_seconds = 0
    print(czas)
    try:
        v = czas[-1]
        total_seconds += int(v)
    except:
        pass
    try:
        v = czas[-2]
        total_seconds += 10*int(v)
    except:
        pass
    try:
        v = czas[-4:-2]
        total_seconds += 60*int(v)
    except:
        pass
    try:
        v = czas[:-4]
        total_seconds += 60*60*int(v)
    except:
        pass
    print('total total_seconds=',total_seconds)
    return total_seconds

def minutnik(text_label):
    global liczba_tekst
    global liczba
    global czydziala
    global zegar_zadanie
    print("minutnik nacisniety")
    if czydziala == False:
        if liczba > 0:
            print("minutnik odpalam")
            czydziala = True
            start_minutnik(text_label)
    elif czydziala == True:
        print("minutnik koncze")
        czydziala = False
        text_label.after_cancel(zegar_zadanie)

def start_minutnik(text_label):
    global liczba_tekst
    global liczba
    global czydziala
    global zegar_zadanie
    print("start minutnik")
    if czydziala == True:
        if liczba >= 0:
            print("start minutnik petla")
            mins, secs = divmod(liczba, 60)
            minutniktext = '{:02d}:{:02d}'.format(mins, secs)
            liczba -=1
            text_label['text']= minutniktext
            zegar_zadanie = text_label.after (1000,start_minutnik, text_label)
        else:
            print("start minutnik na False")
            czydziala=False
            text_label.after_cancel(zegar_zadanie)
            liczba = 0
            liczba_tekst = ''

def ustawczas(t,text_label):
    global liczba_tekst
    global liczba
    global czydziala
    if not czydziala:
        if len(liczba_tekst)<4:
            print(liczba_tekst)
            liczba_tekst += t
            print(liczba_tekst)
            liczba = czas_na_sekundy(liczba_tekst)
            
            #sposob1
            # mins, secs = divmod(liczba, 60)
            # minutniktext = '{:02d}:{:02d}'.format(mins, secs)
            # text_label['text']= minutniktext
            
            
            #sposob2 x3x2:x1x0
            liczba_tekst_odwrocony=liczba_tekst[::-1]
            print(liczba_tekst_odwrocony)
            try:
                x0=liczba_tekst_odwrocony[0]
            except:
                x0="0"
            try:
                x1=liczba_tekst_odwrocony[1]
            except:
                x1="0"
            try:
                x2=liczba_tekst_odwrocony[2]
            except:
                x2="0"
            try:
                x3=liczba_tekst_odwrocony[3]
            except:
                x3="0"
            print(x3,x2,x1,x0)
            liczba_tekst_wyswietl=x3+x2+":"+x1+x0
            print(liczba_tekst_wyswietl)
            text_label['text']= liczba_tekst_wyswietl

def liczbadel(text_label):
    global liczba_tekst
    global liczba
    global czydziala
    global zegar_zadanie
    if czydziala == True:
        text_label.after_cancel(zegar_zadanie)
    czydziala = False
    liczba_tekst = ''
    liczba = 0
    print(liczba_tekst)
    print(liczba)
    mins, secs = divmod(liczba, 60)
    minutniktext = '{:02d}:{:02d}'.format(mins, secs)
    text_label['text']= minutniktext

def app2_pokaz(ramka):
    # zmiene
    global liczba
    global czydziala
    liczba = 0
    szerokosc = 80  # szerokosc przycisku
    wys = 65
    lewo = 5
    srodek = 7
    prawo = 9
    czas = liczba
    czydzialal = False
    # GUI
    # ramka.pack()
    ramka.columnconfigure(0, minsize=225)
    ramka.rowconfigure([0, 1], minsize=100)
    # menu
    gtext_label = customtkinter.CTkLabel(ramka, text="Wybierz czas:")
    gtext_label.place(x=350, y=40)
    # tu ma byc czas wyswietlany
    text_label = Label(ramka, font=100, bg=_from_rgb((555, 555, 555)), fg="white", text=czas)
    text_label.place(x=380, y=70)
    Przycisk1 = customtkinter.CTkButton(ramka, text="1", width=szerokosc, height=wys, command=lambda: ustawczas('1',text_label))
    Przycisk1.place(x=255, y=200)
    Przycisk2 = customtkinter.CTkButton(ramka, text="2", width=szerokosc, height=wys, command=lambda: ustawczas('2',text_label))
    Przycisk2.place(x=350, y=200)
    Przycisk3 = customtkinter.CTkButton(ramka, text="3", width=szerokosc, height=wys, command=lambda: ustawczas('3',text_label))
    Przycisk3.place(x=445, y=200)
    Przycisk4 = customtkinter.CTkButton(ramka, text="4", width=szerokosc, height=wys, command=lambda: ustawczas('4',text_label))
    Przycisk4.place(x=255, y=270)
    Przycisk5 = customtkinter.CTkButton(ramka, text="5", width=szerokosc, height=wys, command=lambda: ustawczas('5',text_label))
    Przycisk5.place(x=350, y=270)
    Przycisk6 = customtkinter.CTkButton(ramka, text="6", width=szerokosc, height=wys, command=lambda: ustawczas('6',text_label))
    Przycisk6.place(x=445, y=270)
    Przycisk7 = customtkinter.CTkButton(ramka, text="7", width=szerokosc, height=wys, command=lambda: ustawczas('7',text_label))
    Przycisk7.place(x=255, y=340)
    Przycisk8 = customtkinter.CTkButton(ramka, text="8", width=szerokosc, height=wys, command=lambda: ustawczas('8',text_label))
    Przycisk8.place(x=350, y=340)
    Przycisk9 = customtkinter.CTkButton(ramka, text="9", width=szerokosc, height=wys, command=lambda: ustawczas('9',text_label))
    Przycisk9.place(x=445, y=340)
    Przycisk00 = customtkinter.CTkButton(ramka, text="00s", width=szerokosc, height=wys, command=lambda: ustawczas('00',text_label))
    Przycisk00.place(x=255, y=410)
    Przycisk0 = customtkinter.CTkButton(ramka, text="0", width=szerokosc, height=wys, command=lambda: ustawczas('0',text_label))
    Przycisk0.place(x=350, y=410)
    PrzyciskBack = customtkinter.CTkButton(ramka, text="del", width=szerokosc, height=wys, command=lambda: liczbadel(text_label))
    PrzyciskBack.place(x=445, y=410)
    PMinutnik = customtkinter.CTkButton(ramka, text="start", width=szerokosc, height=wys, command=lambda: minutnik(text_label))
    PMinutnik.place(x=540, y=410)
    PrzyciskPowrot = customtkinter.CTkButton(ramka, text="<-", width=50, height=40, command=lambda: minutnik_do_stronaglowna(text_label))
    PrzyciskPowrot.place(x=0, y=0)
    ramka.pack()


#APP3--------------------------------------------BAZA DANYCH
bazasfa="bazasfa"
drzewo = None
przycisk_plus = None
przycisk_minus = None
przycisk_usun = None
przycisk_odswiez = None
przycisk_dodajprodukt = None
wpis = None
przycisk_dodaj = None
przycisk_Powrot = None

def napisz():
    wpisdobazy = wpis.get()
    print(wpisdobazy)

def zaladujdane():
    baza = sqlite3.connect(bazasfa)
    dane = baza.execute("SELECT * FROM Produkt;").fetchall()
    print("Dane z bazy: ", dane)
    drzewo.delete(*drzewo.get_children())
    for wiersz_z_bazy in dane:
        print("wrzucam wiersz_z_bazy: ", wiersz_z_bazy)
        drzewo.insert("", tk.END, values=wiersz_z_bazy)

def dodawanie():
    wpisdobazy = wpis.get()
    print (wpisdobazy)
    baza = sqlite3.connect(bazasfa)
    print("insert into Produkt values ("+ wpisdobazy +",1);")
    baza.execute('insert into Produkt values ("'+ wpisdobazy +'",1);')
    baza.commit()
    zaladujdane()
    x = False
    for x in drzewo.get_children():
        if drzewo.item(x,"values")[0] == wpisdobazy:
            break
    if x:
        drzewo.selection_set(x)


def usunwpis():
    wybrany_wiersz = drzewo.selection()[0]
    wybrany_wiersz_bazy =  drzewo.item(wybrany_wiersz,"values")[0]
    print("usuwany wiersz w bazie: ",drzewo.item(wybrany_wiersz,"values")[0])
    drzewo.delete(wybrany_wiersz)
    baza = sqlite3.connect(bazasfa)
    print("DELETE FROM Produkt WHERE produkt='" + wybrany_wiersz_bazy + "';")
    baza.execute("DELETE FROM Produkt WHERE produkt='" + wybrany_wiersz_bazy + "'")
    baza.commit()

def zwieksz():
    wybrany_wiersz = drzewo.selection()[0]
    print(drzewo.item(drzewo.selection()))
    wybrany_wiersz_bazy =  drzewo.item(wybrany_wiersz,"values")[0]
    print("zwiekszany wiersz w bazie: ",drzewo.item(wybrany_wiersz,"values")[0])
    baza = sqlite3.connect(bazasfa)
    baza.execute("UPDATE Produkt SET iloscp = iloscp + 1 WHERE produkt ='" + wybrany_wiersz_bazy + "'")
    baza.commit()
    zaladujdane()
    print(drzewo.get_children())
    x = False
    for x in drzewo.get_children():
        if drzewo.item(x,"values")[0] == wybrany_wiersz_bazy:
            print(x)
            break
    if x:
        drzewo.selection_set(x)

def zmniejsz():
    wybrany_wiersz = drzewo.selection()[0]
    wybrany_wiersz_bazy =  drzewo.item(wybrany_wiersz,"values")[0]
    print("zmniejszany wiersz w bazie: ",drzewo.item(wybrany_wiersz,"values")[0])
    print("aktualna wartosc: ",drzewo.item(wybrany_wiersz,"values")[1])
    if (int(drzewo.item(wybrany_wiersz,"values")[1])) > 0:
        baza = sqlite3.connect(bazasfa)
        baza.execute("UPDATE Produkt SET iloscp = iloscp - 1 WHERE produkt ='" + wybrany_wiersz_bazy + "'")
        baza.commit()
    zaladujdane()
    x = False
    for x in drzewo.get_children():
        if drzewo.item(x,"values")[0] == wybrany_wiersz_bazy:
            print(x)
            break
    if x:
        drzewo.selection_set(x)

def app3_pokaz(ramka):
    global drzewo
    global przycisk_plus
    global przycisk_minus
    global przycisk_usun
    global przycisk_odswiez
    global przycisk_dodajprodukt
    global wpis
    global przycisk_dodaj
    global przycisk_Powrot
    drzewo = None
    przycisk_plus = None
    przycisk_minus = None
    przycisk_usun = None
    przycisk_odswiez = None
    przycisk_dodajprodukt = None
    wpis = None
    przycisk_dodaj = None
    przycisk_Powrot = None
    drzewo = ttk.Treeview(ramka, columns=("kolumna1", "kolumna2"), show="headings", selectmode="browse")
    drzewo.heading("#1", text="Nazwa produktu")
    drzewo.heading("#2", text="Ilość produktu")
    ttk.Style().configure("Treeview", background="black", foreground="white", fieldbackground="dark")

    sb = Scrollbar(orient=VERTICAL)

    drzewo.config(yscrollcommand=sb.set)
    sb.config(command=drzewo.yview)

    drzewo.pack()

    przycisk_plus = customtkinter.CTkButton(master=ramka, text="+", command=zwieksz, width=35, height=30)
    przycisk_plus.place(x=280, y=285)
    przycisk_minus = customtkinter.CTkButton(master=ramka, text="-", command=zmniejsz, width=35, height=30)
    przycisk_minus.place(x=315, y=285)
    przycisk_usun = customtkinter.CTkButton(master=ramka, text="usuń", command=usunwpis, width=35, height=30)
    przycisk_usun.place(x=350, y=285)
    przycisk_odswiez = customtkinter.CTkButton(master=ramka, text="odswież", command=zaladujdane, width=35,
                                               height=30)
    przycisk_odswiez.place(x=393, y=285)
    przycisk_dodajprodukt = customtkinter.CTkLabel(ramka, text="Dodaj produkt:")
    przycisk_dodajprodukt.pack()
    wpis = customtkinter.CTkEntry(ramka, width=80)
    wpis.pack()
    przycisk_dodaj = customtkinter.CTkButton(master=ramka, text="dodaj", width=35, height=30, command=dodawanie)
    przycisk_dodaj.place(x=454, y=285)
    przycisk_Powrot = customtkinter.CTkButton(master=ramka, text="<-", width=35, height=30,
                                              command=produkty_do_stronaglowna)
    przycisk_Powrot.place(x=0, y=0)

    zaladujdane()


#START--------------------------------------------
if __name__ == "__main__":
    #tworze ekran
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()
    root.title("SFA")
    root.geometry("800x480")
    #tworze ramki
    app1 = customtkinter.CTkFrame(root, width=800, height=480)
    app1_pokaz(app1)


    root.mainloop()