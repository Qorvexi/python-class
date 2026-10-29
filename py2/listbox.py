# The Listbox and Combobox widgets allows users to select items from a list.

# Listbox: Displays multiple items in a list.
# Combobox: Displays a dropdown list of options.

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Listbox Widget")
root.geometry("300x200")


listbox = tk.Listbox(root, width=100, height=20, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)
listbox.insert(tk.END, "Python")
listbox.insert(tk.END, "Java")
listbox.insert(tk.END, "Javascript")
listbox.insert(tk.END, "C++")

# importaant methods we can use with Listbox
# listbox.insert(tk.END, "Python") -- Adds an item to the list
# listbox.get(index) -- Retrieves an item at a spercific index
# listbox.curselection() -- Returns the index of the selected item
# listbox.delete(0, tk.END) -- Removes all items


# Retrieve a selected item

def show_selection():
    selections = []
    selected = listbox.curselection()
    for i in selected:
        selections.append(listbox.get(i))

    if selected:
        # item = listbox.get(selected)
        messagebox.showinfo("Selections:", "\n".join(map(str, selections)))
    else:
        messagebox.showwarning("Warning", "Please select an item")

def clear_selection():
    listbox.select_clear(0, tk.END)

tk.Button(root, text="Submit", command=show_selection).pack()
tk.Button(root, text="Clear", command=clear_selection).pack()

root.mainloop()