import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\pythonServer')

import mysql.connector
import json
from Ingrediente import *
from DAO.ConexionBD import ConexionBD

class IngredienteDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarIngrediente(self, Ingrediente):
        print("LLEGUE aki")
        mensaje="No se pudo guardar."
        try:
            self.crearConexion()

            self._micur.execute("INSERT INTO Ingrediente(idIngrediente, nombre) values (%s, %s)", (Ingrediente.idIngrediente, Ingrediente.nombre))
            self._bd.commit()
            mensaje = "Ingrediente guardado."
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

if __name__ == '__main__':
    pass
    
        