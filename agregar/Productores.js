
// Productor kafka popularidadReceta

const { Kafka } = require('kafkajs');

async function popularidadReceta(idReceta, signo) {
  const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
  });

  const producer = kafka.producer();

  const mkafka = {
    idReceta: idReceta,
    popularidad: signo
  };

  console.log('Este es el JSON');
  console.log(mkafka);

  await producer.connect();
  await producer.send({
    topic: 'popularidadReceta',
    messages: [{ value: JSON.stringify(mkafka) }]
  });

  await producer.disconnect();
}

// Ejemplo de uso:
popularidadReceta(123, '+1');



//Productor kafka popularidadUsuario

const { Kafka } = require('kafkajs');

async function popularidadUsuario(usuario, signo) {
  const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
  });

  const producer = kafka.producer();

  const mkafka = {
    usuario: usuario,
    popularidad: signo
  };

  console.log('Este es el JSON');
  console.log(mkafka);

  await producer.connect();
  await producer.send({
    topic: 'popularidadUsuario',
    messages: [{ value: JSON.stringify(mkafka) }]
  });

  await producer.disconnect();
}

// Ejemplo de uso:
popularidadUsuario('juan', '+');



// Productor kafka comentario

const { Kafka } = require('kafkajs');

async function comentario(usuario, idReceta, comentario) {
  const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
  });

  const producer = kafka.producer();

  const mkafka = {
    usuario: usuario,
    idReceta: idReceta,
    comentario: comentario
  };

  console.log('Este es el JSON');
  console.log(mkafka);

  await producer.connect();
  await producer.send({
    topic: 'comentario',
    messages: [{ value: JSON.stringify(mkafka) }]
  });

  await producer.disconnect();
}

// Ejemplo de uso:
comentario('juan', 123, 'Este es un comentario de ejemplo');
