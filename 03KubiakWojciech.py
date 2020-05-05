
def read_data(path):
    W = []
    P = []
    with open(path) as input_file:
        for row_id, line in enumerate(input_file):
            W.append([float("inf") if i == "-" else int(i)
                      for i in line.split()])
            P.append([None if i == "-" else row_id+1 for i in line.split()])
    return W, P


class graph:
    def __init__(self, W, P):
        self.W = W
        self.P = P

    def repr_W(self):
        for w in self.W:
            print(' '.join(map(str, w)))
        print()

    def repr_P(self):
        for p in self.P:
            print(' '.join(map(str, p)))
        print()

    def floyd_warshall(self, n):
        stop = False
        for t in range(n):
            print("W", t, "=")
            self.repr_W()
            print("P", t, "=")
            self.repr_P()
            if stop:
                print("STOP - ujemny cykl. Nie ma rozwiązania.")
                return False
            for i in range(n):
                for j in range(n):
                    if i != t and j != t:
                        if self.W[i][j] > self.W[i][t] + self.W[t][j]:
                            self.W[i][j] = self.W[i][t] + self.W[t][j]
                            self.P[i][j] = self.P[t][j]
                            if i == j and self.W[i][j] < 0:
                                stop = True
        return True

    def get_path(self, a, b):
        L = [b]
        x = b - 1
        i = a - 1
        while(x != i):
            Vk = self.P[i][x]
            if Vk == None:
                return None
            x = Vk-1
            L.insert(0, Vk)
        return L

    def run(self):
        if (self.floyd_warshall(len(self.W))):
            print("Ostateczna macierz odleglosci:")
            self.repr_W()
            print("Ostateczna macierz poprzednikow:")
            self.repr_P()
            print("Najkrotsze sciezki:")
            for i in range(1, len(self.W)+1):
                print("z 1 do", i, ":",  ' '.join(
                    map(str, self.get_path(1, i))))


def main():
    # tu trzeba podać ścieżke do pliku
    W, P = read_data('./Ex3/graph.txt')
    graph(W, P).run()


if __name__ == "__main__":
    main()
