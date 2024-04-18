# database.py
import sqlite3

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                               (website TEXT PRIMARY KEY, username TEXT, encrypted_password TEXT)''')
        self.conn.commit()

    def insert_password(self, website, username, encrypted_password):
        self.cursor.execute('''INSERT OR REPLACE INTO passwords (website, username, encrypted_password) VALUES (?, ?, ?)''',
                            (website, username, encrypted_password))
        self.conn.commit()

    def get_password(self, website):
        self.cursor.execute('''SELECT encrypted_password FROM passwords WHERE website=?''', (website,))
        password = self.cursor.fetchone()
        if password:
            return password[0]
        else:
            return None

    def update_password(self, website, encrypted_password):
        self.cursor.execute('''UPDATE passwords SET encrypted_password=? WHERE website=?''',
                            (encrypted_password, website))
        self.conn.commit()

    def delete_password(self, website):
        self.cursor.execute('''DELETE FROM passwords WHERE website=?''', (website,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
