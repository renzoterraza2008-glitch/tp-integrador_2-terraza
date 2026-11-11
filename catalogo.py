import json
from satelite import Satelite
from funciones_base import obtener_posicion

def leer_catalogo(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    return datos

def crear_catalogo(registros):
    lista_satelites = []
    for reg in registros:
        try:
            lat, lon, alt = obtener_posicion(reg)
            nombre = reg["OBJECT_NAME"]
            cat = int(reg["NORAD_CAT_ID"])
            sat = Satelite(nombre, cat, lat, lon, alt)
            lista_satelites.append(sat)
        except:
            continue
    return lista_satelites

def resumir_catalogo(sats):
    tipos = ["LEO", "MEO", "GEO", "HEO"]
    resumen = {}
    
    for t in tipos:
        filtrados = []
        for s in sats:
            if s.tipo_orbita() == t:
                filtrados.append(s)
        
        cant = len(filtrados)
        if cant > 0:
            altitudes = []
            for s in filtrados:
                altitudes.append(s.altitud)
            
            resumen[t] = {
                "cantidad": cant,
                "min": min(altitudes),
                "max": max(altitudes),
                "promedio": sum(altitudes) / cant
            }
        else:
            resumen[t] = {"cantidad": 0, "min": 0.0, "max": 0.0, "promedio": 0.0}
    return resumen

def obtener_satelites_en_zona(sats, lon_min, lat_min, lon_max, lat_max):
    resultado = []
    for s in sats:
        if s.en_zona(lon_min, lat_min, lon_max, lat_max):
            resultado.append(s)
    return resultado