import uuid
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


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
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs(node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    if node and node.id not in visited:
        visited.add(node.id)
        order.append(node.id)
        dfs(node.left, visited, order)
        dfs(node.right, visited, order)
    return order


def bfs(root):
    if not root:
        return []
    visited, order, queue = set(), [], Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        if node.id not in visited:
            visited.add(node.id)
            order.append(node.id)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
    return order


def generate_color(index, total):
    base_red, base_green, base_blue = 18, 38, 240
    red = min(base_red + index * 10, 255)
    green = min(base_green + index * 10, 255)
    blue = min(base_blue + index * 10, 255)
    return f"#{red:02x}{green:02x}{blue:02x}"


def draw_tree_with_traversal_colors(tree_root, traversal_type="dfs"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    if traversal_type == "dfs":
        order = dfs(tree_root)
    else:  # bfs
        order = bfs(tree_root)
    total_nodes = len(order)
    colors = [
        generate_color(order.index(node), total_nodes) if node in order else "skyblue"
        for node in tree.nodes()
    ]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.title(f"{traversal_type.upper()} Traversal with Color Gradient")
    plt.show()


def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    plt.figure(figsize=(16, 5))

    plt.subplot(1, 2, 1)
    tree_dfs = nx.DiGraph()
    pos_dfs = {root.id: (0, 0)}
    tree_dfs = add_edges(tree_dfs, root, pos_dfs)
    order_dfs = dfs(root)
    total_nodes_dfs = len(order_dfs)
    colors_dfs = [
        generate_color(order_dfs.index(node), total_nodes_dfs)
        if node in order_dfs
        else "skyblue"
        for node in tree_dfs.nodes()
    ]
    labels_dfs = {node[0]: node[1]["label"] for node in tree_dfs.nodes(data=True)}
    nx.draw(
        tree_dfs,
        pos=pos_dfs,
        labels=labels_dfs,
        arrows=False,
        node_size=2500,
        node_color=colors_dfs,
    )
    plt.title("DFS Traversal with Color Gradient")

    plt.subplot(1, 2, 2)
    tree_bfs = nx.DiGraph()
    pos_bfs = {root.id: (0, 0)}
    tree_bfs = add_edges(tree_bfs, root, pos_bfs)
    order_bfs = bfs(root)
    total_nodes_bfs = len(order_bfs)
    colors_bfs = [
        generate_color(order_bfs.index(node), total_nodes_bfs)
        if node in order_bfs
        else "skyblue"
        for node in tree_bfs.nodes()
    ]
    labels_bfs = {node[0]: node[1]["label"] for node in tree_bfs.nodes(data=True)}
    nx.draw(
        tree_bfs,
        pos=pos_bfs,
        labels=labels_bfs,
        arrows=False,
        node_size=2500,
        node_color=colors_bfs,
    )
    plt.title("BFS Traversal with Color Gradient")

    plt.show()


if __name__ == "__main__":
    main()
