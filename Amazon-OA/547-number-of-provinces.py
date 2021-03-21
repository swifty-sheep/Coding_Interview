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


def find_circle_num_bfs(a: List[List[int]]):
    seen = set()
    res = 0
    # for each city, if its not seen yet then create a queue and put it in there
    for i in range(len(a)):
        if i not in seen:
            to_see = [i]
            # while the queue is not empty, pop one city out and keep searching
            # for the neighbor
            while len(to_see):
                current_city = to_see.pop()
                if current_city not in seen:
                    seen.add(current_city)
                    to_see = [nei for nei, adj in enumerate(a[current_city]) if
                              adj and nei not in seen] + to_see
            res += 1
    return res


def main():
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    ans = find_circle_num_dfs(is_connected)
    print(ans)
    bfs_ans = find_circle_num_bfs(is_connected)
    print(bfs_ans)


# Driver Code
if __name__ == "__main__":
    main()
