class Satelite:
    def __init__(self, nombre: str, numero_catalogo: int, latitud: float, longitud: float, altitud: float):
        if not (isinstance(nombre, str) and nombre.strip() and isinstance(numero_catalogo, int) and 
                -90 <= latitud <= 90 and -180 <= longitud <= 180 and altitud >= 100):
            raise ValueError("Parámetros de satélite inválidos.")

        self.nombre, self.numero_catalogo = nombre.strip(), numero_catalogo
        self.latitud, self.longitud, self.altitud = float(latitud), float(longitud), float(altitud)

    def tipo_orbita(self) -> str:
        if self.altitud < 2000: return "LEO"
        if self.altitud < 34000: return "MEO"
        if self.altitud <= 37000: return "GEO"
        return "HEO"

    def en_zona(self, lon_min: float, lat_min: float, lon_max: float, lat_max: float) -> bool:
        return lon_min <= self.longitud <= lon_max and lat_min <= self.latitud <= lat_max

    def __str__(self) -> str:
        return f"{self.nombre} | {self.numero_catalogo} | {self.tipo_orbita()} | {self.altitud:.1f} km"