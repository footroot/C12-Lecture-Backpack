import sqlite3

class BookDatabaseManager:

    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def create_table(self):
        with self.db:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL,
                author VARCHAR(50) NOT NULL,
                year_pub INTEGER NOT NULL
                );
                """)
            
    def insert_book(self, title, author, year_pub):
        with self.db:
            self.cursor.execute(f"""INSERT INTO Books(title, author, year_pub)
                VALUES (
                    '{title}',
                    '{author}',
                     {year_pub}
                );
                """)
            
    def delete_book(self, id):
        with self.db:
            self.cursor.execute(f"DELETE FROM Books WHERE ID={id};")

    def view_books(self):
        self.cursor.execute("SELECT * FROM Books;")
        for record in self.cursor:
            print(record)
            
    def close_connection(self):
        self.db.close()
    



db_manager = BookDatabaseManager("library.sqlite")
# db_manager.create_table()
# db_manager.insert_book("This is my NEW book!", "ME", 2026)
# db_manager.delete_book(2)
db_manager.view_books()
db_manager.close_connection()