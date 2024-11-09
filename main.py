import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # type: ignore

root = tk.Tk()
root.title("Das ist der Titel")
root.geometry("400x400")
# root.minsize(width=200, height=200)
# root.maxsize(width=500, height= 400)
# root.resizable(width=False, height= True)

image = Image.open("Leopard.jpg").resize((300, 200)) # hier im Allgemeinen werden nur Bilder erstellt
photo = ImageTk.PhotoImage(image)

text_variable = tk.StringVar() #tk.IntVar(Ganzzahlen) tk.BooleanVar(Wahrheitswert)
text_variable.set("Lol das is der neue Text")

text_variable.set("Und das ist der andere Text der jetzt angezeigt wird")
print(text_variable.get()) #man kann auch die get - Methode verwenden um zu sehen was in der Variable steht (Konsole)

# image2 = Image.open("kunstwerk.jpg")
# photo2 = ImageTk.PhotoImage(image2)


Label1 = ttk.Label(root, textvariable=text_variable , image=photo, compound="top", background="red")
Label1.pack()

Label1.config(font= ("Arial", 10)) #mit config manuell Änderungen durchführen

# print(Label1.keys()) # Anschauen was für Optionen für ein Widgets in der Konsole anzeigen lassen

for item in Label1.keys():
    print(item, ":", Label1[item])

# Label1["image"] = photo2 #Änderungen im Nachhinein durchführen

# Label1.config(text="Lol das klappt")

root.mainloop() 


