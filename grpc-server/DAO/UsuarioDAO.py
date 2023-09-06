import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\grpc-server\Objetos')
sys.path.append(r'C:\Users\camil\Documents\GitHub\tpSD1\grpc-server\Objetos')
from Usuario import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD

class UsuarioDAO(ConexionBD):
    def __int__(self):
        pass
    
    def traerUsuarioSIMPLE(self, idUsuario):
        usTraido = None
        try:
            self.crearConexion()
            self.cursorDict()
            #self._micur.execute('SELECT idUsuario, email, tipoUsuario FROM usuario WHERE usuario.idUsuario = %s', (idUsuario,))
            self._micur.execute('SELECT * FROM usuario WHERE usuario.usuario = %s', (idUsuario,))
            usTraido = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return usTraido

    def agregarUsuario(self, usuario):
        print("agregar usuario")
        mensaje = "Alta Fail"
        try:
            self.crearConexion()

#            self._micur.execute("SELECT * FROM inscripcion where idReceta = %s and idExamen = %s", (idUsuario, idExamen))
#            inscripcion = self._micur.fetchone()
            self._micur.execute("INSERT INTO usuario(usuario, email, nombre, password, tipo) values (%s, %s, %s, %s, %s)", (usuario.idUsuario, usuario.email, usuario.nombre, usuario.password, usuario.tipo))
            self._bd.commit()
            mensaje = "Alta Exitosa"
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

    #Recetas favoritas

    def agregarFavorito(self, usuario, idReceta):
        mensaje = "Error."
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO receta_favorita(usuario, idReceta) values (%s, %s)", (usuario, idReceta))
            self._bd.commit()
            mensaje = "favorito guardado."

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

    def traerRecetasFavoritas(self, usuario):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            #agregar inner join
            self._micur.execute("SELECT receta_favorita.idReceta FROM receta_favorita WHERE receta_favorita.usuario = %s", (usuario,))
            listaDeRecetasFavoritas = self._micur.fetchall()
            for r in listaDeRecetasFavoritas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas

    #Seguir personas
    def seguirUsuario(self, follower, seguido):
        mensaje = "Error."
        if (follower != seguido):
            try:
                self.crearConexion()
                self._micur.execute("INSERT INTO siguiendo(Usuario_Seguidor, Usuario_Seguido) values (%s, %s)", (follower, seguido))
                self._bd.commit()
                mensaje = "Seguimiento guardado."

            except mysql.connector.errors.IntegrityError as err:
                print("Error: " + str(err))

            finally:
                self.cerrarConexion()
        
        return (mensaje)
    
    def traerUsuariosQueSigo(self, usuario):
        lstSeguidos = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT siguiendo.Usuario_Seguido FROM siguiendo WHERE siguiendo.Usuario_Seguidor = %s", (usuario,))
            listaDeSeguidos = self._micur.fetchall()
            for r in listaDeSeguidos:
                lstSeguidos.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstSeguidos

    def traerUsuariosQueMeSiguen(self, usuario):
        lstSeguidores = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT siguiendo.Usuario_Seguidor FROM siguiendo WHERE siguiendo.Usuario_Seguido = %s", (usuario,))
            listaDeRecetasSeguidores = self._micur.fetchall()
            for r in listaDeRecetasSeguidores:
                lstSeguidores.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstSeguidores

    

if __name__ == '__main__':

    udao = UsuarioDAO()

    us1 = Usuario(idUsuario="Elnombre2",email="loc@yahoo.com", nombre="Lucas", password="sinco", tipo= "admin")
    us2 = Usuario(idUsuario="alguien",email="fsdfsg@yahoo.com", nombre="gff", password="fgdsg", tipo= "sdgfsdg")
    
    #print(udao.agregarUsuario(us1))
    #print(udao.agregarUsuario(us2))
    #print(udao.seguirUsuario("Elnombre2","alguien"))

    print("Elnombre es seguido por :")
    print(udao.traerUsuariosQueMeSiguen("Elnombre2"))

    print("Elnombre sigue a :")
    print(udao.traerUsuariosQueSigo("Elnombre2"))

    print(udao.agregarFavorito("Elnombre2",1))
    print(udao.traerRecetasFavoritas("Elnombre2"))

    #print(udao.traerUsuarioSIMPLE("Elnombre"))

    print("Finnn eaaa")