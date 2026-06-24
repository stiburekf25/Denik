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
FONTCOLOR_hodnota = "#000000"
MARKER_hodnota = "#ffff00"
BARVY = {
    "Black": "#000000",
    "White": "#ffffff",
    "Red": "#ff0000",
    "Green": "#00aa00",
    "Blue": "#0000ff",
    "Yellow": "#ffff00"
}

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

def CURSIVE():
    global CURSIVE_stav

    CURSIVE_stav = not CURSIVE_stav

def UNDERLINE():
    global UNDERLINE_stav

    UNDERLINE_stav = not UNDERLINE_stav

def MARKER(vybrana_barva_pozadi):
    global MARKER_stav, MARKER_hodnota

    if vybrana_barva_pozadi == "None":
        MARKER_stav = False
        
    else:
        MARKER_hodnota = BARVY[vybrana_barva_pozadi]
        MARKER_stav = True
       
    

def FONTCOLOR(vybrana_barva):
    global FONTCOLOR_stav, FONTCOLOR_hodnota

    FONTCOLOR_hodnota = BARVY[vybrana_barva]
    FONTCOLOR_stav = vybrana_barva != "Black"


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
    nazev_casti.append(FONTCOLOR_hodnota.replace("#", ""))
    nazev_casti.append(MARKER_hodnota.replace("#", ""))
    nazev = "_".join(nazev_casti)


    if nazev not in textbox._textbox.tag_names():
        textbox._textbox.tag_configure(nazev, font=font, underline=UNDERLINE_stav, background=MARKER_hodnota if MARKER_stav else "", foreground=FONTCOLOR_hodnota if FONTCOLOR_stav else "")
    
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

def novy_denik():
    textbox._textbox.delete("1.0", "end")
    global BOLD_stav, CURSIVE_stav, UNDERLINE_stav, MARKER_stav, FONTCOLOR_stav, FONTCOLOR_hodnota, MARKER_hodnota, FONT_stav, FONT_velikost
    BOLD_stav = False
    CURSIVE_stav = False
    UNDERLINE_stav = False
    MARKER_stav = False
    FONTCOLOR_stav = False
    FONTCOLOR_hodnota = "#000000"
    MARKER_hodnota = "#ffff00"
    FONT_stav = "Calibri"
    FONT_velikost = 14

def otevreni_menu(event=None):
    global menu_otevreno, dropdown_frame
    if not menu_otevreno:
        dropdown_frame = customtkinter.CTkFrame(okno, width=200, height=300, fg_color="#545151")
        dropdown_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        dropdown_frame.columnconfigure(0, weight=5)
        dropdown_frame.columnconfigure(1, weight=50)
        dropdown_frame.columnconfigure(2, weight=5)
        tlacitko_novy_chat = customtkinter.CTkButton(dropdown_frame, text="Nový deník", command=novy_denik, width=200, height=40, bg_color="#545151")
        tlacitko_novy_chat.grid(row=0, column=1, padx=0, pady=5, sticky="ew")
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

tlacitko_marker = customtkinter.CTkOptionMenu(horni_lista, values=["None", "Black", "White", "Red", "Green", "Blue", "Yellow"], command=MARKER, width=40, height=40, bg_color="#1c1c1c")
tlacitko_marker.grid(row=0, column=4, padx=0, pady=10, sticky="n")
tlacitko_marker.set("None")
okno.bind("<Control-m>", lambda event: MARKER())

tlacitko_fontcolor = customtkinter.CTkOptionMenu(horni_lista, values=["Black", "White", "Red", "Green", "Blue", "Yellow"], command=FONTCOLOR, width=40, height=40, bg_color="#1c1c1c")
tlacitko_fontcolor.grid(row=0, column=5, padx=0, pady=10, sticky="n")
tlacitko_fontcolor.set("Black")
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