"""
https://leetcode.com/discuss/interview-question/1120850/Amazon-OA-Question-doubt-or-March-2021

"""
from typing import List


def lazy_count_swaps(arr: List[int]) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


def merge_sort(arr: List[int]):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        count += merge_sort(left)
        count += merge_sort(right)
        # two iters for traversing two halves
        i = 0
        j = 0
        # iter for main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[i]
                j += 1
                count += 1
            # move to the next slot
            k += 1

        # for all remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return count


def main():
    arr = [1, 20, 6, 4, 5]
    # arr = [5, 1, 4, 2]
    ans = lazy_count_swaps(arr=arr)
    print(ans)
    arr = [5, 1, 4, 2]
    ans = merge_sort(arr=arr)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
