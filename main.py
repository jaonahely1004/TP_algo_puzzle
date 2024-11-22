import pygame
from Utils import generate_puzzle, generate_resolvable_puzzle
from Solver import a_star_solver

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


# Fonction pour choisir la dimension du puzzle

def choose_dimension(screen):
    font = pygame.font.Font(None, 74)
    options = [3, 4]  # Dimensions disponibles
    running = True
    selected = None
    #k = None



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
    #k = get_k_value(screen)
    return selected
def get_k_value(screen):
    font = pygame.font.Font(None, 50)
    input_text = ''
    running = True
    while running:
        screen.fill((255, 255, 255))

        promt_text = font.render("entrer la valeur de k :", True, (0, 0,  0))
        screen.blit(promt_text, (0, 0))

        k_text = font.render(input_text, True , (0, 0, 0))
        screen.blit(k_text, (250, 250))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT : running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        return int(input_text)
                    else:
                        input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isdigit():
                    input_text += event.unicode
    return ( int(k_text) + 1 )
#fonction pour la recherche de la case vide
def find_empty_pos(puzzle):
    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            if value == 0:  # Trouver la case vide
                return (i, j)

def draw_button(screen, text, x, y, width, height, font_size=50):
    font = pygame.font.Font(None, font_size)
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (200, 200, 200), button_rect)  # Couleur de fond
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Bordure noire

    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect


def draw_message(screen, message, width, height, font_size=50, max_width=None):
    """
    Affiche un message au centre de l'écran avec un ajustement automatique.

    :param screen: L'écran Pygame.
    :param message: Le message à afficher.
    :param width: Largeur de l'écran.
    :param height: Hauteur de l'écran.
    :param font_size: Taille initiale de la police.
    :param max_width: Largeur maximale du texte (facultatif).
    """
    font = pygame.font.Font(None, font_size)

    # Découper le message en lignes si nécessaire
    if max_width is None:
        max_width = width - 20  # Ajouter une marge de 20 pixels

    words = message.split()
    lines = []
    current_line = []

    for word in words:
        # Tester la largeur actuelle de la ligne
        test_line = ' '.join(current_line + [word])
        text_surface = font.render(test_line, True, (0, 0, 0))
        if text_surface.get_width() <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    # Ajouter la dernière ligne
    if current_line:
        lines.append(' '.join(current_line))

    # Dessiner chaque ligne au centre
    y_offset = (height - font_size * len(lines)) // 2
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (0, 255, 0))
        text_rect = text_surface.get_rect(center=(width // 2, y_offset + i * font_size))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()  # Mettre à jour l'écran


def solve_puzzle(screen, puzzle, goal, block_size):
    solution_steps = a_star_solver(puzzle, goal, 5)  # Résolution avec A*
    if solution_steps:
        for step in solution_steps:
            draw_puzzle(screen, step, block_size)
            pygame.display.flip()
            pygame.time.delay(200)  # Pause pour animer les étapes

        # Dessiner l'état final (dernier état de solution_steps)
        draw_puzzle(screen, solution_steps[-1], block_size)
        pygame.display.flip()  # S'assurer que l'affichage reste à jour

        return solution_steps  # Retourne les étapes pour mise à jour dans main
    else:
        print("Aucune solution trouvée.")
        return None


def is_solved(puzzle, goal):
    """
    Vérifie si le puzzle est dans l'état résolu (égal à l'état final).

    :param puzzle: Le puzzle actuel.
    :param goal: L'état final.
    :return: True si le puzzle est résolu, sinon False.
    """
    return puzzle == goal

# Fonction principale pour lancer le jeu
def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Afficher le menu pour choisir la dimension
    dimension = choose_dimension(screen)
    k = get_k_value(screen)

    if dimension is None:  # Si l'utilisateur quitte sans choisir
        pygame.quit()
        return

    pygame.display.set_caption(f"{dimension}x{dimension} Puzzle")

    # Exemple de génération de puzzle
    if k == 0:
        # Générer un puzzle résolvable si k == 0
        puzzle = generate_resolvable_puzzle(dimension)
    else:
        # Générer un puzzle aléatoire classique
        puzzle = generate_puzzle(dimension)
    print(puzzle)

    goal = [[(i * dimension + j + 1) % (dimension * dimension) for j in range(dimension)] for i in range(dimension)]

    # Taille d'une case dans le puzzle
    block_size = WIDTH // dimension

    # Position de la case vide (initialement à la dernière position)
    empty_pos = find_empty_pos(puzzle)
    print(empty_pos)

    # Nombre de déplacements effectués
    move_count = 0

    # Bouton pour la résolution automatique
    solve_button_rect = draw_button(screen, "Résoudre", 200, 620, 200, 50)

    # Liste pour suivre les pièces sélectionnées pour swap
    selected_pieces = []

    running = True
    solving = False
    game_finished = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Si la partie est terminée, attendre une nouvelle partie
            if game_finished:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # L'utilisateur peut cliquer pour redémarrer une nouvelle partie
                    dimension = choose_dimension(screen)
                    if dimension:
                        k = get_k_value(screen)
                        if k == 0:
                            # Générer un puzzle résolvable si k == 0
                            puzzle = generate_resolvable_puzzle(dimension)
                        else:
                            # Générer un puzzle aléatoire classique
                            puzzle = generate_puzzle(dimension)
                        print(puzzle)
                        goal = [[(i * dimension + j + 1) % (dimension * dimension) for j in range(dimension)]
                                for i in range(dimension)]
                        block_size = WIDTH // dimension
                        empty_pos = find_empty_pos(puzzle)
                        move_count = 0
                        solving = False
                        game_finished = False  # Réinitialiser l'état de fin
                continue

            # Détecter le clic sur le bouton
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button_rect.collidepoint(event.pos):
                    solving = True
            # Gérer les touches de direction pour déplacer une pièce
            if event.type == pygame.KEYDOWN:
                row, col = empty_pos
                old_empty_pos = empty_pos
                if event.key == pygame.K_UP and row < len(puzzle) - 1:  # Déplacer vers le haut si possible
                    puzzle[row][col], puzzle[row + 1][col] = puzzle[row + 1][col], puzzle[row][col]
                    empty_pos = (row + 1, col)
                elif event.key == pygame.K_DOWN and row > 0:  # Déplacer vers le bas si possible
                    puzzle[row][col], puzzle[row - 1][col] = puzzle[row - 1][col], puzzle[row][col]
                    empty_pos = (row - 1, col)
                elif event.key == pygame.K_LEFT and col < len(puzzle[0]) - 1:  # Déplacer vers la gauche si possible
                    puzzle[row][col], puzzle[row][col + 1] = puzzle[row][col + 1], puzzle[row][col]
                    empty_pos = (row, col + 1)
                elif event.key == pygame.K_RIGHT and col > 0:  # Déplacer vers la droite si possible
                    puzzle[row][col], puzzle[row][col - 1] = puzzle[row][col - 1], puzzle[row][col]
                    empty_pos = (row, col - 1)
                if empty_pos != old_empty_pos:
                    move_count += 1

                # Afficher l'état du puzzle après le mouvement
                screen.fill((255, 255, 255))
                draw_puzzle(screen, puzzle, block_size)
                pygame.display.flip()

                # Vérifier si le puzzle est résolu après le mouvement
                if is_solved(puzzle, goal):
                    game_finished = True

            # Si le nombre de déplacements atteint k, demander un swap

            if k == 0:
                pass
            elif move_count % k == 0 and move_count > 0:
                    selected_pieces = select_swap_pieces(screen, puzzle, block_size)
                    if selected_pieces:
                        # Swap les pièces sélectionnées
                        swap_pieces(puzzle, selected_pieces)
                        move_count = 0

        # Résolution automatique
        if solving:
            solution_steps = solve_puzzle(screen, puzzle, goal, block_size)
            if solution_steps:  # Si une solution a été trouvée
                puzzle = solution_steps[-1]  # Mettre à jour le puzzle avec l'état final
                game_finished = True
            solving = False

        # Effacer l'écran uniquement si nécessaire
        #if not solving:
            #screen.fill((255, 255, 255))

        if game_finished:
            draw_message(screen, "Partie Terminer ! Cliquez pour recommencer.", WIDTH, HEIGHT)
        else:
            # Dessiner le puzzle
            draw_puzzle(screen, puzzle, block_size)

            # Dessiner le bouton de résolution
            solve_button_rect = draw_button(screen, "Résoudre", 200, 620, 200, 50)

        pygame.display.flip()

    pygame.quit()

# Fonction pour sélectionner les pièces à échanger (swap)
def select_swap_pieces(screen, puzzle, block_size):
    font = pygame.font.Font(None, 74)
    selected = []
    running = True
    while running and len(selected) < 2:
        screen.fill((250, 255, 255))
        draw_puzzle(screen, puzzle, block_size)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Détecter la position du clic
                mouse_x, mouse_y = event.pos
                col = mouse_x // block_size
                row = mouse_y // block_size
                piece = puzzle[row][col]

                # Ajouter la pièce sélectionnée
                if piece != 0 and piece not in selected:
                    selected.append((row, col))
    return selected

# Fonction pour échanger deux pièces

def swap_pieces(puzzle, selected_pieces):
    (row1, col1), (row2, col2) = selected_pieces
    # Échanger les deux pièces sélectionnées
    puzzle[row1][col1], puzzle[row2][col2] = puzzle[row2][col2], puzzle[row1][col1]

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
