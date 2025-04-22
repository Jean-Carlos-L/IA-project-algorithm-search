import random
import numpy as np

class MazeDynamics:
    def __init__(self, maze: np.ndarray, mouse_pos: tuple[int, int], cheese_pos: tuple[int, int]):
        self.maze = maze
        self.height, self.width = self.maze.shape
        self.mouse_pos = mouse_pos
        self.cheese_pos = cheese_pos


    def mutate(self) -> np.ndarray:
        """Devuelve una copia del laberinto con una mutación aplicada."""
        mutated_maze = self.maze.copy()

        mutation_type = random.choices(
            population=['add', 'remove', 'move'],
            weights=[1, 2, 4],
            k=1
        )[0]

        if mutation_type == 'add':
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if mutated_maze[x, y] == ' ' and (x, y) != self.mouse_pos and (x, y) != self.cheese_pos:
                mutated_maze[x, y] = '#'

        elif mutation_type == 'remove':
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if mutated_maze[x, y] == '#':
                mutated_maze[x, y] = ' '

        elif mutation_type == 'move':
            walls = [(i, j) for i in range(self.height) for j in range(self.width) if mutated_maze[i, j] == '#']
            spaces = [(i, j) for i in range(self.height) for j in range(self.width)
                      if mutated_maze[i, j] == ' ' and (i, j) != self.mouse_pos and (i, j) != self.cheese_pos]
            if walls and spaces:
                wx, wy = random.choice(walls)
                fx, fy = random.choice(spaces)
                mutated_maze[wx, wy] = ' '
                mutated_maze[fx, fy] = '#'

        return mutated_maze