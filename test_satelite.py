from satelite import Satelite

class EvaluadorSatelite:
    def probar_todo(self):
        self.probar_creacion_valida()
        self.probar_tipos_orbita()
        self.probar_zona()
        print("todas las pruebas manuales pasaron con éxito")

    def probar_creacion_valida(self):
        sat = Satelite("ISS (ZARYA)", 25544, -30.5, -60.2, 419.7)
        assert sat.nombre == "ISS (ZARYA)"
        assert sat.tipo_orbita() == "LEO"
        print("prueba de creación válida pasada.")

    def probar_tipos_orbita(self):
        s1 = Satelite("SAT1", 1, 0, 0, 1500)
        s2 = Satelite("SAT2", 2, 0, 0, 15000)
        s3 = Satelite("SAT3", 3, 0, 0, 35000)
        s4 = Satelite("SAT4", 4, 0, 0, 40000)
        
        assert s1.tipo_orbita() == "LEO"
        assert s2.tipo_orbita() == "MEO"
        assert s3.tipo_orbita() == "GEO"
        assert s4.tipo_orbita() == "HEO"
        print("prueba de tipos de órbita pasada.")

    def probar_zona(self):
        sat = Satelite("SAT5", 5, -41.0, -71.0, 500) 
        dentro = sat.en_zona(-75.0, -45.0, -65.0, -35.0)
        assert dentro == True
        print("prueba de zona geográfica pasada.")

if __name__ == "__main__":
    evaluador = EvaluadorSatelite()
    evaluador.probar_todo()