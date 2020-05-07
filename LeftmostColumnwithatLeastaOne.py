# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        mn = binaryMatrix.dimensions()
        m = mn[0]
        n = mn[1]
        res = n # or infinity 1e9 - 5
        for i in range(m):
            l=0
            r=n-1
            while l<=r:
                m = l + (r-l)//2
                cur = binaryMatrix.get(i, m)
                if cur==1:
                    res = min(res, m)
                    r = m - 1
                else:
                    l = m + 1
        return res if res!=n else -1
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        mn = binaryMatrix.dimensions()
        m = mn[0]
        n = mn[1]
        res = n
        i = 0
        j = n - 1
        while i<m and j>=0:
            cur = binaryMatrix.get(i, j)
            if cur==1:
                res = min(res, j)
                j-=1
            else:
                i+=1
        return res if res!=n else -1