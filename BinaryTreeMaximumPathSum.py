# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        def inorder(root: TreeNode) -> int:
            if root==None: return 0
            l = inorder(root.left)
            r = inorder(root.right)
            a=max(l+root.val, r+root.val)
            self.ans = max(self.ans, l+root.val+r)#max((self.ans, a, l+root.val+r))
            return a if a>0 else 0 
        self.ans=root.val
        inorder(root)
        return self.ans