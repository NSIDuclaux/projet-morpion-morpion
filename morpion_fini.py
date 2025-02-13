from tkinter import *
from random import randint

class Morpion_1vPCdef_et_off(Tk):
    """
    Classe représentant le jeu de Morpion contre un ordinateur défensif et offensif.
    defensif: bloque le joueur quand il a une opportunité de gagner
    offensif: défait le joueur quand il a une opportunité de gagner
    si l'ordinateur ne voit pas que le joueur ou lui-même peut gagner alors il joue aléatoirement
    """
    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        self.resizable(width=False, height=False)

        self.grid_rowconfigure(0, weight=0)  # ajoute une barre en plus pour ajouter des elements supplementaires
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton1)

        bouton2 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton2)

        bouton3 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton3)

        bouton4 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton4)

        bouton5 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton5)

        bouton6 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton6)

        bouton7 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton7)

        bouton8 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton8)

        bouton9 = Button(self, text="  ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton9)
        
        retour_modedejeu_bouton = Button(self, text="mode de jeu", command=self.mode_de_jeu, bg='gray24', fg='white', font=("Arial", 14))
        retour_modedejeu_bouton.grid(column=0, row=6, columnspan=3, sticky="nsew", padx=3, pady=3)

        quitter_bouton = Button(self, text="Quitter", command=self.quitter_jeu, bg='gray24', fg='white', font=("Arial", 14))
        quitter_bouton.grid(column=0, row=7, columnspan=3, sticky="nsew", padx=3, pady=3)


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
        self.geometry("400x450")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")
        
        self.compteur = 0
        
    
    
    def mode_de_jeu(self):
        self.destroy()
        fenetre_modedejeu = Mode_de_jeu_morpion()
        fenetre_modedejeu.mainloop()
        
    def surligner_bouton(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="floral white")
            if self.joueur_actuel == "X":
                self.liste_boutons[row * 3 + col].config(text="X")
            else:
                self.liste_boutons[row * 3 + col].config(text="O")

    def enlever_surligneur(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="#d9d9d9")
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
    
    def verif_cases_gagnantes(self, symbole):
        """Retourne les cases où 'symbole' peut gagner (version générique)"""
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "]
        cases_gagnantes = []

        for row, col in cases_vides:
            morpion_copie = [ligne.copy() for ligne in self.morpion]
            morpion_copie[row][col] = symbole
            if self.a_gagne_sur_copie(morpion_copie):
                cases_gagnantes.append((row, col))
        return cases_gagnantes

    # regarde les cases gagnantes pour le joueur X
    def x_cases_verif(self):
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "]
        cases_gagnantes_pour_x = []

        for row, col in cases_vides:
            # Créer une copie du morpion pour la simulation
            morpion_copie = [ligne.copy() for ligne in self.morpion]
            morpion_copie[row][col] = "X" # place un x sur la case précisée
            if self.a_gagne_sur_copie(morpion_copie): #regarde si cette case résulte à une victoire pour le joueur X
                cases_gagnantes_pour_x.append((row, col))
        return cases_gagnantes_pour_x


    def ordinateur_defensif_et_offensif(self):
        print("L'IA offensive réfléchit...\n")
        
        # 1. Vérifier si l'IA (O) peut gagner immédiatement
        cases_gagnantes_o = self.verif_cases_gagnantes("O")
        if cases_gagnantes_o:
            row, col = cases_gagnantes_o[0]
            print(f"L'IA marque la case gagnante {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1
            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"
            return  # Sortir après avoir joué
        
        # 2. Sinon, bloquer le joueur (X) si nécessaire
        cases_gagnantes_x = self.verif_cases_gagnantes("X")
        if cases_gagnantes_x:
            row, col = cases_gagnantes_x[0]
            print(f"L'IA bloque la case {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1
            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"
            return  # Sortir après avoir bloqué

        # 3. Si aucune opportunité, jouer aléatoirement
        self.ordinateur_alea()
        
    def sur_bouton_clique(self, row, col):
        print(f"{self.joueur_actuel} a cliqué sur la case {row}, {col}\n")

        if self.verif_tour(row, col) and self.joueur_actuel == "X":
            self.liste_boutons[row * 3 + col].config(text=self.joueur_actuel, state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "O"
                self.ordinateur_defensif_et_offensif()  # Appel de la nouvelle IA
                
    def ordinateur_alea(self):
        print("L'ordinateur réfléchit...\n")
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "] # renvoie une liste de couples de coordonees de toutes les cases vides

        if cases_vides: # s'il y a des cases vides
            row, col = cases_vides[randint(0, len(cases_vides) - 1)] # choisit une case parmis les cases vides
            print(f"L'ordinateur choisit la case {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"  # Retour au joueur humain

    def a_gagne_sur_copie(self, morpion_copie):
        # Vérifie les victoires sur la copie sans modifier l'interface
        for i in range(3):
            if morpion_copie[i][0] == morpion_copie[i][1] == morpion_copie[i][2] != " ":
                return True
            if morpion_copie[0][i] == morpion_copie[1][i] == morpion_copie[2][i] != " ":
                return True
        if morpion_copie[0][0] == morpion_copie[1][1] == morpion_copie[2][2] != " ":
            return True
        if morpion_copie[0][2] == morpion_copie[1][1] == morpion_copie[2][0] != " ":
            return True
        return False

    def a_gagne(self):
        print("a gagné?")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != " ":
                self.colorier_vert([(i, 0), (i, 1), (i, 2)])
                return True
                
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                self.colorier_vert([(0, i), (1, i), (2, i)])
                return True
            
                
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            self.colorier_vert([(0, 0), (1, 1), (2, 2)])
            return True
            
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            self.colorier_vert([(0, 2), (1, 1), (2, 0)])
            return True
        

        print(f"non, le joueur {self.joueur_actuel} n'a pas gagné")
        print("------------------------------------------------------\n")
        return False

    def colorier_vert(self, positions):
        for row, col in positions:
            self.liste_boutons[row * 3 + col].config(bg="green")
    
    def gagnant(self, joueur):
        print(f"{self.joueur_actuel} est gagnant !")
        print("------------------------------------------------------\n")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
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
            winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
            self.arret_partie()
            self.ajouter_bouton_rejouer()
            return True
        return False
    
    def ajouter_bouton_rejouer(self):
        rejouer_bouton = Button(self, text="Rejouer", command=self.reinitialiser_jeu, bg='gray24', fg='white', font=("Arial", 14))
        rejouer_bouton.grid(column=0, row=5, columnspan=3, sticky="nsew", padx=10, pady=10)

    def reinitialiser_jeu(self):
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "] for _ in range(3)]
        self.compteur = 0
        for bouton in self.liste_boutons:
            bouton.config(text=" ", state=NORMAL, bg='white')
        for widget in self.grid_slaves():
            if isinstance(widget, Label):
                widget.destroy()

class Morpion_1vPCdef(Tk):
    """
    Classe représentant le jeu de Morpion contre un ordinateur défensif.
    defensif: bloque le joueur quand il a une opportunité de gagner
    si l'ordinateur ne voit pas que le joueur peut gagner alors il joue aléatoirement
    """
    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        self.resizable(width=False, height=False)

        self.grid_rowconfigure(0, weight=0)  # ajoute une barre en plus pour ajouter des elements supplementaires
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton1)

        bouton2 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton2)

        bouton3 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton3)

        bouton4 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton4)

        bouton5 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton5)

        bouton6 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton6)

        bouton7 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton7)

        bouton8 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton8)

        bouton9 = Button(self, text="  ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton9)
        
        retour_modedejeu_bouton = Button(self, text="mode de jeu", command=self.mode_de_jeu, bg='gray24', fg='white', font=("Arial", 14))
        retour_modedejeu_bouton.grid(column=0, row=6, columnspan=3, sticky="nsew", padx=3, pady=3)

        quitter_bouton = Button(self, text="Quitter", command=self.quitter_jeu, bg='gray24', fg='white', font=("Arial", 14))
        quitter_bouton.grid(column=0, row=7, columnspan=3, sticky="nsew", padx=3, pady=3)


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
        self.geometry("400x450")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")
        
        self.compteur = 0
        
    
    
    def mode_de_jeu(self):
        self.destroy()
        fenetre_modedejeu = Mode_de_jeu_morpion()
        fenetre_modedejeu.mainloop()
        
    def surligner_bouton(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="floral white")
            if self.joueur_actuel == "X":
                self.liste_boutons[row * 3 + col].config(text="X")
            else:
                self.liste_boutons[row * 3 + col].config(text="O")

    def enlever_surligneur(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="#d9d9d9")
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
    


    # regarde les cases gagnantes pour le joueur X
    def x_cases_verif(self):
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "]
        cases_gagnantes_pour_x = []

        for row, col in cases_vides:
            # Créer une copie du morpion pour la simulation
            morpion_copie = [ligne.copy() for ligne in self.morpion]
            morpion_copie[row][col] = "X" # place un x sur la case précisée
            if self.a_gagne_sur_copie(morpion_copie): #regarde si cette case résulte à une victoire pour le joueur X
                cases_gagnantes_pour_x.append((row, col))
        return cases_gagnantes_pour_x


    def ordinateur_defensif(self):
        print("L'IA réfléchit...\n")
        cases_gagnantes_pour_x = self.x_cases_verif()
        if cases_gagnantes_pour_x:
            # Bloque une victoire potentielle du joueur X si elle existe
            row, col = cases_gagnantes_pour_x[0]
            print(f"L'ordinateur bloque la case {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1
            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"  # Retour au joueur humain
        else:
            self.ordinateur_alea()
        
    def sur_bouton_clique(self, row, col):
        print(f"{self.joueur_actuel} a cliqué sur la case {row}, {col}\n")  # Pour le débogage

        if self.verif_tour(row, col) and self.joueur_actuel == "X":  # Tour du joueur humain
            self.liste_boutons[row * 3 + col].config(text=self.joueur_actuel, state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "O"  # Changement de tour vers l'ordinateur
                self.ordinateur_defensif()  # L'ordinateur joue automatiquement ################# a enlever
                
    def ordinateur_alea(self):
        print("L'ordinateur réfléchit...\n")
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "] # renvoie une liste de couples de coordonees de toutes les cases vides

        if cases_vides: # s'il y a des cases vides
            row, col = cases_vides[randint(0, len(cases_vides) - 1)] # choisit une case parmis les cases vides
            print(f"L'ordinateur choisit la case {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"  # Retour au joueur humain

    def a_gagne_sur_copie(self, morpion_copie):
        # Vérifie les victoires sur la copie sans modifier l'interface
        for i in range(3):
            if morpion_copie[i][0] == morpion_copie[i][1] == morpion_copie[i][2] != " ":
                return True
            if morpion_copie[0][i] == morpion_copie[1][i] == morpion_copie[2][i] != " ":
                return True
        if morpion_copie[0][0] == morpion_copie[1][1] == morpion_copie[2][2] != " ":
            return True
        if morpion_copie[0][2] == morpion_copie[1][1] == morpion_copie[2][0] != " ":
            return True
        return False

    def a_gagne(self):
        print("a gagné?")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != " ":
                self.colorier_vert([(i, 0), (i, 1), (i, 2)])
                return True
                
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                self.colorier_vert([(0, i), (1, i), (2, i)])
                return True
            
                
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            self.colorier_vert([(0, 0), (1, 1), (2, 2)])
            return True
            
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            self.colorier_vert([(0, 2), (1, 1), (2, 0)])
            return True
        

        print(f"non, le joueur {self.joueur_actuel} n'a pas gagné")
        print("------------------------------------------------------\n")
        return False

    def colorier_vert(self, positions):
        for row, col in positions:
            self.liste_boutons[row * 3 + col].config(bg="green")
    
    def gagnant(self, joueur):
        print(f"{self.joueur_actuel} est gagnant !")
        print("------------------------------------------------------\n")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
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
            winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
            self.arret_partie()
            self.ajouter_bouton_rejouer()
            return True
        return False
    
    def ajouter_bouton_rejouer(self):
        rejouer_bouton = Button(self, text="Rejouer", command=self.reinitialiser_jeu, bg='gray24', fg='white', font=("Arial", 14))
        rejouer_bouton.grid(column=0, row=5, columnspan=3, sticky="nsew", padx=10, pady=10)

    def reinitialiser_jeu(self):
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "] for _ in range(3)]
        self.compteur = 0
        for bouton in self.liste_boutons:
            bouton.config(text=" ", state=NORMAL, bg='white')
        for widget in self.grid_slaves():
            if isinstance(widget, Label):
                widget.destroy()
# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class Morpion_1vPCalea(Tk):
    """
    Classe représentant le jeu de Morpion contre un ordinateur qui joue sur une case non-prise aléatoire.
    """
    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        
        self.minsize(400, 450)
        self.resizable(width=False, height=False)

        self.grid_rowconfigure(0, weight=0)  # ajoute une barre en plus pour ajouter des elements supplementaires
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton1)


        bouton2 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton2)


        bouton3 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton3)


        bouton4 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton4)


        bouton5 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton5)


        bouton6 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton6)


        bouton7 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton7)


        bouton8 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton8)


        bouton9 = Button(self, text="  ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton9)

        
        retour_modedejeu_bouton = Button(self, text="mode de jeu", command=self.mode_de_jeu, bg='gray24', fg='white', font=("Arial", 14))
        retour_modedejeu_bouton.grid(column=0, row=6, columnspan=3, sticky="nsew", padx=3, pady=3)

        quitter_bouton = Button(self, text="Quitter", command=self.quitter_jeu, bg='gray24', fg='white', font=("Arial", 14))
        quitter_bouton.grid(column=0, row=7, columnspan=3, sticky="nsew", padx=3, pady=3)



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
        self.geometry("400x450")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")
        
        self.compteur = 0
        
    
    def mode_de_jeu(self):
        self.destroy()
        fenetre_modedejeu = Mode_de_jeu_morpion()
        fenetre_modedejeu.mainloop()
        
    def surligner_bouton(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="floral white")
            if self.joueur_actuel == "X":
                self.liste_boutons[row * 3 + col].config(text="X")
            else:
                self.liste_boutons[row * 3 + col].config(text="O")

    def enlever_surligneur(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="#d9d9d9")
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
        print(f"{self.joueur_actuel} a cliqué sur la case {row}, {col}\n")  # Pour le débogage

        if self.verif_tour(row, col) and self.joueur_actuel == "X":  # Tour du joueur humain
            self.liste_boutons[row * 3 + col].config(text=self.joueur_actuel, state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant(self.joueur_actuel)
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "O"  # Changement de tour vers l'ordinateur
                self.ordinateur_joue()  # L'ordinateur joue automatiquement
                
    def ordinateur_joue(self):
        print("L'ordinateur réfléchit...\n")
        cases_vides = [(i, j) for i in range(3) for j in range(3) if self.morpion[i][j] == " "] # renvoie une liste de couples de coordonees de toutes les cases vides

        if cases_vides: # s'il y a des cases vides
            row, col = cases_vides[randint(0, len(cases_vides) - 1)] # choisit une case parmis les cases vides
            print(f"L'ordinateur choisit la case {row}, {col}\n")
            self.morpion[row][col] = "O"
            self.liste_boutons[row * 3 + col].config(text="O", state=DISABLED)
            self.compteur += 1

            if self.a_gagne():
                self.gagnant("O")
            elif self.jeu_nul():
                pass
            else:
                self.joueur_actuel = "X"  # Retour au joueur humain

                    
                    

    def a_gagne(self):
        print("a gagné?")
    # on regarde pour les lignes droites avec une boucle for
        for i in range(3): 
            if self.morpion[i][0] == self.morpion[i][1] == self.morpion[i][2] != " ":
                self.colorier_vert([(i, 0), (i, 1), (i, 2)])
                return True
                
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                self.colorier_vert([(0, i), (1, i), (2, i)])
                return True
            
                
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            self.colorier_vert([(0, 0), (1, 1), (2, 2)])
            return True
            
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            self.colorier_vert([(0, 2), (1, 1), (2, 0)])
            return True
        
        self.jeu_nul()

        print(f"non, le joueur {self.joueur_actuel} n'a pas gagné")
        print("------------------------------------------------------\n")
        return False

    def colorier_vert(self, positions):
        for row, col in positions:
            self.liste_boutons[row * 3 + col].config(bg="green")
    
    def gagnant(self, joueur):
        print(f"{self.joueur_actuel} est gagnant !")
        print("------------------------------------------------------\n")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
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
            winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
            self.arret_partie()
            self.ajouter_bouton_rejouer()
            return True
        return False
    
    def ajouter_bouton_rejouer(self):
        rejouer_bouton = Button(self, text="Rejouer", command=self.reinitialiser_jeu, bg='gray24', fg='white', font=("Arial", 14))
        rejouer_bouton.grid(column=0, row=5, columnspan=3, sticky="nsew", padx=10, pady=10)

    def reinitialiser_jeu(self):
        self.joueur_actuel = "X"
        self.morpion = [[" ", " ", " "] for _ in range(3)]
        self.compteur = 0
        for bouton in self.liste_boutons:
            bouton.config(text=" ", state=NORMAL, bg='white')
        for widget in self.grid_slaves():
            if isinstance(widget, Label):
                widget.destroy()
    
class Mode_de_IA(Tk):
    """
    Classe représentant une fenêtre avant de jouer au morpion qui permet de choisir la difficulté de l'ordinateur adversaire.
    """
    
    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        
        self.title("Choix de difficulté")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        bouton1v1 = Button(self, text="Facile", font=("Arial",20), height=6, width=12, command=lambda: self.creer_morpion_IA_Facile())
        bouton1v1.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        
        bouton1v1 = Button(self, text="Moyen", font=("Arial",20), height=6, width=12, command=lambda: self.creer_morpion_IA_Moyen())
        bouton1v1.grid(column=1, row=0, sticky="nsew", padx=10, pady=10)
        
        bouton1v1 = Button(self, text="Difficile", font=("Arial",20), height=6, width=12, command=lambda: self.creer_morpion_IA_Difficile())
        bouton1v1.grid(column=2, row=0, sticky="nsew", padx=10, pady=10)
        
    def creer_morpion_IA_Facile(self):
        self.destroy()
        fenetre = Morpion_1vPCalea()
        fenetre.mainloop()
        
    def creer_morpion_IA_Moyen(self):
        self.destroy()
        fenetre = Morpion_1vPCdef()
        fenetre.mainloop()

    def creer_morpion_IA_Difficile(self):
        self.destroy()
        fenetre = Morpion_1vPCdef_et_off()
        fenetre.mainloop()
    
class Mode_de_jeu_morpion(Tk):
    """
    Classe représentant la fenêtre de choix du mode de jeu de morpion. c'est aussi la première fenêtre aui s'affiche lors du démarrage
    """
    
    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        
        self.geometry("800x700")

        self.title("Choix du mode du jeu")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.grid_columnconfigure(1, weight=1)
        
        
        
        bouton1v1 = Button(self, text="1 v 1", font=("Arial",20), command=lambda: self.creer_morpion1v1())
        bouton1vpc = Button(self, text="1 v IA", font=("Arial",20), command=lambda: self.mode_morpion1vPC())
        
        
        bouton1v1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        bouton1vpc.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
    
    def creer_morpion1v1(self):
        self.destroy()
        fenetre = Morpion_1v1()
        fenetre.mainloop()
        
    def mode_morpion1vPC(self):
        self.destroy()
        fenetre = Mode_de_IA()
        fenetre.mainloop()
    
class Morpion_1v1(Tk):
    """
    Classe représentant le jeu de Morpion contre un autre joueur, les deux joueurs étant sur le même ordinateur 
    """

    def __init__(self):
        super().__init__()

        self.icon = PhotoImage(file="icon.png")
        self.iconphoto(False, self.icon)
        self.resizable(width=False, height=False)

        self.grid_rowconfigure(0, weight=0)  # ajoute une barre en plus pour ajouter des elements supplementaires
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(background='gray24')

        self.liste_boutons = list()

        bouton1 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 0))
        bouton1.grid(column=0, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton1)

        bouton2 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 1))
        bouton2.grid(column=1, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton2)

        bouton3 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(0, 2))
        bouton3.grid(column=2, row=1, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton3)

        bouton4 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 0))
        bouton4.grid(column=0, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton4)

        bouton5 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 1))
        bouton5.grid(column=1, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton5)

        bouton6 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(1, 2))
        bouton6.grid(column=2, row=2, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton6)

        bouton7 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 0))
        bouton7.grid(column=0, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton7)

        bouton8 = Button(self, text=" ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 1))
        bouton8.grid(column=1, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton8)

        bouton9 = Button(self, text="  ", font=("Arial",20), height=5, width=5, command=lambda: self.sur_bouton_clique(2, 2))
        bouton9.grid(column=2, row=3, sticky="nswe", padx=10, pady=10)
        self.liste_boutons.append(bouton9)
        
        retour_modedejeu_bouton = Button(self, text="mode de jeu", command=self.mode_de_jeu, bg='gray24', fg='white', font=("Arial", 14))
        retour_modedejeu_bouton.grid(column=0, row=6, columnspan=3, sticky="nsew", padx=3, pady=3)

        quitter_bouton = Button(self, text="Quitter", command=self.quitter_jeu, bg='gray24', fg='white', font=("Arial", 14))
        quitter_bouton.grid(column=0, row=7, columnspan=3, sticky="nsew", padx=3, pady=3)


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
        self.geometry("400x450")

        # On ajoute un titre à la fenêtre
        self.title("Morpion")
        
        self.compteur = 0

    def mode_de_jeu(self):
        self.destroy()
        fenetre_modedejeu = Mode_de_jeu_morpion()
        fenetre_modedejeu.mainloop()
        
    def surligner_bouton(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="floral white")
            if self.joueur_actuel == "X":
                self.liste_boutons[row * 3 + col].config(text="X")
            else:
                self.liste_boutons[row * 3 + col].config(text="O")

    def enlever_surligneur(self, row, col):
        if self.morpion[row][col] == " ":
            self.liste_boutons[row * 3 + col].config(bg="#d9d9d9")
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
                self.colorier_vert([(i, 0), (i, 1), (i, 2)])
                return True
                
            if self.morpion[0][i] == self.morpion[1][i] == self.morpion[2][i] != " ":
                self.colorier_vert([(0, i), (1, i), (2, i)])
                return True
            
                
    # on regarde pour les lignes diagonales
        if self.morpion[0][0] == self.morpion[1][1] == self.morpion[2][2] != " ":
            self.colorier_vert([(0, 0), (1, 1), (2, 2)])
            return True
            
        if self.morpion[0][2] == self.morpion[1][1] == self.morpion[2][0] != " ":
            self.colorier_vert([(0, 2), (1, 1), (2, 0)])
            return True
        
        self.jeu_nul()

        print(f"non, le joueur {self.joueur_actuel} n'a pas gagné")
        print("------------------------------------------------------\n")
        return False

    def colorier_vert(self, positions):
        for row, col in positions:
            self.liste_boutons[row * 3 + col].config(bg="green")
    
    def gagnant(self, joueur):
        print(f"{self.joueur_actuel} est gagnant !")
        print("------------------------------------------------------\n")
        winner_label = Label(self, text=f"joueur {joueur} a gagné!", bg='gray24', fg='white', font=("Arial", 16))
        winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
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
            winner_label.grid(column=0, row=4, columnspan=3, sticky="nsew", padx=10, pady=10)
            self.arret_partie()
            self.ajouter_bouton_rejouer()
            return True
        return False
    
    def ajouter_bouton_rejouer(self):
        rejouer_bouton = Button(self, text="Rejouer", command=self.reinitialiser_jeu, bg='gray24', fg='white', font=("Arial", 14))
        rejouer_bouton.grid(column=0, row=5, columnspan=3, sticky="nsew", padx=10, pady=10)

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
window = Mode_de_jeu_morpion()

#changement de l'icone de la fenetre

#window.iconphoto(False, PhotoImage(file="icon.png"))
#window.iconbitmap("icon.png")

window.mainloop()

### a faire :
###
### 1: ajouter des commentaires et une docstring pour la class
###
###

