# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    	def height(root):
    		if root == None: return -1 #si ponemos 0 nos suma implicitamente los 2 que necesitamos para unir ambos caminos a la raiz
    		u = height(root.left)
    		v = height(root.right)
		    return u + 1 if u > v else v + 1
        if root==None: return 0
        ldiameter=self.diameterOfBinaryTree(root.left)
        rdiameter=self.diameterOfBinaryTree(root.right)
        return max(height(root.left)+height(root.right)+2, max(ldiameter, rdiameter))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def height(root):
            if root == None: return 0
            L = height(root.left)
            R = height(root.right)
            self.ans = max(self.ans, L+R+1) # Here we use the Nodes
            return L + 1 if L > R else R + 1
        height(root)
        return self.ans - 1 # quit the extra node that we sum each time

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def height(root):
            if root == None: return -1
            L = height(root.left)
            R = height(root.right)
            self.ans = max(self.ans, L+R+2) # now we use the Edges
            return L + 1 if L > R else R + 1
        height(root)
        return self.ans
            