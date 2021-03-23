"""
https://leetcode.com/discuss/interview-question/1122378/Amazon-online-assessment%3A-Find-max-hard-disk-space

similar to 239-sliding window max
https://leetcode.com/problems/sliding-window-maximum/

"""
from collections import deque
from typing import List


def find_max_among_all_min(
        num_computer: int,
        hard_disk_space: List[int],
        segment_length: int,
) -> int:
    deq = deque()
    minimums = []

    for i in range(segment_length):
        while len(deq) != 0:
            if hard_disk_space[i] < hard_disk_space[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)

    for i in range(segment_length, num_computer):
        minimums.append(hard_disk_space[deq[0]])
        if deq[0] < i-segment_length+1:
            deq.popleft()
        while len(deq) != 0:
            if hard_disk_space[i] < hard_disk_space[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)
    minimums.append(hard_disk_space[deq[0]])
    return max(minimums)


def main():
    ans = find_max_among_all_min(
        num_computer=3,
        hard_disk_space=[8, 2, 4],
        segment_length=2,
    )
    print(ans)
    ans = find_max_among_all_min(
        num_computer=10,
        hard_disk_space=[8, 2, 4, 1, 6, 10, 3, 99, 1000, 5],
        segment_length=2,
    )
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
