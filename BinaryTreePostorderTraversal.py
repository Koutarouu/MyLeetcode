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
  def postorderTraversal(self, root: TreeNode) -> list:
    def postOrder(root):
      if root:
        postOrder(root.left)
        postOrder(root.right)
        res.append(root.val)
    res=[]
    postOrder(root)
    return res
          

tree = BinarySearchTree()
arr = list(map(int, input().split()))
for i in range(len(arr)):
  tree.create(arr[i])
s=Solution()
print(s.postorderTraversal(tree.root))
