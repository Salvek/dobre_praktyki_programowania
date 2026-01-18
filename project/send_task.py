import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="127.0.0.1")
)
channel = connection.channel()

channel.queue_declare(queue="image_tasks", durable=True)

task = {"image_file": "people.jpg"}

channel.basic_publish(
    exchange="",
    routing_key="image_tasks",
    body=json.dumps(task),
    properties=pika.BasicProperties(delivery_mode=2),
)

print("Task sent")

connection.close()
