import sqlite3

def test_complete_task():
    conn = sqlite3.connect('../tasks.db')
    cursor = conn.cursor()
    
    print("\n=== Görev Tamamlama Testi ===")
    task_id = input("Tamamlandı olarak işaretlemek istediğiniz görevin ID'sini girin: ")
    
    cursor.execute("SELECT id, task_name, completed FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    
    if task:
        task_id, task_name, completed = task
        
        if completed:
            print(f"ID: {task_id} olan görev zaten tamamlanmış!")
        else:
            cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
            conn.commit()
            print(f"ID: {task_id} olan '{task_name}' görevi tamamlandı olarak işaretlendi!")
    else:
        print(f"ID: {task_id} olan görev bulunamadı!")
    
    conn.close()

if __name__ == "__main__":
    test_complete_task()
