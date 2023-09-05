import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\pythonServer')
sys.path.append(r'C:\Users\camil\Documents\GitHub\tpSD1\pythonServer')

from Categoria import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD

class CategoriaDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarCategoria(self, Categoria):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO Categoria(nombre) values (%s)", ( Categoria.nombre,))
            self._bd.commit()
            mensaje = "Categoria guardado"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def traerCategoria(self, nombre):
        caTraida = None
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute('SELECT * FROM Categoria WHERE Categoria.nombre = %s', (nombre,))
            caTraida = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return caTraida

if __name__ == '__main__':

    cat = Categoria(nombre="postre")
    
    cdao = CategoriaDAO()

    print(cdao.agregarCategoria(cat))

    print("traer:")
    print(cdao.traerCategoria("postre"))

    print("Finnn eaaa")
    
        