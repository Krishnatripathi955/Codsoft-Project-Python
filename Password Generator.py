import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        password_label.config(text="Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_password_callback():
    length = int(length_entry.get())
    password = generate_password(length)
    if password is not None:
        password_label.config(text=f"Generated Password: {password}")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

def copy_password_callback():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

def regenerate_password_callback():
    generate_password_callback()

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_callback)
generate_button.pack()

password_entry = tk.Entry(root, width=40)
password_entry.pack()

password_label = tk.Label(root, text="")
password_label.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password_callback)
copy_button.pack()

regenerate_button = tk.Button(root, text="Regenerate Password", command=regenerate_password_callback)
regenerate_button.pack()

root.mainloop()