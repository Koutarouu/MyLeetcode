class Solution:
  def moveZeroes(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k, l, r = 0, 0, len(nums)-1
    while l <= r:
      if nums[r] == 0:
        r -= 1
      elif nums[l] == 0:
        nums[r], nums[l] = nums[l], nums[r]
        l+=1
        k+=1
      else:
        l+=1
      print(nums)
    for i in range(0, len(nums) - k - 1):
      nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
  def moveZeros(self, nums: list) -> None:
      r = len(nums)-1
      i=0
      while i < r:
        if nums[i]==0:
          for j in range(i, r):
            nums[j], nums[j+1] = nums[j+1], nums[j]
          r-=1
        if nums[i]!=0:
          i+=1
  def moveZeroesuff(self, nums: list) -> None:
    lastNonZero = 0
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[lastNonZero] = nums[i]
        lastNonZero+=1
    for i in range(lastNonZero, len(nums)):
      nums[i] = 0
  def moveZeroes(self, nums: list) -> None:
    slow=0
    for current in range(1, len(nums)):
      if nums[slow]!=0:
        slow+=1
      elif nums[current] != 0:
        nums[current], nums[slow] = nums[slow], nums[current]
        slow+=1
  def moveZeroes(self, nums: list) -> None:
    slow=0
    for current in range(len(nums)):
      if nums[current] != 0:
        nums[current], nums[slow] = nums[slow], nums[current]
        slow+=1
S = Solution()
nums = list(map(int, input().split()))
S.moveZeroes(nums)
print(nums)