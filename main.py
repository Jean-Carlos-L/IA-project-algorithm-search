from src.algorithms.depth_first_search import depth_first_search
from src.algorithms.breadth_first_search import breadth_first_search
from src.algorithms.a_star_algorithm import a_star_search
from src.utils.node import Node
from src.utils.maze_dynamics import MazeDynamics
import numpy as np
from src.views.show_tree import plot_tree

if __name__ == "__main__":
    # maze = np.array(
    #     [
    #         [" ", "#", " ", " ", "#", " "],
    #         [" ", "#", " ", "#", " ", " "],
    #         [" ", " ", " ", "#", " ", "#"],
    #         ["#", " ", "#", " ", " ", " "],
    #         [" ", " ", " ", " ", "#", " "],
    #         ["#", "#", "#", " ", "#", " "],
    #     ]
    # )
    maze = np.array([[" ", " ", " ", "#"], ["#", " ", "#", " "], [" ", " ", " ", " "]])


    maze_dynamics = MazeDynamics(maze, (0,0), (2,3))
# eso es lo que le digo que pasa cuando le dejaba un paso y esa vaina se ponía loco 
    start_node = Node(maze, (0, 0), (2, 3))
    start_node.heuristic = start_node.calculate_heuristic()

    #all_nodes = depth_first_search(start_node)
    #all_nodes = breadth_first_search(start_node)
    all_nodes = a_star_search(start_node)
    plot_tree(all_nodes)
    for node in all_nodes:
        children = node.get_successors(maze_dynamics=maze_dynamics)
        # print(
        #     f"Node: {node.mouse_pos}, Children: {[child.mouse_pos for child in children]}"
        # )
        print(f"Node: {node.mouse_pos}")#
