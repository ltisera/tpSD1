class Usuario():
    def __init__(self, idUsuario = None, email = "", nombre ="", constraseña="", tipo = ""):
        self._idUsuario = idUsuario
        self._email = email
        self._nombre = nombre
        self._contraseña = constraseña
        self._tipo = tipo
    
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
    def constraseña(self):
        return self._constraseña
    
    @nombre.setter
    def constraseña (self, constraseña):
        self._constraseña = constraseña
    

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo (self, tipo):
        self._tipo = tipo

    def __str__(self):
        return str (
            "idUsuario: " + str(self.idUsuario) +
            " email: " + str(self.email) +
            " nombre: " + str(self.nombre) +
            " constraseña: " + str(self.nombre) +
            " tipo = " + str(self.nombre)
        )


if __name__ == '__main__':
    print("Main de Usuario para test")
    print("Creando usuaruio us1")
    us1 = Usuario(email="loc@yahoo.com", nombre="Lucas", constraseña="sinco", tipo= "admin")
    print("Imprimiendo us1")
    print(us1)
    print("impreso... Izi Usuario")
    