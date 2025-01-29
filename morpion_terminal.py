
#initialisation du morpion
def creation_jeu():
    morpion = [[" "," "," "],
               [" "," "," "],
               [" "," "," "]]
    return morpion, 0

# initialisation/ premiere partie
def premiere_partie():
    ligne = int(input("ligne: "))
    print(ligne)
    colonne = int(input("colonne: "))
    print(colonne)

    morpion[ligne-1][colonne-1] = "X"
    compteur += 1
    return morpion

def afficher_morpion(morpion):
    for ligne in morpion:
        print(morpion[ligne])

#debut partie et toutes les parties jouées par x (fait)
def tour_joueur(morpion, joueur):
    ligne = int(input(f"{joueur}, entrez la ligne (1-3): ")) - 1
    colonne = int(input(f"{joueur}, entrez la colonne (1-3): ")) - 1

    if morpion[ligne][colonne] != " ":
        print("Cette case est déjà prise. Choisissez une autre case.")
        return morpion, False

    morpion[ligne][colonne] = joueur
    return morpion, True


#lancer une partie apres la premiere (fait)
def lancer_tour():
    joueur_actuel = "X"
    morpion, compteur = creation_jeu()
    jeu_en_cours = True

    while jeu_en_cours:
        afficher_morpion(morpion)
        print(f"c'est au tour de {joueur_actuel}")


#a gagné x ?(fait)
def a_gagne_x(morpion):
    if morpion[0][0] == morpion[0][1] == morpion[0][2] and morpion[0][0] == "X":
        arrete_partie()
        return True
    elif morpion[1][0] == morpion[1][1] == morpion[1][2] and morpion[1][0] == "X":
        arrete_partie()
        return True
    elif morpion[2][0] == morpion[2][1] == morpion[2][2] and morpion[2][0] == "X":
        arrete_partie()
        return True
    elif morpion[0][0] == morpion[1][1] == morpion[2][2] and morpion[0][0] == "X":
        arrete_partie()
        return True
    elif morpion[0][2] == morpion[1][1] == morpion[2][0] and morpion[0][2] == "X":
        arrete_partie()
        return True
    elif morpion[0][0] == morpion[1][0] == morpion[2][0] and morpion[0][0] == "X":
        arrete_partie()
        return True
    elif morpion[0][1] == morpion[1][1] == morpion[2][1] and morpion[0][1] == "X":
        arrete_partie()
        return True

#a gagné o ?(fait)
def a_gagne_o(morpion):
    if morpion[0][0] == morpion[0][1] == morpion[0][2] and morpion[0][0] == "O":
        arrete_partie()
        return True
    elif morpion[1][0] == morpion[1][1] == morpion[1][2] and morpion[1][0] == "O":
        arrete_partie()
        return True
    elif morpion[2][0] == morpion[2][1] == morpion[2][2] and morpion[2][0] == "O":
        arrete_partie()
        return True
    elif morpion[0][0] == morpion[1][1] == morpion[2][2] and morpion[0][0] == "O":
        arrete_partie()
        return True
    elif morpion[0][2] == morpion[1][1] == morpion[2][0] and morpion[0][2] == "O":
        arrete_partie()
        return True
    elif morpion[0][0] == morpion[1][0] == morpion[2][0] and morpion[0][0] == "O":
        arrete_partie()
        return True
    elif morpion[0][1] == morpion[1][1] == morpion[2][1] and morpion[0][1] == "O":
        arrete_partie()
        return True

# fonction qui retourne le gagnant en tant que string
def gagnant():
    if a_gagne_x() == True:
        return "X"
    elif a_gagne_o() == True:
        return "O"
     
