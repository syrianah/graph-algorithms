
def read_data(path):
    matrix = []
    vertices_in = []

    with open(path) as f:
        num_vertices = int(f.readline().split("\n")[0])
        for _ in range(num_vertices):
            line = f.readline().split("\n")[0].split(" ")
            matrix.append([float("inf") if i == "-" else int(i) for i in line])
        for x in f.readlines():
            new_x = [y.replace("\n", "").replace(" ", "") for y in x]
            new_x = list(filter(lambda x: x != '', new_x))
            vertices_in.append((int(new_x[0]), int(new_x[1])))

    return num_vertices, matrix, vertices_in


# print(num_vertices)
# print(matrix)
# print(vertices_in)


class graph_weights():
    def __init__(self, num_vertices, matrix, vertices_in):
        self.num_vertices = num_vertices
        self.matrix = matrix
        self.vertices_in = vertices_in
        self.adj_dict = {}
        self.edge_dict = {}
        self.header = {}

        self.update()

    def adjacency_list(self):
        for i, row in enumerate(self.matrix):
            vertex = {}
            for j, x in enumerate(row):
                if x != float("inf"):
                    vertex[j+1] = x
            self.adj_dict[i+1] = vertex

    def edge_list(self):
        for i, row in enumerate(self.matrix):
            for j, x in enumerate(row):
                if x != float("inf"):
                    if (j+1, i+1) not in self.edge_dict.keys():
                        self.edge_dict[(i+1, j+1)] = x

    def create_header(self):
        for i, row in enumerate(self.matrix):
            vertex = []
            for j, x in enumerate(row):
                if x != float("inf"):
                    vertex.append(j+1)
            self.header[i+1] = vertex

    def add_vertex(self):
        self.num_vertices += 1
        for row in self.matrix:
            row.append(float("inf"))
        self.matrix.append([float("inf") for x in range(self.num_vertices)])

    def del_vertex(self, vertex):
        if vertex <= self.num_vertices:
            print("Delete vertex: " + str(vertex))
            self.num_vertices -= 1
            self.matrix.pop(vertex-1)
            for row in self.matrix:
                row.pop(vertex-1)
            self.update()

        else:
            print("Vertex " + str(vertex) + " don't exist in graph.")

    def add_edge(self, edge, weight):
        if max(edge) <= self.num_vertices:
            print("Add edge: " + str(edge))
            self.matrix[edge[0]-1][edge[1]-1] = weight
            self.matrix[edge[1]-1][edge[0]-1] = weight
            self.update()
        else:
            print("Can't add, this edge ")

    def del_edge(self, edge):
        if max(edge) <= self.num_vertices:
            print("Delete edge: " + str(edge))
            self.matrix[edge[0]-1][edge[1]-1] = float('inf')
            self.matrix[edge[1]-1][edge[0]-1] = float('inf')
            self.update()
        else:
            print("Can't add, this edge ")

    def edge_weight(self, edge):
        if edge in self.edge_dict.keys():
            print("Edge weight: " + self.edge_dict[edge])
        else:
            print("This edge: " + str(edge) + " don't exist in graph.")

    def update(self):
        self.adjacency_list()
        self.edge_list()
        self.create_header()


# num_vertices, matrix, vertices_in = read_data("Ex1/graph.txt")
# graph = graph_weights(num_vertices, matrix, vertices_in)
# print(graph.edge_weight((2, 5)))
# graph.add_vertex()
# graph.del_vertex(9)
# print(graph.matrix)
# print(graph.edge_dict)
# print(graph.header)
# graph.add_edge((2, 6), 3)
# print(graph.header)
# graph.del_edge((2, 6))
# print(graph.header)
# print(graph.edge_dict)
# print(graph.matrix)
