class Satelite:
    def __init__(self, nombre: str, numero_catalogo: int, latitud: float, longitud: float, altitud: float):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no debe estar vacío.")
        if not isinstance(numero_catalogo, int):
            raise ValueError("El número de catálogo debe ser un entero.")
        if not (-90 <= latitud <= 90):
            raise ValueError("La latitud debe estar entre -90 y 90.")
        if not (-180 <= longitud <= 180):
            raise ValueError("La longitud debe estar entre -180 y 180.")
        if altitud < 100:
            raise ValueError("La altitud debe ser de al menos 100 km.")

        self.nombre = nombre.strip()
        self.numero_catalogo = numero_catalogo
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.altitud = float(altitud)

    def tipo_orbita(self) -> str:
        if self.altitud < 2000:
            return "LEO"
        elif 2000 <= self.altitud < 34000:
            return "MEO"
        elif 34000 <= self.altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def en_zona(self, lon_min: float, lat_min: float, lon_max: float, lat_max: float) -> bool:
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)

    def __str__(self) -> str:
        return f"{self.nombre} | {self.numero_catalogo} | {self.tipo_orbita()} | {self.altitud:.1f} km"