class Solution:
  def nextPermutation(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    Le=r=len(nums)-1
    t=None
    while r>0 and nums[r]<=nums[r-1]: r-=1
    t=r-1
    if r==0:
      for i in range((Le//2)+1):
        nums[i],nums[Le-i]=nums[Le-i],nums[i]
    else:
      r=Le
      while r>0 and nums[t]>=nums[r]: r-=1
      nums[t],nums[r]=nums[r],nums[t]    
      t+=1
      r=Le
      while t<r:
        nums[t],nums[r]=nums[r],nums[t]
        t+=1
        r-=1
    print(nums)


s=Solution()
arr = list(map(int, input().split()))
s.nextPermutation(arr)