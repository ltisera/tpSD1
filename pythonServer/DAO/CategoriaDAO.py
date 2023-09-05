import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\pythonServer')

import mysql.connector
import json
from Categoria import *
from DAO.ConexionBD import ConexionBD

class CategoriaDAO(ConexionBD):
    def __int__(self):
        pass
    

    def agregarCategoria(self, Categoria):
        print("LLEGUE aki")
        mensaje="No se pudo guardar."
        try:
            self.crearConexion()

            self._micur.execute("INSERT INTO Categoria(nombre) values (%s, %s)", (Categoria.nombre))
            self._bd.commit()
            mensaje = "Categoria guardado."
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (mensaje)

if __name__ == '__main__':
    pass
    
        