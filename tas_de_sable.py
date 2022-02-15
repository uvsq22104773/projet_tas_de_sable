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
        grille[i].append(random.randint(0,3))
    label[i].config(text=grille[i])
    label[i].grid(row=i, column=1)

# Setting geometry 
root.geometry('100x100')

# Creating a style object
style = Style()

# Setting up Tbutton
style.configure('W.TButton', font = ('Courier New', 20))


# Functions
def config_aleatoire():
    global grille, label
    grille=[]
    for i in range(3):
        grille.append([])
        for j in range(3):
            grille[i].append(random.randint(0,3))
        label[i].config(text=grille[i])
        label[i].grid(row=i, column=1)
    

# Tkinter Parameters
Title = root.title("Tas de sable")


# Buttons
Generation_Button = Button(root, text='Generate', style="W.TButton", command = config_aleatoire)
Generation_Button.grid(row=0, column=0, padx=0)

label.config(text=grille)
label.grid(row=0,column=1)



###################################################################

# debut de code

a= random.randint(0,10)
b= random.randint(0,10)
c= random.randint(0,10)
d= random.randint(0,10)
e= random.randint(0,10)
z= random.randint(0,10)
g= random.randint(0,10)
t= random.randint(0,10)
y= random.randint(0,10)


# Keep at the end
root.mainloop()