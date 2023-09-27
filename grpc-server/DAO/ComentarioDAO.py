import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from objetos.Comentario import *
import mysql.connector
import json
from mysql.connector import Error
from DAO.ConexionBD import ConexionBD
from DAO.CONFIGS.variablesGlobales import TCOMENTARIO

class ComentarioDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarComentario(self, comentario):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TCOMENTARIO + "(comentario, idReceta, usuario, respondeA) values (%s,%s,%s,%s)", ( comentario.comentario, comentario.idReceta, comentario.usuario, comentario.respondeA))
            self._bd.commit()
            mensaje = "Comentario guardado"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def traerComentarios(self, idReceta):
        lstComentarios = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT " + TCOMENTARIO + ".comentario FROM " + TCOMENTARIO + " WHERE " + TCOMENTARIO + ".idReceta = %s", (idReceta,))
            listaDeComentarios = self._micur.fetchall()
            for r in listaDeComentarios:
                lstComentarios.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstComentarios

if __name__ == '__main__':
    pass
    
        