from satelite import Satelite
from catalogo import resumir_catalogo, obtener_satelites_en_zona

class EvaluadorCatalogo:
    def probar_todo(self):
        print("Iniciando pruebas de Catalogo...")
        self.probar_resumen()
        self.probar_zona()
        print("¡Todas las pruebas del catálogo pasaron con éxito!")
    def probar_resumen(self):
        sats = [
            Satelite("SAT-LEO", 1, 0.0, 0.0, 500.0),
            Satelite("SAT-GEO", 2, 0.0, 0.0, 35000.0)
        ]   
        resumen = resumir_catalogo(sats)
        assert resumen["LEO"]["cantidad"] == 1
        assert resumen["GEO"]["cantidad"] == 1
        assert resumen["LEO"]["min"] == 500.0
        print("[OK] Prueba de resumen de catálogo pasada.")

    def probar_zona(self):
        sats = [
            Satelite("SAT-BARILOCHE", 1, -41.0, -71.0, 500.0), 
            Satelite("SAT-LEJOS", 2, 10.0, 10.0, 500.0)       
        ]
        zona = obtener_satelites_en_zona(sats, -75.0, -45.0, -65.0, -35.0)
        assert len(zona) == 1
        assert zona[0].nombre == "SAT-BARILOCHE"
        print("[OK] Prueba de filtrado por zona pasada.")

if __name__ == "__main__":
    evaluador = EvaluadorCatalogo()
    evaluador.probar_todo()