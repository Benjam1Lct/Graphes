class Graphe:
    """un graphe comme un dictionnaire d'adjacence"""

    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arete(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].append(s2)

    def arete(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj)

    def voisins(self, s):
        return self.adj[s]

if __name__ == '__main__':
    g1 = Graphe()
    g1.ajouter_arete(0, 1)
    g1.ajouter_arete(0, 3)
    g1.ajouter_arete(1, 2)
    g1.ajouter_arete(3, 1)

    print(g1.adj)
    print(g1.sommets())
    print(g1.voisins(0))

    dic = {0: [1, 3], 1: [0, 2, 3], 2: [1], 3: [0, 1]}
    g2 = Graphe()
    g2.adj = dic
    print(g2.adj)
    print(g2.sommets())
    print(g2.voisins(1))

