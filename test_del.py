import sqlite3

def test_delete_task():
    conn = sqlite3.connect('../tasks.db')
    cursor = conn.cursor()
    
    print("\n=== Görev Silme Testi ===")
    task_id = input("Silmek istediğiniz görevin ID'sini girin: ")
    
    cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    
    if task:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        print(f"ID: {task_id} olan görev silindi!")
    else:
        print(f"ID: {task_id} olan görev bulunamadı!")
    
    conn.close()

if __name__ == "__main__":
    test_delete_task()
