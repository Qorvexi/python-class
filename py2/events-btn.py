import tkinter as tk
# What are Events

# Events are user actions, such as clicking a button or 
# pressing a key, that trigger a response in an application.

# The command Parameter

# The command parameter specifies the function to execute when a button is clicked.


# Example Button Command
def greet():
    label.config(text="Welcome to Tkinter!")  # Update the label text
    button.config(text="You just clicked me")

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Click Me", command=greet)
button.pack()

root.mainloop()

# Practice Exercise

# Create a window with a button labelled Change Text. When clicked, 
# it should change a label's text to your name.