class Receta():
    def __init__(self, idReceta=None, titulo="", descripcion="", foto1="", foto2="", foto3="", foto4="", foto5="", pasos="", tiempoEnMinutos="", categoria="", creador="", popularidad=""):
        self._idReceta = idReceta
        self._titulo = titulo
        self.descripcion = descripcion
        self._pasos = pasos
        self._tiempoEnMinutos = tiempoEnMinutos
        self._categoria = categoria
        self._creador = creador
        self._foto1 = foto1
        self._foto2 = foto2
        self._foto3 = foto3
        self._foto4 = foto4
        self._foto5 = foto5
        self._lstIngredientes = []
        self._popularidad = popularidad
        

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
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = str(descripcion)

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

    @property
    def foto1(self):
        return self._foto1

    @foto1.setter
    def foto1(self, foto1):
        self._foto1 = foto1

    #2
    @property
    def foto2(self):
        return self._foto2

    @foto2.setter
    def foto2(self, foto2):
        self._foto2 = foto2

    #3
    @property
    def foto3(self):
        return self._foto3

    @foto3.setter
    def foto3(self, foto3):
        self._foto3 = foto3

    #4
    @property
    def foto4(self):
        return self._foto4

    @foto4.setter
    def foto4(self, foto4):
        self._foto4 = foto4

    #5
    @property
    def foto5(self):
        return self._foto5

    @foto5.setter
    def foto5(self, foto5):
        self._foto5 = foto5

    @property
    def lstIngredientes(self):
        return self._lstIngredientes

    @lstIngredientes.setter
    def lstIngredientes(self, lst):
        self._lstIngredientes = lst

    @property
    def popularidad(self):
        return self._popularidad
    
    @popularidad.setter
    def popularidad (self, popularidad):
        self._popularidad = popularidad

    def __str__(self):
        return str("id: " + str(self.idReceta)
                   + " titulo: " +
                   str(self.titulo) + " descripcion: " +
                   str(self.descripcion) + " pasos: " +
                   str(self.pasos) + " tiempoEnMinutos: " +
                   str(self._tiempoEnMinutos) + " creador: " +
                   str(self._creador) + " categoria: " +
                   str(self._categoria) + " popularidad= " + 
                   str(self.popularidad)
        )