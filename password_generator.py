import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x220")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Length Input
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
)
generate_button.pack(pady=10)

# Password Display
password_entry = tk.Entry(root, width=40, justify="center", font=("Arial", 12))
password_entry.pack(pady=5)

# Copy Button
copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    width=20
)
copy_button.pack(pady=10)

root.mainloop()