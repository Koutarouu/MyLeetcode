class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h={0: -1}
        max_len = count = 0
        for i in range(len(nums)):
            count = (count-1 if nums[i]==0 else count+1)
            if count in h:
                max_len = max(max_len, i-h[count])
            else:
                h[count] = i
        return max_len
        
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-2]*(2*len(nums)+1)
        arr[len(nums)] = -1
        max_len = count = 0
        for i in range(len(nums)):
            count = count + (-1 if nums[i]==0 else 1)
            if arr[count + len(nums)] >= -1:
                max_len = max(max_len, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i
        return max_len

    def findMaxLength(self, nums: List[int]) -> int:
        if nums==[]: return 0
        z = 0
        red=[]
        typ=nums[0]
        for i in nums:
            if i==typ:
                z+=1
            else:
                typ=i
                red.append(z)
                z=1
        red.append(z)
        if len(red)<=1:
            return 0
        res = 0
        for i in range(len(red)-1):
            a = +red[i]
            b = False
            c = red[i]
            for j in range(i+1, len(red)):
                c += red[j]
                if b:
                    a+=red[j]
                    b=False
                else:
                    a-=red[j]
                    b=True
                if a==0:
                    res = max(res, c)
        if res==0:
            m=min(red)
            return m*2
        return res
