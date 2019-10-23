import collections

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    root = None

  def createTree(self):
    res = ''
    data=int(input("Type your data: "))
    apunt = TreeNode(data)
    print("have left? ")
    res = input()
    if res=='s':
      self.createTree()
      apunt.left = self.root
    print("have right? ")
    res = input()
    if res=='s':
      self.createTree()
      apunt.right = self.root
    self.root = apunt

  def levelOrder(self):
    q = deque()
    q.append(self.root)
    while q:
      t = q.popleft()
      if t.left: q.append(t.left)
      if t.right: q.append(t.right)
      print(t.val)

  def reroot(self):
    return self.root


class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p == None and q==None: return True
    try:
      if p.val == q.val:
        res1=self.isSameTree(p.left, q.left)
        res2=self.isSameTree(p.right, q.right)
      else:
        return False
    except AttributeError:
      return False
    return (res1 and res2)

  def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
    que = collections.deque()
    que.append((p, q))
    while que:
      a, b = que.popleft()
      if a is None and b is None:
        continue
      if (a is None) != (b is None):
        return False
      if a.val != b.val: return False
      que.append((a.left, b.left))
      que.append((a.right, b.right))
    return True

  def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
      return True
    if p == None or q == None:
      return False
    if p.val != q.val:
      return False
    return self.isSameTree3(p.left, q.left) and self.isSameTree3(p.right, q.right) #verify the 2 ways

tree1 = Tree()
tree1.createTree()
tree2 = Tree()
tree2.createTree()
s = Solution()
print(s.isSameTree3(tree1.reroot(), tree2.reroot()))
"""
Input sample
1
s
2
0
0
s
3
0
0
sample 2
1
s
2
0
0
0
y
1
0
s
2
0
0
"""