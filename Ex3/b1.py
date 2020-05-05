import sys

W = []
P = []

with open('graph.txt') as input_file:
    for row_id, line in enumerate(input_file):
        W.append([float("inf") if i == "-" else int(i) for i in line.split()])
        P.append([None if i == "-" else row_id+1 for i in line.split()])


# print(W)
# print(P)



def floyd_warshall(n):
    stop = False
    for t in range(n):
        print("W", t, "=")
        print(*W, sep="\n")
        print()
        print("P", t, "=")
        print(*P, sep="\n")
        print()
        if stop:
            print("STOP - ujemny cykl")
            return False
        for i in range(n):
            for j in range(n):
                if i != t and j != t:
                    if W[i][j] > W[i][t] + W[t][j]:
                        W[i][j] = W[i][t] + W[t][j]
                        P[i][j] = P[t][j]
                        if i == j and W[i][j] < 0:
                            stop = True
    return True


def give_path(a, b):
    L = [b]
    x = b - 1
    i = a - 1
    while(x != i):
        Vk = P[i][x]
        if Vk == None:
            return None
        x = Vk-1
        L.insert(0, Vk)
    return L


if (floyd_warshall(len(W))):
    for i in range(1, len(W)+1):
        print("z 1 do", i, give_path(1, i))
