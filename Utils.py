import random

def generate_puzzle(n):
    # Génère un puzzle n x n mélangé
    puzzle = list(range(1, n * n)) + [0]  # 0 représente la case vide
    random.shuffle(puzzle[:-1])
    return [puzzle[i:i + n] for i in range(0, len(puzzle), n)]


def swap_pieces(puzzle):
    # Permet de swap deux pièces
    x1, y1, x2, y2 = get_random_positions(puzzle)
    puzzle[x1][y1], puzzle[x2][y2] = puzzle[x2][y2], puzzle[x1][y1]


def get_neighbors(state):
    # Renvoie les voisins possibles pour A*
    pass


def get_random_positions(puzzle):
    # Retourne deux positions aléatoires
    n = len(puzzle)
    x1, y1 = random.randint(0, n - 1), random.randint(0, n - 1)
    x2, y2 = random.randint(0, n - 1), random.randint(0, n - 1)
    return x1, y1, x2, y2



