import sys
class Solution:
    def maxProduct(self, nums: list) -> int:
        if len(nums)==1: return nums[0]
        res= - sys.maxsize - 1
        n=nums[:]
        for i in range(1, len(nums)):
            res = max(res, max(nums[i], nums[i]*nums[i-1]))
            if nums[i-1]!=0: nums[i]*=nums[i-1]
        for i in range(len(n)-2, -1, -1):
            res = max(res, max(n[i], n[i]*n[i+1]))
            if n[i+1]!=0: n[i]*=n[i+1]
        return res

S=Solution()
nums=list(map(int, input().split()))
print(S.maxProduct(nums))
"""
Ex:
2 3 -2 4 0 9 1 4 -2
36
"""