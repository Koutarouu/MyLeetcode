class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        easy=bin(n)
        c=0
        for i in easy:
            if i=='1':
                c+=1
        return c
        