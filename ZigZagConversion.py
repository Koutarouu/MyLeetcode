class Solution:
    def convert(self, s: str, numRows: int) -> str:
    	if numRows==1 or len(s)<=numRows: return s
        A=[[""]*(len(s)//2+1) for i in range(numRows)]
        i=j=0; fl=True
        for w in s:
        	if fl and i<numRows:
        		A[i][j]=w
        		i+=1
        		if i==numRows: i-=2; j+=1; fl=False; 
       		else:
       			A[i][j]=w
       			if i>0: i-=1; j+=1
       			else: fl=True; i+=1;
       	R=["".join(A[i]) for i in range(numRows)]
       	return "".join(R)

S=Solution()
string = input()
print(S.convert(string, int(input())))