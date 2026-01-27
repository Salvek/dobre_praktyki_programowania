import csv
import time

FILE_NAME = "tasks.csv"

def consume_tasks():
    """Odczytuje i przetwarza prace z pliku."""
    while True:
        tasks = []
        task_found = False

        try:
            with open(FILE_NAME, mode="r") as file:
                reader = csv.DictReader(file)
                tasks = list(reader)
        except FileNotFoundError:
            print("Brak pliku z zadaniami.")
            time.sleep(5)
            continue

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "in_progress"
                task_found = True
                print(f"Rozpoczęto wykonywanie zadania: {task['id']}")
                
                time.sleep(30)  
                task["status"] = "done"
                print(f"Zadanie {task['id']} zakończone.")
                break

        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "status"])
            writer.writeheader()
            writer.writerows(tasks)

        if not task_found:
            print("Brak zadań do wykonania. Czekam...")
            time.sleep(5)

if __name__ == "__main__":
    consume_tasks()
