import tkinter as tk
from tkinter import Canvas

NODE_RADIUS = 20
X_SPACING = 100  # Aumentar el espaciado entre nodos
Y_SPACING = 50 # Espaciado entre niveles de profundidad


def layout_tree(node, x=100, y=100, depth=0, positions=None):
    if positions is None:
        positions = {}

    # Asignar la posición del nodo
    positions[node] = (x, y)
    
    # Obtener los hijos del nodo
    children = node.children
    if not children:
        return x, positions

    # Ajustar la posición inicial de los hijos
    child_x = x - (len(children) - 1) * (X_SPACING / 2)

    # Llamar recursivamente para los hijos
    for child in children:
        child_x, positions = layout_tree(child, child_x, y + Y_SPACING, depth + 1, positions)
        child_x += X_SPACING  

    return child_x, positions

def draw_tree(canvas, node, positions, drawn=None):
    if drawn is None:
        drawn = set()

    x, y = positions[node]

    # Dibujar nodo
    canvas.create_oval(x - NODE_RADIUS, y - NODE_RADIUS, x + NODE_RADIUS, y + NODE_RADIUS, fill="lightblue")
    canvas.create_text(x, y, text=str(node.state))

    # Dibujar líneas hacia hijos
    for child in node.children:
        child_x, child_y = positions[child]
        canvas.create_line(x, y + NODE_RADIUS, child_x, child_y - NODE_RADIUS)
        draw_tree(canvas, child, positions, drawn)

def show_tree(root_node):
    # Generar layout
    _, positions = layout_tree(root_node)

    # Crear ventana tkinter
    window = tk.Tk()
    window.title("Árbol de búsqueda")

    # Ajustar el tamaño del canvas
    canvas_width = max(x for x, y in positions.values()) + 300  # Agregar un margen extra
    canvas_height = max(y for x, y in positions.values()) + 300  # Agregar un margen extra

    canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    draw_tree(canvas, root_node, positions)
    window.mainloop()
