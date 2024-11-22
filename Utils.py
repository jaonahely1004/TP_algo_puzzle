import random

def generate_puzzle(n):
    # Génère un puzzle n x n mélangé
    puzzle = list(range(1, n * n)) + [0]  # 0 représente la case vide
    random.shuffle(puzzle)
    return [puzzle[i:i + n] for i in range(0, len(puzzle), n)]

def generate_resolvable_puzzle(dimension, shuffle_moves=100):
    """
    Génère un puzzle résolvable en partant d'un état final et en effectuant des déplacements valides.

    :param dimension: Taille du puzzle (par exemple, 3 pour un puzzle 3x3).
    :param shuffle_moves: Nombre de déplacements aléatoires pour mélanger le puzzle.
    :return: Puzzle mélangé et solvable.
    """
    # Créer l'état final (goal)
    puzzle = [[(i * dimension + j + 1) % (dimension * dimension) for j in range(dimension)] for i in range(dimension)]

    # Trouver la position initiale de la case vide (0)
    empty_pos = (dimension - 1, dimension - 1)

    # Effectuer des déplacements inverses aléatoires
    for _ in range(shuffle_moves):
        row, col = empty_pos
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite
        random.shuffle(moves)  # Mélanger les directions

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < dimension and 0 <= new_col < dimension:
                # Échanger la case vide avec la case voisine
                puzzle[row][col], puzzle[new_row][new_col] = puzzle[new_row][new_col], puzzle[row][col]
                empty_pos = (new_row, new_col)
                break  # Effectuer un seul mouvement valide

    return puzzle


def swap_pieces(puzzle):
    # Permet de swap deux pièces
    x1, y1, x2, y2 = get_random_positions(puzzle)
    puzzle[x1][y1], puzzle[x2][y2] = puzzle[x2][y2], puzzle[x1][y1]


def get_neighbors(state):
    neighbors = []
    n = len(state)
    # Trouver la position de la case vide
    empty_pos = [(i, j) for i in range(n) for j in range(n) if state[i][j] == 0][0]
    row, col = empty_pos

    # Vérifier les mouvements possibles et générer les états voisins
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            new_state = [list(row) for row in state]  # Copie du tableau
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)

    return neighbors


def get_random_positions(puzzle):
    # Retourne deux positions aléatoires
    n = len(puzzle)
    x1, y1 = random.randint(0, n - 1), random.randint(0, n - 1)
    x2, y2 = random.randint(0, n - 1), random.randint(0, n - 1)
    return x1, y1, x2, y2



