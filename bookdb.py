import sqlite3

class BookManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("bookDatabase.db")

    def create_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE BookData (
            gid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            publication_year INTEGER,
            isbn TEXT,
            available_copies INTEGER,
            total_copies INTEGER,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES UserData(id)
        );
        """)
        self.conn.commit()
        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()

        data = [
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, '9780743273565', 10, 15,1),
            ('To Kill a Mockingbird', 'Harper Lee', 'Classics', 1960, '9780061120084', 8, 12,2),
            ('1984', 'George Orwell', 'Dystopian', 1949, '9780451524935', 5, 10,3),
            ('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, '9780141439518', 12, 18,4),
            ('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 1951, '9780316769480', 7, 14, 0),
            ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Magical Realism', 1967, '9780061120084', 6, 12,0),
            ('Moby-Dick', 'Herman Melville', 'Adventure', 1851, '9780142437247', 9, 15,0),
            ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, '9780547928227', 11, 20,0),
            ('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 1979, '9780345391803', 8, 15,0),
            ('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 1954, '9780545010221', 10, 18,0),
            ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997, '9780590353427', 15, 25,0),
            ('Brave New World', 'Aldous Huxley', 'Dystopian', 1932, '9780060850524', 7, 12,0),
            ('The Odyssey', 'Homer', 'Epic Poetry', -700, '9780199536788', 10, 16,0),
            ('The Shining', 'Stephen King', 'Horror', 1977, '9780385121675', 6, 12,0),
            ('The Alchemist', 'Paulo Coelho', 'Philosophical Fiction', 1988, '9780061120084', 12, 20,0),
            ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, '9780307387899', 8, 14,0),
            ('Frankenstein', 'Mary Shelley', 'Gothic Fiction', 1818, '9780486282114', 9, 16,0),
            ('The Color Purple', 'Alice Walker', 'Historical Fiction', 1982, '9780156028356', 7, 12,0),
            ('Wuthering Heights', 'Emily BrontÃ«', 'Gothic Fiction', 1847, '9780141439556', 10, 18,0),
            ('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical Fiction', 1880, '9780140449242', 6, 12,0),
            ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'History', 2014, '9780062316097', 15, 25,0)
        ]

        for item in data:
            self.cur.execute("INSERT INTO BookData (title, author, genre, publication_year, isbn, available_copies, total_copies, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from BookData")
        self.conn.commit()
        self.conn.close()

    def add_book(self, title, author, genre, publication_year, isbn, available_copies, total_copies, user_id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO BookData(title, author, genre, publication_year, isbn, available_copies, total_copies, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (title, author, genre, publication_year, isbn, available_copies, total_copies, user_id))
        self.conn.commit()
        self.conn.close()

    def list_books(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from BookData")
        users = self.cur.fetchall()
        self.conn.close()
        return users

    def delete_book(self, id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from BookData where bid=?", [id])
        self.conn.commit()

    def edit_book(self, title, author, genre, publication_year, isbn, available_copies, total_copies):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update BookData set title=?, author=?, genre=?, publication_year=?, isbn=?, available_copies=?, total_copies=? where bid=?",
                         [title, author, genre, publication_year, isbn, available_copies, total_copies, id])
        self.conn.commit()
    
    #TODO update 
    def book_detail(self, book):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from BookData where username=?", [book])
        user = self.cur.fetchone()
        self.conn.close()
        return user

