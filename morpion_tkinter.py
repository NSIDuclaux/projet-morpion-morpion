from tkinter import *
from PIL import ImageTk, Image

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

        self.boutons = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


        self.boutons[0][0] = Button(self, text="B1", command=lambda: self.sur_bouton_clique(0, 0))
        self.boutons[0][0].grid(column=0, row=1, sticky="nswe", padx=3, pady=3)

        self.boutons[0][1] = Button(self, text="B2", command=lambda: self.sur_bouton_clique(0, 1))
        self.boutons[0][1].grid(column=1, row=1, sticky="nswe", padx=3, pady=3)

        self.boutons[0][2] = Button(self, text="B3", command=lambda: self.sur_bouton_clique(0, 2))
        self.boutons[0][2].grid(column=2, row=1, sticky="nswe", padx=3, pady=3)

        self.boutons[1][0] = Button(self, text="B4", command=lambda: self.sur_bouton_clique(1, 0))
        self.boutons[1][0].grid(column=0, row=2, sticky="nswe", padx=3, pady=3)
        
        self.boutons[1][1] = Button(self, text="B5", command=lambda: self.sur_bouton_clique(1, 1))
        self.boutons[1][1].grid(column=1, row=2, sticky="nswe", padx=3, pady=3)
        
        self.boutons[1][2] = Button(self, text="B6", command=lambda: self.sur_bouton_clique(1, 2))
        self.boutons[1][2].grid(column=2, row=2, sticky="nswe", padx=3, pady=3)
        
        self.boutons[2][0] = Button(self, text="B7", command=lambda: self.sur_bouton_clique(2, 0))
        self.boutons[2][0].grid(column=0, row=3, sticky="nswe", padx=3, pady=3)
        
        self.boutons[2][1] = Button(self, text="B8", command=lambda: self.sur_bouton_clique(2, 1))
        self.boutons[2][1].grid(column=1, row=3, sticky="nswe", padx=3, pady=3)
        
        self.boutons[2][2] = Button(self, text="B9", command=lambda: self.sur_bouton_clique(2, 2))
        self.boutons[2][2].grid(column=2, row=3, sticky="nswe", padx=3, pady=3)
        
        
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        
        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")

        
        img_path = 'path/tic-tac-toe-icon.png'
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)

        self.iconphoto(False, img)

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
    
    def gagnant(self, joueur):
        print("gagnant")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=3, pady=3)
        for row in self.buttons:
            for button in row:
                button.config(state=DISABLED)


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()
window.mainloop()