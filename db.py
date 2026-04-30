import sqlite3

DB_NAME = "db.sqlite3"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

# جدول کاربران
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        counter_search INTEGER DEFAULT 3,
        counter_get INTEGER DEFAULT 3
    )
""")
    # جدول گروه‌ها
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        chat_id TEXT PRIMARY KEY
    )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# عملیات روی جدول کاربران
# -------------------------------
def add_user(user_id, counter_search=10, counter_get=3):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, counter_search, counter_get) VALUES (?, ?, ?)",
        (user_id, counter_search, counter_get)
    )
    conn.commit()
    conn.close()

def decrease_counter_search(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET counter_search = counter_search - 1 WHERE user_id = ?", (user_id,))
    conn.commit()
    cursor.execute("SELECT counter_search FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def decrease_counter_get(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET counter_get = counter_get - 1 WHERE user_id = ?", (user_id,))
    conn.commit()
    cursor.execute("SELECT counter_get FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None# -------------------------------

def get_counter_search(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT counter_search FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def get_counter_get(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT counter_get FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# عملیات روی جدول گروه‌ها
# -------------------------------
def add_group(chat_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO groups (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()

def get_group(chat_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM groups WHERE chat_id = ?", (chat_id,))
    group = cursor.fetchone()
    conn.close()
    return group

def delete_group(chat_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM groups WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()

def get_all_groups():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM groups")
    groups = cursor.fetchall()
    conn.close()
    return groups
