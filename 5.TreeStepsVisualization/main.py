from node import Node
from graph import add_edges, draw_tree
from search import dfs_with_color_change, bfs_with_color_change

# Створюємо дерево
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Приклад використання
print("Алгоритм DFS:")
dfs_with_color_change(root)
draw_tree(root, "DFS")

print("\nАлгоритм BFS:")
bfs_with_color_change(root)
draw_tree(root, "BFS")
