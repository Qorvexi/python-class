import tkinter as tk


app = tk.Tk()

tk.Label(app, text="Username:").grid(row=0,column=0, pady=10)
tk.Entry(app).grid(row=0,column=1)
tk.Label(app, text="Password:").grid(row=2,column=0)
tk.Entry(app).grid(row=2,column=1)
tk.Button(app, text="Login").grid(row=4,column=1, pady=10)

app.mainloop()