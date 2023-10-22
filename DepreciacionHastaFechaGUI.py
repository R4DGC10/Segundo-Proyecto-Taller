#Librerias
from tkinter import *
import tkinter as tk
from tkinter import ttk



def metodosHastaFecha(dataframe,ruta):
    hastaFechaMenu = Toplevel()
    hastaFechaMenu.geometry("800x400")
    hastaFechaMenu.resizable(False,False)
    hastaFechaMenu.iconbitmap(ruta)
    ttk.Label(hastaFechaMenu, text="Seleccione el metodo depreciacion hasta la fecha").grid(column=4, row=0)
    print(dataframe)