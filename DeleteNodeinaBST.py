# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMin(self, root):
        if root:
            while root.left:
                root=root.left
            return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root==None: return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left==None and root.right ==None:
                root=None
            elif root.left==None:
                root = root.right
            elif root.right==None:
                root = root.left
            else:
                root.val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root
