# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isUtil(root: TreeNode, inf: int, sup: int) -> bool:
            if root==None: return True
            if inf<root.val<sup and isUtil(root.left, inf, root.val) and isUtil(root.right, root.val, sup): return True
            return False
        return isUtil(root, -2147483650, 2147483650)