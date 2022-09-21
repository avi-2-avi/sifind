from tkinter import *
from tkinter import filedialog
import os

interface = Tk()

# --------- Variables Globales -------- #

filename = StringVar()

# --------- Funcion para cargar archivos -------- #

def openFile():
    file = filedialog.askopenfile(title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    set(file)

# --------- Funcion evaluar caracteres ------ #



# --------- Funcion crear grafico -------- #


# --------- Pantalla de mostrar graficos -------- #


# --------- Pantalla de inicio ------ #

interface.resizable(0, 0)
interface.title("SiFind")
iconWindow = PhotoImage(file="img/chart.png")
interface.wm_iconphoto(True, iconWindow)

frMain = Frame(interface, width=300, height=200)
frMain.pack()

# Mensaje de bienvenida
lbWelcome = Label(frMain, text="¡Bienvenido a SiFind!\nEliga el archivo para analizar: ")
lbWelcome.place(x=10, y=10)

entFilename = Entry(frMain, width=50, textvariable=filename)
entFilename.place(x=10, y=40)

imgDir = PhotoImage(file = "img/btnDirectory.png")
btnDirectory = Button(interface, image=imgDir, command=openFile,width=20, height=12)
btnDirectory.place(x=200, y=40)

btnAnalize = Button(interface, text="Analizar")
btnAnalize.place(x=80, y=100)

interface.mainloop()