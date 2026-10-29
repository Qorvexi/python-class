# What is Tkinter?
# Tkinter is a standard python library used to create GUI (Graphical User Interface)
# desktop applications.

# Key Components of Tkinter:
# Window(tk): The main application window
# Label(label1): Displays text or images
# Button(button1): A clickable button that can trigger actions
# Entry (entry1): Accepts single-line user input
# Text (text1): Accepts multi-line user input
# Frame (frame1): A container to organize widgets


# FIRST TKINTER PROGRAM
import tkinter as tk #Import the Tkinter library

root = tk.Tk() #Create the main application window
root.title("My First App") # sets the title of the window
root.geometry("300x200") # sets the size of the window
root.mainloop() #Starts the Tkinter event loop, allowing the window to be displayed and interacted with


