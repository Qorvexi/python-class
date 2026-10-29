# Class work
# Build a Feedback Form with the following features:
# 1. A label displaying “Enter Your Feedback”.
# 2. A Text widget for multiline input.
# 3. A Submit button that displays the submitted feedback in a label.
# 4. A Clear button that removes all text from the Text widget.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Feedback Form")
root.geometry("500x500")

result = tk.Label(root, text="")
textlabel = tk.Label(root, text="Enter your Feedback")
textlabel.grid(row=0, column=0, pady=10)
textbox = tk.Text(root, height=5, width=20)
textbox.grid(row=2, column=0, pady=10)

def show_text():
    message = textbox.get("1.0", "1.2")
    if not message:
        messagebox.showwarning("error", "Field cannot be Empty")
    else:
        result.config(text=message)
    
def clear():
    answer = messagebox.askyesno("confirm","Do you want to delete?")
    if answer:
        messagebox.showinfo("Delete", "Cleared Successful")
        textbox.delete("1.0", tk.END)

result.grid(row=3, column=1)

tk.Button(root, text="Submit", command=show_text).grid(row=4, column=0, pady=10, padx=0)
tk.Button(root, text="Clear", command=clear).grid(row=4, column=1, pady=5, padx=0)
root.mainloop()