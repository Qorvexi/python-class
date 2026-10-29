
import tkinter as tk
# What Are Tkinter Variables?
# Tkinter variables store values that can be linked to widgets and updated dynamically.

# Types of Tkinter Variables

# StringVar(): Stores text values.
# IntVar(): Stores integer values.
# DoubleVar(): Stores decimal values.
# BooleanVar(): Stores Boolean values (True or False).

# Example: Using StringVar()

root = tk.Tk()
root.geometry("400x250")

name = tk.StringVar()  # Create a text variable

entry = tk.Entry(root, textvariable=name)  # Link variable to entry
entry.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

def display_name():
    label.config(text=name.get())  # Retrieve the variable's value

tk.Button(root, text="Display Name", command=display_name).pack()

root.mainloop()

name.set("Larry")  # Set the variable's value
print(name.get())  # Display the current value