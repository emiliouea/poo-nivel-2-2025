# Seguimiento de Temperaturas - Programación Tradicional

def ingresar_temperaturas(dias=7):
    """
    Función para ingresar temperaturas diarias
    
    Args:
        dias (int): Número de días para ingresar temperaturas (predeterminado 7)
    
    Returns:
        list: Lista de temperaturas ingresadas
    """
    temperaturas = []
    for dia in range(1, dias + 1):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
    
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Función para calcular el promedio semanal de temperaturas
    
    Args:
        temperaturas (list): Lista de temperaturas
    
    Returns:
        float: Promedio de temperaturas
    """
    if not temperaturas:
        return 0
    
    return sum(temperaturas) / len(temperaturas)

def mostrar_resumen(temperaturas):
    """
    Función para mostrar un resumen de las temperaturas
    
    Args:
        temperaturas (list): Lista de temperaturas
    """
    promedio = calcular_promedio_semanal(temperaturas)
    print("\n--- Resumen de Temperaturas ---")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Promedio semanal: {promedio:.2f}°C")
    
    # Información adicional
    print(f"Temperatura máxima: {max(temperaturas)}°C")
    print(f"Temperatura mínima: {min(temperaturas)}°C")

def main():
    """
    Función principal para ejecutar el programa de seguimiento de temperaturas
    """
    print("Programa de Seguimiento de Temperaturas")
    temperaturas_semanales = ingresar_temperaturas()
    mostrar_resumen(temperaturas_semanales)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
