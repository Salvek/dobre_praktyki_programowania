import sqlite3
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

def consume_tasks():
    """Odczytuje i przetwarza zadania z bazy danych."""
    while True:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM tasks WHERE status = 'pending' LIMIT 1")
            task = cursor.fetchone()
            
            if task:
                task_id = task[0]
                print(f"Rozpoczęto wykonywanie zadania: {task_id}")
                
                cursor.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ?", (task_id,))
                conn.commit()
                
                time.sleep(30) 

                cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
                conn.commit()
                print(f"Zadanie {task_id} zakończone.")
            else:
                print("Brak zadań do wykonania. Czekam...")
                time.sleep(5)

if __name__ == "__main__":
    initialize_db()
    consume_tasks()
