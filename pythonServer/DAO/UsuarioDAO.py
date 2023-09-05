import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\pythonServer')
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
    


    def traerListaRecetas(self, idUsuario, carreras):
        try:
            examenesDisponibles = []
            lstExamenes = []
            self.crearConexion()
            self.cursorDict()
            for c in carreras:
                print("de carrera imprimo su id ",c["idCarrera"])
                self._micur.execute("SELECT * FROM examen INNER JOIN carrera ON examen.idCarrera = carrera.idCarrera  WHERE examen.disponible = 1 and examen.idCarrera = %s", (c["idCarrera"],))
                examenesDeCarrera = self._micur.fetchall()
                for e in examenesDeCarrera:
                    examenesDisponibles.append(e)
            
            for examen in examenesDisponibles:
                self._micur.execute("SELECT * FROM inscripcion WHERE inscripcion.idUsuario =%s and inscripcion.idExamen =%s", (idUsuario, examen['idExamen']))
                inscripcion = self._micur.fetchone()
                
                if inscripcion == None:
                    lstExamenes.append(examen)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstExamenes

    def agregarUsuario(self, usuario):
        print("agregar usuario")
        try:
            self.crearConexion()

#            self._micur.execute("SELECT * FROM inscripcion where idReceta = %s and idExamen = %s", (idUsuario, idExamen))
#            inscripcion = self._micur.fetchone()
            self._micur.execute("INSERT INTO usuario(usuario, email, nombre, password, tipo) values (%s, %s, %s, %s, %s)", (usuario.idUsuario, usuario.email, usuario.nombre, usuario.password, usuario.tipo))
            self._bd.commit()
            mensaje = "receta guardada."
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

if __name__ == '__main__':

#    print("testing Usuario DAO")
#    print("Creando usuario local")
#    us1 = Usuario(idUsuario="Elnombre",email="loc@yahoo.com", nombre="Lucas", password="sinco", tipo= "admin")
#    print("Uss: ")
#    print(us1)
#    print("Persistiendo")
    
    udao = UsuarioDAO()

    print(udao.traerUsuarioSIMPLE("Elnombre"))

    print("Finnn eaaa")