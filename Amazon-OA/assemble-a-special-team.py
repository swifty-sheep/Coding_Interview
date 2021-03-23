"""
https://leetcode.com/discuss/interview-question/1122369/Amazon-Online-Assessment-for-SDE-role

input args
    num (int) - num of associates
    skills (List[int]) - skills levels of associates
    min_associates (int) - min num of team members
    min_level (int) - lower limit for skill level, inclusive
    max_level (int) - upper limit for skill level, inclusive
"""
import math

from typing import List


def find_all_team_combination(
        num: int,
        skills: List[int],
        min_associates: int,
        min_level: int,
        max_level: int,
) -> int:
    qualified = []
    for associate in skills:
        if min_level <= associate <= max_level:
            qualified.append(associate)
    num_of_qualified = len(qualified)
    if num_of_qualified < min_associates:
        return 0

    total_team = 0
    for i in range(min_associates, num_of_qualified + 1):
        total_team += math.factorial(num_of_qualified) / (
                math.factorial(num_of_qualified - i) * math.factorial(i))
    return int(total_team)


def main():
    ans = find_all_team_combination(
        num=5,
        skills=[12, 4, 6, 13, 5, 10],
        min_associates=3,
        min_level=4,
        max_level=10
    )
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
