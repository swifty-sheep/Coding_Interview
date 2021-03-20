""" Knight's Tour example for back tracking algorithm."""
from typing import List


class KnightsTour:

    def __init__(self, n):
        self.n = n

    def is_safe(self, x: int, y: int, board: List[List[int]]) -> bool:
        if 0 <= x < self.n and 0 <= y < self.n and board[x][y] == -1:
            return True
        return False

    def print_solution(self, board):
        for i in range(self.n):
            for j in range(self.n):
                print(board[i][j], end=" ")
            print()

    def solve_kt_util(self, board, curr_x, curr_y, move_x, move_y, pos):
        if pos == self.n ** 2:
            return True
        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if self.is_safe(new_x, new_y, board):
                board[new_x][new_y] = pos
                if self.solve_kt_util(board, new_x, new_y, move_x, move_y, pos+1):
                    return True
                board[new_x][new_y] = -1
        return False

    def solve_kt(self):
        board = [[-1 for i in range(self.n)] for i in range(self.n)]
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]
        board[0][0] = 0
        pos = 1
        if not self.solve_kt_util(board, 0, 0, move_x, move_y, pos):
            print("solution not exist")
        else:
            self.print_solution(board)


def main():
    knights_tour = KnightsTour(8)
    knights_tour.solve_kt()


# Driver Code
if __name__ == "__main__":
    main()
