import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from objetos.Calificacion import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD
from DAO.CONFIGS.variablesGlobales import TCALIFICACION

class CalificacionDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarCalificacion(self, calificacion):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TCALIFICACION + "(calificacion, idReceta, usuario) values (%s,%s,%s)", ( calificacion.calificacion, calificacion.idReceta, calificacion.usuario))
            self._bd.commit()
            mensaje = "Calificacion guardada"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def traerCalificacion(self, receta, usuario):
        caTraida = None
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM " + TCALIFICACION + " WHERE " + TCALIFICACION + ".receta = %s" + TCALIFICACION + ".usuario = %s", (receta, usuario))
            caTraida = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return caTraida

if __name__ == '__main__':
    pass
    
        