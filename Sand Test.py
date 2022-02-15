#########################################
# groupe BITD
# Théo JOLY
# Djebrouni Ouail
# Ledien Nils
# Matveev Erik
# https://github.com/uvsq-info/l1-python
#########################################


# Module Imports
import random
from tkinter import *
from tkinter.ttk import *

# Global Variables

root = Tk()
label = Label(root)
Button1 = Button(root)
grille = []

# Iniatiation grille

for i in range(3):
    label.append(Label(root))

for i in range(3):
    grille.append([])
    for j in range(3):
        grille[i].append(random.randint(0, 3))
    label[i].config(text=grille[i])
    label[i].grid(row=i, column=1)

# Setting geometry
root.geometry('100x100')

# Creating a style object
style = Style()

# Setting up Tbutton
style.configure('W.TButton', font=('Courier New', 20))


# Functions
def config_aleatoire():
    global grille, label
    grille = []
    for i in range(3):
        grille.append([])
        for j in range(3):
            grille[i].append(random.randint(0, 3))
        label[i].config(text=grille[i])
        label[i].grid(row=i, column=1)

    pass


# Tkinter Parameters
Title = root.title("Tas de sable")
# parametre tkinter
root.title("Tas de sable")

Button1.config(command=config_aleatoire())
Button1.grid(row=0, column=0)
label.config()
import tkinter as tk

# Buttons
Generation_Button = Button(root, text='Generate', style="W.TButton", command=config_aleatoire)
Generation_Button.grid(row=0, column=0, padx=0)

label.config(text=grille)
label.grid(row=0, column=1)

'''root.title("Un premier exemple") # ajoute un titre
label = tk.Label(racine, text="Un texte dans ma fenêtre", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
racine.mainloop() # Lancement de la boucle principale
# laisser à la fin
root.mainloop()'''

###################################################################

# debut de code

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
e = random.randint(0, 10)
z = random.randint(0, 10)
g = random.randint(0, 10)
t = random.randint(0, 10)
y = random.randint(0, 10)

root.title("Tas de sable")
canvas = tk.Canvas(root, bg="Green", height=500, width=500)
label = tk.Label(root, text="tasser le sable", font=("helvetica", "20"))

# Keep at the end
root.mainloop()