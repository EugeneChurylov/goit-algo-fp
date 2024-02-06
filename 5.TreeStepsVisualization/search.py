from collections import deque
from colorsys import hsv_to_rgb


def dfs_with_color_change(node, depth=0, visited=None):
    if visited is None:
        visited = set()

    if node is not None and node not in visited:
        print(f"Переходимо на Node {node.val}")
        hue = 200.0
        saturation = 1.0
        value = 1.0 - (len(visited) * 0.19)
        alpha = 0.99
        r, g, b = hsv_to_rgb(hue / 360, saturation, value)
        node.color = (r, g, b, alpha)
        visited.add(node)
        dfs_with_color_change(node.left, depth + 1, visited)
        dfs_with_color_change(node.right, depth + 1, visited)


def bfs_with_color_change(node):
    if node is None:
        return

    queue = deque([(node, 0)])
    visited = set()
    step = 0

    while queue:
        step += 1

        current, depth = queue.popleft()
        if current not in visited:
            print(f"Переходимо на Node {current.val}")
            hue = 200.0
            saturation = 1.0
            value = 1.0 - (step * 0.16)
            alpha = 1.0
            r, g, b = hsv_to_rgb(hue / 360, saturation, value)
            current.color = (r, g, b, alpha)
            visited.add(current)

            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))
