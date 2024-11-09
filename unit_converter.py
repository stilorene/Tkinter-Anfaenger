import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # type: ignore

def on_check():
    print("Status:", var.get())



root = tk.Tk()
root.geometry("400x400")
var = tk.BooleanVar()


def on_check():
    Simple_text = tk.Label(root, text ="Das ist der Hammer junge, but fuck off oi mate", font=("Arial", 14))
    Simple_text.pack()

entryfield = tk.Entry(root,text="Stilvoller Checkbutton", font=("Arial", 12, "italic"),bg="#303841", fg="#f6c90e")          

entryfield.pack()

checkbox = tk.Checkbutton(
    root,
    text="Stilvoller Checkbutton",
    variable=var,
    command=on_check,
    font=("Arial", 12, "italic"),
    bg="#303841",              # Hintergrundfarbe
    fg="#f6c90e",              # Textfarbe
    activebackground="#3a4750", # Hintergrundfarbe beim Aktivieren
    activeforeground="#eeeeee", # Textfarbe beim Aktivieren
    selectcolor="#00adb5",     # Farbe des Kästchens, wenn aktiviert
    padx=10, pady=5            # Innenabstand für bequemere Positionierung
)
checkbox.pack()

for item in checkbox.keys():
    print(item, ":", checkbox[item])

root.mainloop()