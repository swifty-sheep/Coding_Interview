# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heapreplace, heappop, heapify

        dummy = node = ListNode(0)
        h = [(n.val, i, n) for i, n in enumerate(lists) if n]
        heapify(h)

        while h:
            val, i, n = h[0]
            if n.next is None:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, i, n.next))
            node.next = n
            node = node.next
        return dummy.next
