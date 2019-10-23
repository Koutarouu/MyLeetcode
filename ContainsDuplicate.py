class Solution:
  def containsDuplicate(self, nums) -> bool:
    return len(nums)!=len(set(nums))
    d={}
    for i in nums:
    	if i in d:
    		return True
    	d[i] = 1
    return False

  def containsDuplicate2(self, nums) -> bool:
  	return not (len(set(nums)) == len(nums))

so = Solution()
l=list(map(int, input().split()))
print(so.containsDuplicate2(l))