import json
from kafka import KafkaProducer  


    ### Productor kafka popularidadReceta
def popularidadReceta(idReceta, signo):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  
    mkafka = {
        "idReceta": idReceta, 
        "popularidad" : signo
    }
    #signo + para agregar 1 o - para restar 1
    print("este es el json") 
    print(mkafka)
    producer.send(topic = 'popularidadReceta', value=json.dumps(mkafka).encode("utf-8"))
    producer.close()

### Productor kafka popularidadUsuario
def popularidadUsuario(usuario, signo):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  
    mkafka = {
        "usuario": usuario, 
        "popularidad" : signo
    }
    #signo + para agregar 1 o - para restar 1
    print("este es el json") 
    print(mkafka)
    producer.send(topic = 'popularidadUsuario', value=json.dumps(mkafka).encode("utf-8"))
    producer.close()

### Productor kafka comentario
def comentario(usuario, idReceta, comentario):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')  
    mkafka = {
        "usuario": usuario, 
        "idReceta" : idReceta,
        "comentario" : comentario
    }
    #signo + para agregar 1 o - para restar 1
    print("este es el json") 
    print(mkafka)
    producer.send(topic = 'comentario', value=json.dumps(mkafka).encode("utf-8"))
    producer.close()


if __name__ == '__main__':
    pass
    for i in range(40):
        popularidadReceta(12, "+")
        popularidadReceta(13, "+")