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

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton1)

        bouton2 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton2)

        bouton3 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton3)

        bouton4 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton4)

        bouton5 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton5)

        bouton6 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton6)

        bouton7 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton7)

        bouton8 = Button(self, text=" ", command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton8)

        bouton9 = Button(self, text="  ", command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton9)

        
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        
        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")

        
        img = Image.open("https://github.com/NSIDuclaux/projet-morpion-morpion/blob/main/tic-tac-toe-icon.png")
        img = ImageTk.PhotoImage(img)

        self.iconphoto(False, img)


    def arret_partie(self):
        for bouton in self.liste_boutons:
            bouton.config(state=DISABLED)


        # renvoie True si c'est bien a ce joueur-la de jouer, False sinon
    def verif_tour(self, row, col):
        if self.morpion[row][col] == " ":
            self.morpion[row][col] = self.joueur_actuel
            return True
        return False

    def sur_bouton_clique(self, row, col):
        print("sur button clique")
        if self.verif_tour(row, col):
            self.liste_boutons[row * 3 + col].config(text=self.joueur_actuel, state=DISABLED)
            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            else:
                if self.joueur_actuel == "X":
                    self.joueur_actuel = "O"
                else:
                    self.joueur_actuel = "X"

    def a_gagne(self):
        print("a gagne")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != " ":
                return True
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                return True
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            return True
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            return True
        return False
    
    def gagnant(self, joueur):
        print("gagnant")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=3, pady=3)
        self.arret_partie()


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()
window.mainloop()