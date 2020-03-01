from graph_weights import graph_weights, read_data

num_vertices, matrix, vertices_in = read_data("Ex1/graph.txt")
graph = graph_weights(num_vertices, matrix, vertices_in)

print(graph)

for edge in vertices_in:
    if edge in graph.edge_dict.keys():
        graph.del_edge(edge)
    else:
        graph.add_edge(edge, 3)

print(graph)
