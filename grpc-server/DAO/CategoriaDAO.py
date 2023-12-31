import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from objetos.Categoria import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD
from DAO.CONFIGS.variablesGlobales import TCATEGORIA

class CategoriaDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarCategoria(self, Categoria):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TCATEGORIA + "(nombre) values (%s)", ( Categoria.nombre,))
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
            self._micur.execute("SELECT * FROM " + TCATEGORIA + " WHERE " + TCATEGORIA + ".nombre = %s", (nombre,))
            caTraida = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return caTraida

if __name__ == '__main__':

    cat = Categoria(nombre="postre2")
    
    cdao = CategoriaDAO()

    print(cdao.agregarCategoria(cat))

    print("traer:")
    print(cdao.traerCategoria("postre"))

    print("Finnn eaaa")
    
        