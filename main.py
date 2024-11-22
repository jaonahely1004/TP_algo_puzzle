import pygame
from Utils import generate_puzzle  # Importation de la fonction pour générer le puzzle

# Fonction pour choisir la dimension du puzzle
def choose_dimension(screen):
    font = pygame.font.Font(None, 74)
    options = [3, 4]  # Dimensions disponibles
    running = True
    selected = None

    while running:
        screen.fill((255, 255, 255))

        # Afficher les options
        for idx, option in enumerate(options):
            text = font.render(f"{option}x{option}", True, (0, 0, 0))
            rect = text.get_rect(center=(300, 200 + idx * 100))
            pygame.draw.rect(screen, (200, 200, 200), rect.inflate(20, 20))
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for idx, option in enumerate(options):
                    rect = pygame.Rect(240, 180 + idx * 100, 120, 40)
                    if rect.collidepoint(event.pos):
                        selected = option
                        running = False

    return selected

# Fonction pour dessiner le puzzle
def draw_puzzle(screen, puzzle, block_size):
    font = pygame.font.Font(None, 74)  # Police pour les numéros

    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            x = j * block_size
            y = i * block_size

            # Dessiner une case (sauf si c'est la case vide)
            if value != 0:
                pygame.draw.rect(screen, (200, 200, 200), (x, y, block_size, block_size))
                pygame.draw.rect(screen, (0, 0, 0), (x, y, block_size, block_size), 2)

                # Dessiner le numéro de la case
                text = font.render(str(value), True, (0, 0, 0))
                screen.blit(text, (x + block_size // 4, y + block_size // 4))
            else:
                # Dessiner la case vide (simple case sans numéro)
                pygame.draw.rect(screen, (255, 255, 255), (x, y, block_size, block_size))

# Fonction principale pour lancer le jeu
def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Afficher le menu pour choisir la dimension
    dimension = choose_dimension(screen)

    if dimension is None:  # Si l'utilisateur quitte sans choisir
        pygame.quit()
        return

    pygame.display.set_caption(f"{dimension}x{dimension} Puzzle")

    # Exemple de génération de puzzle
    puzzle = generate_puzzle(dimension)

    # Taille d'une case dans le puzzle
    block_size = WIDTH // dimension

    # Position de la case vide (initialement à la dernière position)
    empty_pos = (dimension - 1, dimension - 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Gérer les touches de direction pour déplacer une pièce
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Flèche haut
                    empty_pos = move_puzzle("up", puzzle, empty_pos)
                elif event.key == pygame.K_DOWN:  # Flèche bas
                    empty_pos = move_puzzle("down", puzzle, empty_pos)
                elif event.key == pygame.K_LEFT:  # Flèche gauche
                    empty_pos = move_puzzle("left", puzzle, empty_pos)
                elif event.key == pygame.K_RIGHT:  # Flèche droite
                    empty_pos = move_puzzle("right", puzzle, empty_pos)

        # Effacer l'écran
        screen.fill((255, 255, 255))

        # Dessiner le puzzle
        draw_puzzle(screen, puzzle, block_size)

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()

# Fonction pour déplacer le puzzle selon la direction
def move_puzzle(direction, puzzle, empty_pos):
    row, col = empty_pos

    if direction == "up" and row > 0:  # Déplacer vers le haut
        puzzle[row][col], puzzle[row - 1][col] = puzzle[row - 1][col], puzzle[row][col]
        empty_pos = (row - 1, col)
    elif direction == "down" and row < len(puzzle) - 1:  # Déplacer vers le bas
        puzzle[row][col], puzzle[row + 1][col] = puzzle[row + 1][col], puzzle[row][col]
        empty_pos = (row + 1, col)
    elif direction == "left" and col > 0:  # Déplacer vers la gauche
        puzzle[row][col], puzzle[row][col - 1] = puzzle[row][col - 1], puzzle[row][col]
        empty_pos = (row, col - 1)
    elif direction == "right" and col < len(puzzle[0]) - 1:  # Déplacer vers la droite
        puzzle[row][col], puzzle[row][col + 1] = puzzle[row][col + 1], puzzle[row][col]
        empty_pos = (row, col + 1)

    return empty_pos

# Point d'entrée du programme
if __name__ == "__main__":
    main()
