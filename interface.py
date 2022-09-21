from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import tkinter
from src.logic import List
from graphs import Graphs

interface = Tk()

# --------- Variables Globales -------- #

filename = StringVar()
picParF = Image.open("img/primeras_pareto.png")
resized = picParF.resize((333, 250), Image.ANTIALIAS)
picParF = ImageTk.PhotoImage(resized)

picParL = Image.open("img/ultimas_pareto.png")
resized = picParL.resize((333, 250), Image.ANTIALIAS)
picParL = ImageTk.PhotoImage(resized)

picDonF = Image.open("img/primeras_donut.png")
resized = picDonF.resize((333, 250), Image.ANTIALIAS)
picDonF = ImageTk.PhotoImage(resized)

picDonL = Image.open("img/ultimas_donut.png")
resized = picDonL.resize((333, 250), Image.ANTIALIAS)
picDonL = ImageTk.PhotoImage(resized)

picBurF = Image.open("img/primeras_burbuja.png")
resized = picBurF.resize((333, 250), Image.ANTIALIAS)
picBurF = ImageTk.PhotoImage(resized)

picBurL = Image.open("img/ultimas_burbuja.png")
resized = picBurL.resize((333, 250), Image.ANTIALIAS)
picBurL = ImageTk.PhotoImage(resized)
        

# --------- Funcion para cargar archivos -------- #

def openFile():
    file = filedialog.askopenfilename(title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    filename.set(file)

# --------- Pantalla de informacion -------- #

def infoWindow():
    tkinter.messagebox.showinfo("Sobre SiFind", "SiFind es un software que recibe un archivo de texto con información de mensajes de texto y muestra de manera visual la frecuencia de las palabras usadas.")

# --------- Pantalla de graficos -------- #

def openGraphsWindow(filename):
    if (filename == ''):
        tkinter.messagebox.showerror("Error", "No ha seleccionado un documento")
    else:
        gWindow = Toplevel(interface)

        gWindow.resizable(0, 0)
        gWindow.title("Gráficos de SiFind")
        iconWindow = PhotoImage(file="img/chart.png")
        gWindow.wm_iconphoto(True, iconWindow)

        frWin = Frame(gWindow, width=1100, height=650)
        frWin.pack()
        # Evaluar caracteres
        ls = List()
        firstDic, lastDic = ls.get_lists(filename) 
        
        # Crear Graficos
        grFirst = Graphs(firstDic, "primeras") 
        grLast = Graphs(lastDic, "ultimas") 
        grFirst.graph()
        grLast.graph()
        
        # Insertar Graficos
        _x = 20
        dx = 360 
        _y = 60
        dy = 270
        lbFirst = Label(gWindow, text="Gráficos para primeras palabras", font=(16)).place(x=20, y=20)
        lbFPareto= Label(gWindow, image=picParF).place(x=_x, y=_y)
        lbFDonut = Label(gWindow, image=picDonF).place(x=_x + dx, y=_y)
        lbFBur = Label(gWindow, image=picBurF).place(x=_x + dx*2, y=_y)
        
        lbLast = Label(gWindow, text="Gráficos para ultimas palabras", font=(16)).place(x=20, y=_y + dy)
        _y = 100
        lbFPareto= Label(gWindow, image=picParL).place(x=_x, y=_y + dy)
        lbFDonut = Label(gWindow, image=picDonL).place(x=_x + dx, y=_y + dy)
        lbFBur = Label(gWindow, image=picBurL).place(x=_x + dx*2, y=_y + dy)

# --------- Pantalla de inicio ------ #

interface.resizable(0, 0)
interface.title("SiFind")
iconWindow = PhotoImage(file="img/chart.png")
interface.wm_iconphoto(True, iconWindow)

frMain = Frame(interface, width=355, height=140)
frMain.pack()

# Mensaje de bienvenida
lbWelcome = Label(frMain, text="¡Bienvenido a SiFind!")
lbWelcome.place(x=10, y=10)
lbDescription = Label(frMain, text="Eliga un archivo para analizar: ")
lbDescription.place(x=10, y=40)

entFilename = Entry(frMain, width=50, textvariable=filename)
entFilename.place(x=10, y=70)

imgDir = PhotoImage(file = "img/btnDirectory.png")
btnDirectory = Button(interface, image=imgDir, command=openFile, width=20, height=12)
btnDirectory.place(x=320, y=70)

imgInfo = PhotoImage(file = "img/info.png")
btnDirectory = Button(interface, image=imgInfo, command=infoWindow, width=20, height=20)
btnDirectory.place(x=320, y=10)

btnAnalize = Button(interface, text="Analizar", command=lambda: openGraphsWindow(filename.get()))
btnAnalize.place(x=140, y=100)

interface.mainloop()