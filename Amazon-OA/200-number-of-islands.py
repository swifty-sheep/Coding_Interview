"""
200. Number of Islands
medium
https://leetcode.com/problems/number-of-islands/

"""
from typing import List


def dfs(grid: List[List[str]], i: int, j: int):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][
        j] != "1":
        return
    grid[i][j] = "#"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


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


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ans = num_islands_dfs(grid)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
