class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l + r + 1)//2
            if nums[mid-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid
        return l

s=Solution()
nums = list(map(int, input().split()))
print(s.findPeakElement(nums))