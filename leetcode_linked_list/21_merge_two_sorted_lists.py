# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        root = head = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                root.next = l1
                root = root.next
                l1 = l1.next
            else:
                root.next = l2
                root = root.next
                l2 = l2.next
        root.next = l1 or l2
        return head.next
