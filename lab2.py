import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(30)
G.add_edge(0, 15)
G.add_edge(29, 15)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

centrality_values = list(centrality.values())
plt.plot(range(len(centrality_values)), centrality_values, 'o-')
#nx.draw(G, with_labels=True)
plt.show()
