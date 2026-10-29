# CHECKBUTTON AND RADIOBUTTON WIDGETS
# 1. Checkbutton: A Checkbutton allows users to select or deselect an option independently.

# 2. Radiobutton: A Radiobutton allows users to select only one option from a group.

# Example: Checkbutton and Radiobutton

import tkinter as tk

root = tk.Tk()
root.title("Selection Form")
root.geometry("350x300")

# Checkbutton
subscribe = tk.BooleanVar()

tk.Checkbutton(
    root, 
    text="Suscribe to newsletter", 
    variable=subscribe
    ).pack(pady=10)

# Radiobutton
gender = tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender,
    value="Male"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender,
    value="Female"
).pack()

# Display selections

def show_selection():
    print("Subscribed:", subscribe.get())
    print("Gender:", gender.get())

tk.Button(root, 
          text="Submit",
          command=show_selection
          ).pack(pady=10)

root.mainloop()

# Note:
# text="Male" is the visible text displayed beside the Radiobutton in the window.

# variable=gender : Links the Radiobutton to the Tkinter variable named gender.

# value="Male" : The value asigned to gender when this Radiobutton is selected.
