class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    if m == 0 or 2*m <= n: return 0
    mul=m
    for i in range(m+1, n+1):
      mul&=i
    return mul

S = Solution()
m,n = map(int, input().split())
print(S.rangeBitwiseAnd(m, n))
