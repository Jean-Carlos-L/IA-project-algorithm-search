import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import numpy as np


def choose_file_and_load():
    def on_submit():
        selected_algorithm = algorithm_var.get()
        file_path = file_var.get()

        if not file_path:
            messagebox.showerror("Error", "Debes seleccionar un archivo.")
            return

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                mouse_pos = tuple(map(int, lines[0].split()))
                cheese_pos = tuple(map(int, lines[1].split()))
                maze_data = [list(line.strip()) for line in lines[2:]]
                maze = np.array(maze_data)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")
            return

        # Cerrar la ventana y devolver los datos
        root.result = (mouse_pos, cheese_pos, maze, selected_algorithm)
        root.destroy()

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            file_var.set(file_path)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Configuración Inicial")

    tk.Label(root, text="Seleccionar archivo de configuración:").pack(pady=5)
    file_var = tk.StringVar()
    tk.Entry(root, textvariable=file_var, width=50).pack(padx=10)
    tk.Button(root, text="Examinar", command=browse_file).pack(pady=5)

    # Selección del algoritmo
    tk.Label(root, text="Selecciona el algoritmo de búsqueda:").pack(pady=5)
    algorithm_var = tk.StringVar(value="DFS")
    algorithm_menu = ttk.Combobox(
        root, textvariable=algorithm_var, values=["DFS", "BFS", "A*"], state="readonly"
    )
    algorithm_menu.pack(pady=5)

    tk.Button(root, text="Cargar Configuración", command=on_submit).pack(pady=10)

    root.mainloop()

    return getattr(root, "result", (None, None, None, None))
