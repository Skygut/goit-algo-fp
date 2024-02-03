import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges_combined(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            add_edges_combined(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            add_edges_combined(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs(root):
    visited = set()
    stack = [root]
    dfs_order = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            dfs_order.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return dfs_order


def bfs(root):
    visited = set()
    queue = deque([root])
    bfs_order = []
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.add(node)
            bfs_order.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return bfs_order


def update_node_colors_by_order_new(root, order):
    order_dict = {val: idx for idx, val in enumerate(order)}

    def update_colors(node):
        if node:
            color_intensity = order_dict[node.val] / len(order)
            node.color = (0.7, 0.7, 1 - color_intensity)
            update_colors(node.left)
            update_colors(node.right)

    update_colors(root)


def copy_tree(node):
    if node is None:
        return None
    new_node = Node(node.val)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    return new_node


def draw_trees_combined(dfs_root, bfs_root):
    dfs_tree = nx.DiGraph()
    dfs_pos = {}
    dfs_tree = add_edges_combined(dfs_tree, dfs_root, dfs_pos)

    bfs_tree = nx.DiGraph()
    bfs_pos = {}
    bfs_tree = add_edges_combined(bfs_tree, bfs_root, bfs_pos)

    dfs_colors = [node[1]["color"] for node in dfs_tree.nodes(data=True)]
    dfs_labels = {node[0]: node[1]["label"] for node in dfs_tree.nodes(data=True)}

    bfs_colors = [node[1]["color"] for node in bfs_tree.nodes(data=True)]
    bfs_labels = {node[0]: node[1]["label"] for node in bfs_tree.nodes(data=True)}

    plt.figure(figsize=(16, 8))
    plt.subplot(1, 2, 1)
    nx.draw(
        dfs_tree,
        pos=dfs_pos,
        labels=dfs_labels,
        arrows=False,
        node_size=2500,
        node_color=dfs_colors,
    )
    plt.title("DFS Tree Visualization")

    plt.subplot(1, 2, 2)
    nx.draw(
        bfs_tree,
        pos=bfs_pos,
        labels=bfs_labels,
        arrows=False,
        node_size=2500,
        node_color=bfs_colors,
    )
    plt.title("BFS Tree Visualization")
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(2)

# Виконання обходу DFS та оновлення кольорів
dfs_order = dfs(root)
dfs_tree_root = copy_tree(root)
update_node_colors_by_order_new(dfs_tree_root, dfs_order)

# Виконання обходу BFS та оновлення кольорів
bfs_order = bfs(root)
bfs_tree_root = copy_tree(root)
update_node_colors_by_order_new(bfs_tree_root, bfs_order)

# Візуалізація обох дерев на одній фігурі
draw_trees_combined(dfs_tree_root, bfs_tree_root)
