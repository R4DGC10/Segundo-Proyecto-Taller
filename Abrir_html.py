#Librerias
import pandas as pd

def aperturaHTML():
    ruta="fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    return df
