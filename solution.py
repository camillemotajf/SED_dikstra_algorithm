import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = [] # inicializando uma lista vazia para cada source

        for s, d, weight in edges:
            adj[s].append([d, weight])
        
        shortest = {}
        parent = {src: None}
        minHeap = [[0, src]]
        while minHeap:
            print(minHeap)
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if not n2 in shortest:
                    parent[n2] = n1
                    heapq.heappush(minHeap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest, parent
    
def plot_graph_with_path(edges, n, parent):

    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    
    for s, d, w in edges:
        G.add_edge(s, d, weight=w)

    pos = nx.spring_layout(G, seed=42)

    # 🟩 Construir o conjunto de arestas do caminho mínimo
    shortest_edges = []
    for node in parent:
        p = parent[node]
        if p is not None:
            shortest_edges.append((p, node))

    plt.figure(figsize=(8, 6))

    # Desenhar arestas normais
    nx.draw_networkx_edges(G, pos,
                           edgelist=G.edges(),
                           edge_color="gray",
                           arrows=True,
                           alpha=0.5)

    # Desenhar arestas do caminho mínimo em verde
    nx.draw_networkx_edges(G, pos,
                           edgelist=shortest_edges,
                           edge_color="green",
                           width=3,
                           arrows=True)

    # Nós
    nx.draw_networkx_nodes(G, pos,
                           node_color="skyblue",
                           node_size=2000)

    # Rótulos
    nx.draw_networkx_labels(G, pos, font_size=15, font_weight='bold')

    # Pesos
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Grafo com Caminhos Mínimos Destacados")
    plt.axis("off")
    plt.show()

    
if __name__ == "__main__":
    n = 5
    edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
    src = 0

    sol = Solution()

    shortest, parent = sol.shortestPath(n, edges, src)
    plot_graph_with_path(edges, n, parent)
    print(shortest)