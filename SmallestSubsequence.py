class Solution:
    def smallestSubsequence(self, text: str) -> str:
    	h={}
    	for i in text:
    		if i in h:
    			h[i]+=1
    		h[i]=1
    	return h

s=Solution()
t=input()
print(s.smallestSubsequence(t))