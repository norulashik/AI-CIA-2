import matplotlib.pyplot as plt
import heapq
import numpy as np
import networkx as nx

class AStar:
    def __init__(self, edges, heuristic_values):
        self.edges = edges
        self.graph = {}
        self.heuristics = heuristic_values
        self.path_found = False

        for start, end, cost in edges:
            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append((end, cost))

    def find_path(self, start_node, end_node):
        open_list = [(0, start_node, [])] 
        closed_set = set()

        while open_list:
            total_cost, current_node, path = heapq.heappop(open_list)

            if current_node == end_node:
                path.append(current_node)
                return path

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in closed_set:
                    heuristic_cost = self.heuristics[neighbor]
                    new_total_cost = total_cost + cost + heuristic_cost
                    new_path = path + [current_node]
                    heapq.heappush(open_list, (new_total_cost, neighbor, new_path))

        return []

    def show_path(self, start_node, end_node):
        path = self.find_path(start_node, end_node)
        if path:
            print("Path derived by A* Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

edges = [('S', 'A', 4), ('S', 'B', 5), ('A', 'B', 1), ('B', 'A', 3),
         ('A', 'D', 2), ('D', 'F', 1), ('B', 'C', 1), ('C', 'E', 2), ('F', 'G', 1)]
heuristic_values = {'S': 7, 'A': 3, 'B': 7, 'C': 1, 'D': 9, 'E': 3, 'F': 6, 'G': 3}


def plot_graph(edges, heuristic_values):
    nodes = set()
    for start, end, _ in edges:
        nodes.add(start)
        nodes.add(end)

    pos = {}
    for node in nodes:
        pos[node] = np.random.rand(2)

    plt.figure(figsize=(5, 5))
    for start, end, _ in edges:
        plt.plot([pos[start][0], pos[end][0]], [pos[start][1], pos[end][1]], 'b-')
    for node in nodes:
        plt.text(pos[node][0], pos[node][1], node, fontsize=16, ha='center')

    for node, value in heuristic_values.items():
        plt.text(pos[node][0], pos[node][1] - 0.1, f"H={value}", fontsize=12, ha='center')

    plt.show()



a_star = AStar(edges, heuristic_values)
a_star.show_path('S', 'G')
plot_graph(edges, heuristic_values)

