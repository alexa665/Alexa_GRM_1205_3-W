print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, universidad, especialidad, nombre, edad):
        Universidad.__init__(self, universidad)
        Carrera.__init__(self, especialidad)
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.nombre}.")

persona = Estudiante("cbtis 128", "programasion", "alexa", 15)
persona.datos()
