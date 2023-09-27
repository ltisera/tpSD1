class Usuario():
    def __init__(self, idUsuario = None, email = "", nombre ="", password="", tipo = "", popularidad=""):
        self._idUsuario = idUsuario
        self._email = email
        self._nombre = nombre
        self._password = password
        self._tipo = tipo
        self._popularidad = popularidad
    
    @property
    def idUsuario(self):
        return self._idUsuario
    
    @idUsuario.setter
    def idUsuario(self, id):
        self._idUsuario = id

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email (self, email):
        self._email = email
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password (self, password):
        self._password = password
    

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo (self, tipo):
        self._tipo = tipo

    @property
    def popularidad(self):
        return self._popularidad
    
    @popularidad.setter
    def popularidad (self, popularidad):
        self._popularidad = popularidad

    def __str__(self):
        return str (
            "idUsuario: " + str(self.idUsuario) +
            " email: " + str(self.email) +
            " nombre: " + str(self.nombre) +
            " password: " + str(self.nombre) +
            " tipo = " + str(self.nombre) +
            " popularidad= " + str(self.popularidad)
        )


if __name__ == '__main__':
    print("Main de Usuario para test")
    print("Creando usuaruio us1")
    us1 = Usuario(email="loc@yahoo.com", nombre="Lucas", password="sinco", tipo= "admin")
    print("Imprimiendo us1")
    print(us1)
    print("impreso... Izi Usuario")
    