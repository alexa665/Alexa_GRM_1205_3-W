print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))

moto = Moto(2, "Gris", "$50000")
print("OBJETO = moto")
moto.cantidad()

print("OBJETO = carro")
carro = Carro(4, "Negro", "$150000")
carro.cantidad()
