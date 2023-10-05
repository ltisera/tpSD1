import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(CURRENT_DIR + '\\proto')
sys.path.append(CURRENT_DIR + '\\DAO')

from kafka import KafkaConsumer
import time
from DAO.RecetaDAO import RecetaDAO
import json



# Configura el consumidor de Kafka
consumer = KafkaConsumer('popularidadReceta', bootstrap_servers='localhost:9092', group_id="un grupo", auto_offset_reset='earliest', consumer_timeout_ms = 1)

while True:
    puntajes = {}
    leer_mensajes = True
    for mensaje in consumer:
        puntos = 0

        # Procesa el mensaje aquí
        # Convierte el mensaje en un diccionario
        m = json.loads(mensaje.value.decode('utf-8'))
        print(m)
        if m['popularidad'] == "+":
            puntos = 1
        elif m['popularidad'] == "-":
            puntos = -1

        if m['idReceta'] in puntajes:
            puntajes[m['idReceta']] += puntos

        else:
            # Si es la primera vez que se encuentra el idReceta, agrégalo al diccionario con su puntaje
            puntajes[m['idReceta']] = puntos
       
    pDAO = RecetaDAO()
    
    for idReceta, puntaje in puntajes.items():
        print(pDAO.popularidadReceta(idReceta, puntaje) + " idReceta: " + idReceta)

    print("duerme por una hora")
    # Espera durante una hora antes de volver a consumir
    time.sleep(3600)  # 3600 segundos = 1 hora
