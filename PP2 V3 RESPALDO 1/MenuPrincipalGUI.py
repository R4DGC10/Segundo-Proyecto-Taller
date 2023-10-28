#Librerias
from tkinter import *
import tkinter as tk
import pandas as pd
import ctypes

#Nombre de esta ventana tkinter: menuPrincipal =Tk()
#Modulos
from DepreciacionAnualGUI import metodosAnual
from DepreciacionHastaFechaGUI import metodosHastaFecha

def aperturaHTML():
    ruta="fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    return df

#Modulos



#Icono del Taskbar
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Carga del HTML
dataframe = aperturaHTML()
print(dataframe)

def menuPrincipalGUI(activo,posicionActivo):
    #Inicia la ventana(GUI) del MenuPrincipal
    menuPrincipal = Tk()

    

    #ruta logotipo ATI
    ruta = "atiLogo.ico"

    #Ajustes del GUI MenuPrincipal
    frm = tk.Frame(menuPrincipal)
    frm.grid(column=0, row=1, padx=10, pady=10)
    menuPrincipal.geometry("600x300")
    menuPrincipal.resizable(False,False)
    menuPrincipal.title("Depreciacion de Activos ATI")
    menuPrincipal.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="Bienvenido al Sistema", background="skyblue",font=("Arial",14,"bold")).grid(column=0, row=0)
    tk.Label(frm, text="A continuacion seleccione la forma que desee utilizar para calcular la depreciación",font=("Arial",12)).grid(column=0,row=1)
    tk.Label(frm, text="de los activos almacenados en el archivo HTML cargado",font=("Arial",12)).grid(column=0,row=2)
    tk.Label(frm, text=" ").grid(column=0,row=3)

    #Seleccion de opciones mediante botones

    #Opcion1
    anualOpcion = tk.Button(frm, text="Depreciacion Anual")
    anualOpcion.grid(column=0, row=8)
    #Ejecuta las funciones metodosAnual
    anualOpcion['command'] = lambda:metodosAnual(dataframe,ruta,posicionActivo)

    #Opcion2
    hastaLaFechaOpcion = tk.Button(frm, text="Depreciacion hasta la fecha")
    hastaLaFechaOpcion.grid(column=0, row=11)
    #Ejecuta las funciones metodosHastaFechaGUI
    hastaLaFechaOpcion['command'] = lambda:metodosHastaFecha(dataframe,ruta,posicionActivo)


    #Boton de Cierre (Termina Ejecucion)
    tk.Button(frm, text="Cerrar programa", command=menuPrincipal.destroy).grid(column=0, row=13)
    menuPrincipal.mainloop()

