#Librerias
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd
import datetime as dt

#Modulos
from OpenAI import GPTRequest

#Linea Recta hasta la fecha
def lineaRectaHastaLaFecha(posicion,dataframe,ruta):

    lineaRectaHastaLaFechaGUI = Tk()

    #Ajustes del GUI MenuPrincipal
    frm = tk.Frame(lineaRectaHastaLaFechaGUI)
    frm.grid(column=0, row=1, padx=10, pady=10)
    lineaRectaHastaLaFechaGUI.geometry("1000x800")
    lineaRectaHastaLaFechaGUI.resizable(False,False)
    lineaRectaHastaLaFechaGUI.title("Depreciacion de Activos ATI")
    lineaRectaHastaLaFechaGUI.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="TABLA DEPRECIACION HASTA FECHA MEDIANTE LINEA RECTA",font=("Arial",12)).grid(column=0,row=0)
    tk.Label(frm, text=" ").grid(column=0,row=3)

    # Variables a utilizar en metodo Linea Recta para Depreciación Anual
    activo = posicion
    df = dataframe
    detalleActivo = df.iloc[activo, 2]
    print("\n")
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamento = int(df.iloc[activo, 6])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    fecha_compra_str = df.iloc[activo, 4]
    fecha_compra = dt.datetime.strptime(fecha_compra_str, "%d/%m/%Y")
    valorRecuperacion = dt.datetime.now().year - fecha_compra.year
    periodoRecuperacionOriginal = int(df.iloc[activo, 7])
    moneda = df.iloc[activo, 5]
    año = fecha_compra.year + 1

    

    if periodoRecuperacionOriginal == 0:
        print("EL ACTIVO: ", detalleActivo, "NO ES SUJETO A DEPRECIACION\nIntentelo de nuevo")
    else:
        data = []
        valorEnLibros = valorInicial
        periodo = 1
        while periodo <= valorRecuperacion:
            depreciacionAnual = (valorInicial - valorSalvamento) / valorRecuperacion
            tasa = 1 / valorRecuperacion
            valorEnLibros -= depreciacionAnual
            data.append({
                'AÑO': año,
                'PERIODO': periodo,
                'DEPRECIACION ANUAL': depreciacionAnual,
                'TASA DE DEPRECIACION': tasa,
                'VALOR EN LIBROS': valorEnLibros
            })
            año += 1
            periodo += 1
            if periodo > periodoRecuperacionOriginal:
                # Si el período supera el período de recuperación original, establecer los valores a 0
                depreciacionAnual = 0
                tasa = 0
                valorEnLibros = valorSalvamento
                data[-1] = {
                    'AÑO': año - 1,
                    'PERIODO': periodo-1,
                    'DEPRECIACION ANUAL': depreciacionAnual,
                    'TASA DE DEPRECIACION': tasa,
                    'VALOR EN LIBROS': valorEnLibros
                }
        dfResultado = pd.DataFrame(data)
        # REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['TASA DE DEPRECIACION'] = dfResultado['TASA DE DEPRECIACION'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)
        print("")
        print("Identificador:        ", numeroActivo)
        print("Categoria:            ", categoria)
        print("Detalle:              ", detalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fecha_compra)
        print("Moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamento)
        print("Periodo de Recuperación:         ", valorRecuperacion)
        print("============================= Tabla de Proyección: Método Lineal hasta Fecha Actual=============================")

        
        # Create a Treeview widget
        treeview = ttk.Treeview(lineaRectaHastaLaFechaGUI)

        # Define the column names
        treeview["columns"] = list(dfResultado.columns)
        treeview["show"] = "headings"

        # Create the columns
        for column in dfResultado.columns:
            treeview.heading(column, text=column) # let the column heading = column name

        # Add the data from the DataFrame to the Treeview
        for index, row in dfResultado.iterrows():
            treeview.insert("", "end", values=list(row))

        # Grid the Treeview widget
        treeview.grid(column=0, row=4)

        GPTRequest(detalleActivo)

    lineaRectaHastaLaFechaGUI.mainloop()





#LineaRecta Anual
def lineaRectaAnual(posicion,dataframe,ruta):

    lineaRectaAnualGUI = Tk()

    #Ajustes del GUI MenuPrincipal
    frm = tk.Frame(lineaRectaAnualGUI)
    frm.grid(column=0, row=1, padx=10, pady=10)
    lineaRectaAnualGUI.geometry("1000x800")
    lineaRectaAnualGUI.resizable(False,False)
    lineaRectaAnualGUI.title("Depreciacion de Activos ATI")
    lineaRectaAnualGUI.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="TABLA DEPRECIACION ANUAL MEDIANTE LINEA RECTA",font=("Arial",12)).grid(column=0,row=0)
    tk.Label(frm, text=" ").grid(column=0,row=3)

    #Variables a utilizar en metodo Linea Recta para Depreciacion Anual
    activo = posicion
    df = dataframe
    detalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", detalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamiento = int(df.iloc[activo, 6])
    periodoRecuperacion = int(df.iloc[activo, 7])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    fechaCompra = df.iloc[activo, 4]
    moneda = df.iloc[activo, 5]
    fechaCompraObj = dt.datetime.strptime(fechaCompra, "%d/%m/%Y")
    año =fechaCompraObj.year+1
    periodo=1


    if periodoRecuperacion == 0:
        print("EL ACTIVO: ", detalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo\n") 
        lineaRectaAnual()
        

    else:
        data = []
        valorEnLibros = valorInicial
        while periodo <= periodoRecuperacion:
            depreciacionAnual = (valorInicial - valorSalvamiento) / periodoRecuperacion
            valorEnLibros -= depreciacionAnual
            tasa= 1/periodoRecuperacion

            data.append({
                'AÑO': año,
                'PERIODO': periodo,
                'DEPRECIACION ANUAL': depreciacionAnual,
                'TASA DE DEPRECIACION': tasa,
                'VALOR EN LIBROS': valorEnLibros
            })
            año += 1  
            periodo +=1
        
        dfResultado = pd.DataFrame(data)

        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['TASA DE DEPRECIACION'] = dfResultado['TASA DE DEPRECIACION'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)

        print("")
        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", detalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fechaCompra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamiento)
        print("Periodo de Recuperacion:         ", periodoRecuperacion)
        print("============================= Tabla de Proyeccion: Metodo Lineal =============================")
        

        
        # Create a Treeview widget
        treeview = ttk.Treeview(lineaRectaAnualGUI)

        # Define the column names
        treeview["columns"] = list(dfResultado.columns)
        treeview["show"] = "headings"

        # Create the columns
        for column in dfResultado.columns:
            treeview.heading(column, text=column) # let the column heading = column name

        # Add the data from the DataFrame to the Treeview
        for index, row in dfResultado.iterrows():
            treeview.insert("", "end", values=list(row))

        # Grid the Treeview widget
        treeview.grid(column=0, row=4)

        
        GPTRequest(detalleActivo)

    lineaRectaAnualGUI.mainloop()
    

