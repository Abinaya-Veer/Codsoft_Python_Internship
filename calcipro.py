import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields for numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Radio buttons for selecting the operation
operation_var = tk.StringVar()
operation_var.set("+")

operations = ["+", "-", "*", "/"]

operation_label = tk.Label(root, text="Choose operation:")
operation_label.pack(pady=5)

for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(anchor=tk.W)

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
