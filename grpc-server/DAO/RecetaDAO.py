import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import mysql.connector
import json
from objetos.Receta import *
from DAO.ConexionBD import ConexionBD

from mysql.connector import Error


class RecetaDAO(ConexionBD):
    def __int__(self):
        pass
    

    def traerRecetas(self):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM Receta")
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas
    

    def traerRecetasxCategoria(self, categoria):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM Receta WHERE Receta.categoria = %s", (categoria,))
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas

    def traerRecetasxCreador(self, creador):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM Receta WHERE Receta.creador = %s", (creador,))
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas

    def traerReceta(self, idReceta):
        usTraido = None
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute('SELECT * FROM Receta WHERE Receta.idReceta = %s', (idReceta,))
            usTraido = self._micur.fetchone()
        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
        
        return usTraido

    def agregarReceta(self, receta):
        print("LLEGUE aki")
        print(receta)
        mensaje="Error."
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO Receta(idReceta, titulo, descripcion, foto1, foto2, foto3, foto4, foto5, pasos, tiempoEnMinutos, categoria, creador) values (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)", (receta.idReceta, receta.titulo, receta.descripcion, receta.foto1, receta.foto2, receta.foto3, receta.foto4, receta.foto5, receta.pasos, receta.tiempoEnMinutos, receta.categoria, receta.creador))
            self._bd.commit()
            mensaje = "receta guardada."
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def agregarIngredienteAReceta(self, receta, ingrediente, cantidad, tipoDeMedida):
        mensaje = "Error."
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO receta_has_ingrediente(idReceta, ingrediente, cantidad, tipoDeMedida) values (%s, %s, %s, %s)", (receta, ingrediente, cantidad, tipoDeMedida))
            self._bd.commit()
            mensaje = "ingrediente guardado."

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

if __name__ == '__main__':
    
    rdao = RecetaDAO()

    rec = Receta(titulo="flan",tiempoEnMinutos=5,categoria="Cena",descripcion="Rico", creador="roberto", pasos="1)hacer el flan")
    

    print(rdao.agregarReceta(rec))

    print("traer:")
    print(rdao.traerReceta(3))
    
    #print(rdao.agregarIngredienteAReceta(1, "Azucar", 10, "gramos"))

    print("Finnn eaaa")
    
        