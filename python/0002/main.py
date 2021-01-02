# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_carry = 0

        current = ListNode(0)
        head = current

        while l1 or l2 or current_carry:
            current_val = current_carry
            current_val += 0 if l1 is None else l1.val
            current_val += 0 if l2 is None else l2.val

            if current_val >= 10:
                current_val -= 10
                current_carry = 1
            else:
                current_carry = 0

            current.next = ListNode(current_val)
            current = current.next

            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        return head.next
