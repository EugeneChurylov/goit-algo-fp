from node import Node
from graph import add_edges, draw_tree
from search import dfs_with_color_change, bfs_with_color_change

# Create the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Example usage
print("Depth-First Search (DFS) with Color Change:")
dfs_with_color_change(root)
draw_tree(root)

print("\nBreadth-First Search (BFS) with Color Change:")
bfs_with_color_change(root)
draw_tree(root)
