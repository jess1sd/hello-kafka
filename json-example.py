import json
from kafka import KafkaProducer, KafkaConsumer

# Producer with JSON serializer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

data = {'message': 'Hello from Python with JSON!'}
producer.send('test-topic', data)
producer.flush()

# Consumer with JSON deserializer
consumer = KafkaConsumer('test-topic', bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         group_id='my-group')

for message in consumer:
    print(f"Received message: {message.value}")
