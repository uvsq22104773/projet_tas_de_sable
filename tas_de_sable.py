#########################################
# groupe BITD
# Théo JOLY
# Djebrouni Ouail
# Ledien Nils
# Matveev Erik
# https://github.com/uvsq-info/l1-python
#########################################


# import des modules
from random import randint
from tkinter import *


# variables globales
root = Tk()
Button1 = Button(root)
label = Label(root)

# fonction
def config_aleatoire():
    pass


# parametre tkinter
root.title("Tas de sable")

Button1.config(command=config_aleatoire())
Button1.grid(row=0, column=0)
label.config()
import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Un premier exemple") # ajoute un titre
label = tk.Label(racine, text="Un texte dans ma fenêtre", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
racine.mainloop() # Lancement de la boucle principale
# laisser à la fin
root.mainloop()

