import csv
import uuid
import time

FILE_NAME = "tasks.csv"

def add_task():
    """Dodaje nową pracę do pliku."""
    task_id = str(uuid.uuid4())
    task = {"id": task_id, "status": "pending"}
    
    file_exists = False
    try:
        with open(FILE_NAME, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "status"])
        if not file_exists: 
            writer.writeheader()
        writer.writerow(task)
        print(f"Zadanie {task_id} zostało dodane do kolejki.")

if __name__ == "__main__":
    while True:
        add_task()
        time.sleep(10)
