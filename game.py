import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Stone', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    # Update the result labels
    user_label.config(text=f"Your choice: {user_choice}")
    computer_label.config(text=f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!")
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="You Lose!")

# Create the main application window
root = tk.Tk()
root.title("Stone, Paper, Scissors")

# Create labels and buttons for user input
instruction_label = tk.Label(root, text="Choose Stone, Paper, or Scissors:")
instruction_label.pack(pady=20)

# Buttons for Stone, Paper, Scissors
stone_button = tk.Button(root, text="Stone", width=15, command=lambda: determine_winner("Stone"))
stone_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: determine_winner("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: determine_winner("Scissors"))
scissors_button.pack(pady=5)

# Labels to display the choices
user_label = tk.Label(root, text="Your choice: ")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer's choice: ")
computer_label.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=('Helvetica', 16))
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
