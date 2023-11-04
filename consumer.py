# https://pulsar.apache.org/docs/3.1.x/client-libraries-python-use/

import pulsar
from message import Message
from pulsar.schema import AvroSchema
import psycopg2
#from records import Record, Integer, String

db_params = {
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432,
}

create_table_query = """
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL,
    text TEXT,
    extra TEXT
);
"""

def write_message_to_db(message):
    conn = None
    try:
        # Устанавливаем соединение с базой данных
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute(create_table_query)

        # Выполняем SQL-запрос для вставки данных в таблицу
        insert_query = "INSERT INTO messages (id, text, extra) VALUES (%s, %s, %s)"
        if hasattr(message, "extra"):
            extra = message.extra
        else:
            extra = None
        data = (message.id, message.text, extra)
        cursor.execute(insert_query, data)

        # Подтверждаем изменения
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print(f"Ошибка при записи в базу данных: {error}")
    finally:
        if conn is not None:
            conn.close()

client = pulsar.Client('pulsar://localhost:6650')

try:
    consumer = client.subscribe('message-topic', 'my-subscription', schema=AvroSchema(Message))
    while True:
        message = consumer.receive()
        print(message.value())
        write_message_to_db(message.value())
        consumer.acknowledge(message)

finally:
    client.close()