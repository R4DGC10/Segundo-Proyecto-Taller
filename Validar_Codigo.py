#Librerias
import pandas as pd
import numpy as np


def validarCodigo():
  
  validez = True

  while validez:

    codigoActivo = str(input("Digite el codigo del activo a consultar -> "))
    ruta="fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    columnaID = df.iloc[:,0:1]
    listaIdentificadores = columnaID.iloc[1:]
    codigos = [str(codigo[0]) for codigo in listaIdentificadores.values]

    if codigoActivo in codigos:
      posicionActivo = np.where(np.array(codigos) == codigoActivo)[0][0] + 1
      return posicionActivo
    else:
      print("ADVERTENCIA: Activo NO encontrado! Por favor ingrese una opcion valida")
