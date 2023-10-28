#Librerias
from tkinter import *
import tkinter as tk
import ctypes

#Modulos
from validarID import validar_activo
from validarID import obtienePosicion

from MenuPrincipalGUI import menuPrincipalGUI

#ruta logotipo ATI
ruta = "atiLogo.ico"

#Icono del Taskbar
myappid = 'mycompany.myproduct.subproduct.version' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def digitarID():
    #Inicializa la ventana Tk
    digitarID = Tk()

    #Ajustes del GUI digitarID
    frm = tk.Frame(digitarID)
    frm.grid(column=0, row=1, padx=10, pady=10)
    digitarID.geometry("600x300")
    digitarID.resizable(False,False)
    digitarID.title("Depreciacion de Activos ATI")
    digitarID.iconbitmap(ruta)

    frm.grid()
    tk.Label(frm,text="Ingrese el identificador del activo a consultar",font=("Arial",14,"bold")).grid(column=0, row=0)
    identificador = tk.Entry(frm)
    identificador.grid(column=0, row=1)
    
    
    def comprobacionID(identificador):

        activo = identificador.get()
        idDigitado = validar_activo(identificador.get())
        posicionActivo = obtienePosicion(activo)

        if idDigitado == True:
            return menuPrincipalGUI(activo,posicionActivo)
        else:
            msg = tk.Label(frm,text = "Identificador invalido, por favor reintentar!", font = "arial")
            msg.grid(column=0,row=5)
            digitarID.after(1500, msg.destroy) 

    confirmacionEntrada = tk.Button(frm, text="Consultar", command=lambda: comprobacionID(identificador))
    confirmacionEntrada.grid(column=0, row=2)

    digitarID.mainloop()
digitarID()
    