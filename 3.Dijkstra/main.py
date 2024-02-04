import heapq
import networkx as nx
import matplotlib.pyplot as plt

def initialize_graph():
    # Ініціалізація графа з вагами ребер
    graph = {
    'A': {'B': 1, 'C': 4, 'E': 3, 'F': 5},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
    'E': {'A': 3, 'D': 7},
    'F': {'B': 4, 'C': 3, 'E': 2}
}
    return graph

def visualize_graph(graph):
    G = nx.Graph()

    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = {
        'A': (0, 0),
        'B': (0.5, 1),
        'C': (1.5, 1),
        'D': (2, 0),
        'E': (1.5, -1),
        'F': (0.5, -1)
    }

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

def initialize_algorithm(graph, start_vertex):
    # Ініціалізація відстаней та бінарної купи
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    return distances, priority_queue

def dijkstra_algorithm(graph, start_vertex):
    distances, priority_queue = initialize_algorithm(graph, start_vertex)

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

def main():
    graph = initialize_graph()
    start_vertex = 'A'
    shortest_paths = dijkstra_algorithm(graph, start_vertex)

    print("Найкоротші шляхи від вершини {} до:".format(start_vertex))
    for vertex, distance in shortest_paths.items():
        print("Вершини {}: {}".format(vertex, distance))

    graph = initialize_graph()
    visualize_graph(graph)

if __name__ == "__main__":
    main()
