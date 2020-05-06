class graph():
    def __init__(self, num_vertices, matrix):
        self.num_vertices = num_vertices
        self.matrix = matrix
        self.adj_dict = {}
        self.edge_dict = {}
        self.header = {}

        self.update()

    def __repr__(self):
        return f"{self.header}\n{self.adj_dict}\n{self.edge_dict}\nAdjacency list:\n{self.repr_adjacency_list()}"

    def repr_adjacency_list(self):
        list_str = ""
        for key in self.header.keys():
            list_str += f"{key} : {' '.join(map(str, self.header[key]))}\n"
        return list_str

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
            self.matrix[edge[0]-1][edge[1]-1] = float("inf")
            self.matrix[edge[1]-1][edge[0]-1] = float("inf")
            self.update()
            del self.edge_dict[edge]
        else:
            print("Can't add, this edge ")

    def edge_weight(self, edge):
        if edge in self.edge_dict.keys():
            print("Edge weight: " + self.edge_dict[edge])
        else:
            print("This edge: " + str(edge) + " don't exist in graph.")

    def neighbours(self, ver):
        if ver not in self.adj_dict:
            print("Vertex does not exist")
        else:
            return list(self.adj_dict[ver].keys())

    def update(self):
        self.adjacency_list()
        self.edge_list()
        self.create_header()

    def roberts_flores(self, v):
        S = []
        S.append(v)
        u = self.neighbours(v)[0]
        print(' '.join(map(str, S)))
        while len(S) != 0:
            S.append(u)
            print(*S, sep=" ")
            if len(S) == self.num_vertices and (u, v) in self.edge_dict:
                print('CYKL HAMILTONA:', ' '.join(map(str, S)), v)
            lu = [x for x in self.neighbours(u) if x not in S]
            if len(lu) != 0:
                u = lu[0]
            else:
                while len(S) != 0:
                    S.pop()
                    print(' '.join(map(str, S)))
                    if len(S) != 0:
                        w = S[-1]
                        lw = [x for x in self.neighbours(w) if x not in S]
                        if u != lw[-1]:
                            u = lw[lw.index(u)+1]
                            break
                        else:
                            u = w


def get_num_vertices(matrix):
    num_vertices = 0
    for row in matrix:
        for ele in row:
            if ele == 1:
                num_vertices += 1
    return int(num_vertices/2)


def read_data():
    matrix = []

    with open('graph09.txt') as input_file:
        for line in input_file:
            matrix.append([float("inf") if i == "-" else int(i)
                           for i in line.split()])

    num_vertices = get_num_vertices(matrix)

    return num_vertices, matrix


num_vertices, matrix = read_data()

graph = graph(num_vertices, matrix)
graph.roberts_flores(1)
