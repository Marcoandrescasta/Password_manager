# password_manager.py
from encryption import encrypt_password, decrypt_password, generate_key
from database import Database

class PasswordManager:
    def __init__(self, db_filename):
        self.db = Database(db_filename)
        self.db.create_table()
        self.key = generate_key()

    def add_password(self, website, username, password):
        encrypted_password = encrypt_password(password, self.key)  # Encrypt the password
        self.db.insert_password(website, username, encrypted_password)

    def get_password(self, website):
        encrypted_password = self.db.get_password(website)
        print("Type of encrypted_password:", type(encrypted_password))
        if encrypted_password:
            return decrypt_password(encrypted_password, self.key)
        else:
            return None

    def update_password(self, website, new_password):
        encrypted_password = encrypt_password(new_password)  # Encrypt the new password
        self.db.update_password(website, encrypted_password)

    def delete_password(self, website):
        self.db.delete_password(website)
