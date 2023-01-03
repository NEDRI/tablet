import customtkinter
from customtkinter import *

class strona(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(strona):
   def __init__(self, *args, **kwargs):
       strona.__init__(self, *args, **kwargs)
       liczba= 0
       szerokosc=80 #szerokosc przycisku
       wys=65
       lewo=5
       srodek=7
       prawo=9
       czas=liczba
       czydzialal = False

class glowny_widok(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page1(self)
        p3 = Page1(self)

        buttonframe = customtkinter.CTkFrame(self)
        container = customtkinter.CTkFrame(self)
        buttonframe.place(x=15, y=100)
        container.place(x=20,y=100)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = customtkinter.CTkButton(buttonframe, text="Page 1", command=p1.show)
        b2 = customtkinter.CTkButton(buttonframe, text="Page 2", command=p2.show)
        b3 = customtkinter.CTkButton(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()
    main = glowny_widok(root)
    main.pack
    root.wm_geometry("800x480")
    root.mainloop()