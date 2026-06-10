import tkinter
import customtkinter
from PIL import Image, ImageTk

menu_otevreno = False
dropdown_frame = None
CAPS_stav = False




def CAPS():
    global CAPS_stav
    if not CAPS_stav:
        CAPS_stav = True
        textbox.set(textbox.get().upper())
    else:
        CAPS_stav = False
        textbox.set(textbox.get().lower())

def otevreni_menu(event=None):
    global menu_otevreno, dropdown_frame
    if not menu_otevreno:
        dropdown_frame = customtkinter.CTkFrame(okno, width=200, height=300, fg_color="#545151")
        dropdown_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        textbox.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky="nsew")
        menu_otevreno = True
    else:
        dropdown_frame.destroy()
        textbox.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
        menu_otevreno = False
        dropdown_frame = None

okno = customtkinter.CTk()
okno.geometry("800x600")
okno.columnconfigure(0, weight=1)
okno.columnconfigure(1, weight=10)
okno.rowconfigure(1, weight=1)
okno.minsize(300, 250)
okno.maxsize(1920, 1080)
okno.title("Deník")
okno.resizable(True, True)
okno.configure(fg_color="#2b2b2b")

menuVelikost = 50
listaNadMenuVelikost = 2000



obrazek = Image.open("menu.png").convert("RGBA")
obrazek = obrazek.resize((menuVelikost, menuVelikost))
foto = ImageTk.PhotoImage(obrazek)


#CANVAS
canvas_lista_nad_menu = tkinter.Canvas(okno, width=listaNadMenuVelikost, height=menuVelikost + 10, highlightthickness=0, bg="#1c1c1c")
canvas_lista_nad_menu.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

canvas_menu_ikona = tkinter.Canvas(okno, width=menuVelikost, height=menuVelikost, highlightthickness=0, bg="#1c1c1c")
canvas_menu_ikona.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
canvas_menu_ikona.create_image(0, 0, anchor="nw", image=foto)
canvas_menu_ikona.configure(cursor="hand2")
canvas_menu_ikona.bind("<Button-1>", otevreni_menu)


textbox = customtkinter.CTkTextbox(okno, fg_color="#ffffff", text_color="#000000", font=("Arial", 14))
textbox.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

tlacitko = customtkinter.CTkButton(okno, text="B", command=CAPS, width=40, height=40, bg_color ="#1c1c1c")
tlacitko.grid(row=0, column=1, padx=0, pady=5, sticky="n")

okno.mainloop()