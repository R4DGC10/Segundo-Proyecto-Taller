#Librerias
from tkinter import *
import tkinter as tk


#Modulos
from lineaRecta import lineaRectaHastaLaFecha
from sumaDigitos import sumarDigitosHastaLaFecha


def metodosHastaFecha(dataframe,ruta,posicionActivo):
    hastaFechaMenu = Toplevel()
    hastaFechaMenu.geometry("800x400")
    hastaFechaMenu.resizable(False,False)
    hastaFechaMenu.iconbitmap(ruta)
    tk.Label(hastaFechaMenu, text="Seleccione el metodo para calcular la depreciacion hasta la fecha").grid(column=4, row=0)
    
    #Opcion1
    lineaRectaHastaFecha = tk.Button(hastaFechaMenu, text="Linea Recta")
    lineaRectaHastaFecha.grid(column=0, row=8)
    #Ejecuta las funcion
    #Aqui iria hastafecha con LineaRecta
    lineaRectaHastaFecha['command'] = lambda:lineaRectaHastaLaFecha(posicionActivo,dataframe,ruta)
    
    #Opcion2
    sumaDigitosHastaFecha = tk.Button(hastaFechaMenu, text="Suma Digitos")
    sumaDigitosHastaFecha.grid(column=0, row=11)
    #Ejecuta las funcion 
    #Aqui iria hastafehca con SumaDigitos 
    sumaDigitosHastaFecha['command'] = lambda:sumarDigitosHastaLaFecha(posicionActivo,dataframe,ruta)