import sqlite3


conn = sqlite3.connect('vuln.db')

def create_database():
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students;")
    cursor.execute(
        """
        CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE
        )
        """
    )
    cursor.executemany(
        """INSERT INTO students (first_name, last_name, email)
        VALUES (?, ?, ?)""", (("John", "Doe", "john@doe.com"),
                              ("Peter", "Parker", "peter@gmail.com"),
                              ("Tina", "Johnson", "tina@yahoomail.com"),))
    
    conn.commit()
    
def user_search():
    cursor = conn.cursor()

    user_input = input("Enter First Name: ")

    query = f"SELECT * FROM students WHERE first_name = '{user_input}';"
    print(f"Query: {query}")

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for record in results:
                print(record)
        else:
            print("No results!")
    except sqlite3.Error as e:
        print(f"Error: {e}")

create_database()
user_search()
conn.close()