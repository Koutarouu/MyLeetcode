class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0 or x==1: return 1
        base=x
        for i in range(abs(n)-1):
        	x*=base
        if n>0: return x
        return 1/x

    def myPow2(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        if n==2: return x*x
        if n<0: return self.myPow2(1/x, -n) # 1/self.myPow2(x,-n)
        if n%2==0:
        	return self.myPow2(self.myPow2(x,n/2), 2)
        else:
        	return x*self.myPow2(self.myPow2(x,(n-1)/2), 2)

    def myPow3(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        if n==2: return x*x
        if n<0: return self.myPow3(1/x, -n)
        if n%2==0:
        	res=self.myPow3(x, n/2)
        	return res * res
        else:
        	return x*self.myPow3(x, n-1)
        	
s=Solution()
x=float(input())
n=int(input())
print(s.myPow3(x,n))