import tkinter
import customtkinter
from PIL import Image, ImageTk

menu_otevreno = False
dropdown_frame = None
BOLD_stav = False
CURSIVE_stav = False
UNDERLINE_stav = False
MARKER_stav = False
FONTCOLOR_stav = False



FONT_stav = "Calibri"
FONT_velikost = 14
def zmen_font(vybrany_font):
    global FONT_stav
    FONT_stav = vybrany_font

def zmen_velikost_fontu(vybrana_velikost):
    global FONT_velikost
    FONT_velikost = int(vybrana_velikost)

def BOLD():
    global BOLD_stav

    BOLD_stav = not BOLD_stav

    if BOLD_stav:
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

def UNDERLINE():
    global UNDERLINE_stav

    UNDERLINE_stav = not UNDERLINE_stav

    if UNDERLINE_stav:
        tlacitko_underline.configure(fg_color="#3b82f6")
    else:
        tlacitko_underline.configure(fg_color="#1f6aa5")

def MARKER():
    global MARKER_stav

    MARKER_stav = not MARKER_stav

    if MARKER_stav:
        tlacitko_marker.configure(fg_color="#3b82f6")
    else:
        tlacitko_marker.configure(fg_color="#1f6aa5")

def FONTCOLOR():
    global FONTCOLOR_stav

    FONTCOLOR_stav = not FONTCOLOR_stav

    if FONTCOLOR_stav:
        tlacitko_fontcolor.configure(fg_color="#3b82f6")
    else:
        tlacitko_fontcolor.configure(fg_color="#1f6aa5")


def ziskat_tag():

    casti = []
    if BOLD_stav:
        casti.append("bold")
    if CURSIVE_stav:
        casti.append("italic")
    
    font = (FONT_stav, FONT_velikost)
    if BOLD_stav and CURSIVE_stav:
        font = (FONT_stav, FONT_velikost, "bold italic")
    elif BOLD_stav:
        font = (FONT_stav, FONT_velikost, "bold")
    elif CURSIVE_stav:
        font = (FONT_stav, FONT_velikost, "italic")

    nazev_casti = []

    if BOLD_stav:
        nazev_casti.append("bold")
    if CURSIVE_stav:
        nazev_casti.append("italic")
    if UNDERLINE_stav:
        nazev_casti.append("underline")
    if MARKER_stav:
        nazev_casti.append("marker")
    if FONTCOLOR_stav:
        nazev_casti.append("fontcolor")

    nazev_casti.append(FONT_stav.replace(" ", "_"))
    nazev_casti.append(str(FONT_velikost))
    nazev = "_".join(nazev_casti)


    if nazev not in textbox._textbox.tag_names():
        textbox._textbox.tag_configure(nazev, font=font, underline=UNDERLINE_stav, background="#ffff00" if MARKER_stav else "", foreground="#ff0000" if FONTCOLOR_stav else "")
    
    return nazev

def psani_textu(event):
    if not event.char or event.keysym in ["BackSpace", "Delete", "Return", "Tab"]:
        return

    start = textbox._textbox.index("insert")      
    textbox._textbox.insert("insert", event.char)  
    end = textbox._textbox.index("insert")         
 
    tag = ziskat_tag()
    if tag != "normal":
        textbox._textbox.tag_add(tag, start, end)
 
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
horni_lista.columnconfigure(3, weight=1)
horni_lista.columnconfigure(4, weight=1)
horni_lista.columnconfigure(5, weight=1)
horni_lista.columnconfigure(6, weight=1)
horni_lista.columnconfigure(7, weight=1)
horni_lista.columnconfigure(8, weight=50)

canvas_menu_ikona = tkinter.Canvas(horni_lista, width=menuVelikost, height=menuVelikost, bg="#1c1c1c", highlightthickness=0)
canvas_menu_ikona.grid(row=0, column=0, padx=5, pady=5, sticky="w")
canvas_menu_ikona.create_image(0, 0, anchor="nw", image=foto)
canvas_menu_ikona.configure(cursor="hand2")
canvas_menu_ikona.bind("<Button-1>", otevreni_menu)

textbox = customtkinter.CTkTextbox(okno, fg_color="#ffffff", text_color="#000000", font=("Arial", 14))
textbox.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

textbox._textbox.bind("<KeyPress>", psani_textu)

tlacitko = customtkinter.CTkButton(horni_lista, text="B", command=BOLD, width=40, height=40, bg_color="#1c1c1c")
tlacitko.grid(row=0, column=1, padx=0, pady=10, sticky="n")
okno.bind("<Control-b>", lambda event: BOLD())

tlacitko_cursive = customtkinter.CTkButton(horni_lista, text="I", command=CURSIVE, width=40, height=40, bg_color="#1c1c1c")
tlacitko_cursive.grid(row = 0, column = 2, padx = 0, pady = 10, sticky = "n")
okno.bind("<Control-i>", lambda event: CURSIVE())

tlacitko_underline = customtkinter.CTkButton(horni_lista, text="U", command=UNDERLINE, width=40, height=40, bg_color="#1c1c1c")
tlacitko_underline.grid(row=0, column=3, padx=0, pady=10, sticky="n")
okno.bind("<Control-u>", lambda event: UNDERLINE())

tlacitko_marker = customtkinter.CTkButton(horni_lista, text="M", command=MARKER, width=40, height=40, bg_color="#1c1c1c")
tlacitko_marker.grid(row=0, column=4, padx=0, pady=10, sticky="n")
okno.bind("<Control-m>", lambda event: MARKER())

tlacitko_fontcolor = customtkinter.CTkButton(horni_lista, text="A", command=FONTCOLOR, width=40, height=40, bg_color="#1c1c1c")
tlacitko_fontcolor.grid(row=0, column=5, padx=0, pady=10, sticky="n")
okno.bind("<Control-a>", lambda event: FONTCOLOR())

tlacitko_fontpicker = customtkinter.CTkOptionMenu(
    horni_lista,
    values=["Arial", "Calibri", "Segoe UI", "Times New Roman", "Courier New", "Verdana", "Comic Sans MS"],
    command=zmen_font, width=100, height=40, bg_color="#1c1c1c")
tlacitko_fontpicker.grid(row=0, column=6, padx=0, pady=10, sticky="n")
tlacitko_fontpicker.set("Calibri")

tlacitko_velikost_fontu = customtkinter.CTkOptionMenu(horni_lista, values=["8","10","12","14", "16", "18", "20", "22", "24", "26", "28", "36", "48", "72"], command=zmen_velikost_fontu, width=80, height=40, bg_color="#1c1c1c")
tlacitko_velikost_fontu.grid(row=0, column=7, padx=0, pady=10, sticky="n")
tlacitko_velikost_fontu.set("14")


okno.mainloop()