"""
200. Number of Islands
medium
https://leetcode.com/problems/number-of-islands/

"""
import collections
from typing import List


def is_valid(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    return True


def dfs(grid: List[List[str]], i: int, j: int):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][
        j] != "1":
        return
    grid[i][j] = "#"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


def dfs_another_one(grid, row, col):
    grid[row][col] = "0"
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in directions:
        nrow, ncol = row + d[0], col + d[1]
        if is_valid(grid, nrow, ncol) and grid[nrow][ncol] == "1":
            dfs_another_one(grid, nrow, ncol)


def num_islands_dfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1
    print(grid)
    return count


def bfs(grid, row, col):
    queue = collections.deque()
    queue.append((row, col))
    grid[row][col] = "#"
    while queue:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        row, col = queue.popleft()
        for d in directions:
            nrow, ncol = row + d[0], col + d[1]
            if is_valid(grid, nrow, ncol) and grid[nrow][ncol] == "1":
                queue.append((nrow, ncol))
                grid[nrow][ncol] = "#"


def num_islands_bfs(grid) -> int:
    if not grid or not grid[0]:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                bfs(grid, i, j)
                count += 1
    print(f"another result grid: \n{grid}")
    return count


class Sol:

    def __init__(self, grid):
        row, col = len(grid), len(grid[0])
        self.count = sum(
            grid[i][j] == "1" for i in range(row) for j in range(col))

    def num_islands_union_find(self, grid):
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        parent = [i for i in range(row * col)]

        def find(x):
            if parent[x] != x:  # it is not it's parent, then find it
                return find(parent[x])
            return x

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                index = i * col + j
                if j < col - 1 and grid[i][j + 1] == "1":
                    union(index, index + 1)
                if i < row - 1 and grid[i + 1][j] == "1":
                    union(index, index + col)
        return self.count


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ans = num_islands_dfs(grid)
    print(ans)
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ans = num_islands_bfs(grid)
    print(ans)
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    union_find_sol = Sol(grid=grid)
    ans = union_find_sol.num_islands_union_find(grid)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
