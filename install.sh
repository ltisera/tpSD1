pip install mysql-connector-python grpcio-tools
# https://kafka.apache.org/quickstart
# wget https://downloads.apache.org/kafka/3.6.0/kafka-3.6.0-src.tgz
tar -xzf kafka-3.6.0-src.tgz
cd ./kafka-3.6.0-src
./gradlew jar -PscalaVersion=2.13.11