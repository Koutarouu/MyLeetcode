class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n-1):
        	for j in range(i+1, n):
        		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
        	for j in range(n//2):
        		matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
s=Solution()
n=int(input())
image = [[0]*n for i in range(n)]
c=1
for i in range(n):
	for j in range(n):
		image[i][j] = c
		c+=1
print(image)
s.rotate(image)
print(image)