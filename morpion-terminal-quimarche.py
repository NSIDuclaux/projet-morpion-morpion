#initialisation du morpion
def creation_jeu():
    morpion = [[" "," "," "],
               [" "," "," "],
               [" "," "," "]]
    return morpion, 0

# initialisation/ premiere partie
def premiere_partie(morpion, compteur):
    print("Premiere partie : Joueur X commence.")
    ligne = int(input("ligne (1-3): "))
    colonne = int(input("colonne (1-3): "))

    morpion[ligne-1][colonne-1] = "X"
    compteur += 1
    return morpion, compteur

def afficher_morpion(morpion):
    for ligne in morpion:
        print("|" + "|".join(ligne) + "|")
        print("-------")

#debut partie et toutes les parties jouées par x (fait)
def tour_joueur(morpion, joueur):
    while True:
        ligne = int(input(f"{joueur}, entrez la ligne (1-3): ")) - 1
        colonne = int(input(f"{joueur}, entrez la colonne (1-3): ")) - 1

        if not (0 <= ligne <= 2 and 0 <= colonne <= 2):
            print("Ligne ou colonne invalide. Veuillez entrer des nombres entre 1 et 3.")
            continue

        if morpion[ligne][colonne] != " ":
            print("Cette case est deja prise. Choisissez une autre case.")
            continue

        morpion[ligne][colonne] = joueur
        return morpion


#lancer une partie apres la premiere (fait)
def lancer_tour():
    morpion, compteur = creation_jeu()
    morpion, compteur = premiere_partie(morpion, compteur)
    joueur_actuel = "O"
    jeu_en_cours = True

    while jeu_en_cours:
        afficher_morpion(morpion)
        print(f"C'est au tour de {joueur_actuel}")
        morpion = tour_joueur(morpion, joueur_actuel)
        compteur += 1

        if a_gagne_x(morpion):
            afficher_morpion(morpion)
            print("X a gagne!")
            jeu_en_cours = False
        elif a_gagne_o(morpion):
            afficher_morpion(morpion)
            print("O a gagne!")
            jeu_en_cours = False
        elif compteur == 9:
            afficher_morpion(morpion)
            print("Match nul!")
            jeu_en_cours = False
        else: 
            joueur_actuel = "X" if joueur_actuel == "O" else "O"



#a gagné x ?(fait)
def a_gagne_x(morpion):
    for i in range(3):
        if morpion[i][0] == morpion[i][1] == morpion[i][2] == "X":
            return True
        if morpion[0][i] == morpion[1][i] == morpion[2][i] == "X":
            return True
    if morpion[0][0] == morpion[1][1] == morpion[2][2] == "X":
        return True
    if morpion[0][2] == morpion[1][1] == morpion[2][0] == "X":
        return True
    return False

#a gagné o ?(fait)
def a_gagne_o(morpion):
    for i in range(3):
        if morpion[i][0] == morpion[i][1] == morpion[i][2] == "O":
            return True
        if morpion[0][i] == morpion[1][i] == morpion[2][i] == "O":
            return True
    if morpion[0][0] == morpion[1][1] == morpion[2][2] == "O":
        return True
    if morpion[0][2] == morpion[1][1] == morpion[2][0] == "O":
        return True
    return False

# fonction qui retourne le gagnant en tant que string - you don't really need this, because you can just check a_gagne_x and a_gagne_o directly
def gagnant(morpion):
    if a_gagne_x(morpion):
        return "X"
    elif a_gagne_o(morpion):
        return "O"
    else:
        return None


# arrete partie et affiche le tableau final ( i've removed this because it's not really needed, just print the board)
def arrete_partie():
    print("fin de partie")

lancer_tour()