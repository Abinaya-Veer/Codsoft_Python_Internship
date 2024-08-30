import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Initialize contact book as an empty dictionary
contact_book = {}

# Load contacts from a JSON file (if exists)
try:
    with open("contacts.json", "r") as f:
        contact_book = json.load(f)
except FileNotFoundError:
    pass

# Save contacts to a JSON file
def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contact_book, f)

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact's name:")
    if name in contact_book:
        messagebox.showerror("Error", "Contact already exists!")
        return
    
    phone = simpledialog.askstring("Input", "Enter contact's phone number:")
    email = simpledialog.askstring("Input", "Enter contact's email:")
    address = simpledialog.askstring("Input", "Enter contact's address:")
    
    contact_book[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts()
    update_contact_list()

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contact_book.items():
        contact_list.insert(tk.END, f"{name}: {details['phone']}")

# Function to search a contact
def search_contact():
    search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
    found = False
    for name, details in contact_book.items():
        if search_term == name or search_term == details['phone']:
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            found = True
            break
    if not found:
        messagebox.showerror("Error", "Contact not found!")

# Function to update an existing contact
def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
    if name not in contact_book:
        messagebox.showerror("Error", "Contact not found!")
        return

    phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact_book[name]['phone'])
    email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact_book[name]['email'])
    address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact_book[name]['address'])

    contact_book[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts()
    update_contact_list()

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
    if name in contact_book:
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?")
        if confirm:
            del contact_book[name]
            save_contacts()
            update_contact_list()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Create the main application window
root = tk.Tk()
root.title("Contact Book")

# Buttons for contact operations
add_button = tk.Button(root, text="Add Contact", width=20, command=add_contact)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Contact List", width=20, command=update_contact_list)
view_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", width=20, command=search_contact)
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", width=20, command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", width=20, command=delete_contact)
delete_button.pack(pady=5)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

# Populate the contact list initially
update_contact_list()

# Start the GUI event loop
root.mainloop()
