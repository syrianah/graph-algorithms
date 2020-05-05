#!/usr/bin/env python3
import sys

class Graph:

    __wAdjlist = {}

    def __init__(self, matrix):
        self.__make_w_adjlist(matrix)

    def __make_w_adjlist(self, matrix):
        self.__wAdjlist.clear()
        for rowIdx, row in enumerate(matrix):
            self.__wAdjlist[rowIdx+1] = {}
            for colIdx, col in enumerate(row):
                if col != float('inf'):
                    self.__wAdjlist[rowIdx+1][colIdx+1] = col
                
    def __print_dict(self, dic):
        for key, value in dic.items():
            print(key, ' : ', value)
        print()
    
    def print_w_adjlist(self):
        self.__print_dict(self.__wAdjlist)

    def print_adjlist(self):
        for key, value in self.__wAdjlist.items():
            print(key, ': ', end='')
            for key2 in value:
                print(key2, end=' ')
            print()
        
    def add_node(self, node):
        if node not in self.__wAdjlist:
            self.__wAdjlist[node] = {}

    def remove_node(self, node):
        if node in self.__wAdjlist:
            for key in self.__wAdjlist[node]:
                self.__wAdjlist[key].pop(node)
            self.__wAdjlist.pop(node)

    def number_of_nodes(self):
        return len(self.__wAdjlist)

    def add_edge(self, a, b, w):
        if a not in self.__wAdjlist or b not in self.__wAdjlist:
            raise ValueError('Node does not exist')
        else:
            self.__wAdjlist[a][b] = w
            self.__wAdjlist[b][a] = w

    def remove_edge(self, a, b):
        if a not in self.__wAdjlist or b not in self.__wAdjlist:
            raise ValueError('Node does not exist')
        else:
            self.__wAdjlist[a].pop(b)
            self.__wAdjlist[b].pop(a)

    def edge_weight(self, a, b):
        if a not in self.__wAdjlist or b not in self.__wAdjlist:
            raise ValueError('Node does not exist')
        elif b in self.__wAdjlist[a]:
            return self.__wAdjlist[a][b]
        else:
            raise ValueError('Edge does not exist')

    def neighbours_with_weights(self, node):
        if node not in self.__wAdjlist:
            raise ValueError('Node does not exist')
        else:
            return self.__wAdjlist[node]

    def neighbours(self, node):
        if node not in self.__wAdjlist:
            raise ValueError('Node does not exist')
        else:
            return list(self.__wAdjlist[node].keys())

    def edges(self):
        edgelist = []
        for a in self.__wAdjlist:
            for b in self.__wAdjlist[a]:
                if (b, a) not in edgelist:
                    edgelist.append((a, b))
        return edgelist