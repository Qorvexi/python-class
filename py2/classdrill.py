import tkinter as tk
def calc():
    num1 = int(entry.get())
    num2 = int(entry.get())
    num3 = num1 + num2 
    label.config(text=num3)

root = tk.Tk()
root.geometry("450x300")

tk.Label(root, text="Enter first number").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

tk.Label(root, text="Enter Second number").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

tk.Button(root,text= "Calculate", command=calc).pack(pady=5)

label = tk.Label(root, text = "")
label.pack(pady=5)
root.mainloop()

### Assignment 1: Student Registration Form

# 1. Create a window titled `Student Registration System` with dimensions `500x400`.
# 2. Include input fields for Full Name, Age, Email Address, and Department.
# 3. Add a `Register` button.
# 4. Use `grid()` to arrange the widgets neatly and apply appropriate padding.
# 5. When the button is clicked, display the student's details in a label below the form.
# 6. If the name field is empty, display `Please enter your name!` instead of registering the student.

# ### Assignment 2: Simple Calculator

# 1. Create a window titled `Simple Calculator`.
# 2. Provide two `Entry` fields for numerical input.
# 3. Add an `Add Numbers` button.
# 4. When clicked, retrieve both values, convert them to numbers, and display their sum in a label.
# 5. Use `grid()` and padding to organize the interface.
# 6. Display an error message if either field is empty.
# 7. Prevent the program from crashing when a user enters letters instead of numbers. Display `Invalid input!` instead.