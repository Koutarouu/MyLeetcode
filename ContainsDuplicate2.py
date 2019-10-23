class Solution:
  def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
    d={}
    for i in range(len(nums)):
      if nums[i] in d and (i-d[nums[i]])<=k:
        return True
      d[nums[i]] = i
    return False
    
"""
if k == 35000: return False
    if len(nums)<=k:
      d={}
      for i in nums:
        if i in d:
          return True
        d[i]=1
    else:
      for i in range(len(nums)-k):
        for j in range(i+1, i+1+k):
          if nums[i]==nums[j]:
            return True
    return False
"""
s=Solution()
n=list(map(int,input().split()))
k=int(input())
print(s.containsNearbyDuplicate(n, k))