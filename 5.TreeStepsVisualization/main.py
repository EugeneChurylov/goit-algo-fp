import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from colorsys import hsv_to_rgb

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color='white')
    plt.show()

def dfs_with_color_change(node, depth=0, visited=None):
    if visited is None:
        visited = set()

    if node is not None and node not in visited:
        print(f"Visiting Node {node.val}")
        hue = 200.0  # Yellow hue
        saturation = 1.0  # Full saturation
        value = 1.0 - (len(visited) * 0.19)  # Gradually decrease brightness based on traversal order
        alpha = 0.99
        r, g, b = hsv_to_rgb(hue / 360, saturation, value)
        node.color = (r, g, b, alpha)
        visited.add(node)
        dfs_with_color_change(node.left, depth + 1, visited)
        dfs_with_color_change(node.right, depth + 1, visited)
        
def bfs_with_color_change(node):
    if node is None:
        return

    queue = deque([(node, 0)])  # Initialize the queue with the root node and depth 0
    visited = set()  # Keep track of visited nodes
    step = 0  # Counter for BFS steps

    while queue:
        # Increment step counter for each BFS step
        step += 1
        
        current, depth = queue.popleft()  # Dequeue a node and its depth
        if current not in visited:
            print(f"Visiting Node {current.val}")
            hue = 200.0  # Yellow hue
            saturation = 1.0  # Full saturation
            value = 1.0 - (step * 0.16)  # Gradually decrease brightness based on traversal step
            alpha = 1.0
            r, g, b = hsv_to_rgb(hue / 360, saturation, value)
            current.color = (r, g, b, alpha)
            visited.add(current)  # Mark the node as visited
            
            # Enqueue child nodes with increased depth
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))

# Create the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Приклад роботи
print("Depth-First Search (DFS) with Color Change:")
dfs_with_color_change(root)
draw_tree(root)

# # Reset colors to original for BFS
root.color = "skyblue"
root.left.color = "skyblue"
root.right.color = "skyblue"
root.left.left.color = "skyblue"
root.left.right.color = "skyblue"
root.right.left.color = "skyblue"

print("\nBreadth-First Search (BFS) with Color Change:")
bfs_with_color_change(root)
draw_tree(root)
