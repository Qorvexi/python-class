# MESSAGEBOX  ALERTS AND NOTIFICATIONS
# What Is a Messagebox?
# A Messagebox displays popup dialogs for messages, warnings, errors, and confirmations.

# Common Messagebox Methods

# showinfo() — Displays an information message.
# showwarning() — Displays a warning message.
# showerror() — Displays an error message.
# askyesno() — Asks a Yes/No question and returns True or False.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

def show_message():
    messagebox.showinfo("success", "Registration Successful")

def confirm_action():
    answer = messagebox.askyesno("confirm", "Do you want to continue?")
    if answer:
        messagebox.showinfo("Response", "You selected Yes")

tk.Button(root, text="Register", command=show_message).pack(pady=10)
tk.Button(root, text="Continue", command=confirm_action).pack(pady=10)

root.mainloop()
# Class Work

# Create a registration form with a sunmit button that:
# 1. Checks whether the name field is empty
# 2. Displays a warning message if it is empty.
# 3. Displays a confirmation popup  if the field contains a name.
# 4. Displays a success message if the user confirms the action.