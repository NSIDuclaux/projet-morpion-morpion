Morpion_1vPC(Tk):
    """
    Classe représentant une interface graphique pour un jeu de Morpion (Tic-Tac-Toe) en mode joueur contre ordinateur.

    Cette classe hérite de Tk, le conteneur principal de la bibliothèque tkinter. Elle permet à un joueur humain de jouer contre un
    ordinateur dans un jeu de Morpion, avec un plateau de jeu de 3x3 cases. Le joueur humain utilise "X" et l'ordinateur utilise "O".

    Attributs:
    - liste_boutons (list): Liste contenant les boutons représentant les cases du plateau de jeu.
    - joueur_actuel (str): Indique quel joueur est actuellement en train de jouer, "X" pour le joueur humain et "O" pour l'ordinateur.
    - morpion (list): Matrice 3x3 représentant l'état actuel du jeu, chaque case peut contenir " ", "X", ou "O".
    - compteur (int): Compteur des tours joués, utilisé pour déterminer si la partie est terminée.

    Méthodes:
    - __init__(): Initialise la fenêtre de jeu, configure l'interface utilisateur et les boutons du plateau, et définit les règles de jeu.
    - mode_de_jeu(): Change le mode de jeu en affichant la fenêtre de sélection du mode de jeu.
    - surligner_bouton(row, col): Modifie le fond et le texte d'un bouton pour le mettre en surbrillance lorsque le curseur de la souris passe dessus.
    - enlever_surligneur(row, col): Enlève la surbrillance d'un bouton lorsqu'il n'est plus survolé.
    - arret_partie(): Désactive tous les boutons du jeu lorsque la partie est terminée.
    - quitter_jeu(): Ferme la fenêtre du jeu et arrête l'application.
    - verif_tour(row, col): Vérifie si un joueur peut jouer sur une case donnée et met à jour l'état du jeu.
    - sur_bouton_clique(row, col): Gère l'action d'un joueur qui clique sur une case. Si c'est au joueur de jouer, la case est marquée.
    - ordinateur_joue(): Fait jouer l'ordinateur en choisissant une case vide aléatoirement et met à jour l'état du jeu.
    - a_gagne(): Vérifie si un joueur a gagné la partie en contrôlant les lignes, colonnes, et diagonales.
    - colorier_boutons(positions): Change la couleur des boutons pour marquer une ligne gagnante.
    - gagnant(joueur): Affiche un message indiquant quel joueur a gagné et désactive les boutons du jeu.
    - jeu_nul(): Vérifie si la partie est nulle, c'est-à-dire qu'il n'y a plus de cases vides et qu'aucun joueur n'a gagné.
    - ajouter_bouton_rejouer(): Ajoute un bouton permettant de recommencer une nouvelle partie.
    - reinitialiser_jeu(): Réinitialise le jeu, remettant toutes les cases à vide et redémarrant les compteurs.
    """

    def __init__(self):
        """
        Initialise la fenêtre du jeu de Morpion avec les boutons représentant les cases du plateau de jeu,
        configure l'affichage, et définit le joueur humain ("X") comme premier joueur.
        """
        super().__init__()
        pass

Mode_de_jeu_morpion(Tk):
    """
    Classe représentant l'écran de sélection du mode de jeu pour un jeu de Morpion.

    Cette classe hérite de Tk, le conteneur principal de la bibliothèque tkinter. Elle permet au joueur de choisir entre
    deux modes de jeu : un jeu à 2 joueurs (1v1) ou un jeu contre l'ordinateur (1vPC). L'interface présente deux boutons
    permettant au joueur de choisir son mode de jeu.

    Attributs:
    - morpion (list): Matrice 3x3 représentant l'état actuel du jeu. Cependant, cet attribut est inutilisé dans cette classe,
      il semble être un reliquat d'une version précédente du code.

    Méthodes:
    - __init__(): Initialise la fenêtre de sélection du mode de jeu avec deux boutons permettant de choisir entre les modes "1 v 1" ou "1 v Ordinateur".
    - creer_morpion1v1(): Change la fenêtre actuelle pour créer une nouvelle partie de Morpion avec 2 joueurs (mode 1v1).
    - creer_morpion1vPC(): Change la fenêtre actuelle pour créer une nouvelle partie de Morpion contre l'ordinateur (mode 1vPC).
    """
    
    def __init__(self):
        """
        Initialise la fenêtre de sélection du mode de jeu avec deux boutons permettant de choisir entre les modes de jeu "1 v 1" ou "1 v Ordinateur".
        """
        pass


Morpion_1v1(Tk):
    """
    Classe représentant la fenêtre de jeu pour une partie de Morpion en mode 1v1 (2 joueurs).

    Cette classe hérite de Tk, le conteneur principal de la bibliothèque tkinter. Elle permet de jouer une partie de Morpion
    à 2 joueurs. L'interface affiche une grille de boutons pour que les joueurs puissent choisir où jouer leur coup.
    Chaque joueur joue à tour de rôle en appuyant sur les cases de la grille. La classe gère également la logique de fin de partie
    (gagnant ou match nul), l'affichage des messages de victoire ou de match nul, et permet de rejouer une nouvelle partie.

    Attributs:
    - liste_boutons (list): Liste contenant les boutons représentant chaque case de la grille de jeu.
    - joueur_actuel (str): Le joueur qui doit jouer actuellement, soit "X" soit "O".
    - morpion (list): La matrice 3x3 représentant l'état du jeu, avec " " pour une case vide, "X" ou "O" pour les cases occupées.
    - compteur (int): Compteur des coups joués, utilisé pour déterminer si la partie est nulle.

    Méthodes:
    - __init__(): Initialise la fenêtre de jeu, les boutons représentant la grille, et configure l'état initial du jeu.
    - mode_de_jeu(): Retourne à l'écran de sélection du mode de jeu.
    - surligner_bouton(row, col): Met en surbrillance un bouton lorsque la souris passe dessus, en affichant un "X" ou "O" selon le joueur actif.
    - enlever_surligner(row, col): Enlève la surbrillance d'un bouton quand la souris quitte la case.
    - arret_partie(): Désactive tous les boutons de la grille une fois la partie terminée.
    - quitter_jeu(): Ferme la fenêtre de jeu.
    - verif_tour(row, col): Vérifie si c'est au joueur actuel de jouer sur la case donnée. Si oui, marque la case avec son symbole.
    - sur_bouton_clique(row, col): Gère le clic sur un bouton de la grille, vérifie le tour du joueur, met à jour l'état et vérifie si quelqu'un a gagné.
    - a_gagne(): Vérifie si un joueur a gagné en vérifiant les lignes, colonnes et diagonales.
    - colorier_boutons(positions): Colorie en vert les boutons correspondant à une ligne, colonne ou diagonale gagnante.
    - gagnant(joueur): Affiche un message indiquant le gagnant et désactive les boutons.
    - jeu_nul(): Vérifie si la partie est nulle (toutes les cases sont remplies sans gagnant).
    - ajouter_bouton_rejouer(): Ajoute un bouton "Rejouer" après la fin de la partie pour recommencer une nouvelle partie.
    - reinitialiser_jeu(): Réinitialise la grille et l'état du jeu pour démarrer une nouvelle partie.
    """
    
    def __init__(self):
        """
        Initialise la fenêtre de jeu avec une grille de boutons et configure l'état initial du jeu.
        """
        pass

Morpion:
    """
    Classe représentant un jeu de Morpion (Tic-Tac-Toe).

    Cette classe gère le tableau de jeu, les tours des joueurs, la vérification des conditions de victoire et de match nul,
    et permet de lancer une partie complète en alternant les tours des joueurs jusqu'à ce qu'un joueur gagne ou que la partie
    se termine en match nul.

    Attributs:
    ----------
    morpion : list
        Une matrice 3x3 représentant l'état actuel du tableau du jeu. Chaque case peut être "X", "O", ou " ".
    compteur : int
        Un compteur pour suivre le nombre de tours joués.
    joueur_actuel : str
        Le joueur actuel, soit "X" soit "O".
    
    Méthodes:
    --------
    __init__(): Initialise l'état du jeu (tableau, compteur et joueur actuel).
    afficher_morpion(): Affiche le tableau du jeu dans la console.
    tour_joueur(): Permet à un joueur de jouer un tour en entrant les coordonnées de la case où il veut jouer.
    a_gagne(joueur): Vérifie si le joueur donné a gagné la partie.
    gagnant(): Détermine et retourne le gagnant, ou `None` si aucun gagnant.
    arrete_partie(): Affiche la fin de la partie et l'état final du tableau.
    lancer_tour(): Gère l'enchaînement des tours et déclare le gagnant ou un match nul.
    """
    
    def __init__(self):
        """
        Initialise l'état du jeu avec un tableau vide, un compteur à 0, et le joueur X comme premier joueur.
        """
        pass