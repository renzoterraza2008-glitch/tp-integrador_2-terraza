import sys
from catalogo import leer_catalogo, crear_catalogo, resumir_catalogo, obtener_satelites_en_zona

def main():
    if len(sys.argv) < 3:
        print("Uso: python consultar_satelites.py <archivo.json> [resumen | zona <lon_min> <lat_min> <lon_max> <lat_max>]")
        sys.exit(1)

    satelites = crear_catalogo(leer_catalogo(sys.argv[1]))
    accion = sys.argv[2].lower()

    if accion == "resumen":
        for tipo, datos in resumir_catalogo(satelites).items():
            if datos["cantidad"] > 0:
                print(f"{tipo} -> Cantidad: {datos['cantidad']} | Mín: {datos['min']:.1f} km | Máx: {datos['max']:.1f} km | Promedio: {datos['promedio']:.1f} km")
            else:
                print(f"{tipo} -> Cantidad: 0")

    elif accion == "zona" and len(sys.argv) == 7:
        lon_min, lat_min, lon_max, lat_max = map(float, sys.argv[3:7])
        sats_zona = obtener_satelites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max)
        
        print(f"Satélites en la zona ({len(sats_zona)})")
        for sat in sats_zona:
            print(sat)
    else:
        print("Error")

if __name__ == "__main__":
    main()