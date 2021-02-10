"""longest common subsequence"""


class LCS:
    def __init__(self):
        self.lcs = ""

    def longest_common_subsequence(self, x: str, y: str, m: int, n: int):
        if m == 0 or n == 0:
            return 0
        elif x[m - 1] == y[n - 1]:
            return 1 + self.longest_common_subsequence(x, y, m - 1, n - 1)
        else:
            return max(self.longest_common_subsequence(x, y, m, n - 1), self.longest_common_subsequence(x, y, m - 1, n))

    @staticmethod
    def memo_longest_common_subsequence(x: str, y: str):
        m = len(x)
        n = len(y)
        memo = [[None] * (n + 1) for i in range(m + 1)]
        print(type(memo[0]))
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    memo[i][j] = 0
                elif x[m - 1] == y[n - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])
        return memo[m][n]

    def get_lcs(self):
        return self.lcs


def main():
    lcs = LCS()
    x = "AGGTAB"
    y = "GXTXAYB"
    print(f"Length of lcs of {x} and {y} is {lcs.longest_common_subsequence(x, y, len(x), len(y))}")
    print(f"Memoization : {lcs.memo_longest_common_subsequence(x, y)}")
    print(f"lcs is {lcs.get_lcs()}")


if __name__ == "__main__":
    main()
