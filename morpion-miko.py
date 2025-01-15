class Morpion:
    """
    Classe représentant un jeu de Morpion.

    Attributs:
    ----------
    morpion : list
        Une matrice 3x3 représentant le tableau du jeu.
    compteur : int
        Un compteur pour suivre le nombre de tours joués.
    joueur_actuel : str
        Le joueur actuel, soit "X" soit "O".
    """
    def __init__(self):
        self.morpion = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        self.compteur = 0
        self.joueur_actuel = "X"

    def afficher_morpion(self):
        for ligne in self.morpion:
            print(ligne)

    def tour_joueur(self):
        ligne = int(input(f"{self.joueur_actuel}, entrez la ligne (1-3): ")) - 1
        colonne = int(input(f"{self.joueur_actuel}, entrez la colonne (1-3): ")) - 1

        if self.morpion[ligne][colonne] != " ":
            print("Cette case est déjà prise. Choisissez une autre case.")
            return False

        self.morpion[ligne][colonne] = self.joueur_actuel
        self.compteur += 1
        return True

    def a_gagne(self, joueur):
        morpion = self.morpion
        return (
            (morpion[0][0] == morpion[0][1] == morpion[0][2] == joueur) or
            (morpion[1][0] == morpion[1][1] == morpion[1][2] == joueur) or
            (morpion[2][0] == morpion[2][1] == morpion[2][2] == joueur) or
            (morpion[0][0] == morpion[1][0] == morpion[2][0] == joueur) or
            (morpion[0][1] == morpion[1][1] == morpion[2][1] == joueur) or
            (morpion[0][2] == morpion[1][2] == morpion[2][2] == joueur) or
            (morpion[0][0] == morpion[1][1] == morpion[2][2] == joueur) or
            (morpion[0][2] == morpion[1][1] == morpion[2][0] == joueur)
        )

    def gagnant(self):
        if self.a_gagne("X"):
            return "X"
        elif self.a_gagne("O"):
            return "O"
        return None

    def arrete_partie(self):
        print("Partie terminée.")
        self.afficher_morpion()

    def lancer_tour(self):
        jeu_en_cours = True

        while jeu_en_cours:
            self.afficher_morpion()
            print(f"C'est au tour de {self.joueur_actuel}")

            if self.tour_joueur():
                if self.a_gagne(self.joueur_actuel):
                    self.arrete_partie()
                    print(f"Le joueur {self.joueur_actuel} a gagné!")
                    jeu_en_cours = False
                elif self.compteur == 9:
                    self.arrete_partie()
                    print("Match nul!")
                    jeu_en_cours = False
                else:
                    if self.joueur_actuel == "X":
                        self.joueur_actuel = "O"
                    else:
                        self.joueur_actuel = "X"


# lancer le jeu
jeu = Morpion()
jeu.lancer_tour()