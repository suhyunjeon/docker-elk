from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(acks=0,
              client_id='logstash',
              compression_type='gzip',
              bootstrap_servers=['localhost:9092'],
              key_serializer=None,
              value_serializer=lambda x: dumps(x).encode('utf-8'),
              )

TOPIC = 'test-log'
data = {'food': 'pizza'}
producer.send(TOPIC, value=data)
producer.flush()