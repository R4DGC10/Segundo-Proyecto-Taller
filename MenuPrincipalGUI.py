#Librerias
from tkinter import *
from tkinter import ttk
import ctypes


#Modulos
from DepreciacionHastaFechaGUI import metodosHastaFecha
from DepreciacionAnualGUI import metodosAnual
from Abrir_html import aperturaHTML



#ruta logotipo
ruta = "atiLogo.ico"

#Icono del Taskbar
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


#Carga del HTML
dataframe = aperturaHTML()

#Inicia la ventana(GUI) del MenuPrincipal
menuPrincipal = Tk()
#Ajustes del GUI MenuPrincipal
frm = ttk.Frame(menuPrincipal, padding=10)
menuPrincipal.geometry("600x300")
menuPrincipal.resizable(False,False)
menuPrincipal.title("Depreciacion de Activos ATI")
menuPrincipal.iconbitmap(ruta)

#Inicia Mensajes al Usuario
frm.grid()
ttk.Label(frm, text="Bienvenido al Sistema", background="skyblue",font=("Arial",14,"bold")).grid(column=0, row=0)
ttk.Label(frm, text="A continuacion seleccione la forma que desee utilizar para calcular la depreciación",font=("Arial",12)).grid(column=0,row=1)
ttk.Label(frm, text="de los activos almacenados en el archivo HTML cargado",font=("Arial",12)).grid(column=0,row=2)
ttk.Label(frm, text=" ").grid(column=0,row=3)

#Seleccion de opciones mediante botones

#Opcion1
anualOpcion = ttk.Button(frm, text="Depreciacion Anual")
anualOpcion.grid(column=0, row=8)
#Ejecuta las funciones metodosAnual
anualOpcion['command'] = lambda:metodosAnual(dataframe,ruta)

#Opcion2
hastaLaFechaOpcion = ttk.Button(frm, text="Depreciacion hasta la fecha")
hastaLaFechaOpcion.grid(column=0, row=11)
#Ejecuta las funciones metodosHastaFechaGUI
hastaLaFechaOpcion['command'] = lambda:metodosHastaFecha(dataframe,ruta)



#Boton de Cierre (Termina Ejecucion)
ttk.Button(frm, text="Cerrar programa", command=menuPrincipal.destroy).grid(column=0, row=13)
menuPrincipal.mainloop()

