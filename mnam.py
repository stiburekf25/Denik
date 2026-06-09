import tkinter
import customtkinter
from PIL import Image, ImageTk

def hello():
    tlacitko.configure(text= "Hello World!")

def otevreni_menu(event=None):
    print("Kliknuto")
    global menu_otevreno, dropdown_frame
    menu_otevreno = True



okno = customtkinter.CTk()
okno.geometry("500x300")
okno.columnconfigure(0, weight=1)
okno.columnconfigure(1, weight=1)
okno.minsize(200, 100)
okno.maxsize(1920, 1080)
okno.title("Deník")
okno.resizable(True, True)
okno.configure(fg_color="#2b2b2b")

menuVelikost = 50
listaNadMenuVelikost = 2000

menu_otevreno = False
dropdown_frame = None




obrazek = Image.open("menu.png").convert("RGBA")
obrazek = obrazek.resize((menuVelikost, menuVelikost))
foto = ImageTk.PhotoImage(obrazek)


#CANVAS
canvas_lista_nad_menu = tkinter.Canvas(okno, width=listaNadMenuVelikost, height=menuVelikost + 10, highlightthickness=0, bg="#1c1c1c")
canvas_lista_nad_menu.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="ew")

if menu_otevreno:
eeee

if not menu_otevreno:
    canvas_lista_nad_menu.create_image(10, 5, anchor="nw", image=foto)
    canvas_lista_nad_menu.bind("<Button-1>", otevreni_menu)


tlacitko = customtkinter.CTkButton(okno, text="Click me", command=hello, width=120, height=40)
tlacitko.grid(row=1, column=1, padx=20, pady=20)

okno.mainloop()