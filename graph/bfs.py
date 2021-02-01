"""python program to print bfs traversal from a given source vertex.
bfs(int s) traverses vertices reachable from s."""
from graph.graph import Graph


class GraphBfs(Graph):
    """this class represents a directed graph using adjacency list
    representation."""

    def bfs(self, s):
        # mark all vertices as not visited
        visited = [False] * (max(self.graph) + 2)
        # create a queue for bfs
        queue = []
        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


def run_graph_one():
    graph = GraphBfs()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("Following is BFS starting from vertex 2")
    graph.bfs(2)


def run_graph_two():
    graph = GraphBfs()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    print("\nFollowing is BFS starting from vertex 1")
    graph.bfs(1)


def main():
    run_graph_one()
    run_graph_two()


if __name__ == "__main__":
    main()
