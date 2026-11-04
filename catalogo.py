import json
from satelite import Satelite
from funciones_base import obtener_posicion

def leer_catalogo(ruta_json: str) -> list:
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def crear_catalogo(registros: list) -> list:
    satelites = []
    for reg in registros:
        try:
            lat, lon, alt = obtener_posicion(reg)
            nombre = reg.get("OBJECT_NAME", reg.get("nombre", "Desconocido"))
            catalogo = int(reg.get("NORAD_CAT_ID", reg.get("numero_catalogo", 0)))
            
            sat = Satelite(
                nombre=nombre,
                numero_catalogo=catalogo,
                latitud=lat,
                longitud=lon,
                altitud=alt
            )
            satelites.append(sat)
        except (ValueError, TypeError, KeyError):
            continue
    return satelites

def resumir_catalogo(satelites: list) -> dict:
    tipos = ["LEO", "MEO", "GEO", "HEO"]
    resumen = {}
    
    for tipo in tipos:
        sats_tipo = [s for s in satelites if s.tipo_orbita() == tipo]
        cantidad = len(sats_tipo)
        if cantidad > 0:
            altitudes = [s.altitud for s in sats_tipo]
            resumen[tipo] = {
                "cantidad": cantidad,
                "min": min(altitudes),
                "max": max(altitudes),
                "promedio": sum(altitudes) / cantidad
            }
        else:
            resumen[tipo] = {
                "cantidad": 0,
                "min": 0.0,
                "max": 0.0,
                "promedio": 0.0
            }
    return resumen

def obtener_satelites_en_zona(satelites: list, lon_min: float, lat_min: float, lon_max: float, lat_max: float) -> list:
    return [s for s in satelites if s.en_zona(lon_min, lat_min, lon_max, lat_max)]