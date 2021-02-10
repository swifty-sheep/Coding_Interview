# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True


class AnotherSolution:
    
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # get the midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # comparison
        curr = head
        while stack:
            if stack.pop() != curr.val:
                return False
            curr = curr.next
        return True
