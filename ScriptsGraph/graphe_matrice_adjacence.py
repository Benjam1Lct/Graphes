class Graphe:
    """un graphe représenté par une matrice d'adjacence,
       où les sommets sont les entiers 0,1,...,n-1"""

    def __init__(self, n):
        self.n = n
        self.adj = [[0] * n for _ in range(n)]

    def ajouter_arete(self, s1, s2):
        self.adj[s1][s2] = 1

    def arete(self, s1, s2):
        return self.adj[s1][s2]

    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i] == 1:
                v.append(i)
        return v

if __name__ == '__main__':
    g1 = Graphe(4)
    g1.ajouter_arete(0, 1)
    g1.ajouter_arete(0, 3)
    g1.ajouter_arete(1, 2)
    g1.ajouter_arete(3, 1)

    print(g1.adj)

    g2 = Graphe(4)
    L = [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]]
    g2.adj= L
    print(g2.voisins(1))

            
