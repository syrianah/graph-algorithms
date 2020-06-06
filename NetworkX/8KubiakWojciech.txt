import networkx as nx
import matplotlib.pyplot as plt

opcje = {
    "with_labels": True, "node_size": 100
}
G = nx.Graph()
G = nx.cycle_graph(20)

plt.subplot(2, 3, 1)
plt.title('domyslny')
nx.draw(G, **opcje)

plt.subplot(2, 3, 2)
plt.title('kolisty')
nx.draw_circular(G, **opcje)

plt.subplot(2, 3, 3)
plt.title('losowy')
nx.draw_random(G, **opcje)

plt.subplot(2, 3, 4)
plt.title('na okregach')
nx.draw_shell(G, nlist=[[x for x in range(2, 20, 4)], [
              x for x in range(1, 20, 2)], [x for x in range(0, 20, 4)]], **opcje)

plt.subplot(2, 3, 5)
plt.title('dwudzielne')
nx.draw(G, **opcje, pos=nx.bipartite_layout(
    G, nodes=[x for x in range(0, 20, 2)]))

plt.subplot(2, 3, 6)
plt.title('dwudzielne w poziomie')
nx.draw(G, **opcje, pos=nx.bipartite_layout(
    G, nodes=[x for x in range(0, 20, 2)], align="horizontal"))

plt.show()
plt.savefig('nazwa.png')
