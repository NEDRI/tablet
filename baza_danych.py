from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import *

# funkcja do tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

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
    wybrany_wiersz_bazy =  drzewo.item(wybrany_wiersz,"values")[0]
    print("zwiekszany wiersz w bazie: ",drzewo.item(wybrany_wiersz,"values")[0])
    baza = sqlite3.connect(bazasfa)
    baza.execute("UPDATE Produkt SET iloscp = iloscp + 1 WHERE produkt ='" + wybrany_wiersz_bazy + "'")
    baza.commit()
    zaladujdane()

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

# ekran
aplikacja = tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240, 248, 255)))

''''''
bazasfa="D:\GITfld\\tablet\\bazasfa"
bg= PhotoImage(file="D:\GITfld\\tablet\\tlo_baza.png")
''''''

# tlo wyswietlanie 
label1= Label(aplikacja, image = bg)
label1.place(x=0, y=0)

drzewo = ttk.Treeview(aplikacja, columns=("kolumna1", "kolumna2"), show="headings")
drzewo.heading("#1", text="Nazwa produktu")
drzewo.heading("#2", text="Ilość produktu")
ttk.Style().configure("Treeview", background="black", foreground= "white", fieldbackground="black")

sb = Scrollbar(orient=VERTICAL)

drzewo.config(yscrollcommand=sb.set)
sb.config(command=drzewo.yview)

drzewo.pack()

przycisk_plus = tk.Button(text="+", command=zwieksz, width=4, height=1)
przycisk_plus .place(x=280, y=265)
przycisk_minus = tk.Button(text="-", command=zmniejsz, width=4, height=1)
przycisk_minus .place(x=340, y=265)
przycisk_usun = tk.Button(text="usuń", command=usunwpis, width=4, height=1)
przycisk_usun .place(x=400, y=265)
przycisk_odswiez = tk.Button(text="odswież", command=zaladujdane, width=4, height=1)
przycisk_odswiez .place(x=460, y=265)
description = tk.Label(aplikacja, text="Dodaj produkt:").pack()
wpis = tk.Entry(aplikacja,width=40)
wpis.pack()
przycisk_dodaj=tk.Button(text="dodaj",  width=4, height=1, command=dodawanie)
przycisk_dodaj .place(x=520, y=240)

zaladujdane()

aplikacja.mainloop()