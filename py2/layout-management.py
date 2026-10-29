# What is Layout Management?

# Layout management determines how widgets are 
# arranged/positioned  inside  a Tkinter window.

# Types of Layout Managers:
# pack(): Arranges  widget in blocks, typically vertically or hortizontally.
# grid(): Arranges widgets in rows and columns.
# place(): Positions widgets using specific coordinates.

# Example: Using pack()
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

root.title("Layout Management")

tk.Label(root, text="Welcome").pack()
tk.Button(root, text="Submit").pack()
tk.Entry(root).pack()

root.mainloop()


