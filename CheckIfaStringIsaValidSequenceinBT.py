# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)-1
        d = deque()
        is_leaf = lambda node: not (node.left or node.right)
        if root.val==arr[0]:
            d.append((root, 0))
        curlvl=0
        while d and curlvl<=n:
            f, curlvl = d.popleft()
            if curlvl == n:
                if is_leaf(f): return True
                else: continue
            if f.left and f.left.val == arr[curlvl+1]:
                d.append((f.left, curlvl+1))
            if f.right and f.right.val == arr[curlvl+1]:
                d.append((f.right, curlvl+1))
        return False
        