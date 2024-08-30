import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    """
    Generates a random password based on the specified length and complexity.
    
    :param length: Length of the password
    :param complexity: Complexity level (1: only lowercase letters, 
                                        2: lowercase and uppercase letters, 
                                        3: letters and digits, 
                                        4: letters, digits, and special characters)
    :return: Generated password
    """
    if complexity == 1:
        chars = string.ascii_lowercase
    elif complexity == 2:
        chars = string.ascii_letters
    elif complexity == 3:
        chars = string.ascii_letters + string.digits
    elif complexity == 4:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be between 1 and 4")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def on_generate_password():
    try:
        # Get user inputs from GUI
        length = int(length_entry.get())
        complexity = complexity_var.get()
        
        # Validate inputs
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return
        if complexity < 1 or complexity > 4:
            messagebox.showerror("Error", "Invalid complexity level. Please choose between 1 and 4.")
            return
        
        # Generate password
        password = generate_password(length, complexity)
        
        # Display the password
        result_label.config(text=f"Generated Password: {password}")
    
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Password length input
length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Complexity options
complexity_var = tk.IntVar()
complexity_var.set(1)  # Default value

complexity_label = tk.Label(root, text="Select password complexity:")
complexity_label.pack(pady=10)

complexity_options = [
    ("1 - Only lowercase letters", 1),
    ("2 - Lowercase and uppercase letters", 2),
    ("3 - Letters and digits", 3),
    ("4 - Letters, digits, and special characters", 4)
]

for text, value in complexity_options:
    tk.Radiobutton(root, text=text, variable=complexity_var, value=value).pack(anchor=tk.W)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_password)
generate_button.pack(pady=20)

# Result label to display generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
