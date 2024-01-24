import networkx as nx
import matplotlib.pyplot as plt

# Define the input data
edges = [('A', 'B', 6), ('B', 'C', 3), ('B', 'D', 2), ('C', 'E', 5), ('D', 'E', 8), ('E', 'J', 5), ('A', 'F', 3),
         ('F', 'G', 1), ('F', 'H', 7), ('G', 'I', 3), ('H', 'I', 2), ('I', 'E', 5), ('I', 'J', 3)]

# Define the weights of nodes
node_weights = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 3, 'J': 0}

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph with weights
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Calculate shortest path using A* algorithm
shortest_path = nx.astar_path(G, source='A', target='J', weight='weight')

# Calculate the weight of the shortest path
shortest_path_weight = sum(G[shortest_path[i]][shortest_path[i + 1]]['weight'] for i in range(len(shortest_path) - 1))

# Create a list of edge colors for visualization (red for the shortest path, gray for others)
edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) else 'gray' for u, v in G.edges()]

# Create a list of node colors based on their weights
node_colors = [node_weights[node] for node in G.nodes()]

# Draw the graph with edge and node colors
pos = nx.spring_layout(G)  # Position nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, cmap=plt.cm.RdYlBu, node_size=800)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Add edge weights as labels

# Add node weights as labels
node_labels = {node: f'Weight: {node_weights[node]}' for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Display the weight of the shortest path
plt.text(0.5, 1.1, f'Shortest Path Weight: {shortest_path_weight}', transform=plt.gca().transAxes, fontsize=12)

# Show the graph
plt.show()