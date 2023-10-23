import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import mysql.connector
import json
from objetos.Receta import *
from objetos.Ingrediente import *
from DAO.ConexionBD import ConexionBD
from DAO.IngredienteDAO import IngredienteDAO
from DAO.CategoriaDAO import CategoriaDAO
from DAO.CONFIGS.variablesGlobales import TRECETA, TRECETAFAVORITA,TCOMENTARIOS
from kafka import KafkaProducer
from mysql.connector import Error

producer = KafkaProducer(bootstrap_servers='localhost:9092')

class ComentarioDAO(ConexionBD):
    def __int__(self):
        pass
    def traerComentarios(self, idReceta):
        lstComentarios = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM " + TCOMENTARIOS + " WHERE idReceta = %s", (idReceta,))
            listaDeComentarios = self._micur.fetchall()
            for r in listaDeComentarios:
                lstComentarios.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstComentarios
    def agregarComentario(self, comentario):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TCOMENTARIOS + "(idReceta, idUsuario, comentario) values (%s, %s, %s)", ( comentario.idReceta, comentario.idUsuario, comentario.comentario))
            self._bd.commit()
            mensaje = "Comentario guardado"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    def eliminarComentario(self, idComentario):
        mensaje = "Error"
        try:
            self.crearConexion()
            self._micur.execute("DELETE FROM " + TCOMENTARIOS + " WHERE idComentario = %s", (idComentario,))
            self._bd.commit()
            mensaje = "Comentario eliminado"
        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
   
        