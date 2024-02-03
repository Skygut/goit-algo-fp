import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def heap_to_tree(heap):
    if not heap:
        return None

    root = Node(heap[0])
    node_queue = deque([root])
    i = 1

    while i < len(heap):
        current = node_queue.popleft()

        # Left child
        if i < len(heap):
            current.left = Node(heap[i])
            node_queue.append(current.left)
            i += 1

        # Right child
        if i < len(heap):
            current.right = Node(heap[i])
            node_queue.append(current.right)
            i += 1

    return root


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


def visualize_heap(heap):
    if not heap:
        return

    graph = nx.DiGraph()
    n = len(heap)

    for i in range(n):
        graph.add_node(heap[i])
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n:
            graph.add_edge(heap[i], heap[left_index])

        if right_index < n:
            graph.add_edge(heap[i], heap[right_index])

    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog="dot")
    nx.draw(
        graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12
    )
    plt.title("Min Heap Visualization")
    plt.show()


# Список елементів для створення мінімальної купи
elements = [0, 4, 5, 10, 1, 2, 3]

# Створення мінімальної купи зі списку
heapq.heapify(elements)

# Візуалізація мінімальної купи
visualize_heap(elements)

# Перетворення купи назад в бінарне дерево для обходу
min_heap_tree_for_traversal = heap_to_tree(elements)

# Виконання обходу DFS та BFS
dfs_result = dfs(min_heap_tree_for_traversal)
bfs_result = bfs(min_heap_tree_for_traversal)

dfs_result, bfs_result
