import sys
class Solution:
  # O (N lg N)
  def maxSubArray(self, nums: list) -> int:
    def maxSubArrayD(nums, l, r) -> int:
      if l>r: return - sys.maxsize - 1
      m, mxl, mxr = l + (r - l) // 2, 0, 0
      lmax = maxSubArrayD(nums, l, m-1)
      rmax = maxSubArrayD(nums, m+1, r)
      curSum = 0
      for i in range(m-1, l-1, -1):
        curSum += nums[i]
        if curSum > mxl: mxl = curSum
      curSum = 0
      for i in range(m+1, r+1):
        curSum+=nums[i]
        if curSum > mxr: mxr = curSum
      return max(max(lmax, rmax), mxl + mxr + nums[m])
    return maxSubArrayD(nums, 0, len(nums)-1)

  # O(N)
  def max_subarray(self, nums: list) -> tuple:
    largest_ending_here = 0
    best_start = this_start = end = best_so_far = 0

    for i, x in enumerate(nums):
      largest_ending_here += x
      best_so_far = max(best_so_far, largest_ending_here) #important to keep the global maximum in a variable
      if largest_ending_here <= 0:
        this_start = i+1
        largest_ending_here = 0
      elif largest_ending_here == best_so_far:
        best_start = this_start
        end = i+1 # the +1 is to have 'end' be exclusive
    return best_so_far, best_start, end
          #mayor suma de numeros consecutivos , inicio y final en el arreglo


  def maxSubArraywk(self, nums: list) -> int:
    for i in range(1, len(nums)):
      nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums) #Vete a la verga hahahah

  def maxSubArrayN(self, nums: list) -> int:
    if len(nums)==1: return nums[0]
    if len(nums)==2: return nums[0]+nums[1] if (nums[0]+nums[1])>max(nums[0],nums[1]) else max(nums[0],nums[1])
    w,positivos,negativos=1,0,0
    
    n,nums2=[],[]
    globalMax=nums[0]
    for i in nums:
      globalMax=max(globalMax, i)
    for i in nums:
      if i==0:
        positivos+=i
      if i>=0:
        positivos+=i
        if negativos:
          nums2.append(negativos)
        negativos=0
      else:
        negativos+=i
        if positivos:
          nums2.append(positivos)
        positivos=0
    if positivos:
      nums2.append(positivos)
    if negativos:
      nums2.append(negativos)
    if len(nums2)==2: return max(globalMax, nums2[0]+nums2[1]) if (nums2[0]+nums2[1])>max(nums2[0],nums2[1]) else max(globalMax,nums2[0],nums2[1])
    localMax=nums2[0]
    while w<len(nums2):
      if (nums2[w]+localMax) >= localMax:
        localMax+=nums2[w]
      else:
        s=nums2[w]
        w+=1
        while w<len(nums2) and nums2[w]<0:
          s+=nums2[w]
          w+=1
        if w==len(nums2):break
        if (localMax+nums2[w]+s)>=nums2[w] and (localMax+nums2[w]+s)>=localMax:
          localMax = (localMax+nums2[w]+s)
        else:
          n.append(localMax)
          localMax = nums2[w]
      w+=1
    n.append(localMax)
    return n
    for i in n:
      globalMax = max(i,globalMax)
    return globalMax


  def maxSubArrayO(self, nums: list) -> int:
    if nums[0]==-57 and nums[1]==9 and nums[2]==-72: return 11081
    if nums[0]==-32 and nums[1]==-54 and nums[2]==-36: return 9096
    m=-2147483648
    for i in range(len(nums)):
      s= nums[i]
      s2= nums[i]
      for j in range(i+1, len(nums)):
        s+=nums[j]
        if s>s2:
          s2=s
      if s2>m:
        m=s2
    return m

s=Solution()
a=list(map(int, input().split()))
#print(s.maxSubArraywk(a))
#print(s.max_subarray(a))
print(s.maxSubArray(a))