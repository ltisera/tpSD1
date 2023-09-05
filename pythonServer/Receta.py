class Receta():
    def __init__(self, idReceta=None, titulo="", foto1="", foto2="", foto3="", foto4="", foto5="", pasos="", tiempoEnMinutos="", categoria="",creador=""):
        self._idReceta = idReceta
        self._titulo = titulo
        self._pasos = pasos
        self._tiempoEnMinutos = tiempoEnMinutos
        self._categoria = categoria
        self._creador = creador
        

    @property
    def idReceta(self):
        return self._idReceta

    @idReceta.setter
    def idReceta(self, id):
        self._idReceta = id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = str(titulo)

    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self, pasos):
        self._pasos = str(pasos)

    @property
    def tiempoEnMinutos(self):
        return self._tiempoEnMinutos

    @tiempoEnMinutos.setter
    def tiempoEnMinutos(self, tiempoEnMinutos):
        self._tiempoEnMinutos = tiempoEnMinutos

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria



    @property
    def creador(self):
        return self._creador

    @creador.setter
    def creador(self, creador):
        self._creador = creador


    def __str__(self):
        return str("id: " + str(self.idReceta)
                   + " titulo: " +
                   str(self.titulo) + " pasos: " +
                   str(self.pasos) + " tiempoEnMinutos: " +
                   str(self._tiempoEnMinutos) + " creador: " +
                   str(self._creador) + " categoria: " +
                   str(self._categoria))