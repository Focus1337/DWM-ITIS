# https://pulsar.apache.org/docs/3.1.x/client-libraries-python-use/

import pulsar
import sys
from message import Message
from pulsar.schema import AvroSchema

client = pulsar.Client("pulsar://localhost:6650")

try:
    producer = client.create_producer("message-topic", schema=AvroSchema(Message))
    id = 1
    for line in sys.stdin:
        line = line.strip()
        message = Message(id = id, text = line, extra = "42")

        print(message)
        producer.send(message)
        id += 1

finally:
    client.close()