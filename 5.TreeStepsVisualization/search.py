from collections import deque
from colorsys import hsv_to_rgb


def dfs_with_color_change(node, depth=0, visited=None):
    if visited is None:
        visited = set()

    if node is not None and node not in visited:
        print(f"Visiting Node {node.val}")
        hue = 200.0  # Yellow hue
        saturation = 1.0  # Full saturation
        value = 1.0 - (
            len(visited) * 0.19
        )  # Gradually decrease brightness based on traversal order
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
            value = 1.0 - (
                step * 0.16
            )  # Gradually decrease brightness based on traversal step
            alpha = 1.0
            r, g, b = hsv_to_rgb(hue / 360, saturation, value)
            current.color = (r, g, b, alpha)
            visited.add(current)  # Mark the node as visited

            # Enqueue child nodes with increased depth
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))
