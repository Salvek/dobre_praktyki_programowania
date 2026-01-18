import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq")
)
channel = connection.channel()
channel.queue_declare(queue="image_tasks", durable=True)

def publish(data: dict):
    channel.basic_publish(
        exchange="",
        routing_key="image_tasks",
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
