import random


class MazeProblem:
    def __init__(self, maze, initial_mouse, initial_cheese):
        self.maze = maze  # Matriz 2D de celdas: ' ' libre, '#' pared
        self.initial_state = (initial_mouse, initial_cheese)
        self.height = len(maze)
        self.width = len(maze[0])

    def is_goal(self, state):
        mouse_pos, cheese_pos = state
        return mouse_pos == cheese_pos

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.height and 0 <= y < self.width

    def is_free(self, pos):
        x, y = pos
        return self.maze[x][y] != "#"

    def move_cheese(self, cheese):
        """Mueve el queso aleatoriamente a una celda libre adyacente."""
        x, y = cheese
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds((nx, ny)) and self.is_free((nx, ny)):
                return (nx, ny)
        return cheese  # Si no puede moverse, se queda

    def mutate_walls(self):
        """De forma aleatoria agrega, elimina o mueve paredes en el laberinto."""
        mutation_type = random.choice(["add", "remove", "move"])
        if mutation_type == "add":
            # Intenta agregar una pared en una celda libre
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            if self.maze[x][y] == " ":
                self.maze[x][y] = "#"

        elif mutation_type == "remove":
            # Intenta eliminar una pared existente
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            if self.maze[x][y] == "#":
                self.maze[x][y] = " "

        elif mutation_type == "move":
            # Intenta mover una pared de una posición a otra
            wall_positions = [
                (i, j)
                for i in range(self.height)
                for j in range(self.width)
                if self.maze[i][j] == "#"
            ]
            if wall_positions:
                wx, wy = random.choice(wall_positions)
                free_positions = [
                    (i, j)
                    for i in range(self.height)
                    for j in range(self.width)
                    if self.maze[i][j] == " "
                ]
                if free_positions:
                    fx, fy = random.choice(free_positions)
                    self.maze[wx][wy] = " "
                    self.maze[fx][fy] = "#"

    def result(self, state, action):
        """
        Aplica una acción al estado actual y devuelve un nuevo estado y su costo.
        Las acciones posibles son: 'UP', 'RIGHT', 'DOWN', 'LEFT'.
        """
        dir_map = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

        (mouse, cheese) = state
        dx, dy = dir_map[action]
        new_mouse = (mouse[0] + dx, mouse[1] + dy)

        if not self.in_bounds(new_mouse) or not self.is_free(new_mouse):
            return None, 0  # Movimiento inválido

        # Mover el queso aleatoriamente después del movimiento del ratón
        new_cheese = self.move_cheese(cheese)

        # Aplicar una mutación aleatoria a las paredes
        self.mutate_walls()

        return (new_mouse, new_cheese), 1  # El costo de cada movimiento es 1

    def heuristic(self, state):
        """Heurística: distancia Manhattan entre el ratón y el queso."""
        (mouse, cheese) = state
        return abs(mouse[0] - cheese[0]) + abs(mouse[1] - cheese[1])
