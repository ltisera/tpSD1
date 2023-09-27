class Calificacion():
    def __init__(self, idReceta="", usuario="", calificacion=""):
        self._idReceta = idReceta
        self._usuario = usuario
        self._calificacion = calificacion

   @property
    def idReceta(self):
        return self._idReceta

    @idReceta.setter
    def idReceta(self, id):
        self._idReceta = id

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = str(usuario)

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        self._calificacion = str(calificacion)
    
    def __str__(self):
        return str("id: " + str(" calificacion: " +
                   str(self.calificacion)))