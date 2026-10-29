# Class Work

# Create a registration form with a sunmit button that:
# 1. Checks whether the name field is empty
# 2. Displays a warning message if it is empty.
# 3. Displays a confirmation popup  if the field contains a name.
# 4. Displays a success message if the user confirms the action.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

def reg_user():
    name = entry.get()
    password = entry2.get()

    if not name:
        messagebox.showwarning("Warning", "Name field cannot be empty !!!")
    else:
       answer =  messagebox.askyesno("Confirm", "Ensure all fields are correct")
       if answer:
           messagebox.showinfo("Success", "Registration Successful")
    

tk.Label(root, text="Username :").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Password :").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

tk.Button(root, text="Register", command=reg_user).grid(row=2, column=1, pady=5)
root.mainloop()
