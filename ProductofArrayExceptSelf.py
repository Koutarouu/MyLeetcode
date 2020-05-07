class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * (l+1)
        for i in range(1, l+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = [1] * (l+1)
        for i in range(l-1, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
        answer = [0] * l
        for i in range(l):
            answer[i] = prefix[i] * suffix[i+1]
        return answer
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        answer = []
        lproduct=1
        for i in nums:
            answer.append(lproduct)
            lproduct*=i
        rproduct=1
        for i in range(l-1, -1, -1):
            answer[i] = answer[i] * rproduct
            rproduct *= nums[i]
        return answer