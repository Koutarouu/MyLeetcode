class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        l=0
        r=len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            fh = nums[l] <= nums[m]
            sh = nums[m] <= nums[r]
            if fh and nums[l] <= target <= nums[m]:
                r = m - 1
            elif fh:
                l = m + 1
            elif sh and nums[m] <= target <= nums[r]:
                l = m + 1
            elif sh:
                r = m - 1
        return -1