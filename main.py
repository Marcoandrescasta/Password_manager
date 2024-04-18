# main.py
import tkinter as tk
from password_manager import PasswordManager

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        
        self.password_manager = PasswordManager("passwords.db")

        # Create GUI elements
        self.label_website = tk.Label(master, text="Website:")
        self.label_username = tk.Label(master, text="Username:")
        self.label_password = tk.Label(master, text="Password:")
        
        self.entry_website = tk.Entry(master)
        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")

        self.button_add = tk.Button(master, text="Add Password", command=self.add_password)
        self.button_get = tk.Button(master, text="Get Password", command=self.get_password)

        # Layout GUI elements
        self.label_website.grid(row=0, column=0, sticky="e")
        self.label_username.grid(row=1, column=0, sticky="e")
        self.label_password.grid(row=2, column=0, sticky="e")
        
        self.entry_website.grid(row=0, column=1)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_get.grid(row=4, column=0, columnspan=2)

    def add_password(self):
        website = self.entry_website.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        if website and username and password:
            self.password_manager.add_password(website, username, password)
            self.clear_entries()

    def get_password(self):
        website = self.entry_website.get()
        if website:
            password = self.password_manager.get_password(website)
            if password:
                self.entry_password.delete(0, tk.END)
                self.entry_password.insert(0, password)

    def clear_entries(self):
        self.entry_website.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
