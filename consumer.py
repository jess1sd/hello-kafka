from kafka import KafkaConsumer

# Establish connection
consumer = KafkaConsumer('test-topic', bootstrap_servers='localhost:9092', group_id='my-group')

# Continuously poll for messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
