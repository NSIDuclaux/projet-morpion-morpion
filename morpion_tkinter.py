from tkinter import *


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class morpion_jeu(Tk):

    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=0)  # ajoute une barre en plus pour ajouter des elements supplementaires
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        # barre du haut
        top_bar = Label(self, text="Morpion", bg='gray24', fg='white', font=("Arial", 16))
        top_bar.grid(column=0, row=0, columnspan=3, sticky="nsew", padx=3, pady=3)

        button1 = Button(self, text="B1")
        button1.grid(column=0, row=1, sticky="nswe", padx=3, pady=3)

        button2 = Button(self, text="B2")
        button2.grid(column=1, row=1, sticky="nswe", padx=3, pady=3)

        button3 = Button(self, text="B3")
        button3.grid(column=2, row=1, sticky="nswe", padx=3, pady=3)

        button4 = Button(self, text="B4")
        button4.grid(column=0, row=2, sticky="nswe", padx=3, pady=3)
        
        button5 = Button(self, text="B5")
        button5.grid(column=1, row=2, sticky="nswe", padx=3, pady=3)
        
        button6 = Button(self, text="B6")
        button6.grid(column=2, row=2, sticky="nswe", padx=3, pady=3)
        
        button7 = Button(self, text="B7")
        button7.grid(column=0, row=3, sticky="nswe", padx=3, pady=3)
        
        button8 = Button(self, text="B8")
        button8.grid(column=1, row=3, sticky="nswe", padx=3, pady=3)
        
        button9 = Button(self, text="B9")
        button9.grid(column=2, row=3, sticky="nswe", padx=3, pady=3)

        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        
        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")

        # renvoie True si c'est bien a ce joueur-la de jouer, False sinon
    def verif_tour(self, row, col):
        if self.morpion[row][col] == " ":
            self.morpion[row][col] = self.joueur_actuel
            return True
        return False

    def sur_bouton_clique(self, row, col):
        print("sur button clique")
        if self.verif_tour(row, col):
            self.buttons[row][col].config(text=self.joueur_actuel)
            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            else:
                self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"

    def a_gagne(self):
        print("a gagne")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != "":
                return True
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != "":
                return True
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != "":
            return True
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != "":
            return True
        return False
    
    def gagnant(self, player):
        print("gagnant")
        winner_label = Label(self, text=f"Player {player} wins!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=3, pady=3)
        for row in self.buttons:
            for button in row:
                button.config(state=DISABLED)


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()
window.mainloop()