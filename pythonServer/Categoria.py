class Categoria():
    def __init__(self, idCategoria=None, nombre=""):
        self._idCategoria = idCategoria
        self._nombre = nombre
        

    @property
    def idCategoria(self):
        return self._idCategoria

    @idCategoria.setter
    def idCategoria(self, id):
        self._idCategoria = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = str(nombre)
    

    def __str__(self):
        return str("id: " + str(self.idCategoria)
                   + " nombre: " +
                   str(self.nombre))