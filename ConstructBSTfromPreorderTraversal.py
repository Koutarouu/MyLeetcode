# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = TreeNode(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
                else:
                    break
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode: #O(NlgN)
        tree = BinarySearchTree()
        for i in preorder:
            tree.create(i)
        return tree.root

class Solution:
    def __init__(self):
        self.idx=0
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode: #O(N)
        def helper(limit: int):
            if self.idx==len(preorder) or preorder[self.idx]>limit:
                return None
            root = TreeNode(preorder[self.idx])
            self.idx+=1
            root.left = helper(root.val)
            root.right = helper(limit)
            return root
        return helper(1e9 - 5)

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode: #O(N**2)
        if preorder==[]:
            return None
        root = TreeNode(preorder[0])
        lower = []; higher = []
        for i in range(1, len(preorder)):
            if preorder[i]<root.val:
                lower.append(preorder[i])
            else:
                higher.append(preorder[i])
        root.left = self.bstFromPreorder(lower)
        root.right = self.bstFromPreorder(higher)
        return root