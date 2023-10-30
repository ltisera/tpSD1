class Comentario():
    def __init__(self, idUsuario = None, idReceta = "", idComentario ="", comentario=""):
        self._idUsuario = idUsuario
        self._idReceta = idReceta
        self._idComentario = idComentario
        self._comentario = comentario

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self._idUsuario = idUsuario
    
    @property
    def idReceta(self):
        return self._idReceta
    
    @idReceta.setter
    def idReceta(self, idReceta):
        self._idReceta = idReceta

    @property
    def idComentario(self):
        return self._idComentario
    
    @idComentario.setter
    def idComentario(self, idComentario):
        self._idComentario = idComentario

    @property
    def comentario(self):
        return self._comentario
    
    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario

    def __str__(self):
        return str("idUsuario: " + str(self.idUsuario) +
                   " idReceta: " + str(self.idReceta) +
                   " idComentario: " + str(self.idComentario) +
                   " comentario: " + str(self.comentario))
    

    