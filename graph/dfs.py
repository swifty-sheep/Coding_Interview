"""python program to print bfs traversal from a given source vertex.
bfs(int s) traverses vertices reachable from s."""
from _collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def dfs_util(self, s: int, visited: set):
        visited.add(s)
        print(s, end=" ")
        for neighbor in self.graph[s]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, s: int):
        visited = set()
        self.dfs_util(s, visited)


def run_graph_one():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("Following is DFS starting from vertex 2")
    graph.dfs(2)


def run_graph_two():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    print("\nFollowing is DFS starting from vertex 1")
    graph.dfs(1)


def main():
    run_graph_one()
    run_graph_two()


if __name__ == "__main__":
    main()
