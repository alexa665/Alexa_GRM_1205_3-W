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

# Ejemplo de uso:
estudiante = Estudiante("Juan", "Pérez", "Ingeniería")
print(estudiante.nombre_completo())  # Imprime el nombre completo
estudiante.mostrar_carrera()         # Imprime la carrera
