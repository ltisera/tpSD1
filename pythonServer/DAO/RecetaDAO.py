import sys

sys.path.append(r'C:\Users\LucsPC\Downloads\distribuidos\Entrega\tpBDR\tpSD1\pythonServer')

import mysql.connector
import json
from Receta import *
from DAO.ConexionBD import ConexionBD

class RecetaDAO(ConexionBD):
    def __int__(self):
        pass
    


    def traerListaRecetas(self, idUsuario, carreras):
        try:
            examenesDisponibles = []
            lstExamenes = []
            self.crearConexion()
            self.cursorDict()
            for c in carreras:
                print("de carrera imprimo su id ",c["idCarrera"])
                self._micur.execute("SELECT * FROM examen INNER JOIN carrera ON examen.idCarrera = carrera.idCarrera  WHERE examen.disponible = 1 and examen.idCarrera = %s", (c["idCarrera"],))
                examenesDeCarrera = self._micur.fetchall()
                for e in examenesDeCarrera:
                    examenesDisponibles.append(e)
            
            for examen in examenesDisponibles:
                self._micur.execute("SELECT * FROM inscripcion WHERE inscripcion.idUsuario =%s and inscripcion.idExamen =%s", (idUsuario, examen['idExamen']))
                inscripcion = self._micur.fetchone()
                
                if inscripcion == None:
                    lstExamenes.append(examen)

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return lstExamenes

    def agregarReceta(self, receta):
        print("LLEGUE aki")
        mensaje="Ya estabas inscripto."
        try:
            self.crearConexion()

#            self._micur.execute("SELECT * FROM inscripcion where idReceta = %s and idExamen = %s", (idUsuario, idExamen))
#            inscripcion = self._micur.fetchone()
            self._micur.execute("INSERT INTO receta(idReceta, titulo, tiempoEnMinutos, categoria, creador) values (%s, %s, %s, %s, %s)", (receta.idReceta, receta.titulo, receta.tiempoEnMinutos, receta.categoria, receta.creador))
            self._bd.commit()
            mensaje = "receta guardada."
#            self._micur.execute("SELECT * FROM inscripcion where idUsuario = %s and idExamen = %s", (idUsuario, idExamen))
            inscripcion = self._micur.fetchone()
                

        except mysql.connector.errors.IntegrityError as err:
            print("Error: " + str(err))

        finally:
            self.cerrarConexion()
        
        return (inscripcion, mensaje)

if __name__ == '__main__':

    #print("TEST INSCRIPCIONNNNNNNNNNNNNNNNNNN")
    #print(alumnoDao.inscripcionAExamen(2,1))

    #print("EXAMENES A RENDIR")
    #print(alumnoDao.traerExamenesARendir(2))

    #print("Responder pregunta")
    #alumnoDao.responderPregunta(1,2,1)
    #alumnoDao.responderPregunta(1,3,1)

    #print("FINALIZAR EXAMEN")
    #alumnoDao.finalizarExamen(1,2)

    print("RENDIR EXAMEN")
    
        