class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
       	if nums==[]: return 0
        if target > nums[-1]: return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target :
                return i

s=Solution()
arr = list(map(int, input().split()))
target = int(input()) 
print(s.searchInsert(arr, target))


""" #this is valid doesn't exist an input [] empty 
for i in range(len(nums)):
    if nums[i] >= target :
        return i
return i+1
"""