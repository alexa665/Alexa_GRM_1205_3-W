print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Crear una instancia de Persona solicitando al usuario los datos
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))

# Llamar al método cumpleaños dos veces
p.cumpleaños()

# Imprimir el nombre y la edad actualizada
print(f"{p.nombre} cumple {p.edad} años")
