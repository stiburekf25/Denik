import tkinter
import customtkinter
from PIL import Image, ImageTk

def hello():
    tlacitko.configure(text= "Hello World!")



okno = customtkinter.CTk()
okno.geometry("500x300")
okno.minsize(200, 100)
okno.maxsize(800, 400)
okno.title("Deník")
okno.resizable(True, True)
okno.configure(fg_color="#2b2b2b")

menuVelikost = 40


obrazek = Image.open("menu.png").convert("RGBA")
obrazek = obrazek.resize((menuVelikost, menuVelikost))
foto = ImageTk.PhotoImage(obrazek)

canvas = tkinter.Canvas(okno, width=menuVelikost, height=menuVelikost, highlightthickness=0, bg="#2b2b2b")
canvas.grid(padx=10, pady=10, sticky="w")

canvas.create_image(0, 0, anchor="nw", image=foto)



tlacitko = customtkinter.CTkButton(okno, text="Click me", command=hello, width=120, height=40)
tlacitko.grid(padx=20, pady=20)

okno.mainloop()