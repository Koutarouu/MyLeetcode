class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0
        guess=1
        while guess**2 < x:
        	guess+=1
        return guess if guess%guess==x else guess-1

    def mySqrtNM(self, x: int) -> int:
        if x==0: return 0
        x0=x
        error=99999999
        while error>=1:
        	x1=x0 - (x0*x0 - x)/(2*x0)
        	x0 = x1
        	print(x0)
        	error=abs(x0*x0 - x)
        return int(x0)

    def mySqrtBS(self, x: int) -> int:
    	if x==0: return 0
    	li=1
    	ls=x
    	guess=(li+ls)//2
    	while guess>li:
    		if guess**2 == x:
    			return int(guess)
    		elif guess**2 < x:
    			li=guess
    			guess=(li+ls)//2
    		else:
    			ls=guess
    			guess=(li+ls)//2
    	return int(guess)
s=Solution()
I=int(input())
print(s.mySqrtBS(I))
#print(s.mySqrtNM(I))
#print(s.mySqrt(I))