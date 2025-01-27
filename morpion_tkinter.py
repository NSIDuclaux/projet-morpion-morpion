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

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton1)

        bouton2 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton2)

        bouton3 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton3)

        bouton4 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton4)

        bouton5 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton5)

        bouton6 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton6)

        bouton7 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton7)

        bouton8 = Button(self, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton8)

        bouton9 = Button(self, text="  ", font=("Helvetica",20), height=3, width=6, command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=3, pady=3)
        self.liste_boutons.append(bouton9)


        quitter_bouton = Button(self, text="Quitter", command=self.quitter_jeu, bg='gray24', fg='white', font=("Arial", 14))
        quitter_bouton.grid(column=0, row=6, columnspan=3, sticky="nsew", padx=3, pady=3)


        for i in range(3):
            for j in range(3):
                bouton = self.liste_boutons[i * 3 + j]
                bouton.bind("<Enter>", lambda event, row=i, col=j: self.surligner_bouton(row, col))
                bouton.bind("<Leave>", lambda event, row=i, col=j: self.enlever_surligneur(row, col))

        
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        
        # On dimensionne la fenêtre (400 pixels de large par 400 de haut).
        self.geometry("400x400")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")
        
        self.compteur = 0

        
    def surligner_bouton(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="floral white")
            if self.joueur_actuel == "X":
                self.liste_boutons[row * 3 + col].config(text="X")
            else:
                self.liste_boutons[row * 3 + col].config(text="O")

    def enlever_surligneur(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="white")
            self.liste_boutons[row * 3 + col].config(text=" ")

    def arret_partie(self):
        for bouton in self.liste_boutons:
            bouton.config(state=DISABLED)

    def quitter_jeu(self):
        self.destroy()

    # renvoie True si c'est bien a ce joueur-la de jouer, False sinon
    def verif_tour(self, row, col):
        if self.morpion[row][col] == " ":
            self.morpion[row][col] = self.joueur_actuel
            return True
        return False

    def sur_bouton_clique(self, row, col):
        print("------------------------------------------------------")
        print(f"{self.joueur_actuel} a cliqué sur le bouton {str(row * 3 + col + 1)}\n") # pour deboggage
        if self.verif_tour(row, col):
            self.liste_boutons[row * 3 + col].config(text=self.joueur_actuel, state=DISABLED)
            self.compteur += 1
            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            elif self.jeu_nul():
                pass # le jeu est deja arrete grace a la condition donc on peut juste mettre pass
            else:
                self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"
                    

    def a_gagne(self):
        print("a gagné?")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != " ":
                self.colorier_boutons([(i, 0), (i, 1), (i, 2)])
                return True
                
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                self.colorier_boutons([(0, i), (1, i), (2, i)])
                return True
            
                
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            self.colorier_boutons([(0, 0), (1, 1), (2, 2)])
            return True
            
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            self.colorier_boutons([(0, 2), (1, 1), (2, 0)])
            return True
        
        self.jeu_nul()

        print(f"non, le joueur {self.joueur_actuel} n'a pas gagné")
        print("------------------------------------------------------\n")
        return False

    def colorier_boutons(self, positions):
        for row, col in positions:
            self.liste_boutons[row * 3 + col].config(bg="green")
    
    def gagnant(self, joueur):
        print(f"{self.joueur_actuel} est gagnant !")
        print("------------------------------------------------------\n")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=3, pady=3)
        self.arret_partie()
        self.ajouter_bouton_rejouer()

    def jeu_nul(self):
        if self.compteur == 9:
            for i in range(3):
                for j in range(3):
                    if self.morpion[i][j] == " ":
                        return False
            print(f"la partie est nulle, aucun gagnant !")
            print("------------------------------------------------------\n")
            winner_label = Label(self, text="Match nul!", bg='gray24', fg='white', font=("Arial", 16))
            winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=3, pady=3)
            self.arret_partie()
            self.ajouter_bouton_rejouer()
            return True
        return False
    
    def ajouter_bouton_rejouer(self):
        rejouer_bouton = Button(self, text="Rejouer", command=self.reinitialiser_jeu, bg='gray24', fg='white', font=("Arial", 14))
        rejouer_bouton.grid(column=0, row=5, columnspan=3, sticky="nsew", padx=3, pady=3)

    def reinitialiser_jeu(self):
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "] for _ in range(3)]
        self.compteur = 0
        for bouton in self.liste_boutons:
            bouton.config(text=" ", state=NORMAL, bg='white')
        for widget in self.grid_slaves():
            if isinstance(widget, Label):
                widget.destroy()


# On crée notre fenêtre et on l'affiche
window = morpion_jeu()

#changement de l'icone de la fenetre

#window.iconphoto(False, PhotoImage(file="tic-tac-toe-icon.ico"))
#window.iconbitmap("tic-tac-toe-icon.ico")

window.mainloop()

### a faire :
###
### 1: ajouter des commentaires et une docstring pour la class
###
###

