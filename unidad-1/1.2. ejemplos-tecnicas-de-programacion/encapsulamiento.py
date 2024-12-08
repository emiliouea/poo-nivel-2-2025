class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados
        self.__titular = titular  # Privado
        self.__saldo = saldo_inicial  # Privado
        self._numero_cuenta = None  # Protegido

    # Métodos de acceso (getters)
    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

    # Métodos de modificación controlada
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

# Uso del encapsulamiento
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)  # Método controlado
print(cuenta.obtener_saldo())  # Acceso controlado