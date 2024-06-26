import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    
    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1.")
        return
    
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    
    if not (include_uppercase or include_lowercase or include_digits or include_special):
        messagebox.showerror("Error", "Select at least one character type.")
        return
    
    characters = ''
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    if len(characters) == 0:
        messagebox.showerror("Error", "No characters selected.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_text.delete(1.0, tk.END)  # Clear previous content
    password_text.insert(tk.END, password)  # Insert generated password

# GUI 
root = tk.Tk()
root.title("Random Password Generator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid()

# Password length input
ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_entry = ttk.Entry(main_frame, width=5)
length_entry.grid(row=0, column=1, sticky="w")
length_entry.insert(0, "12")  

# Character type checkboxes
uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(main_frame, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, sticky="w")

lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(main_frame, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=2, column=0, sticky="w")

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(main_frame, text="Digits", variable=digits_var)
digits_check.grid(row=3, column=0, sticky="w")

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(main_frame, text="Special Characters", variable=special_var)
special_check.grid(row=4, column=0, sticky="w")

# Generate button
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Display generated password
ttk.Label(main_frame, text="Generated Password:").grid(row=6, column=0, sticky="w", pady=(10, 0))
password_text = tk.Text(main_frame, height=1, width=30)
password_text.grid(row=6, column=1, sticky="w", pady=(10, 0))

# Run the main loop
root.mainloop()
