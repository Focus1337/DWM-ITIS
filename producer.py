import time
import random
from faker import Faker

import pulsar
from pulsar.schema import Record, String, Integer

fake = Faker()
names = [fake.name() for _ in range(30)]


class TripEvent(Record):
    trip_id = Integer()
    client_name = String()
    price = Integer()


def random_price():
    return random.randint(1000, 30000)    

def random_id():
    return random.randint(1, 1000)

def random_name_id():
    return random.randint(1, 29)

TOPIC_NAME = 'persistent://public/default/clickhouse-test'


def create_event():
    event = TripEvent()
    event.trip_id = random_id()
    event.client_name = names[random_name_id()]
    event.price = random_price()
    return event


print("Starting producer")
client = pulsar.Client('pulsar://localhost:6650',
                           authentication=pulsar.AuthenticationBasic(username='admin', password='apachepulsar'))

producer = client.create_producer(topic=TOPIC_NAME, schema=pulsar.schema.JsonSchema(TripEvent))
while True:
    event = create_event()
    message_id = producer.send(event)
    print(f'Message: {event.trip_id} {event.client_name} {event.price}')
    time.sleep(1)