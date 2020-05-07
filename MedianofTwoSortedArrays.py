import sys

class Solution:
  def findMedianSortedArrays(self, n1: list, n2: list) -> float:
    m, n = len(n1), len(n2)
    if m>n: return self.findMedianSortedArrays(n2, n1)
    l, r = 0, m # starts in m because we have covered that case
    while l <= r:
      px = (l+r)//2
      py = (m+n+1)//2 - px
      mxinLx = n1[px-1] if px>0 else -sys.maxsize-1
      mninRx = n1[px] if px<m else sys.maxsize
      mxinLy = n2[py-1] if py>0 else -sys.maxsize-1
      mninRy = n2[py] if py<n else sys.maxsize
      if mxinLx <= mninRy and mxinLy <= mninRx:
        if (m+n)%2==0: return (max(mxinLx, mxinLy) + min(mninRx, mninRy))/2
        return max(mxinLx, mxinLy)
      if mxinLx > mninRy:
        r = px - 1
      else:
        l = px + 1

s=Solution()
nums1=list(map(int, input().split()))
nums2=list(map(int, input().split()))
print(s.findMedianSortedArrays(nums1, nums2))
#Dengeki-Bunko.blogspot.com