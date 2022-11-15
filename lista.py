# from tkinter import Tk, Label, Button
from tkinter import ttk, Button
import tkinter as tk
import sqlite3

# funkcja do tła
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def zaladujdane():
    baza = sqlite3.connect(bazasfa)
    dane = baza.execute("SELECT * FROM Produkt;").fetchall()
    print("Dane z bazy: ", dane)
    drzewo.delete(*drzewo.get_children())
    for wiersz_z_bazy in dane:
        print("wrzucam wiersz_z_bazy: ", wiersz_z_bazy)
        drzewo.insert("", tk.END, values=wiersz_z_bazy)

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
# obraz= PhotoImage(file= r"D:\\Users\\hjakubowski356\\Desktop\\tak.png")
# baza danych
bazasfa="/home/ai/pliki/bazyd/bazasfa"
# ekran
aplikacja = tk.Tk()
aplikacja.title("SFA")
aplikacja.geometry("800x480")
aplikacja.configure(bg=_from_rgb((240, 248, 255)))

drzewo = ttk.Treeview(aplikacja, columns=("kolumna1", "kolumna2"), show="headings")
drzewo.heading("#1", text="Nazwa produktu")
drzewo.heading("#2", text="Ilość produktu")
drzewo.pack()

przycisk_plus = tk.Button(text="+", command=zwieksz)
przycisk_plus .pack()
przycisk_minus = tk.Button(text="-", command=zmniejsz)
przycisk_minus .pack()
przycisk_usun = tk.Button(text="X", command=usunwpis)
przycisk_usun .pack()
przycisk_odswiez = tk.Button(text="odswiez", command=zaladujdane)
przycisk_odswiez .pack()

zaladujdane()

aplikacja.mainloop()
