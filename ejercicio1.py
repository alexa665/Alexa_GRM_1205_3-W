print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Estudiante():
    def __init__(self, nombre, calif):
        self.nombre = nombre
        self.calif = calif

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.calif}")

    def resultados(self):
        if self. calif >= 7:
            print("PASASTE!")
        else:
            print("REPROBASTE!")

# Crear instancias de Estudiante
estudiante1 = Estudiante("alexa", 9)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("maria", 9)
estudiante2.imprimir()
estudiante2.resultados()
