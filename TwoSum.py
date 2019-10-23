class Solution:
    def twoSum(self, nums: list, target: int) -> list:
    	h={}
    	for i in range(len(nums)):
    		obj = target - nums[i]
    		if nums[i] in h:
    			return [h[nums[i]],i]
    		h[obj] = i

s=Solution()
l=list(map(int, input().split()))
target = int(input()) 
print(s.twoSum(l, target))
        