
#initialisation du morpion
morpion = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
compteur = 0

def premiere_partie():
    ligne = int(input("ligne: "))
    print(ligne)
    colonne = int(input("colonne: "))
    print(colonne)

    morpion[ligne-1][colonne-1] = "X"
    compteur += 1
    return morpion

def afficher_morpion:
    for ligne in morpion:
        print(ligne)

#debut partie et toutes les parties jouées par x
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

#deuxieme partie et toutes les parties jouées par o
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



#nombre de tours (a faire)
def lancer_tour():
    if compteur%2 == 1:
        tour_x()
    elif compteur%2 == 0:
        tour_o()
    else:
        return "Erreur de comptage"



#verification de doublon (a faire)


#a gagné (a faire)
#asdasdasd

