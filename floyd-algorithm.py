
def read_data(path):
    W = []
    P = []
    with open(path) as input_file:
        for row_id, line in enumerate(input_file):
            W.append([float("inf") if i == "-" else int(i)
                      for i in line.split()])
            P.append([None if i == "-" else row_id+1 for i in line.split()])
    return W, P


# print(W)
# print(P)


class graph:
    def __init__(self, W, P):
        self.W = W
        self.P = P

    def floyd_warshall(self, n):
        stop = False
        for t in range(n):
            print("W", t, "=")
            print(self.W, sep="\n")
            print()
            print("P", t, "=")
            print(self.P, sep="\n")
            print()
            if stop:
                print("STOP - ujemny cykl")
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

    def give_path(self, a, b):
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
            for i in range(1, len(self.W)+1):
                print("z 1 do", i, self.give_path(1, i))


def main():
    W, P = read_data('./Ex3/graph.txt')
    graph(W, P).run()


if __name__ == "__main__":
    main()
