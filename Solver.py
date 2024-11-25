from heapq import heappop, heappush

from Utils import get_neighbors


def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:  # Ignorer la case vide
                goal_i, goal_j = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == value][
                    0]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


def a_star_solver(puzzle, goal, k):
    """Résolution A* pour un puzzle n x n."""

    def f(state):
        g_cost = k  # Le coût pour atteindre cet état
        h_cost = manhattan_distance(state, goal)  # Heuristique : distance de Manhattan
        return g_cost + h_cost

    open_set = []
    heappush(open_set, (0, puzzle))
    closed_set = set()
    came_from = {}
    came_from[tuple(tuple(row) for row in puzzle)] = None  # État initial sans parent

    while open_set:
        _, current = heappop(open_set)
        current_tuple = tuple(tuple(row) for row in current)

        # Vérifier si l'état actuel est égal à l'état final (goal)
        if current_tuple == tuple(tuple(row) for row in goal):
            # Reconstituer le chemin depuis le dictionnaire `came_from`
            path = []
            while current_tuple:
                path.append(current)
                current_tuple = came_from[current_tuple]
                if current_tuple:
                    current = [list(row) for row in current_tuple]
            print("Solution trouvée : ", path[::-1])  # Afficher le chemin inversé
            return path[::-1]  # Retourner le chemin dans l'ordre correct

        closed_set.add(current_tuple)
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in closed_set:
                heappush(open_set, (f(neighbor), neighbor))
                came_from[neighbor_tuple] = current_tuple

    return []  # Retourner une liste vide si aucune solution n'est trouvée



# Utilisation pour 8-puzzle 0-swap et 10-swap
if __name__ == "__main__":
    puzzle = [[...]]  # Puzzle initial
    goal = [[...]]  # État cible
    print(a_star_solver(puzzle, goal, 10))  # Résolution avec 10-swap