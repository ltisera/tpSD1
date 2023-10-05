from kafka import KafkaConsumer
import time

# Configura el consumidor de Kafka
consumer = KafkaConsumer('popularidadUsuario', bootstrap_servers='localhost:9092')

while True:
    puntajes = {}
    
    for mensaje in consumer:
        puntos = 0
        
        # Procesa el mensaje aquí
        m = json.loads(mensaje.value.decode('utf-8'))  # Convierte el mensaje en un diccionario
        
        if m['signo'] == "+":
          puntos = 1
        elif m['signo'] == "-":
          puntos = -1
          
        if m['idUsuario'] in puntajes:
          puntajes[m['idUsuario']] += puntos
        
        else:
          # Si es la primera vez que se encuentra el idUsuario, agrégalo al diccionario con su puntaje
          puntajes[m['idUsuario']] = puntos
  
    pDAO = PopularidadDAO()
    for idUsuario, puntaje in puntajes.items():
      pDAO.sumarPopularodadUsuario(idUsuario, puntaje)

    # Espera durante una hora antes de volver a consumir
    time.sleep(3600)  # 3600 segundos = 1 hora


