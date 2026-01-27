import sqlite3
import uuid
import time

DB_NAME = "tasks.db"

def initialize_db():
    """Inicjalizuje bazę danych, jeśli jeszcze nie istnieje."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            status TEXT
        )
        """)
        conn.commit()

def add_task():
    """Dodaje nowe zadanie do bazy danych."""
    task_id = str(uuid.uuid4())
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (id, status) VALUES (?, ?)", (task_id, "pending"))
        conn.commit()
        print(f"Zadanie {task_id} zostało dodane do kolejki.")

if __name__ == "__main__":
    initialize_db()
    while True:
        add_task()
        time.sleep(10)
