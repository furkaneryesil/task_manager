import sqlite3

# SQLite veritabanı bağlantısı kurulumu
def create_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

create_db()
