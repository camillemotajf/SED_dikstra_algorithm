from priority_queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        self.adj_list[v] = []

    def add_edge(self, u, v, dist):
        edge = Edges()
        edge.vertex = v
        edge.distance = dist
        self.adj_list[u].append(edge)


class Vertex:
    def __init__(self):
        self.value = None

    def __repr__(self):
        return f"Vertex({self.value})"


class Edges:
    def __init__(self):
        self.distance = None
        self.vertex = None


def dijkstra(graph, start):
    previous = {v: None for v in graph.adj_list.keys()}
    visited = {v: False for v in graph.adj_list.keys()}
    distances = {v: float("inf") for v in graph.adj_list.keys()}
    distances[start] = 0
    
    queue = PriorityQueue()
    queue.add_task(0, start)

    while len(queue) > 0:
        removed_distance, removed = queue.pop_task()

        if visited[removed]:
            continue

        visited[removed] = True

        for edge in graph.adj_list[removed]:
            if visited[edge.vertex]:
                continue

            new_distance = removed_distance + edge.distance

            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)

    return distances, previous



if __name__ == "__main__":
    graph = Graph()

    A = Vertex(); A.value = "A"
    B = Vertex(); B.value = "B"
    C = Vertex(); C.value = "C"
    D = Vertex(); D.value = "D"
    E = Vertex(); E.value = "E"
    F = Vertex(); F.value = "F"
    G = Vertex(); G.value = "G"
    H = Vertex(); H.value = "H"

    for v in [A, B, C, D, E, F, G, H]:
        graph.add_vertex(v)

    graph.add_edge(A, B, 4)
    graph.add_edge(A, C, 2)
    graph.add_edge(C, B, 1)
    graph.add_edge(B, D, 5)
    graph.add_edge(C, D, 8)
    graph.add_edge(D, E, 6)

    dist, prev = dijkstra(graph, A)

    print("Distâncias:")
    for v in dist:
        print(v.value, "=", dist[v])

    print("\nAnteriores:")
    for v in prev:
        print(v.value, "<--", prev[v].value if prev[v] else None)
