# COMBOBOX WIDGET
# A Combobox displays a dropdown list from which users can select an option.

# it is provided by tkinter.ttk, so you must import ttk
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Combobox Widget")
root.geometry("300x200")

combo = ttk.Combobox(root, values = ["Python", "Java", "Javascript", "C++"], state="readonly")
combo.pack(pady=20)

# Additional methods

# combo.get() -- Retrieves the selected value
# combo.set("Python") -- Sets the displayed value

# RETRIEVING A COMBOBOX SELECTION

def show_selection():
    selected = combo.get()

    if selected:
        messagebox.showinfo("Selection", selected)
    else:
        messagebox.showwarning("Warning", "Please select a lanuguage")

def clear():
    combo.set("")

tk.Button(root, text="Submit", command=show_selection).pack()
tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()

#  CLASS WORK
# Build a Course Selection Form with the following features:
# 1. A label displaying Select Your Course.
# 2. A Listbox containing Python, Java, JavaScript, and C++.
# 3. A Combobox containing Beginner, Intermediate, and Advanced.
# 4. A Submit button that displays the selected course and level.
# 5. A Clear button that clears the course selection and resets the level.
# Note: For the Listbox, use curselection() to retrieve the selected course. 
# For the Combobox, use get() to retrieve the selected level.