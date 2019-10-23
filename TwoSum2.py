class Solution:
    def twoSum(self, nums: list, target: int) -> list:
    	l,r=0,len(nums)-1
    	while l<r:
    		suma=nums[l] + nums[r]
    		if suma == target:
    			return (l+1,r+1)
    		if suma < target:
    			l+=1
    		else:
    			r-=1

s=Solution()
l=sorted(list(map(int, input().split())))
target = int(input()) 
print(s.twoSum(l, target))
        