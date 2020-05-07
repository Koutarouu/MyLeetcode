class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        intersection=[]
        for i in nums1:
            if i not in d:
                d[i] = True
        for i in nums2:
            if i in d and d[i]:
                intersection.append(i)
                d[i]=False
        return intersection
    def intersection2(self, nums1: list, nums2: list):
        return list(set(nums1)&set(nums2))