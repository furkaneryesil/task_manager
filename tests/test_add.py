import sqlite3

def test_add_task():
    conn = sqlite3.connect('../tasks.db')
    cursor = conn.cursor()
    
    print("\n=== Görev Ekleme Testi ===")
    task_name = "Test Görevi"
    
    cursor.execute("INSERT INTO tasks (task_name, completed) VALUES (?, ?)", (task_name, False))
    conn.commit()
    task_id = cursor.lastrowid
    
    print(f"Görev eklendi! ID: {task_id}, Görev: {task_name}")
    conn.close()

if __name__ == "__main__":
    test_add_task()
