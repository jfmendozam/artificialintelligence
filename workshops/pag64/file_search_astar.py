import heapq
import os
import sys

class Node:
    def __init__(self, state, parent, action, g=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # costo desde inicio

class AStarFrontier:
    def __init__(self, heuristic_func, start_g=0):
        self.frontier = []
        self.counter = 0
        self.heuristic = heuristic_func
        self.start_g = start_g

    def add(self, node, goal):
        h = self.heuristic(node.state, goal)
        f = node.g + h
        heapq.heappush(self.frontier, (f, self.counter, node))
        self.counter += 1

    def contains_state(self, state):
        return any(n.state == state for _, _, n in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        f, count, node = heapq.heappop(self.frontier)
        return node

class FileSearchAStar:
    def __init__(self, start_dir, target_file):
        if not os.path.isdir(start_dir):
            raise Exception("Invalid start directory")
        self.start = os.path.abspath(start_dir)
        self.target = target_file
        self.solution = None
        self.num_explored = 0
        self.explored = set()

    def heuristic(self, state, target):
        # Partes del nombre objetivo
        parts = set(target.lower().replace('.', ' ').split())
        name = os.path.basename(state).lower().replace('.', ' ')
        name_parts = set(name.split())
        matched = len(parts & name_parts)
        return len(parts) - matched  # partes que faltan

    def print(self):
        print(f"\nStarting directory: {self.start}")
        if self.solution:
            print("Solution found (A*):")
            print("Path:", " -> ".join(self.solution[0]))
            print(f"Full path: {os.path.join(*self.solution[1])}")
            print(f"Depth: {len(self.solution[0])}")
        else:
            print("No solution found.")
        print(f"Nodes explored: {self.num_explored}")

    def neighbors(self, state):
        result = []
        try:
            for item in os.listdir(state):
                path = os.path.join(state, item)
                if os.path.exists(path):
                    result.append((item, path))
        except:
            pass
        return result

    def solve(self):
        start = Node(state=self.start, parent=None, action=None, g=0)
        frontier = AStarFrontier(self.heuristic)
        frontier.add(start, self.target)
        self.explored = set()

        while True:
            if frontier.empty():
                return

            node = frontier.remove()
            self.num_explored += 1

            if os.path.isfile(node.state) and os.path.basename(node.state) == self.target:
                actions = []
                states = []
                current = node
                while current.parent is not None:
                    actions.append(current.action)
                    states.append(current.state)
                    current = current.parent
                actions.reverse()
                states.reverse()
                self.solution = (actions, states)
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if state not in self.explored and not frontier.contains_state(state):
                    child = Node(state=state, parent=node, action=action, g=node.g + 1)
                    frontier.add(child, self.target)

# === Ejecución ===
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_search_astar.py <dir> <file>")
        sys.exit(1)

    searcher = FileSearchAStar(sys.argv[1], sys.argv[2])
    searcher.solve()
    searcher.print()
