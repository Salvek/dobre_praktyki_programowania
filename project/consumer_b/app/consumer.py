import json
import time
import cv2
import os
from app.rabbit import get_channel
from app.ai import count_people
from app.sender import send_result

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
IMAGES_DIR = os.path.join(BASE_DIR, "images")

channel = get_channel()

def local_file_to_image(filename: str) -> cv2.Mat:
    path = os.path.join(IMAGES_DIR, filename)
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Nie udało się wczytać obrazu: {path}")
    return image

def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        filename = data["image_file"]
        image = local_file_to_image(filename)
        count = count_people(image)
        send_result(filename, count)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"[INFO] Processed {filename}, people: {count}")
    except Exception as e:
        print(f"[WARN] Retry: {e}")
        time.sleep(2)


channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue="image_tasks", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="image_tasks", on_message_callback=callback, auto_ack=False)

print("Consumer started")
channel.start_consuming()
