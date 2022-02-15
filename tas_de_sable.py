#########################################
# groupe BITD
# Théo JOLY
# Djebrouni Ouail
# Ledien Nils
# Matveev Erik
# https://github.com/uvsq-info/l1-python
#########################################

########### object ###############
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
label.config(text="test")
label.grid(row=0,column=1)


# laisser à la fin
root.mainloop()


############################################################################################################

# debut de code

import random
a= random.randint(0,10)
b= random.randint(0,10)
c= random.randint(0,10)
d= random.randint(0,10)
e= random.randint(0,10)
z= random.randint(0,10)
g= random.randint(0,10)
t= random.randint(0,10)
y= random.randint(0,10)

if a > 4 :
    p =random.randint(1,a-1)
    a = a - p
    b = (p/2) + b
    d = (p/2) + d
elif b > 4 :
    p =random.randint(1,b-1)
    b = b - p
    a = (p/3) + a
    e = (p/3) + e
    c = (p/3) + c
elif c > 4 :
     p =random.randint(1,a-1)
     a = a - p
     b = (p/2) + b
     d = (p/2) + d
    

     pass

""" exemple:
racine = tk.Tk() # Création de la fenêtre racine
racine.title("Un premier exemple") # ajoute un titre
label = tk.Label(racine, text="Un texte dans ma fenêtre", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
racine.mainloop() # Lancement de la boucle principale"""
import tkinter as tk
racine= tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, bg="whit", height=500, width=500)
label = tk.Label(racine, text="tasser le sable", font=("helvetica", "20"))

