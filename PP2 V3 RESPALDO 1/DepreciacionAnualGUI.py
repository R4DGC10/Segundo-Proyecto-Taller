#Librerias
from tkinter import *
import tkinter as tk


#Modulos
from lineaRecta import lineaRectaAnual
from sumaDigitos import sumarDigitosAnual

def metodosAnual(dataframe,ruta,posicionActivo):
    anualMenu = Toplevel()
    anualMenu.geometry("800x400")
    anualMenu.resizable(False,False)
    anualMenu.iconbitmap(ruta)
    tk.Label(anualMenu, text="Seleccione el metodo para calcular la depreciacion anual").grid(column = 4, row =0)


    #Opcion1
    lineaRecta = tk.Button(anualMenu, text="Linea Recta")
    lineaRecta.grid(column=0, row=8)
    #Ejecuta las funcion
    #Aqui iria anual con LineaRecta
    lineaRecta['command'] = lambda:lineaRectaAnual(posicionActivo,dataframe,ruta)
    

    #Opcion2
    sumaDigitos = tk.Button(anualMenu, text="Suma Digitos")
    sumaDigitos.grid(column=0, row=11)
    #Ejecuta las funcion
    #Aqui iria anual con SumaDigitos 
    sumaDigitos['command'] = lambda:sumarDigitosAnual(posicionActivo,dataframe,ruta)