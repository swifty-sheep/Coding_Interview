"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn
adjacent (up/down/left/right) human beings into zombies every hour. Find out how
 many hours does it take to infect all humans?

 Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
"""


def min_hour(rows, columns, grid):
    # if there is no row or column then just return
    if not rows or not columns:
        return 0

    # record index in grid that has value 1
    q = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j] == 1]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    time = 0

    while True:
        new = []
        for i, j in q:
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                # check the boundary is valid and is 0 (human, not zombie)
                if 0 <= next_i < rows \
                        and 0 <= next_j < columns \
                        and grid[next_i][next_j] == 0:
                    grid[next_i][next_j] = 1
                    new.append([next_i, next_j])
        # replace q with the list of new infected zombie
        q = new
        # if q is empty then there are no human left, break
        if not q:
            break
        time += 1
    return time


def main():
    grid = [[0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]]
    ans = min_hour(4, 5, grid)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
