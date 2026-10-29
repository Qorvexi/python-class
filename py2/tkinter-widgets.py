# What are widgets?

# Widgets are GUI elements used to build and interact with a tkinter application. They are building blocks

# Common Tkinter Widgets:

# Label(label1): Displays text or images
# Button(button1): A clickable button that can trigger actions
# Entry (entry1): Accepts single-line user input
# Text (text1): Accepts multi-line user input
# Frame (frame1): A container to organize widgets
# Chcekbutton(checkbutton1): A checkbox that allows users to select or deselect an option
# Radiobutton(radiobutton1): A button that allows users to select one option from a group of options

import tkinter as tk
root = tk.Tk()
root.title("Tkinter Widget")
root.geometry("400x300")

label = tk.Label(root, text="Enter your name:") # creats a label
label.pack() # adds the label to the window

entry = tk.Entry(root) # creats an input field
entry.pack() # adds the input field to the window

button = tk.Button(root, text="Submit") # creats a button
button.pack() # adds the button to the window

root.mainloop()


# Create a window containing:

# A label displaying your full name.

# An entry field for entering your age.

# A button labelled Submit.