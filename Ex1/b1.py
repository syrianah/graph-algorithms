matrix = []
vertices = []

with open("graph.txt") as f:
    num_vertices = int(f.readline().split("\n")[0])
    for _ in range(num_vertices):
        line = f.readline().split("\n")[0].split(" ")
        matrix.append([float("inf") if i == "-" else int(i) for i in line])
    for x in f.readlines():
        new_x = [y.replace("\n", "").replace(" ", "") for y in x]
        new_x = list(filter(lambda x: x != '', new_x))
        vertices.append((new_x[0], new_x[1]))

# print(num_vertices)
# print(matrix)
# print(vertices)


def adjacency_list(num_vertices, matrix):
    adj_dict = {}
    for i, row in enumerate(matrix):
        vertex = {}
        for j, x in enumerate(row):
            if x != float("inf"):
                vertex[j+1] = x
        adj_dict[i+1] = vertex
    return adj_dict


def edge_list(num_vertices, matrix):
    edge_dict = {}
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x != float("inf"):
                if (j+1, i+1) not in edge_dict.keys():
                    edge_dict[(i+1, j+1)] = x
    return edge_dict


def graph(num_vertices, matrix):
    vertices = []
    for i in range(num_vertices):
        vertices.append(i+1)
    return vertices


adj = adjacency_list(num_vertices, matrix)
# print(adj)

edge = edge_list(num_vertices, matrix)
print(edge)

graph = graph(num_vertices, matrix)
# print(graph)
