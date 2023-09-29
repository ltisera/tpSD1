from kafka import KafkaConsumer

# Configura las opciones del consumidor
consumer = KafkaConsumer(
    'novedades',
    bootstrap_servers='localhost:9092',  # Reemplaza con la dirección de tu servidor Kafka
    group_id="un grupo",  # Puedes usar cualquier grupo de consumidores
    auto_offset_reset='latest',  # Lee desde la posición más reciente
    enable_auto_commit=False  # Desactiva el auto commit
)




# Obtiene la cantidad total de mensajes en el tema
consumer.poll()
consumer.seek_to_end()
assignment = list(consumer.assignment())
# Verificar si hay particiones antes de continuar
if assignment:
    # Obtener la cantidad total de mensajes en la primera partición
    total_messages = consumer.position(assignment[0])
    # Lleva un registro de cuántos mensajes has consumido
    num_messages_to_read = 5
    messages_read = 0

    # Resto del código para leer los últimos mensajes
    # Lee los últimos 5 mensajes en orden inverso
    for _ in range(num_messages_to_read):
        position = total_messages - messages_read - 1
        consumer.seek(assignment[0], position)
        message = next(consumer)
        print('Mensaje leído: {}'.format(message.value.decode('utf-8')))
        messages_read += 1


    # Cierra el consumidor al final
    consumer.close()
else:
    print("No se asignaron particiones al consumidor.")

    


# Cierra el consumidor al final
