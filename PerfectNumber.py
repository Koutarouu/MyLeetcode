class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        res=1
        if n<=1: return False;
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                res+=i
                res+=n/i
        return res==n

n=int(input())
s=Solution()
print(s.checkPerfectNumber(n))