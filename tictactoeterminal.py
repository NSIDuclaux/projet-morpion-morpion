morpion = [["E","E","E"],["E","E","E"],["E","E","E"]]
    

colonne = int(input("colonne: "))
print(colonne)
ligne = int(input("ligne: "))
print(ligne)
morpion[ligne][colonne] = "X"
print(morpion)
