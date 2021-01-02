# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None:
            return False
        
        if q is None:
            return False

        if p.val != q.val:
            return False

        left_is_same = self.isSameTree(p.left, q.left)
        right_is_same = self.isSameTree(p.right, q.right)

        return left_is_same and right_is_same
