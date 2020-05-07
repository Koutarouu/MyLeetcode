class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = j = answer = 0
        cmltvepr = {0: 1} #CUMULATIVE PREF
        for i in range(len(nums)):
            pref += nums[i]
            if (pref - k) in cmltvepr:
                answer += cmltvepr[pref-k]
            cmltvepr[pref] = cmltvepr[pref]+1 if pref in cmltvepr else 1
        return answer


    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            pref = 0
            for j in range(i, len(nums)):
                pref+=nums[j]
                if pref == k:
                    answer += 1
        return answer

"""
nums[i]
if pref==k:
answer += 1
range(i+1)
"""