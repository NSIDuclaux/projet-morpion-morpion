
#initialisation du morpion
morpion = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
compteur = 0

# initialisation/ premiere partie
def premiere_partie():
    ligne = int(input("ligne: "))
    print(ligne)
    colonne = int(input("colonne: "))
    print(colonne)

    morpion[ligne-1][colonne-1] = "X"
    compteur += 1
    return morpion

def afficher_morpion():
    for ligne in len(morpion):
        print(morpion[ligne])

#debut partie et toutes les parties jouées par x (fait)
def tour_x():
    ligne = int(input("ligne: "))
    print(ligne)
    colonne = int(input("colonne: "))
    print(colonne)
    
    if morpion[ligne-1][colonne-1] == "X":
        return "tu ne peux pas mettre un autre X sur cette case !"
    elif morpion[ligne-1][colonne-1] == "O":
        return "cette case est déjà prise par ton adversaire !"
    else:
        morpion[ligne-1][colonne-1] = "X"
    compteur += 1
    return morpion

#deuxieme partie et toutes les parties jouées par o (fait)
def tour_o():
    ligne = int(input("ligne: "))
    print(ligne)
    colonne = int(input("colonne: "))
    print(colonne)

    if morpion[ligne-1][colonne-1] == "O":
        return "tu ne peux pas mettre un autre O sur cette case !"
    elif morpion[ligne-1][colonne-1] == "X":
        return "cette case est déjà prise par ton adversaire !"
    else:
        morpion[ligne-1][colonne-1] = "O"
    compteur += 1
    return morpion



#lancer une partie apres la premiere (fait)
def lancer_tour():
    if compteur%2 == 1:
        tour_x()
    elif compteur%2 == 0:
        tour_o()
    else:
        return "Erreur de comptage"


#a gagné x ?(fait)
def a_gagne_x():
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
def a_gagne_o():
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
    

