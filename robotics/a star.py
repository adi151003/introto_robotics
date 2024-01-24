import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
G = nx.DiGraph()

# Function for A* search
def astar_search(graph, start, goal):
    path = nx.astar_path(graph, start, goal, weight='weight')
    return path

# Take user input to define nodes, edges, and node weights
while True:
    node = input("Enter a node (or 'done' to finish adding nodes): ")
    if node == 'done':
        break
    node_weight = float(input(f"Enter the weight for node {node}: "))
    G.add_node(node, weight=node_weight)

while True:
    edge_start = input("Enter the start node of an edge (or 'done' to finish adding edges): ")
    if edge_start == 'done':
        break
    edge_end = input("Enter the end node of the edge: ")
    edge_weight = float(input("Enter the edge weight: "))
    G.add_edge(edge_start, edge_end, weight=edge_weight)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Take user input for start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Perform A* search
try:
    path = astar_search(G, start_node, goal_node)
    print("Shortest path:", path)
    print("Total cost:", nx.path_weight(G, path, weight='weight'))
except nx.NetworkXNoPath:
    print("No path found.")
except nx.NodeNotFound:
    print("Invalid node name.")