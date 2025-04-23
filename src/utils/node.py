import numpy as np
from typing import Optional
import random


class Node:
    DIRECTIONS = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

    ORDERED_ACTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

    def __init__(
        self,
        maze: np.ndarray,
        mouse_pos: tuple[int, int],
        cheese_pos: tuple[int, int],
        cost: int = 0,
        heuristic: float = 0.0,
        height=0,
        width = 0,
        parent: Optional["Node"] = None,
        action: Optional[str] = None,
        original_maze: Optional[np.ndarray] = None,
        
    ):
        self.maze = maze
        self.mouse_pos = mouse_pos
        self.cheese_pos = cheese_pos
        self.cost = cost
        self.heuristic = heuristic if heuristic != 0.0 else self.calculate_heuristic()
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1 
        self.original_maze = original_maze if original_maze is not None else None
        self.height, self.width = self.maze.shape

    def is_goal(self) -> bool:
        return self.mouse_pos == self.cheese_pos

    def calculate_heuristic(self) -> float:
        x1, y1 = self.mouse_pos
        x2, y2 = self.cheese_pos
        return abs(x1 - x2) + abs(y1 - y2)

    def get_successors(self) -> list["Node"]:
        successors = []
        # 
        # Determinar el laberinto actual
        # if maze_override is not None:
        #     active_maze = maze_override
        # elif maze_dynamics is not None and self.depth % 2 == 0:
        #     active_maze = maze_dynamics.mutate()
        # else:
        #     active_maze = self.maze

        rows, cols = self.maze.shape


        for action in self.ORDERED_ACTIONS:
            dx, dy = self.DIRECTIONS[action]
            new_x = self.mouse_pos[0] + dx
            new_y = self.mouse_pos[1] + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and self.maze[new_x, new_y] != "#":
                new_mouse_pos = (new_x, new_y)
                new_node = Node(
                    maze=self.maze.copy(),
                    mouse_pos=new_mouse_pos,
                    cheese_pos=self.cheese_pos,
                    cost=self.cost + 1,
                    heuristic=0.0,
                    parent=self,
                    action=action,
                )
                new_node.heuristic = new_node.calculate_heuristic()
                successors.append(new_node)

        return successors
    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.mouse_pos == other.mouse_pos
            and self.cheese_pos == other.cheese_pos
            and np.array_equal(self.maze, other.maze)
        )

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __hash__(self):
        return hash((self.mouse_pos, self.cheese_pos, self.maze.tobytes()))

    def copy(self):
        return Node(
            self.maze.copy(),
            self.mouse_pos,
            self.cheese_pos,
            self.cost,
            self.heuristic,
            self.height,
            self.width,
            self.parent,
            self.action,
            self.original_maze,

        )
    # def __str__(self):
    #     return f"Mouse: {self.mouse_pos}, Cheese: {self.cheese_pos}, Cost: {self.cost}, Heuristic: {self.heuristic}, Action: {self.action}, Depth: {self.depth}"
    def __str__(self):
        return f"M: {self.mouse_pos}, h: {self.heuristic} g: {self.cost}"
    
    def mutate(self):

        self.original_maze = self.maze.copy()
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
        
        self.maze = mutated_maze