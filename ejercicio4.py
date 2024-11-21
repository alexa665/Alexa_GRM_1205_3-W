print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Persona():
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        # Concatenamos correctamente con un espacio
        return f"{self.nombre} {self.apellido}"

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        # Usamos super() para inicializar la clase base
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)

estudiante = Estudiante("alexa", "manzo", "piloto aviador")
print(estudiante.nombre_completo())  
estudiante.mostrar_carrera()
