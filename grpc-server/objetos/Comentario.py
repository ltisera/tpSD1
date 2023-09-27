class Comentario():
    def __init__(self, idComentario="", idReceta="", usuario="", comentario="", respondeA=None):
        self._idComentario = idComentario
        self._idReceta = idReceta
        self._usuario = usuario
        self._comentario = comentario
        self._respondeA = respondeA
    
    @property
    def idComentario(self):
        return self._idComentario

    @idComentario.setter
    def idComentario(self, id):
        self._idComentario = id

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
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._comentario = str(comentario)

    @property
    def respondeA(self):
        return self._respondeA

    @respondeA.setter
    def respondeA(self, respondeA):
        self._respondeA = str(respondeA)
    
    def __str__(self):
        return str("id: " + str(" comentario: " +
                   str(self.comentario)))