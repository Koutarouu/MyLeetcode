class Solution:
  def checkPossibility(self, nums: list) -> bool:
    if len(nums)<=1: return True
    t, a, b=nums[:], True, True
    for i in range(1, len(nums)):
      if nums[i] < nums[i-1]:
        nums[i] = nums[i-1];
        break
    for j in range(len(t)-1):
      if t[j] > t[j+1]:
        t[j] = t[j+1]
        break
    for j in range(len(t)-1):
      if t[j] > t[j+1]: b&=False
      if nums[j] > nums[j+1]: a&=False
    return a or b
  
  def checkPossibility2(self, nums: list) -> bool:
    if len(nums) <= 1: return True
    l, r=0, len(nums)-1
    a,b=True, True
    while l<len(nums)-1:
      if nums[l]<=nums[l+1]:
        l+=1
      else: break
    while r>0:
      if nums[r] >= nums[r-1]:
        r-=1
      else: break
    if r==0 and l==len(nums)-1: return True
    temp=nums[l]
    temp2=nums[r]
    nums[r] = temp
    for i in range(len(nums)-1):
      if nums[i] > nums[i+1]: a&=False
    if a: return True 
    nums[r] = temp2
    nums[l] = temp2
    for i in range(len(nums)-1):
      if nums[i] > nums[i+1]: b&=False    
    if b: return True
    return False

#space 98.90 %
s=Solution()
a=list(map(int, input().split()))
print(s.checkPossibility2(a))
#print(s.checkPossibility(a))
#nums[l] = temp #para dejar al array intacto
