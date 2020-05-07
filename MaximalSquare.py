class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[] or matrix[0]==[]: return 0
        m = len(matrix)
        n = len(matrix[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    a=1
                    b=True
                    while b and (i+a)<m and (j+a)<n:
                        for k in range(j, j+a+1):
                            if matrix[i+a][k]=="0":
                                b=False; break
                        if not b: break
                        for k in range(i, i+a): # +1 haha here we only save one extra operation each time EXTRA PRECISE
                            if matrix[k][j+a]=="0":
                                b=False; break
                        if b: a+=1
                    ans = max(ans, a)
        return ans*ans

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    matrix[i][j]=1
                    if i>0 and j>0:
                        matrix[i][j] += min((matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]))
                    ans = max(ans, matrix[i][j])
                else: matrix[i][j]=0
        return ans*ans
"""
for k in range(i, i+a+1):
    for l in range(j, j+a+1):
        if matrix[k][l]=="0":
            b=False
            break
    if not b: break
"""