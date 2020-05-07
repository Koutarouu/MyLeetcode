class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        f=True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False
        a=abs(dividend)
        b=ob=abs(divisor)
        q=0
        while b<a:
            q+=1
            b+=ob
        if f:
            return q+1 if b==a else q
        return -q-1 if b==a else -q
    def divideBs(self, dividend: int, divisor: int) -> int:
        f=True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False
        if dividend==-2**31 and divisor == -1: return 2**31 -1
        a=abs(dividend)
        b=abs(divisor)
        q=0
        while a > 0:
            ob=b
            t=1
            while ob < a:
                ob += ob# ob <<= 1 #this is because multiplicatio is disallowed
                t += t # t <<= 1
            if ob != a:
                t >>= 1
                ob >>= 1
            q+=t
            a-=ob
        return q if f else -q

s=Solution()
di,div=map(int, input().split())
print(s.divideBs(di,div))