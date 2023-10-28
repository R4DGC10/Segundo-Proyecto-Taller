#Librerias
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import datetime as dt

#Modulos
from OpenAI import GPTRequest


#SumaDigitos hasta la fecha
def sumarDigitosHastaLaFecha(posicion,dataframe,ruta):

    
    sumaDigitosHastaLaFechaGUI = Tk()

    #Ajustes del GUI MenuPrincipal
    frm = tk.Frame(sumaDigitosHastaLaFechaGUI)
    frm.grid(column=0, row=1, padx=10, pady=10)
    sumaDigitosHastaLaFechaGUI.geometry("1000x800")
    sumaDigitosHastaLaFechaGUI.resizable(False,False)
    sumaDigitosHastaLaFechaGUI.title("Depreciacion de Activos ATI")
    sumaDigitosHastaLaFechaGUI.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="TABLA DEPRECIACION HASTA FECHA MEDIANTE SUMA DIGITOS",font=("Arial",12)).grid(column=0,row=0)
    tk.Label(frm, text=" ").grid(column=0,row=3)

    # Variables a utilizar en metodo Suma Digitos para Depreciacion hasta la Fecha
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
    periodoRecuperacion = dt.datetime.now().year - fecha_compra.year
    Periodo_Recuperacion_original = int(df.iloc[activo, 7])
    moneda = df.iloc[activo, 5]
    año = fecha_compra.year + 1
    depreciacionAcumulada = 0
    resultados = []
    parte2 = periodoRecuperacion * (periodoRecuperacion + 1) / 2
    periodo = 1
    vidaUtil = periodoRecuperacion * (periodoRecuperacion + 1) / 2
    

    if Periodo_Recuperacion_original == 0:
        print("EL ACTIVO: ", detalleActivo, "NO ES SUJETO A DEPRECIACION \n")
    else:
        while periodo <= periodoRecuperacion:
            factor = (periodoRecuperacion - periodo + 1) / parte2
            depreciacionAnual = factor * (valorInicial - valorSalvamento)
            depreciacionAcumulada += depreciacionAnual
            valorNeto = valorInicial - depreciacionAcumulada
            resultados.append({
                "AÑO": año,
                "PERIODO": periodo,
                "DEPRECIACION ANUAL": depreciacionAnual,
                "DEPRECIACION ACUMULADA": depreciacionAcumulada,
                "VALOR EN LIBROS": valorNeto
            })
            periodo += 1
            año += 1
            if periodo > Periodo_Recuperacion_original:
                # Si el periodo supera el período de recuperación original, establecer los valores a 0
                depreciacionAnual = 0
                depreciacionAcumulada = valorInicial - valorSalvamento
                valorNeto = valorSalvamento
                resultados[-1] = {
                    "AÑO": año - 1,
                    "PERIODO": periodo - 1,
                    "DEPRECIACION ANUAL": depreciacionAnual,
                    "DEPRECIACION ACUMULADA": depreciacionAcumulada,
                    "VALOR EN LIBROS": valorNeto
                }
        dfResultado = pd.DataFrame(resultados)
        # REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['DEPRECIACION ACUMULADA'] = dfResultado['DEPRECIACION ACUMULADA'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)
        print("Identificador:        ", numeroActivo)
        print("Categoria:            ", categoria)
        print("Detalle:              ", detalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fecha_compra)
        print("Moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamento)
        print("Periodo de Recuperacion: ", periodoRecuperacion)
        print("")
        print("Vida Util del activo   ", vidaUtil)
        print("============================= Tabla de Proyeccion: Metodo Suma Digitos Hasta la Fecha=============================")

        # Create a Treeview widget
        treeview = ttk.Treeview(sumaDigitosHastaLaFechaGUI)

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

    sumaDigitosHastaLaFechaGUI.mainloop()



#SumaDigitos Anual
def sumarDigitosAnual(posicion,dataframe,ruta):

    sumaDigitosAnualGUI = Tk()

    #Ajustes del GUI MenuPrincipal
    frm = tk.Frame(sumaDigitosAnualGUI)
    frm.grid(column=0, row=1, padx=10, pady=10)
    sumaDigitosAnualGUI.geometry("1000x800")
    sumaDigitosAnualGUI.resizable(False,False)
    sumaDigitosAnualGUI.title("Depreciacion de Activos ATI")
    sumaDigitosAnualGUI.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="TABLA DEPRECIACION ANUAL MEDIANTE SUMA DIGITOS",font=("Arial",12)).grid(column=0,row=0)
    tk.Label(frm, text=" ").grid(column=0,row=3)

    #Variables a utilizar en metodo Suma Digitos para Depreciacion hasta la Fecha
    activo = posicion
    df = dataframe
    DetalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", DetalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamento = int(df.iloc[activo, 6])
    periodoRecuperacion = int(df.iloc[activo, 7])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    Fecha_Compra = df.iloc[activo, 4]
    moneda = df.iloc[activo, 5]
    fechaCompraObj = dt.datetime.strptime(Fecha_Compra, "%d/%m/%Y")
    año = fechaCompraObj.year+1
    depreciacionAcumulada = 0
    resultados = []
    parte2=periodoRecuperacion*(periodoRecuperacion+1)/2
    periodoOriginal=periodoRecuperacion
    periodo = 1
    #
    vidaUtil = periodoRecuperacion*(periodoRecuperacion+1)/2
    

    if periodoRecuperacion == 0:
        print("EL ACTIVO: ", DetalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo")
        sumarDigitosAnual()


    else:
        while periodo <= periodoOriginal:
            factor = (periodoOriginal - periodo + 1) / parte2
            depreciacion_anual = factor * (valorInicial - valorSalvamento)
            depreciacionAcumulada += depreciacion_anual
            valor_neto = valorInicial - depreciacionAcumulada
            resultados.append({
                "AÑO": año,
                "PERIODO": periodo,
                "DEPRECIACION ANUAL": depreciacion_anual,
                "DEPRECIACION ACUMULADA": depreciacionAcumulada,
                "VALOR EN LIBROS": valor_neto
            })
            periodo += 1
            año += 1
            dfResultado = pd.DataFrame(resultados)

        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['DEPRECIACION ACUMULADA'] = dfResultado['DEPRECIACION ACUMULADA'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)


        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", DetalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", Fecha_Compra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamento)
        print("Periodo de Recuperacion: ", periodoRecuperacion)
        print("")
        print("Vida Util del activo   ", vidaUtil)
        print("============================= Tabla de Proyeccion: Metodo Suma Digitos =============================")
     

        # Create a Treeview widget
        treeview = ttk.Treeview(sumaDigitosAnualGUI)

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

        GPTRequest(DetalleActivo)

    sumaDigitosAnualGUI.mainloop()
