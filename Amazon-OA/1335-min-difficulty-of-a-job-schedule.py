"""
1335. Minimum Difficulty of a Job Schedule
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/


"""
from typing import List

"""
sol 1 - top down DF with cache
dfs help find the min difficulty.
if start work at ith job with d days left.
If d=1, only one day left, we have to do all jobs
return the max difficulty of jobs.
"""
import functools


class Solution:
    @staticmethod
    def min_difficulty_top_down_dp(job_difficulty: List[int], d: int):
        length = len(job_difficulty)
        if length < d:
            return -1

        @functools.lru_cache(None)
        def dfs(i, days):
            if days == 1:
                return max(job_difficulty[i:])
            res, max_difficulty = float("inf"), 0
            for j in range(i, length - days + 1):
                max_difficulty = max(max_difficulty, job_difficulty[j])
                res = min(res, max_difficulty + dfs(j + 1, d - 1))
            return res

        return dfs(0, d)

    @staticmethod
    def min_difficulty_bottom_up(job_difficulty, d):
        n, inf = len(job_difficulty), float("inf")
        # create dp array
        dp = [[inf] * n + [0] for i in range(d + 1)]

        for d in range(1, d + 1):
            for i in range(n - d + 1):
                max_difficulty = 0
                for j in range(i, n - d + 1):
                    max_difficulty = max(max_difficulty, job_difficulty[j])
                    dp[d][i] = min(dp[d][i], max_difficulty+dp[d-1][j+1])
            return dp[d][0] if dp[d][0] < inf else -1


def main():
    job_difficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    sol = Solution()
    ans = sol.min_difficulty_top_down_dp(job_difficulty=job_difficulty, d=d)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
