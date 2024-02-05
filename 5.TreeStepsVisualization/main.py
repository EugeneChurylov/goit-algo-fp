import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_with_color_change(node):
    if node is not None:
        print(f"Visiting Node {node.val} - Color: 'yellow'")
        node.color = "yellow"  # Change color when visited
        draw_tree(root)  # Call draw_tree to visualize the changes
        dfs_with_color_change(node.left)
        dfs_with_color_change(node.right)

def bfs_with_color_change(node):
    if node is None:
        return

    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(f"Visiting Node {current.val} - Color: 'yellow'")
        current.color = "yellow"  # Change color when visited
        draw_tree(root)  # Call draw_tree to visualize the changes
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)

# Example usage
print("Depth-First Search (DFS) with Color Change:")
dfs_with_color_change(root)

# Reset colors to original for BFS
root.color = "skyblue"
root.left.color = "skyblue"
root.right.color = "skyblue"
root.left.left.color = "skyblue"
root.left.right.color = "skyblue"
root.right.left.color = "skyblue"
draw_tree(root)  # Reset colors

print("\n\nBreadth-First Search (BFS) with Color Change:")
bfs_with_color_change(root)
