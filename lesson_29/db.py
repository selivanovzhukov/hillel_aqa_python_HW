import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        dbname=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASS", "password")
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);")
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def update_user(user_id, name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s WHERE id = %s;", (name, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()