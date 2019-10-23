class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        l=0
        r=len(nums)-1
        while r>l:
        	guess = (l+r)//2
        	if guess%2==0:
        		if nums[guess]!=nums[guess-1] and nums[guess]!=nums[guess+1]:
        			return nums[guess]
        		elif nums[guess] == nums[guess+1]:
        			l=guess
        		else:
        			r=guess
        	else:
        		if nums[guess] != nums[guess+1]:
        			return nums[guess+1]
        		else:
        			return nums[guess-1]

s=Solution()
arr=list(map(int, input().split()))
print(s.singleNonDuplicate(arr))