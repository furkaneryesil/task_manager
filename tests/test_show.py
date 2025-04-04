import sqlite3

def test_show_tasks():
    conn = sqlite3.connect('../tasks.db')
    cursor = conn.cursor()
    
    print("\n=== Görev Listesi ===")
    cursor.execute("SELECT id, task_name, completed FROM tasks")
    tasks = cursor.fetchall()
    
    if not tasks:
        print("Görev listeniz boş!")
    else:
        for task in tasks:
            task_id, task_name, completed = task
            status = "Tamamlandı" if completed else "Tamamlanmadı"
            print(f"ID: {task_id} | Görev: {task_name} | Durum: {status}")
    
    conn.close()

if __name__ == "__main__":
    test_show_tasks()
