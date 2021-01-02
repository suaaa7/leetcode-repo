# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        pointer = head
        fast_pointer = head.next

        while pointer is not None and fast_pointer is not None and fast_pointer.next is not None:
            if pointer == fast_pointer:
                return True
            pointer = pointer.next
            fast_pointer = fast_pointer.next.next

        return False
