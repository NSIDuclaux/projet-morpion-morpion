from tkinter import *


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class morpion_jeu(Tk):

    def __init__(self):
        super().__init__()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        button1 = Button(self, text="B1")
        button1.grid(column=0, row=0, sticky="nswe", padx=3, pady=3)

        button2 = Button(self, text="B2")
        button2.grid(column=1, row=0, sticky="nswe", padx=3, pady=3)

        button3 = Button(self, text="B3")
        button3.grid(column=2, row=0, sticky="nswe", padx=3, pady=3)

        button4 = Button(self, text="B4")
        button4.grid(column=0, row=1, sticky="nswe", padx=3, pady=3)
        
        button5 = Button(self, text="B5")
        button5.grid(column=1, row=1, sticky="nswe", padx=3, pady=3)
        
        button6 = Button(self, text="B6")
        button6.grid(column=2, row=1, sticky="nswe", padx=3, pady=3)
        
        button7 = Button(self, text="B7")
        button7.grid(column=0, row=2, sticky="nswe", padx=3, pady=3)
        
        button8 = Button(self, text="B8")
        button8.grid(column=1, row=2, sticky="nswe", padx=3, pady=3)
        
        button9 = Button(self, text="B9")
        button9.grid(column=2, row=2, sticky="nswe", padx=3, pady=3)

        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()
window.mainloop()