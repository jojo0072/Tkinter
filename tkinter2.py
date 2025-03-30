import tkinter as tk

# Function to insert text into the entry widget
def insert_text():
    entry.insert(tk.END, "Hello, World!")

# Function to get and print the text from the entry widget
def get_text():
    text = entry.get()
    print("Entry contains:", text)

# Function to delete text from the entry widget
def delete_text():
    entry.delete(0, tk.END)  # Delete all text from the entry

# Create the main window
root = tk.Tk()
root.title("Entry Widget Example")

# Create an entry widget
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(pady=20)

# Create buttons to call the functions
insert_button = tk.Button(root, text="Insert Text", command=insert_text, font=("Arial", 20))
insert_button.pack(pady=10)

get_button = tk.Button(root, text="Get Text", command=get_text, font=("Arial", 20))
get_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Text", command=delete_text, font=("Arial", 20))
delete_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
