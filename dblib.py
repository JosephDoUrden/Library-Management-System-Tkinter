import sqlite3

class GradeBookManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("gradebook.db")

    def create_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
        create table GradeBook (
            gid   integer primary key autoincrement,
            fname text,
            lname text,
            grade integer
        );
        """)
        self.conn.commit()
        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        data = [('Melissa', 'Bishop', 70),
                ('Linda', 'Scanlon', 55),
                ('Russel', 'Gruver', 60),
                ('Maria', 'Mayes', 100),
                ('Dennis', 'Hill', 95),
                ('Nathan', 'Martin', 40),
                ('William', 'Biggs', 85),
                ('Lois', 'Ballard', 60),
                ('Larry', 'Manning', 50),
                ('Dustin', 'Smalls', 30),
                ('Alice', 'Lucas', 70),
                ('John', 'Howell', 90)]

        for item in data:
            self.cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from GradeBook")
        self.conn.commit()
        self.conn.close()

    def add_grade(self, fname, lname, grade):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into GradeBook(fname, lname, grade) values(:first, :last, :grade)",
                    {"first": fname,
                     "last": lname,
                     "grade": grade})
        self.conn.commit()
        self.conn.close()

    def list_grades(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from GradeBook")
        grades = self.cur.fetchall()
        self.conn.close()
        return grades

    def get_stats(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select count(*), avg(grade) from GradeBook")
        stats = self.cur.fetchone()
        self.conn.close()
        return stats

    def delete_grade(self, gid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from GradeBook where gid=?", [gid])
        self.conn.commit()

    def edit_grade(self, gid, fname, lname, grade):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update GradeBook set fname=?, lname=?, grade=? where gid=?",
                         [fname, lname, grade, gid])
        self.conn.commit()
