class Solution:
    def transposeEqualsmxn(self, A: list) -> list:
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                A[i][j],A[j][i]=A[j][i],A[i][j]
        return A
    def transpose(self, A: list) -> list:
        rows,columns=len(A),len(A[0])
        TA=[[0]*rows for i in range(columns)]
        for i in range(rows):
            for j in range(columns):
                TA[j][i] = A[i][j]
        return TA
#fijate bien haha

s=Solution()
m,n=map(int,input().split())
M=[[0]*n for i in range(m)]
c=1
for i in range(m):
    for j in range(n):
        M[i][j]=c
        c+=1
#print(s.transpose(M))
print(s.transposeEqualsmxn(M))