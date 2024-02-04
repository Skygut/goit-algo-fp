import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        # Ініціалізація вузла дерева
        self.left = None  # лівий дочірній вузол
        self.right = None  # правий дочірній вузол
        self.val = key  # значення вузла
        self.color = color  # колір вузла (за замовчуванням - небесно-блакитний)
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор для вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додавання вузла до графа
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            # Додавання ребра до лівого дочірнього вузла
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            # Рекурсивний виклик для лівого дочірнього вузла
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            # Додавання ребра до правого дочірнього вузла
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            # Рекурсивний виклик для правого дочірнього вузла
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    # Створення порожнього напрямленого графа
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореня дерева
    tree = add_edges(tree, tree_root, pos)

    # Отримання кольорів і міток для вузлів
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    print(colors)
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))  # Розмір вікна для візуалізації
    # Малювання дерева
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()  # Показати візуалізацію дерева


# Створення дерева та його вузлів
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація дерева
draw_tree(root)
