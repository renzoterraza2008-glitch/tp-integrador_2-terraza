import sys
from catalogo import leer_catalogo, crear_catalogo, resumir_catalogo, obtener_satelites_en_zona

def main():
    if len(sys.argv) < 3:
        print("Uso correcto: python consultar_satelites.py archivo.json resumen")
        print("O bien: python consultar_satelites.py archivo.json zona lon_min lat_min lon_max lat_max")
        sys.exit(1)

    sats = crear_catalogo(leer_catalogo(sys.argv[1]))
    accion = sys.argv[2].lower()

    if accion == "resumen":
        for tipo, datos in resumir_catalogo(sats).items():
            if datos["cantidad"] > 0:
                print(tipo, "Cantidad:", datos["cantidad"], "| Min:", round(datos["min"], 1), "km | Max:", round(datos["max"], 1), "km | Prom:", round(datos["promedio"], 1), "km")
            else:
                print(tipo, "Cantidad: 0")

    elif accion == "zona" and len(sys.argv) == 7:
        lon1 = float(sys.argv[3])
        lat1 = float(sys.argv[4])
        lon2 = float(sys.argv[5])
        lat2 = float(sys.argv[6])
        
        zona = obtener_satelites_en_zona(sats, lon1, lat1, lon2, lat2)
        print("Satelites encontrados en la zona:", len(zona))
        for s in zona:
            print(s)
    else:
        print("Error en los datos ingresados.")

if __name__ == "__main__":
    main()