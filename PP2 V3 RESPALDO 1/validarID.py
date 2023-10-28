import pandas as pd
import numpy as np


def validar_activo(ID):
    ruta = "fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    columnaID = df.iloc[:, 0:1]
    listaIdentificadores = columnaID.iloc[1:]
    codigos = [str(codigo[0]) for codigo in listaIdentificadores.values]

    if ID in codigos:
        return True
    else:
        return False
    
def obtienePosicion(ID):
    ruta = "fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    columnaID = df.iloc[:, 0:1]
    listaIdentificadores = columnaID.iloc[1:]
    codigos = [str(codigo[0]) for codigo in listaIdentificadores.values]

    if ID in codigos:
      posicionActivo = np.where(np.array(codigos) == ID)[0][0] + 1
      return posicionActivo
    else:
        None