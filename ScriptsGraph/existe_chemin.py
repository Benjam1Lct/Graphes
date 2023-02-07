def existe_chemin(g, u, v):
    """existe-t-il un chemin de u à v ?"""
    vus = []
    parcours_profondeur(g, u, vus)
    return v in vus
