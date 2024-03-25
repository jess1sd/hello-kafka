from kafka import KafkaProducer

# Establish a connection to the Kafka broker
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message to the specified topic
message = "Hello from Python Kafka Producer!"
producer.send('test-topic', message.encode('utf-8'))
producer.flush()  # Ensure the message is sent
