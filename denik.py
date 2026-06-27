import tkinter
import customtkinter
from PIL import Image, ImageTk
from datetime import datetime


menu_otevreno = False
dropdown_frame = None
scroll_frame = None

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

deniky = []
aktivni_index = None
tlacitka_deniku = []

def _timestamp():
    return datetime.now().strftime("%d.%m. %H:%M")

def ulozit_aktivni():
    if aktivni_index is None:
        return
    obsah = textbox._textbox.get("1.0", "end-1c")
    tagy = []
    for tag in textbox._textbox.tag_names():
        if tag in ("sel",):
            continue
        for start, end in zip(
            textbox._textbox.tag_ranges(tag)[0::2],
            textbox._textbox.tag_ranges(tag)[1::2],
        ):
            tagy.append((tag, str(start), str(end)))
    deniky[aktivni_index]["obsah"] = obsah
    deniky[aktivni_index]["tagy"] = tagy
 
 
def nacist_denik(index):
    global aktivni_index
    aktivni_index = index
 
    textbox._textbox.delete("1.0", "end")
    textbox._textbox.insert("1.0", deniky[index]["obsah"])
    for tag, start, end in deniky[index]["tagy"]:
        try:
            textbox._textbox.tag_add(tag, start, end)
        except Exception:
            pass
 
    _zvyraznit_aktivni_tlacitko()
 
 
def _zvyraznit_aktivni_tlacitko():
    for i, btn in enumerate(tlacitka_deniku):
        if i == aktivni_index:
            btn.configure(fg_color="#3a7ebf")   # modrá = aktivní
        else:
            btn.configure(fg_color="#3d3d3d")   # šedá = neaktivní
 
 
def novy_denik():
    ulozit_aktivni()
    nazev = f"Deník {_timestamp()}"
    deniky.append({"nazev": nazev, "obsah": "", "tagy": []})
    novy_index = len(deniky) - 1
    _pridat_tlacitko_deniku(novy_index, nazev)
    nacist_denik(novy_index)
 
 
def _pridat_tlacitko_deniku(index, nazev):
    if scroll_frame is None:
        return

    def prepnout(i=index):
        ulozit_aktivni()
        nacist_denik(i)

    btn = customtkinter.CTkButton(
        scroll_frame,
        text=nazev,
        command=prepnout,
        width=180,
        height=36,
        fg_color="#3d3d3d",
        anchor="w",
        font=("Calibri", 12),
    )
    btn.grid(row=index, column=0, padx=10, pady=(10, 3) if index == 0 else 3, sticky="ew")

    def context_menu(e, i=index):
        menu = tkinter.Menu(okno, tearoff=0, bg="#3d3d3d", fg="white",
                            activebackground="#3a7ebf", activeforeground="white",
                            bd=0, relief="flat")

        def rename(i=i):
            dialog = customtkinter.CTkToplevel(okno)
            dialog.title("Přejmenovat")
            dialog.geometry("300x120")
            dialog.resizable(False, False)
            dialog.grab_set()
            dialog.focus_set()
            customtkinter.CTkLabel(dialog, text="Nový název deníku:").pack(pady=(16, 4))
            vstup = customtkinter.CTkEntry(dialog, width=200)
            vstup.pack()
            vstup.insert(0, deniky[i]["nazev"])
            vstup.focus_set()
            vstup.select_range(0, "end")
            def potvrdit():
                novy_nazev = vstup.get()
                if novy_nazev:
                    deniky[i]["nazev"] = novy_nazev
                    btn.configure(text=novy_nazev)
                dialog.destroy()
            vstup.bind("<Return>", lambda e: potvrdit())
            customtkinter.CTkButton(dialog, text="OK", command=potvrdit, width=80).pack(pady=10)

        def delete(i=i):
            global aktivni_index
            if len(deniky) <= 1:
                return
            deniky.pop(i)
            otevreni_menu()
            otevreni_menu()
            if aktivni_index >= len(deniky):
                aktivni_index = len(deniky) - 1
            nacist_denik(aktivni_index)

        def move_up(i=i):
            if i == 0:
                return
            deniky[i], deniky[i-1] = deniky[i-1], deniky[i]
            otevreni_menu()
            otevreni_menu()
            nacist_denik(aktivni_index)

        def move_down(i=i):
            if i >= len(deniky) - 1:
                return
            deniky[i], deniky[i+1] = deniky[i+1], deniky[i]
            otevreni_menu()
            otevreni_menu()
            nacist_denik(aktivni_index)

        menu.add_command(label="Přejmenovat", command=rename)
        menu.add_separator()
        menu.add_command(label="⬆️  Posunout nahoru", command=move_up)
        menu.add_command(label="⬇️  Posunout dolů", command=move_down)
        menu.add_separator()
        menu.add_command(label="Smazat", command=delete)
        menu.tk_popup(e.x_root, e.y_root)

    btn.bind("<Button-3>", context_menu)
    tlacitka_deniku.append(btn) 
 
def _znovu_nakreslit_sidebar():
    for i, d in enumerate(deniky):
        _pridat_tlacitko_deniku(i, d["nazev"])
    _zvyraznit_aktivni_tlacitko()
 



def zmen_font(vybrany_font):
    global FONT_stav
    FONT_stav = vybrany_font
    textbox._textbox.focus_set()


def zmen_velikost_fontu(vybrana_velikost):
    global FONT_velikost
    FONT_velikost = int(vybrana_velikost)
    textbox._textbox.focus_set()


def BOLD():
    global BOLD_stav
    BOLD_stav = not BOLD_stav
    textbox._textbox.focus_set()

def CURSIVE():
    global CURSIVE_stav
    CURSIVE_stav = not CURSIVE_stav
    textbox._textbox.focus_set()


def UNDERLINE():
    global UNDERLINE_stav
    UNDERLINE_stav = not UNDERLINE_stav
    textbox._textbox.focus_set()


def MARKER(vybrana_barva_pozadi):
    global MARKER_stav, MARKER_hodnota

    if vybrana_barva_pozadi == "None":
        MARKER_stav = False
        
    else:
        MARKER_hodnota = BARVY[vybrana_barva_pozadi]
        MARKER_stav = True
    
    textbox._textbox.focus_set()

    

def FONTCOLOR(vybrana_barva):
    global FONTCOLOR_stav, FONTCOLOR_hodnota

    FONTCOLOR_hodnota = BARVY[vybrana_barva]
    FONTCOLOR_stav = vybrana_barva != "Black"

    textbox._textbox.focus_set()


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

def otevreni_menu(event=None):
    global menu_otevreno, dropdown_frame, tlacitka_deniku, scroll_frame
    
    if not menu_otevreno:
        dropdown_frame = customtkinter.CTkFrame(okno, width=200, height=300, fg_color="#545151")
        dropdown_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        dropdown_frame.columnconfigure(0, weight=5)
        dropdown_frame.columnconfigure(1, weight=50)
        dropdown_frame.columnconfigure(2, weight=5)
        tlacitko_novy_chat = customtkinter.CTkButton(dropdown_frame, text="Nový deník", command=novy_denik, width=200, height=40, bg_color="#545151")
        tlacitko_novy_chat.grid(row=0, column=1, padx=0, pady=5, sticky="ew")
        
        vyska_obrazovky = okno.winfo_height()
        scroll_frame = customtkinter.CTkScrollableFrame(dropdown_frame, fg_color="#545151", height=vyska_obrazovky - 300, corner_radius=0)
        scroll_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
        scroll_frame.columnconfigure(0, weight=1)
        
        textbox.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky="nsew")
        tlacitka_deniku = []
        _znovu_nakreslit_sidebar()
        menu_otevreno = True
    else:
        dropdown_frame.destroy()
        tlacitka_deniku = []
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

tlacitko = customtkinter.CTkButton(horni_lista, text="B", command=BOLD, width=40, height=40, bg_color="#1c1c1c", font=("Segoe UI", 18, "bold"))
tlacitko.grid(row=0, column=1, padx=0, pady=10, sticky="n")
okno.bind("<Control-b>", lambda event: BOLD())

tlacitko_cursive = customtkinter.CTkButton(horni_lista, text="I", command=CURSIVE, width=40, height=40, bg_color="#1c1c1c", font=("Georgia", 18, "italic"))
tlacitko_cursive.grid(row = 0, column = 2, padx = 0, pady = 10, sticky = "n")
okno.bind("<Control-i>", lambda event: CURSIVE())

tlacitko_underline = customtkinter.CTkButton(horni_lista, text="U", command=UNDERLINE, width=40, height=40, bg_color="#1c1c1c", font=("Segoe UI", 18, "underline"))
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

deniky.append({"nazev": f"Deník {_timestamp()}", "obsah": "", "tagy": []})
aktivni_index = 0
textbox._textbox.focus_set()
okno.mainloop()