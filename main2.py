import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")

def delete_input():
    entry_widget.delete(0, tk.END) #Die Zahl von wo bis wo gelöscht werden soll

# quit_button = tk.Button(root, text="Bendet das Programm", command=root.destroy)
# quit_button.pack()

entry_widget = tk.Entry(root)
entry_widget.pack()


def print_smth():
    ttk.Label(root, text=entry_widget.get()).pack()

button1 = tk.Button(root, text="Input löschen", padx=10, pady=10, command=delete_input, state=tk.NORMAL)
button1.pack() 
# for item in button1.keys():
#     print(item, ": ", button1[item])

for item in entry_widget.keys():
    print(item, ": ", entry_widget[item])

root.mainloop()