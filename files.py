import piles

"""Implémentation du type abstrait "file" avec deux piles"""


def creer_file():
    """Retourne une file vide"""
    pile_in = piles.creer()
    pile_out = piles.creer()
    return (pile_in, pile_out)


def taille_file(file):
    """Retourne le nombre d'éléments dans la file"""
    return piles.taille(file[0]) + piles.taille(file[1])


def est_vide_file(file):
    """Retourne True si la file est vide, False sinon"""
    return piles.est_vide(file[0]) and piles.est_vide(file[1])


def enfiler(file, element):
    """Ajoute un nouvel élément à l'arrière de la file"""
    piles.empiler(file[0], element)


def transferer(file):
    """Transfère les éléments de la pile d'entrée vers la pile de sortie"""
    while piles.taille(file[0]) != 0:
        item = piles.depiler(file[0])
        piles.empiler(file[1], item)


def defiler(file):
    """Retourne l'élément situé en tête de la file et le supprime de la file"""
    if taille_file(file) == 0:
        return None
    else:
        if piles.sommet(file[1]) is None:
            transferer(file)
        return file[1].pop()


def tete_file(file):
    """Retourne l'élément situé en tête de la file"""
    if taille_file(file) == 0:
        return None
    else:
        if piles.sommet(file[1]) is None:
            transferer(file)
        return piles.sommet(file[1])