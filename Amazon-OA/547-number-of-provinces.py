"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
from typing import List


def find_circle_num_dfs(a: List[List[int]]):
    number_of_cities = len(a)
    seen = set()

    def dfs(node):
        # for enumerate
        # nei is the index
        # adj is the value -> 0 or 1
        for nei, adj in enumerate(a[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)

    ans = 0
    for i in range(number_of_cities):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans


def main():
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    ans = find_circle_num_dfs(is_connected)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
