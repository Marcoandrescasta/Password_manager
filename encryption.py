from cryptography.fernet import Fernet

def generate_key():
    # Generate a new key
    return Fernet.generate_key()

def encrypt_password(password, key):
    # Encrypt a password using a key
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    # Decrypt an encrypted password using a key
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode()