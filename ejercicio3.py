print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2  # Usar el guion correcto para la resta
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        if self._num2 != 0:  # Comprobación para evitar división por cero
            resultado = self._num1 / self._num2  # División normal con decimales
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

# Crear instancias de la clase Calculadora y realizar las operaciones
operacion = Calculadora(55, 10)
operacion.suma()

operacion = Calculadora(90, 50)
operacion.resta()

operacion = Calculadora(43, 11)
operacion.division()

operacion = Calculadora(57, 9)
operacion.multiplicacion()
