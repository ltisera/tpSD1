import mysql.connector

from DAO.RecetaDAO import RecetaDAO

from Receta import *

adminreceta = RecetaDAO()
larec = Receta("1","Tomate",pasos = "paso 1", tiempoEnMinutos="3", categoria ="alguna",creador="Mathov")
adminreceta.agregarReceta(larec)
print(larec.creador);