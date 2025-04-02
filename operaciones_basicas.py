"""Este módulo contiene clases que realizan operaciones matemáticas básicas,
como suma, resta y cálculo del promedio."""


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas como suma y resta."""

    def __init__(self):
        """Inicializa la operación con un resultado inicial de 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado de la operación realizada."""
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de un conjunto de números."""

    def __init__(self, valores):
        """Inicializa con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de los valores proporcionados."""
        suma = 0
        for valor in self.valores:
            suma += valor
        promedio_calculado = suma / len(self.valores)  # Cambio de nombre para evitar conflicto
        return promedio_calculado

    def mostrar_valores(self):
        """Muestra los valores ingresados."""
        return self.valores


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_resultado = calculadora_promedio.calcular_promedio()  # Cambio de nombre
    print(f"El promedio de los números es: {promedio_resultado}")
