import sys
import os

class Node:
    def __init__(self, state, parent, action):
        self.state = state  # Ruta completa del directorio o archivo actual
        self.parent = parent  # Nodo padre
        self.action = action  # Nombre del directorio o archivo al que se accede

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class FileSearch:
    def __init__(self, start_dir, target_file):
        # Validar que el directorio inicial exista
        if not os.path.isdir(start_dir):
            raise Exception("start_dir must be a valid directory")
        self.start = os.path.abspath(start_dir)  # Ruta absoluta del directorio inicial
        self.target = target_file  # Nombre del archivo objetivo
        self.solution = None
        self.num_explored = 0
        self.explored = set()

    def print(self):
        """Imprime el estado inicial, la solución (si existe) y los directorios explorados."""
        print(f"\nStarting directory: {self.start}")
        if self.solution is not None:
            print("Solution found:")
            print("Path:", " -> ".join(self.solution[1]))
        else:
            print("No solution found.")
        print(f"Directories explored: {self.num_explored}")
        #print("Explored directories:", sorted(list(self.explored)))
        print("Explored directories:")
        count = 1
        for node in sorted(list(self.explored)):
            print(f"{count}: {node}")
            count += 1

    def neighbors(self, state):
        """Devuelve los directorios y archivos accesibles desde el estado actual (directorio)."""
        result = []
        try:
            # Listar contenido del directorio actual
            for item in sorted(os.listdir(state)):
                item_path = os.path.join(state, item)
                # Incluir solo directorios y archivos accesibles
                if os.path.isdir(item_path) or os.path.isfile(item_path):
                    result.append((item, item_path))
        except (PermissionError, OSError):
            # Ignorar directorios o archivos a los que no se tiene acceso
            pass
        return result

    def solve(self, use_bfs=False):
        """Encuentra un archivo objetivo en el sistema de archivos usando DFS o BFS."""
        # Inicializar la frontera con el directorio inicial
        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier() if use_bfs else StackFrontier()
        frontier.add(start)
        self.explored = set()

        while True:
            # Si la frontera está vacía, no hay solución
            if frontier.empty():
                raise Exception("no solution")

            # Seleccionar un nodo de la frontera
            node = frontier.remove()
            self.num_explored += 1

            # Verificar si el nodo es el archivo objetivo
            if os.path.isfile(node.state) and os.path.basename(node.state) == self.target:
                actions = []
                paths = []
                while node.parent is not None:
                    actions.append(node.action)
                    paths.append(node.state)
                    node = node.parent
                actions.reverse()
                paths.reverse()
                self.solution = (actions, paths)
                return

            # Marcar el nodo como explorado
            self.explored.add(node.state)
            #print(f"-->{node.state}")

            # Agregar vecinos (directorios y archivos) a la frontera
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python file_search.py start_directory target_file")

    start_dir = sys.argv[1]
    target_file = sys.argv[2]

    print(f"Searching for file: {target_file}")
    fs = FileSearch(start_dir, target_file)

    print("Solving with DFS...")
    try:
        fs.solve(use_bfs=False)
        fs.print()
    except Exception as e:
        print(f"Error: {e}")

    # Opcionalmente, resolver con BFS
    print("\nSolving with BFS...")
    fs = FileSearch(start_dir, target_file)
    try:
        fs.solve(use_bfs=True)
        fs.print()
    except Exception as e:
        print(f"Error: {e}")
