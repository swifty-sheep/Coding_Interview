from collections import defaultdict
from typing import List


class Graph:
    """This class represents a undirected graph using adjacency list
    representation"""
    def __init__(self, vertices):
        """
        :param vertices: number of vertices
        graph: default dictionary to store graph
        """
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        """add an edge to graph"""
        self.graph[u].append(v)

    def find_parent(self, parent: List, i: int):
        """find subset of an element i"""
        # if it has its own subset, return its index
        if parent[i] == -1:
            return i
        # if it has parent then find the root parent of
        # its subset -> use recursive call
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent: List, x: int, y: int):
        """do union of two subsets"""
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        # let root parent of x_set be the new union root of both
        # x_set and y_set
        parent[x_set] = y_set

    def is_cycle(self):
        """main function to check whether a given graph continas
        a cycle"""

        # create v subsets and init all subsets as single element sets
        parent = [-1] * self.vertices
        # iter through all edges of graph, find subset of both vertices
        # of every edge, if both subsets are same, then there is cycle
        # in the graph
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False


def main():
    # Create a graph given in the above diagram
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    if g.is_cycle():
        print("Graph contains cycle")

    else:
        print("Graph does not contain cycle ")


if __name__ == "__main__":
    main()