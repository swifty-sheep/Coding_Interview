"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/

"""
from typing import List


def next_greater_element_my_practice(find_nums: List[int], nums: List[int]) -> \
List[int]:
    next_greater_elem_look_up_table = {}
    stack = []

    for elem in nums:
        if len(stack) == 0 or elem <= stack[-1]:
            stack.append(elem)
        else:
            while stack and stack[-1] < elem:
                next_greater_elem_look_up_table[stack.pop()] = elem
            stack.append(elem)

    result = []
    for num in find_nums:
        if num in next_greater_elem_look_up_table:
            result.append(next_greater_elem_look_up_table[num])
        else:
            result.append(-1)
    return result


def next_greater_element_1(find_nums: List[int], nums: List[int]) -> List[int]:
    cache, stack = {}, []
    for elem in nums:
        if len(stack) == 0:
            stack.append(elem)
        elif elem <= stack[-1]:
            stack.append(elem)
        else:
            while stack and stack[-1] < elem:
                cache[stack.pop()] = elem
            stack.append(elem)

    result = []
    for x in find_nums:
        if x in cache:
            result.append(cache[x])
        else:
            result.append(-1)
    return result


def main():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ans = next_greater_element_1(nums1, nums2)
    print(ans)
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    ans = next_greater_element_my_practice(nums1, nums2)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
