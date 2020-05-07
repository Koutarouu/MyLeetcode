class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if (2*m) < n: return 0
        res=m
        for i in range(m+1 , n+1):
            res &= i
        return res
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m<n:
            n&=n-1
        return n