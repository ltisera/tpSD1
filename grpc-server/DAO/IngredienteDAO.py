import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from objetos.Ingrediente import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD

from DAO.CONFIGS.variablesGlobales import TINGREDIENTE

class IngredienteDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarIngrediente(self, Ingrediente):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TINGREDIENTE + "(nombre) values (%s)", ( Ingrediente.nombre,))
            self._bd.commit()
            mensaje = "Ingrediente guardado"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def traerIngrediente(self, nombre):
        inTraido = None
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM " + TINGREDIENTE + " WHERE " + TINGREDIENTE + ".nombre = %s", (nombre,))
            inTraido = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return inTraido


    
        