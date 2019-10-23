class Solution:
    def searchRange(self, nums: list, target: int) -> list:
    	first_pos=last_pos=-1
    	l,r=0,len(nums)-1
    	while r>=l:
    		guess = (r+l)//2
    		if nums[guess]==target:
    			break
    		if nums[guess] > target:
    			r = guess - 1
    		else:
    			l = guess + 1
    	for i in range(l, guess+1):
    		if nums[i]==target:
    			first_pos=i
    			break
    	for i in range(r, guess-1, -1):
    		if nums[i]==target:
    			last_pos=i
    			break
    	return [first_pos, last_pos]

s=Solution()
array=list(map(int,input().split()))
target=int(input())
print(s.searchRange(array, target))