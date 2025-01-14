from tictactoeterminal import*

class Partie:

    """Classe d'objet créant une partie pour le jeu morpion :

    - Une fois créée, la partie peut être lancée à tout moment
    - La partie se termine lorsqu'un joueur a gagné ou si la grille de la partie est entièrement remplie"""

    def __init__(self, partie, joueurs, compteur):
        self.partie = morpion
        self.joueurs = (joueur1, joueur2)
        joueur1 = 'X'
        joueur2 = 'O'
        self.compteur = 0

    def lancer_partie(self):
        while not morpion.fin_partie():
            lancer_tour()

    def grille_pleine(self):
        if morpion.nb_tours == 9:
            return True

    def fin_partie(self):
        if morpion.grille_pleine() == True:
            morpion.destroy()
            return "Égalité"
        