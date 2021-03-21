"""
239. Sliding Window Maximum - hard
https://leetcode.com/problems/sliding-window-maximum/

https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem
https://1e9.medium.com/monotonic-queue-notes-980a019d5793

sliding window min/max = monotonic queue.

What is monotonic queue (MQ)?
Monotonic queue is a DS that keeps it's elements either entirely in
non-increasing, or entirely in non-decreasing order.

push(new_item) - removes elem from queue compared to value in new_item
    to preserve monotonicity. Then add a new elem.
get_first() - return the first value in the queue, which is usually a
    max or min
remove_first() - removes min or max when it is no longer needed.
"""
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    # base case check
    if not nums:
        return []
    if k == 0:
        return nums
    # define deque and result list
    deq = deque()
    result = []
    # traverse through k elem in nums and only add index of max value to deque
    # note - only store index, NOT value
    # now, compare the new value in nums with last index value from deque
    # if new value is less, we don't need it
    for i in range(k):
        while len(deq) != 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)
    # now deque has index of max elem for the first k values

    # traverse from k to the end of array and do 4 things
    # 1. append left most indexed value in deque to the result
    # 2. check if left most is still in range of k (so it only allows valid
    #    sub-sequence)
    # 3. check if right most indexed elem in deque is less than the new elem
    #    found, if yes remove it
    # 4. append i at the end of the deque
    for i in range(k, len(nums)):
        result.append(nums[deq[0]])

        if deq[0] < i - k + 1:
            deq.popleft()

        while len(deq) != 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)
    # add the max for the last sub-sequence
    result.append(nums[deq[0]])
    return result


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    ans = max_sliding_window(nums=nums, k=k)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
