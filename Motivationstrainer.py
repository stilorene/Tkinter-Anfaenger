import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x400")

def show_name():
    YourName = tk.Label(root, text=f"First Name is: {e1.get()} Last Name: {e2.get()}")
    YourName.grid()
#    ttk.Label(root, text=entry_widget.get()).pack()
#.pack udn 

tk.Label(root, text="First Name").grid(row=1)
tk.Label(root, text="Last Name").grid(row=0) #grid hilft den richigen Platz in einem Grid zu finden

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.insert(10, "Michael")
e2.insert(10, "Der Oide")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1= tk.Button(text="quit now", command=root.quit)
b1.grid(row=3, column=0, pady=4)
b2=tk.Button(text="Show it", command=show_name)
b2.grid(row=3, column=1)



root.mainloop( )

