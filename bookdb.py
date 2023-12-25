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
            bid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            publication_year INTEGER,
            isbn TEXT,
            status TEXT DEFAULT 'available',
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
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, '9780743273565',  'Available', -1),
            ('To Kill a Mockingbird', 'Harper Lee', 'Classics', 1960, '9780061120084', 'Available', -1),
            ('1984', 'George Orwell', 'Dystopian', 1949, '9780451524935', 'Available', -1),
            ('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, '9780141439518',  'Available', -1),
            ('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 1951, '9780316769480', 'Available', -1),
            ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Magical Realism', 1967, '9780061120084', 'Available', -1),
            ('Moby-Dick', 'Herman Melville', 'Adventure', 1851, '9780142437247', 'Available', -1),
            ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, '9780547928227', 'Available', -1),
            ('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 1979, '9780345391803', 'Available', -1),
            ('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 1954, '9780545010221',  'Available', -1),
            ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997, '9780590353427',  'Available', -1),
            ('Brave New World', 'Aldous Huxley', 'Dystopian', 1932, '9780060850524', 'Available', -1),
            ('The Odyssey', 'Homer', 'Epic Poetry', 1900, '9780199536788',  'Available', -1),
            ('The Shining', 'Stephen King', 'Horror', 1977, '9780385121675', 'Available', -1),
            ('The Alchemist', 'Paulo Coelho', 'Philosophical Fiction', 1988, '9780061120084',  'Available', -1),
            ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, '9780307387899', 'Available', -1),
            ('Frankenstein', 'Mary Shelley', 'Gothic Fiction', 1818, '9780486282114', 'Available', -1),
            ('The Color Purple', 'Alice Walker', 'Historical Fiction', 1982, '9780156028356', 'Available', -1),
            ('Wuthering Heights', 'Emily Bront', 'Gothic Fiction', 1847, '9780141439556',  'Available', -1),
            ('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical Fiction', 1880, '9780140449242', 'Available', -1),
            ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'History', 2014, '9780062316097', 'Available', -1)]

        for item in data:
            self.cur.execute("INSERT INTO BookData (title, author, genre, publication_year, isbn, status, user_id ) VALUES (?, ?, ?, ?, ?, ?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from BookData")
        self.conn.commit()
        self.conn.close()

    def add_book(self, title, author, genre, publication_year, isbn, status, user_id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO BookData(title, author, genre, publication_year, isbn, status, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (title, author, genre, publication_year, isbn, status, user_id))
        self.conn.commit()
        self.conn.close()

    def list_books(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from BookData")
        books = self.cur.fetchall()
        self.conn.close()
        return books

    def delete_book(self, id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from BookData where bid=?", [id])
        self.conn.commit()

    def edit_book(self, bid, title, author, genre, publication_year, isbn, status, user_id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update BookData set title=?, author=?, genre=?, publication_year=?, isbn=?, status=?, user_id=? where bid=?",
                         [title, author, genre, publication_year, isbn, status, user_id, bid-1])
        self.conn.commit()
    
    #TODO update 
    def book_detail(self, bid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from BookData where bid=?", [bid])
        book = self.cur.fetchone()
        self.conn.close()
        return book
    
    def issue_book(self, book_id, user_id):
        try:
            # Check if the book is available
            book = self.book_detail(book_id)
            if book and book[6] == 'Available':
                # Update the book's status and assign it to the user
                self.conn = self.get_connection()
                self.cur = self.conn.cursor()
                self.cur.execute("UPDATE BookData SET status=?, user_id=? WHERE bid=?", ('Issued', user_id, book_id))
                self.conn.commit()
                self.conn.close()
                return True  # Book issued successfully
            else:
                return False  # Book not available
        except sqlite3.Error as err:
            # Handle errors if necessary
            print("Error:", err)
            return False

    def return_book(self, book_id):
        try:
            # Check if the book is issued
            book = self.book_detail(book_id)
            if book and book[6] == 'Issued':
                # Update the book's status to 'available' and remove the association with the user
                self.conn = self.get_connection()
                self.cur = self.conn.cursor()
                self.cur.execute("UPDATE BookData SET status=?, user_id=NULL WHERE bid=?", ('Available', book_id))
                self.conn.commit()
                self.conn.close()
                return True  # Book returned successfully
            else:
                return False  # Book not issued or not found
        except sqlite3.Error as err:
            # Handle errors if necessary
            print("Error:", err)
            return False

    def get_my_books(self, user_id):
        if user_id:
            self.conn = self.get_connection()
            self.cur = self.conn.cursor()
            self.cur.execute("select * from BookData WHERE user_id=?", [user_id])
            books = self.cur.fetchall()
            self.conn.close()
            return books
