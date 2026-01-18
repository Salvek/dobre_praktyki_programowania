import pika

print("Connecting...")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("127.0.0.1")
)
print("Connected")
connection.close()
