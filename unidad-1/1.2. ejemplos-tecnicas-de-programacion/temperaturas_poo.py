# Seguimiento de Temperaturas - Programación Orientada a Objetos

class RegistroTemperaturas: 
    def __init__(self, dias=7): 
        self._dias = dias
        self._temperaturas = []
    
    def ingresar_temperaturas(self):
        """
        Método para ingresar temperaturas diarias
        """
        print(f"Ingrese las temperaturas para {self._dias} días:")
        for dia in range(1, self._dias + 1):
            while True:
                try:
                    temperatura = float(input(f"Día {dia}: "))
                    self._temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Error: Ingrese un valor numérico válido.")
    
    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas
        
        Returns:
            float: Promedio de temperaturas
        """
        if not self._temperaturas:
            return 0
        
        return sum(self._temperaturas) / len(self._temperaturas)
    
    def mostrar_resumen(self):
        """
        Método para mostrar un resumen de las temperaturas
        """
        promedio = self.calcular_promedio_semanal()
        print("\n--- Resumen de Temperaturas ---")
        print(f"Temperaturas registradas: {self._temperaturas}")
        print(f"Promedio semanal: {promedio:.2f}°C")
        
        # Información adicional
        print(f"Temperatura máxima: {max(self._temperaturas)}°C")
        print(f"Temperatura mínima: {min(self._temperaturas)}°C")
    
def main():
    """
    Función principal para ejecutar el programa de seguimiento de temperaturas
    """
    print("Programa de Seguimiento de Temperaturas (POO)")
    registro = RegistroTemperaturas()
    registro.ingresar_temperaturas()
    registro.mostrar_resumen()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
