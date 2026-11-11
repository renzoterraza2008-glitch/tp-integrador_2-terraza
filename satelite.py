class Satelite:
    def __init__(self, nombre, numero_catalogo, latitud, longitud, altitud):
        if not (type(nombre) == str and len(nombre.strip()) > 0 and type(numero_catalogo) == int and -90 <= latitud <= 90 and -180 <= longitud <= 180 and altitud >= 100):
            raise ValueError("Datos invalidos")

        self.nombre = nombre.strip()
        self.numero_catalogo = numero_catalogo
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.altitud = float(altitud)

    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        elif self.altitud < 34000:
            return "MEO"
        elif self.altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def en_zona(self, lon_min, lat_min, lon_max, lat_max):
        condicion_lon = lon_min <= self.longitud <= lon_max
        condicion_lat = lat_min <= self.latitud <= lat_max
        return condicion_lon and condicion_lat

    def __str__(self):
        alt_str = str(round(self.altitud, 1))
        return self.nombre + " | " + str(self.numero_catalogo) + " | " + self.tipo_orbita() + " | " + alt_str + " km"