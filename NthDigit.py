class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10: return n
       	res=[]
       	t=tn=10
       	while tn<=n:
       		o=str(t)
       		for i in o:
       			res.append(i)
       		tn+=len(o)
       		t+=1
       	return res[n-10]
    def findNthDigitM(self, n: int) -> int:
    	sizeD, low, high = 1, 1, 9 # sizeD - number of digits in each number of the scope
    	while n > (high - low + 1) * sizeD: 
    		n -= (high - low + 1) * sizeD # n - current scope 
    		sizeD, low, high = sizeD+1 ,low*10, (high+1)*10-1
    	idx_num, idx_digit = (n-1)//sizeD, (n-1)%sizeD # start for the digit and for the digit 
    	return str(low+idx_num)[idx_digit] # applying the above
s=Solution()
n=int(input())
print(s.findNthDigit(n))
print(s.findNthDigitM(n))