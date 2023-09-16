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
from DAO.CONFIGS.variablesGlobales import TRECETA, TRECETAFAVORITA, TINGREDIENTEDERECETA 

from mysql.connector import Error


class RecetaDAO(ConexionBD):
    def __int__(self):
        pass
    

    def traerRecetas(self):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM " + TRECETA + "")
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas
    def traerRecetasXFiltro(self, 
        tiempoEnMinutosMIN,
        tiempoEnMinutosMAX,
        categoria,
        creador,
        titulo,
        idReceta
    ):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            queryBase="SELECT * FROM " + TRECETA + " WHERE {}.titulo is not null ".format(TRECETA)
            if (tiempoEnMinutosMAX != ""):
                queryBase += "AND {}.tiempoEnMinutos <= {} ".format(TRECETA,tiempoEnMinutosMAX)
            if (tiempoEnMinutosMIN != ""):
                queryBase += "AND {}.tiempoEnMinutos >= {} ".format(TRECETA,tiempoEnMinutosMIN)
            if (categoria != ""):
                queryBase += "AND {}.categoria = '{}' ".format(TRECETA,categoria)
            if (creador != ""):
                queryBase += "AND {}.creador = '{}' ".format(TRECETA,creador)
            if (titulo != ""):
                queryBase += "AND {}.titulo LIKE '%{}%' ".format(TRECETA,titulo)
            if (idReceta != ""):
                queryBase += "AND {}.idReceta = {} ".format(TRECETA,idReceta)
            print(queryBase)
            self._micur.execute(queryBase)
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
            self._micur.execute("SELECT * FROM " + TRECETA + " WHERE " + TRECETA + ".categoria = %s", (categoria,))
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
            self._micur.execute("SELECT * FROM " + TRECETA + " WHERE " + TRECETA + ".creador = %s", (creador,))
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas
    
    def traerRecetasxIngrediente(self, ingrediente):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT " + TRECETA + ".idReceta, " + TRECETA + ".titulo, " + TRECETA + ".descripcion, " + TRECETA + ".foto1, " + TRECETA + ".tiempoEnMinutos, " + TRECETA + ".categoria, " + TRECETA + ".creador FROM " + TINGREDIENTEDERECETA + " INNER JOIN " + TRECETA + " ON " + TINGREDIENTEDERECETA + ".idReceta = " + TRECETA + ".idReceta WHERE " + TINGREDIENTEDERECETA + ".ingrediente = %s", (ingrediente,))
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas

    def traerRecetasxTiempo(self, tpMin, tpMax):
        lstRecetas = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT * FROM " + TRECETA + " WHERE " + TRECETA + ".tiempoEnMinutos BETWEEN %s and %s", (tpMin, tpMax))
            listaDeRecetas = self._micur.fetchall()
            for r in listaDeRecetas:
                lstRecetas.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstRecetas



    #Recetas favoritas

    def agregarFavorito(self, usuario, idReceta):
        mensaje = "Error."
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TRECETAFAVORITA + "(usuario, idReceta) values (%s, %s)", (usuario, idReceta))
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
            self._micur.execute("SELECT " + TRECETA + ".idReceta, " + TRECETA + ".titulo, " + TRECETA + ".foto1, " + TRECETA + ".tiempoEnMinutos, " + TRECETA + ".creador FROM " + TRECETAFAVORITA + " INNER JOIN " + TRECETA + " ON " + TRECETAFAVORITA + ".idReceta = " + TRECETA + ".idReceta WHERE " + TRECETAFAVORITA + ".usuario = %s", (usuario,))
            listaDeRecetasFavoritas = self._micur.fetchall()
            for r in listaDeRecetasFavoritas:
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
            self._micur.execute("SELECT * FROM " + TRECETA + " WHERE " + TRECETA + ".idReceta = %s", (idReceta,))
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
            self._micur.execute("INSERT INTO " + TRECETA + "(idReceta, titulo, descripcion, foto1, foto2, foto3, foto4, foto5, pasos, tiempoEnMinutos, categoria, creador) values (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)", (receta.idReceta, receta.titulo, receta.descripcion, receta.foto1, receta.foto2, receta.foto3, receta.foto4, receta.foto5, receta.pasos, receta.tiempoEnMinutos, receta.categoria, receta.creador))
            self._bd.commit()
            mensaje = "receta guardada."                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def agregarIngredienteAReceta(self, receta, ingrediente, cantidad, tipoDeMedida):
        idao = IngredienteDAO().agregarIngrediente(Ingrediente(ingrediente))
        mensaje = "Error."
        try:
            self.crearConexion()
            self._micur.execute("INSERT INTO " + TINGREDIENTEDERECETA + "(idReceta, ingrediente, cantidad, tipoDeMedida) values (%s, %s, %s, %s)", (receta, ingrediente, cantidad, tipoDeMedida))
            self._bd.commit()
            mensaje = "Agregado a ingredientes"

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)
    
    def traerIngredientesDeReceta(self, receta):
        lstIngredientes = []
        try:
            self.crearConexion()
            self.cursorDict()
            self._micur.execute("SELECT " + TINGREDIENTEDERECETA + ".ingrediente, " + TINGREDIENTEDERECETA + ".cantidad, " + TINGREDIENTEDERECETA + ".tipoDeMedida FROM " + TINGREDIENTEDERECETA + " WHERE " + TINGREDIENTEDERECETA + ".idReceta = %s", (receta,))
            listaDeIngredientes = self._micur.fetchall()
            for r in listaDeIngredientes:
                lstIngredientes.append(r)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstIngredientes

if __name__ == '__main__':
    
    rdao = RecetaDAO()

    rec = Receta(titulo="flan",tiempoEnMinutos=5,categoria="Cena",descripcion="Rico", creador="roberto", pasos="1)hacer el flan")
    

    print(rdao.agregarReceta(rec))

    print("traer:")
    print(rdao.traerReceta(3))
    
    #print(rdao.agregarIngredienteAReceta(1, "Azucar", 10, "gramos"))

    print("Finnn eaaa")
    
        