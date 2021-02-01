"""python program of a graph module."""
from _collections import defaultdict


class Graph:
    """this class represents a directed graph using adjacency list
    representation."""

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
