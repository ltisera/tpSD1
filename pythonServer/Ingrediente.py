class Ingrediente():
    def __init__(self, nombre=""):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = str(nombre)
    

    def __str__(self):
        return str("id: " + str(" nombre: " +
                   str(self.nombre)))