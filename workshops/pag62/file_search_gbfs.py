import sys
import os
import heapq

# ================================
# Clase Node (estado en el grafo)
# ================================
class Node:
    def __init__(self, state, parent, action):
        self.state = state    # Ruta completa (ej. "/home/user/docs")
        self.parent = parent  # Nodo padre
        self.action = action  # Nombre del directorio/archivo (ej. "docs")

# =============================================
# Frontera con cola de prioridad (para GBFS)
# =============================================
class PriorityFrontier:
    def __init__(self, heuristic_func, goal):
        self.frontier = []  # [(h_value, counter, node), ...]
        self.counter = 0
        self.heuristic = heuristic_func
        self.goal = goal

    def add(self, node):
        h = self.heuristic(node.state, self.goal)
        heapq.heappush(self.frontier, (h, self.counter, node))
        self.counter += 1

    def contains_state(self, state):
        return any(n.state == state for _, _, n in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        h, count, node = heapq.heappop(self.frontier)
        return node

# =============================================
# Clase principal: Búsqueda de archivos con GBFS
# =============================================
class FileSearchGBFS:
    def __init__(self, start_dir, target_file):
        if not os.path.isdir(start_dir):
            raise Exception("start_dir must be a valid directory")
        self.start = os.path.abspath(start_dir)
        self.target = target_file
        self.solution = None
        self.num_explored = 0
        self.explored = set()

    # -------------------------------
    # Heurística: profundidad + nombre
    # -------------------------------
    def heuristic(self, state, target):
        depth = state.count(os.sep) - self.start.count(os.sep)
        name = os.path.basename(state).lower()
        target_parts = set(target.lower().replace('.', ' ').split())
        name_parts = set(name.replace('.', ' ').split())

        common = len(target_parts & name_parts)
        if common > 0:
            return 0  # ¡muy prometedor!
        return depth + 10  # penalización por profundidad

    # -------------------------------
    # Imprimir resultados
    # -------------------------------
    def print(self):
        print(f"\nStarting directory: {self.start}")
        if self.solution is not None:
            print("Solution found (GBFS):")
            path_names = " -> ".join(self.solution[0])
            full_path = os.path.join(*self.solution[1])
            print(f"Actions: {path_names}")
            print(f"Full path: {full_path}")
        else:
            print("No solution found.")
        print(f"Directories explored: {self.num_explored}")
        if self.solution:
            print(f"Explored directories: {sorted(list(self.explored))[:10]}...")

    # -------------------------------
    # Vecinos: contenido del directorio
    # -------------------------------
    def neighbors(self, state):
        result = []
        try:
            for item in os.listdir(state):
                item_path = os.path.join(state, item)
                if os.path.isdir(item_path) or os.path.isfile(item_path):
                    result.append((item, item_path))
        except (PermissionError, OSError):
            pass  # Ignorar directorios sin acceso
        return result

    # -------------------------------
    # Algoritmo GBFS
    # -------------------------------
    def solve(self):
        start = Node(state=self.start, parent=None, action=None)
        frontier = PriorityFrontier(self.heuristic, self.target)
        frontier.add(start)
        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("no solution")

            node = frontier.remove()
            self.num_explored += 1

            # ¿Es el archivo objetivo?
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

            self.explored.add(node.state)

            # Expandir vecinos
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

# ================================
# Ejecución desde línea de comandos
# ================================
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_search_gbfs.py <start_directory> <target_file>")
        sys.exit(1)

    start_dir = sys.argv[1]
    target_file = sys.argv[2]

    print(f"Searching for file: '{target_file}' in '{start_dir}' using GBFS...")

    searcher = FileSearchGBFS(start_dir, target_file)
    try:
        searcher.solve()
        searcher.print()
    except Exception as e:
        print(f"Error: {e}")
