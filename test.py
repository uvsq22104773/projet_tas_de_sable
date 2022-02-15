#########################################
# groupe BITD
# Théo JOLY
# Djebrouni Ouail
# Ledien Nils
# Matveev Erik
# https://github.com/uvsq-info/l1-python
#########################################

########### object ###############
# Module Imports
import random
from tkinter import *
from tkinter.ttk import * 


# Global Variables
root = Tk()
label = Label(root)
Button1 = Button(root)
grille = []

# Functions
def config_aleatoire():
    global grille
    for i in range(3):
        grille.append([])
        for j in range(3):
            grille[i].append(random.randint(0,3))
    print(grille)


# TKinter Parameters
root.title("Tas de sable")

# Setting geometry 
root.geometry('100x100')

# Creating a style object
style = Style()


# Buttons

Random_Button = Button1.config(command=config_aleatoire())
Button1.grid(row=0, column=0)
label.config(text="test")
label.grid(row=0,column=1)


# laisser à la fin
root.mainloop()

###################################################################
