class Solution:
    def generate(self, numRows: int) -> list:
    	triangle=[[0]*i for i in range(1,numRows+1)]
    	for i in range(numRows):
    		for j in range(i+1):
    			if j==0 or j==i:
    				triangle[i][j]=1
    			else:
    				triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
    	return triangle

    def generate2(self, numRows: int) -> list:
    	def NPT( m:int ,n:int ):
    		if triangle[m][n]!=0:
    			return triangle[m][n]
    		if n==0 or n==m:
    			triangle[m][n]=1
    			return triangle[m][n]
    		triangle[m][n] = NPT(m-1, n-1) + NPT(m-1, n)
    		return triangle[m][n]
    	triangle=[[0]*i for i in range(1,numRows+1)]
    	triangle[0][0]=1
    	for column in range(numRows):
    		NPT(numRows-1, column)
    	return triangle

s=Solution()
print(s.generate2(int(input())))