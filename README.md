# Setup Kafka Locally and Test 
## Install Packages
``` 
$ pip install kafka-python
```

## Run Kafka locally

Go to https://kafka.apache.org/downloads and download the latest tar ball


Unzipped the tar zip by double-clicking or running:
``` 
$ tar -xf ~/kafka_2.13-3.7.0.tar.gz
``` 

Then 
```
$ cd kafka_2.13-3.7.0
```
Run ZooKeeper
```
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
Start Kafka Broker
``` 
$ bin/kafka-server-start.sh config/server.properties
```
Create Topic
``` 
$ bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092
```
Start a Producer, then type some message
``` 
$ bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
> test 1
```

Start a Consumer, and if you have published some messages, you would
see the message show up 
``` 
$ bin/kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092
test 1
```

## Run Python Scripts
Make sure your python is 3.11 or older. I've run into issues with package `six` when using
python 12+

Install python packages
``` 
$ python install kafka-client
```
Run python producer
``` 
$ python producer.py
```

Then, if you check the Consumer tab (if it's still open), you should see
```
test 1
Hello from Python Kafka Producer! 
```
You can also run the python consumer.py and you would see it receive the message
from `producer.py`:
``` 
$ python consumer.py
Received message: Hello from Python Kafka Producer!
```

Finally, you can try an example of reading a json and sending a json to the same topic
``` 
$ python json-example.py
```
If you go to any of the consumer app or tab that is still subscribing, you should see:
``` 
Received message: {"message": "Hello from Python with JSON!"}
```