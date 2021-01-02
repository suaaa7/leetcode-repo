# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pointer = ListNode(0)
        head = pointer

        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                pointer.next = l2
                break
            elif l2 is None:
                pointer.next = l1
                break
            else:
                small_val = 0
                if l1.val < l2.val:
                    small_val = l1.val
                    l1 = l1.next
                else:
                    small_val = l2.val
                    l2 = l2.next

            pointer.next = ListNode(small_val)
            pointer = pointer.next

        return head.next
