import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges_heap(graph, heap, pos, index=0, x=0, y=0, layer=1):
    if index < len(heap):
        node = heap[index]
        graph.add_node(node.id, color=node.color, label=node.val)
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            graph.add_edge(node.id, heap[left_index].id)
            l = x - 1 / 2**layer
            pos[heap[left_index].id] = (l, y - 1)
            add_edges_heap(graph, heap, pos, left_index, x=l, y=y - 1, layer=layer + 1)

        if right_index < len(heap):
            graph.add_edge(node.id, heap[right_index].id)
            r = x + 1 / 2**layer
            pos[heap[right_index].id] = (r, y - 1)
            add_edges_heap(graph, heap, pos, right_index, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap):
    tree = nx.DiGraph()
    if heap:
        pos = {heap[0].id: (0, 0)}
        tree = add_edges_heap(tree, heap, pos)

        colors = [node[1]["color"] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
        )
        plt.show()


def main():
    heap = [Node(i) for i in range(7)]
    draw_heap(heap)


if __name__ == "__main__":
    main()
