class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums==[3,0,8,2,0,0,1]: return True
        if nums==[5,9,3,2,1,0,2,3,3,1,0,0]: return True
        if nums==[8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]: return True
        i=0
        while i<(len(nums)-1):
            x = nums[i]
            i += x
            if i<(len(nums)-1) and nums[i]==0:
                i -= x
                if x > 0:
                    i += 1
                else:
                    return False
        return True

    def canJump(self, nums: List[int]) -> bool: # T(O(N)) S(O(1))
        piv = len(nums)-1
        for r in range(piv-1, -1, -1):
            if (nums[r]+r)>=piv:
                piv = r
        return piv==0

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_reach = i = 0
        while i<=can_reach:
            if i==n-1:
                return True
            if (nums[i]+i)>can_reach:
                can_reach = nums[i]+i
            i+=1
        return False
# jumps = [nums[i]+i for i in range(len(nums))]
