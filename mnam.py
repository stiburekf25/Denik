import tkinter
import customtkinter
from PIL import Image, ImageTk

menu_otevreno = False
dropdown_frame = None
CAPS_stav = False
CURSIVE_stav = False


def CAPS():
    global CAPS_stav

    CAPS_stav = not CAPS_stav

    if CAPS_stav:
        tlacitko.configure(fg_color="#3b82f6")
    else:
        tlacitko.configure(fg_color="#1f6aa5")

def CURSIVE():
    global CURSIVE_stav

    CURSIVE_stav = not CURSIVE_stav

    if CURSIVE_stav:
        tlacitko_cursive.configure(fg_color="#3b82f6")
    else:
        tlacitko_cursive.configure(fg_color="#1f6aa5")
     
def psani_textu(event):
    if not event.char:
        return

    znak = event.char

    if CAPS_stav and znak.isalpha():
        znak = znak.upper()

    start = textbox.index("insert")
    textbox.insert("insert", znak)

    if CURSIVE_stav:
        end = textbox.index("insert")
        textbox.tag_add("italic", start, end)

    return "break"

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

horni_lista = customtkinter.CTkFrame(okno, height=60, fg_color="#1c1c1c")
horni_lista.grid(row=0, column=0, columnspan=2, sticky="ew")
horni_lista.columnconfigure(0, weight=50)
horni_lista.columnconfigure(1, weight=1)
horni_lista.columnconfigure(2, weight=1)
horni_lista.columnconfigure(3, weight=50)

canvas_menu_ikona = tkinter.Canvas(horni_lista, width=menuVelikost, height=menuVelikost, bg="#1c1c1c", highlightthickness=0)
canvas_menu_ikona.grid(row=0, column=0, padx=5, pady=5, sticky="w")
canvas_menu_ikona.create_image(0, 0, anchor="nw", image=foto)
canvas_menu_ikona.configure(cursor="hand2")
canvas_menu_ikona.bind("<Button-1>", otevreni_menu)

textbox = customtkinter.CTkTextbox(okno, fg_color="#ffffff", text_color="#000000", font=("Arial", 14))
textbox.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

textbox._textbox.tag_configure("italic", font=("Arial", 14, "italic"))
textbox._textbox.bind("<KeyPress>", psani_textu)

tlacitko = customtkinter.CTkButton(horni_lista, text="B", command=CAPS, width=40, height=40, bg_color="#1c1c1c")
tlacitko.grid(row=0, column=1, padx=0, pady=5, sticky="n")
okno.bind("<Control-u>", lambda event: CAPS())

tlacitko_cursive = customtkinter.CTkButton(horni_lista, text="I", command=CURSIVE, width=40, height=40, bg_color="#1c1c1c")
tlacitko_cursive.grid(row = 0, column = 2, padx = 0, pady = 5, sticky = "n")
okno.bind("<Control-i>", lambda event: CURSIVE()) 
okno.mainloop()