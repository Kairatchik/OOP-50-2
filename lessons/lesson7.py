import sqlite3

# Подключение к базе данных
db = sqlite3.connect("Users.db")
cursor = db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
    """)
    db.commit()

create_table()

def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?,?,?)',
        (name, age, hoby)
    )
    db.commit()
    print(f"Добавили {name}")

def update_user_by_rowid(name=None, age=None, hoby=None, rowid=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, rowid)
        )
    if age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, rowid)
        )
    if hoby:
        cursor.execute(
            'UPDATE users SET hoby = ? WHERE rowid = ?',
            (hoby, rowid)
        )
    
    db.commit()
    print('Update success')

def delete_user_by_rowid(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    db.commit()
    print('DELETE success')

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}, Hobby: {user[3]}")
    else:
        print("Список пользователей пуст")

def detail_view_user_by_id(user_id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    
    if user:
        print(f"Данные пользователя: ID: {user[0]}, Name: {user[1]}, Age: {user[2]}, Hobby: {user[3]}")
        return user
    else:
        print("Пользователь не найден")
        return None

# Тестовые вызовы
add_user("Ardager", 23, "спать")
add_user("Loli", 23, "спать")
add_user("John", 23, "спать")
add_user("Mike", 23, "спать")

get_all_users()
detail_view_user_by_id(2)

db.close()
