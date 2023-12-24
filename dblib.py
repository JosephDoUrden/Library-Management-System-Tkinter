import sqlite3

class UserDataManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("userDatabase.db")

    def create_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
        create table UserData (
            id   integer primary key autoincrement,
            role text NOT NULL,
            username text NOT NULL,
            password text NOT NULL,
            email text,
            phone integer      
        );
        """)
        self.conn.commit()
        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        data = [('user','yusufhan', 'yusufhan123', 'yusufhan@gmail.com', 11111111111),
                ('user','elif', 'elif123', 'elif1@gmail.com', 22222222222),
                ('user','russelG', 'russel12', 'russelG@yahoo.com', 0000000000),
                ('user','maria', 'mari3', 'maria@gmail.com', 66666666666),
                ('admin','admin', 'admin123', 'admin@gmail.com',11111111112)]

        for item in data:
            self.cur.execute("insert into UserData(role, username, password, email, phone) values(?, ?, ?, ?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from UserData")
        self.conn.commit()
        self.conn.close()

    def add_user(self, role, username, password, email, phone):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into UserData(role, username, password, email, phone) values(:role, :username, :password, :email, :phone)",
                    {"role": role,
                     "username": username,
                     "password": password,
                     "email": email,
                     "phone": phone})
        self.conn.commit()
        self.conn.close()

    def list_users(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from UserData")
        users = self.cur.fetchall()
        self.conn.close()
        return users

    def delete_user(self, gid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from UserData where id=?", [id])
        self.conn.commit()

    def edit_user(self, id, role, username, password, email, phone):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update UserData set role=?, username=?, password=?, email=?, phone=? where id=?",
                         [role, username, password, email, phone, id])
        self.conn.commit()
    
    def user_check(self, uname, password):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select role, username, password from UserData where username=? and password=?",
                          [uname, password])
        user = self.cur.fetchone()
        self.conn.close()
        return user
    
    def user_detail(self, username):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM UserData WHERE username=?", (username,))
        user = self.cur.fetchone()
        self.conn.close()
        return user

    def change_password(self, username, new_password):
        try:
            # Check if the user exists
            user = self.user_detail(username)
            if user:
                # Update the user's password
                self.conn = self.get_connection()
                self.cur = self.conn.cursor()
                self.cur.execute("UPDATE UserData SET password=? WHERE username=?", (new_password, username))
                self.conn.commit()
                self.conn.close()
                return True  # Password changed successfully
            else:
                return False  # User not found
        except sqlite3.Error as err:
            # Handle errors if necessary
            print("Error:", err)
            return False

