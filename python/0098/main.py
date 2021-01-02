# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst_helper(root, float('-inf'), float('inf'))

    def is_valid_bst_helper(
        self,
        root: TreeNode,
        min_val: float,
        max_val: float
    ) -> bool:
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False

        is_valid_left = self.is_valid_bst_helper(root.left, min_val, root.val)
        is_valid_right = self.is_valid_bst_helper(root.right, root.val, max_val)

        return is_valid_left and is_valid_right
