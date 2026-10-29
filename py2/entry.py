# What Is Entry?

# Entry is a Tkinter widget used to accept 
# single-line text input from users.

# Common entry Methods

# get(): Retrieves the entered text
# delete(): Removes text from the entry field.
# insert(0: inserts text into the entry field.

# Example: Retrieving User Input
import tkinter as tk
def greet():
    name = entry.get()  # Retrieve the entered name
    label.config(text=f"Welcome, {name}!")  # Display the name

root = tk.Tk()
root.geometry("400x250")

tk.Label(root, text="Enter your name:").pack(pady=5)

entry = tk.Entry(root)  # Create an input fieldpyth
entry.pack(pady=5)

tk.Button(root, text="Submit", command=greet).pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()