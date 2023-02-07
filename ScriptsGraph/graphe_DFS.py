def parcours_profondeur(g, s, vus):
    """parcours en profondeur depuis le sommet s"""
    if s not in vus:
        vus.append(s)
        for v in g.voisins(s):
            parcours_profondeur(g, v, vus)
    return vus

    
