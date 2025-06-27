import networkx as nx
import matplotlib.pyplot as plt
import math
G = nx.Graph()
n0 = 0

for i in range(6):
    G.add_node(i)

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(1, 4)
G.add_edge(3, 5)
G.add_edge(0, 4)

nx.draw(G, with_labels=True)

# O(n^2)
def dijkstra(G, n0):
    d = [math.inf] * len(G) # длина кратчайшего пути
    used = [False] * len(G) # были проверены
    p = [n0] * len(G) # кратчайший путь
    d[n0] = 0
    for i in range(len(G)):
        v = -1
        # вершина, путь к которой минимален и она не проверялась
        for j in range(len(G)):
            if not used[j] and (v == -1 or d[j] < d[v]):
                v = j

        # если это псоледняя вершина
        if math.isinf(d[v]):
            break

        used[v] = True
        # вычисление длины пути для смежных вершин
        for e in G.edges(v):
            if d[v] + 1 < d[e[1]]:
                d[e[1]] = d[v] + 1
                p[e[1]] = v

    return p

def print_path(p, n0, i):
    print(f"{i}: ", end="")
    while i != n0:
        print(f"{i} - ", end="")
        i = p[i]
    print(f"{n0}")

p = dijkstra(G, n0)
for i in range(len(G)):
    print_path(p, n0, i)


plt.show()


