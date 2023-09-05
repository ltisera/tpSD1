class Ingrediente():
    def __init__(self, idIngrediente=None, nombre=""):
        self._idIngrediente = idIngrediente
        self._nombre = nombre
        

    @property
    def idIngrediente(self):
        return self._idIngrediente

    @idIngrediente.setter
    def idIngrediente(self, id):
        self._idIngrediente = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = str(nombre)
    

    def __str__(self):
        return str("id: " + str(self.idIngrediente)
                   + " nombre: " +
                   str(self.nombre))