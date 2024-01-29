import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


DG = nx.DiGraph()

for i in range(1, 16):
    DG.add_node(i)

weighted_edges = [
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 3),
    (2, 5, 2),
    (3, 6, 3),
    (4, 7, 1),
    (5, 7, 2),
    (6, 8, 1),
    (7, 9, 2),
    (8, 10, 3),
    (9, 10, 1),
    (1, 10, 4),
    (3, 7, 2),
    (5, 11, 2),
    (11, 12, 1),
    (12, 13, 3),
    (13, 14, 2),
    (14, 15, 1),
    (15, 1, 3),
    (10, 14, 15),
    (13, 15, 2),
]
DG.add_weighted_edges_from(weighted_edges)

fixed_positions = {
    1: (0.1, 0.9),
    2: (0.2, 0.7),
    3: (0.1, 0.5),
    4: (0.3, 0.9),
    5: (0.3, 0.7),
    6: (0.1, 0.3),
    7: (0.3, 0.5),
    8: (0.1, 0.1),
    9: (0.3, 0.3),
    10: (0.2, 0.1),
    11: (0.4, 0.9),
    12: (0.5, 0.7),
    13: (0.4, 0.5),
    14: (0.5, 0.3),
    15: (0.4, 0.1),
}


def main():
    graph = {node: {} for node in DG.nodes()}
    for u, v, weight in DG.edges(data="weight"):
        graph[u][v] = weight

    start_node = 1
    shortest_path = dijkstra(graph, start_node)

    plt.figure(figsize=(12, 10))
    nx.draw(
        DG,
        fixed_positions,
        with_labels=True,
        node_color="lightgreen",
        node_size=800,
        font_size=15,
        font_weight="bold",
    )
    nx.draw_networkx_edge_labels(
        DG, fixed_positions, edge_labels=nx.get_edge_attributes(DG, "weight")
    )
    plt.title("Граф транспортної мережі із 15 зупинками (вершинами)")
    plt.show()

    print("Найкоротший шлях від вершини 1 до вершини 15:", shortest_path)

    for node, paths in list(shortest_path.items())[1:]:
        print(f"Найкоротший шлях з вершини {start_node} до вершини {node} = {paths}")


if __name__ == "__main__":
    main()
