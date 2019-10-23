class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == [] or nums2 == []: return
        nums1[:] = [nums1[i] for i in range(m)]+nums2
        nums1.sort()
        return nums1

    def merge2(self, nums1: list, m: int, nums2: list, n: int) -> None:
        if nums1 == [] or nums2 == []: return
        temp=[0]*(len(nums1))
        l=0
        l1=0
        for i in range(len(temp)):
            if (l<len(nums2) and nums2[l]<nums1[l1]) or l1>=(m-n):
                temp[i] = nums2[l]
                l+=1
            else:
                temp[i]=nums1[l1]
                l1+=1
        nums1[:] = temp
        return nums1



s=Solution()
n1=list(map(int, input().split()))
n2=list(map(int, input().split()))
print(s.merge2(n1, len(n1), n2, len(n2)))
"""
4 5 6 0 0 0
1 2 3
1 2 3 0 0 0
4 5 6
Output: [1,2,3,4,5,6]
"""

"""
c1=0
c2=0
while c1<len(nums1) and nums1[c1]<nums2[0]:
    c1+=1
if c1==len(nums1):
    nums1[:]=nums2[:]
    return nums1
t=c1
while c2<n:
    c1=t
    while c1<m:
        if nums1[c1]>nums2[c2] or nums1[c1]==0:
            nums1[c1], nums2[c2] = nums2[c2], nums1[c1]
            break
        c1+=1
    if nums2[c2]==0:
        c2+=1
return nums1
# return nums1, nums2 # nums2 siempre va a quedar lleno de 0's

"""