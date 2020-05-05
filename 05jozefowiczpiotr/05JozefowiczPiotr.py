#!/usr/bin/env python3
import sys
import os
import graph as gr

def roberts_flores(v):
    S = []
    S.append(v)
    u = G.neighbours(v)[0]
    print(*S, sep=" ")
    while len(S) != 0:
        S.append(u)
        print(*S, sep=" ")
        if len(S) == G.number_of_nodes() and (u, v) in G.edges():
            print('CYKL HAMILTONA:', *S, v, sep=" ")
        lu = [x for x in G.neighbours(u) if x not in S]
        if len(lu) != 0:
            u = lu[0]
        else:
            while len(S) != 0:
                S.pop()
                print(*S, sep=" ")
                if len(S) != 0:
                    w = S[-1]
                    lw = [x for x in G.neighbours(w) if x not in S]
                    if u != lw[-1]:
                        u = lw[lw.index(u)+1]
                        break
                    else:
                        u = w
matrix = []

# wczytaj macierz grafu 
with open('graph09.txt') as input_file:
        for rowId, line in enumerate(input_file):
            matrix.append(list(map(lambda x: float('inf') if x == '-' else int(x), line.split())))

G = gr.Graph(matrix)

roberts_flores(1)
