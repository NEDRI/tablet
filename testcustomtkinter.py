import customtkinter

''''
zeby dzialalo GUI z bibloteka trzeba w cmd:
pip install customtkinter   
'''

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

okno = customtkinter.CTk()
okno.geometry("500x350")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=okno)
frame.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frame, text="login system")
lable.pack(pady=12, padx=10)

wejscie1 = customtkinter.CTkEntry(master=frame , placeholder_text="User")
wejscie1.pack(pady=12, padx=10)

wejscie2 = customtkinter.CTkEntry(master=frame , placeholder_text="Password", show="*")
wejscie2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remeber me")
checkbox.pack(pady=12, padx=10)

okno.mainloop()