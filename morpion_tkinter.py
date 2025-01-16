from tkinter import *


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class morpion_jeu(Tk):

    def __init__(self):
        super().__init__()

        button1 = Button(self, text="B1")
        button1.grid(column=0, row=0)

        button2 = Button(self, text="B2")
        button2.grid(column=1, row=0)

        button3 = Button(self, text="B3")
        button3.grid(column=2, row=0)

        button4 = Button(self, text="B4")
        button4.grid(column=0, row=1)
        
        button5 = Button(self, text="B5")
        button5.grid(column=1, row=1)
        
        button6 = Button(self, text="B6")
        button6.grid(column=2, row=1)
        
        button7 = Button(self, text="B7")
        button7.grid(column=0, row=2)
        
        button8 = Button(self, text="B8")
        button8.grid(column=1, row=2)
        
        button9 = Button(self, text="B9")
        button9.grid(column=2, row=2)

        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()
window.mainloop()