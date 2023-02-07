def parcours_largeur(g, source):
    """parcours en largeur depuis le sommet source"""
    dist = {source: 0}
    courant = [source]
    suivant = []
    while len(courant) > 0:
        s = courant.pop()
        for v in g.voisins(s):
            if v not in dist:
                suivant.append(v)
                dist[v] = dist[s] + 1
        if len(courant) == 0:
            courant, suivant = suivant, []
    return dist

def distance(g, u, v):
    """distance de u à v (et None si pas de chemin)"""
    dist = parcours_largeur(g, u)
    return dist[v] if v in dist else None


if __name__ == '__main__':
    from exercice_5_corrige import Graphe
    matrice = [[0 ,1 ,1 ,0 ,0 ,0 ,0 ,0] , 
               [1 ,0 ,0 ,1 ,1 ,0 ,0 ,0] ,
               [1 ,0 ,0 ,1 ,0 ,0 ,0 ,0] ,
               [0 ,1 ,1 ,0 ,1 ,0 ,0 ,0] ,
               [0 ,1 ,0 ,1 ,0 ,1 ,1 ,0] ,
               [0 ,0 ,0 ,0 ,1 ,0 ,1 ,0] ,
               [0 ,0 ,0 ,0 ,1 ,1 ,0 ,1] ,
               [0 ,0 ,0 ,0 ,0 ,0 ,1 ,0]]
    
    g = Graphe(8)
    g.adj = matrice
    print(distance(g, 0, 7))