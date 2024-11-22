from heapq import heappop, heappush

from Utils import get_neighbors


def manhattan_distance(state, goal):
    # Calcul de la distance de Manhattan
    pass


def a_star_solver(puzzle, goal, k):
    open_set = []
    heappush(open_set, (0, puzzle))
    closed_set = set()

    while open_set:
        _, current = heappop(open_set)
        if current == goal:
            return True  # Résolu

        closed_set.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in closed_set:
                heappush(open_set, (f(neighbor), neighbor))

    return False  # Non résolu


# Utilisation pour 8-puzzle 0-swap et 10-swap
if __name__ == "__main__":
    puzzle = [[...]]  # Puzzle initial
    goal = [[...]]  # État cible
    print(a_star_solver(puzzle, goal, 10))  # Résolution avec 10-swap