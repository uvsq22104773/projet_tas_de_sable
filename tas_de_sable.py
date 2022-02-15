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