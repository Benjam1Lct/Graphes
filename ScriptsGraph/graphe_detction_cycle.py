BLANC, GRIS, NOIR = 1, 2, 3

def parcours_cy(g, couleur, s):
    """parcours en profondeur depuis le sommet s"""
    if couleur[s] == GRIS:
        return True
    if couleur[s] == NOIR:
        return False
    couleur[s] = GRIS
    for v in g.voisins(s):
        if parcours_cy(g, couleur, v):
            return True
    couleur[s] = NOIR
    return False

def cycle(g):
    couleur = {}
    for s in g.sommets():
        couleur[s] = BLANC
    for s in g.sommets():
        if parcours_cy(g, couleur, s):
            return True
    return False
