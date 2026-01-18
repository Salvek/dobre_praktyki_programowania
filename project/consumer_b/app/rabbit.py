import pika
import time

def get_channel():
    for i in range(10):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
            return connection.channel()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ nie jest gotowy, próba ponownie...")
            time.sleep(3)
    raise Exception("Nie udało się połączyć z RabbitMQ")
