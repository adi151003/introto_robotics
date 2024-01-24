import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes
G.add_node('A',weight=10)
G.add_node('B',weight=8)
G.add_node('C',weight=5)
G.add_node('D',weight=7)
G.add_node('E',weight=3)
G.add_node('F',weight=6)
G.add_node('G',weight=5)
G.add_node('H',weight=3)
G.add_node('I',weight=1)
G.add_node('J',weight=0)

# Add weighted edges
G.add_edge('A', 'B', weight=6)
G.add_edge('B', 'C', weight=3)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=8)
G.add_edge('E', 'I', weight=5)
G.add_edge('E', 'J', weight=5)
G.add_edge('J', 'I', weight=3)
G.add_edge('F', 'G', weight=1)
G.add_edge('F', 'H', weight=7)
G.add_edge('G', 'I', weight=3)
G.add_edge('H', 'I', weight=2)

for edge in G.edges(data=True):
    print(edge)

def astar_search(graph, start, goal):
    open_set = [(0, start)]  # (f-cost, node)
    visited = set()
    while open_set:
        open_set.sort(key=lambda x: x[0])  # Sort the open set by f-cost (lowest first)
        current_cost, current_node = open_set.pop(0)  # Get the node with the lowest f-cost
        if current_node == goal:
            return current_cost
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                cost = current_cost + graph[current_node][neighbor]['weight']
                heuristic_cost = heuristic(neighbor, goal)  # A* heuristic (in this example, it's just 0)
                f_cost = cost + heuristic_cost
                open_set.append((f_cost, neighbor))
    return float('inf')  # If no path is found

# Define the A* heuristic function (in this example, it's 0)
def heuristic(node, goal):
    return G.nodes[node]['weight']

# Start and goal nodes
start_node = 'A'
goal_node = 'J'

shortest_path_cost = astar_search(G, start_node, goal_node)

if shortest_path_cost != float('inf'):
    print(f"Shortest path cost from {start_node} to {goal_node} is {shortest_path_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")

nx.draw(G, node_color='red', edge_color='blue', with_labels=True)
plt.title("Weighted Graph")
plt.show()