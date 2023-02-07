from queue import *

def parcours_largeur(g, source):
    """parcours en largeur depuis le sommet source"""
    visite = []
    file = Queue()
    file.put(source)
    while file.qsize() > 0:
        sommet = file.get()
        if sommet not in visite:
            visite.append(sommet)
            for s in g.voisins(sommet):
                if s not in visite:
                    file.put(s)
    return visite
