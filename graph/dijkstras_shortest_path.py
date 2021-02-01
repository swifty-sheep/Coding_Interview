"""Dijkstra's shortest path algorithm"""
import sys
from typing import List, Set

class Graph:

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph: List[List[int]] = [[0] * vertices] * vertices

    def print_solution(self, dist: List):
        print("Vertex \t Distance from Source")
        for node in range(self.vertices):
            print(f"{node}\t{dist[node]}")

    def min_distance(self, dist: List, spt_set: List) -> int:
        min_dist = sys.maxsize

        for v in range(self.vertices):
            if dist[v] < min_dist and spt_set[v] is False:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src: int):
        # step 1, create a set to keep track of vertices included in spt
        # ie. whose min dist from source is calculated and finalized.
        spt_set = [False] * self.vertices
        # step 2, assign a distance value to all vertices in input graph.
        # init all dist as infinite.
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        # step 3, while spt set doesn't include all vertices:
        for i in range(self.vertices):
            # a) pick the min dist vertex and is not in spt_set
            u = self.min_distance(dist, spt_set)
            # b) put min dit vertex in spt
            spt_set[u] = True
            # c) update dist value of the adjacent vertices
            # of the picked vertex only if the current distance
            # is greater than new distance and the vertex
            # is not in the spt
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and spt_set[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_solution(dist)


def main():
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)


if __name__ == "__main__":
    main()
