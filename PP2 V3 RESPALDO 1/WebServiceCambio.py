#Librerias
import requests
import datetime
import xml.etree.ElementTree as ElementTree


#Segun el sistema donde se ejecute el codigo
fechaActual = datetime.datetime.now()
parametroFechaActual = fechaActual.strftime("%d/%m/%Y")


def TipoDeCambioCompra():
   
    url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos"
    
    parametros = {
        "Indicador": 317,  # 317 corresponde al tipo de cambio de compra
        "FechaInicio": str(parametroFechaActual),
        "FechaFinal": str(parametroFechaActual),
        "Nombre": "n",  # n significa que no se requiere el nombre
        "SubNiveles": "n",  # n significa que no se requieren los subniveles
        "CorreoElectronico": "cpachecocerdas@gmail.com",
        "Token": "12ECSCR244"  # Debes reemplazar 'token' con tu token personal
    }
    respuesta = requests.get(url, params=parametros)
    return respuesta.text


def TipoDeCambioVenta():
   
    url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos"
    
    parametros = {
        "Indicador": 318,  # 317 corresponde al tipo de cambio de compra
        "FechaInicio": str(parametroFechaActual),
        "FechaFinal": str(parametroFechaActual),
        "Nombre": "n",  # n significa que no se requiere el nombre
        "SubNiveles": "n",  # n significa que no se requieren los subniveles
        "CorreoElectronico": "cpachecocerdas@gmail.com",
        "Token": "12ECSCR244"  # Debes reemplazar 'token' con tu token personal
    }
    respuesta = requests.get(url, params=parametros)
    return respuesta.text



def extraer_valor_compra(xml_data):
    root = ElementTree.fromstring(xml_data)
    for tipo_cambio in root.iter('INGC011_CAT_INDICADORECONOMIC'):
        if tipo_cambio.find('COD_INDICADORINTERNO').text == '317':
            return tipo_cambio.find('NUM_VALOR').text

    xml_compra = TipoDeCambioCompra()
    valor_compra = extraer_valor_compra(xml_compra)
    return valor_compra
print("VALOR DE COMPRA = ",extraer_valor_compra(TipoDeCambioCompra()))

def extraer_valor_venta(xml_data):
    root = ElementTree.fromstring(xml_data)
    for tipo_cambio in root.iter('INGC011_CAT_INDICADORECONOMIC'):
        if tipo_cambio.find('COD_INDICADORINTERNO').text == '318':
            return tipo_cambio.find('NUM_VALOR').text
        
    xml_venta = TipoDeCambioVenta()
    valor_venta = extraer_valor_venta(xml_venta)
    return valor_venta
print("VALOR DE VENTA = ",extraer_valor_venta(TipoDeCambioVenta()))

