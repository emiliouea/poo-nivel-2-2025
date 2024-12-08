class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def calcular_pago(self):
        # Sobrescritura del método de la clase padre
        return self.salario * 1.2  # Bonus del 20%

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def calcular_pago(self):
        return self.salario * 1.5  # Bonus del 50%