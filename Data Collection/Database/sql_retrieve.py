import sqlite3
import os

def read_sql_data():
    db_file = os.path.join(os.path.dirname(__file__), "sample.db")
    
    # Create dummy DB if not exists
    if not os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE users (id int, name text)''')
        c.execute("INSERT INTO users VALUES (1, 'Alice')")
        c.execute("INSERT INTO users VALUES (2, 'Bob')")
        conn.commit()
        conn.close()
        print(f"Created sample database at {db_file}")

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        print("SQL Data:")
        for row in rows:
            print(row)
        conn.close()
    except Exception as e:
        print(f"Error reading SQL database: {e}")

if __name__ == "__main__":
    read_sql_data()
