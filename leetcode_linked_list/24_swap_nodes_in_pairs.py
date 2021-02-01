# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = root = ListNode(0)
        root.next = head

        while root.next and root.next.next:
            a = root.next
            b = root.next.next
            c = root.next.next.next
            root.next = b
            b.next = a
            a.next = c
            root = a
        return dummy.next
