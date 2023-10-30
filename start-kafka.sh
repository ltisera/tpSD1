cd kafka-3.6.0-src
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties
# Topic: novedades
# bin/kafka-topics.sh --create --topic novedades --bootstrap-server localhost:2181