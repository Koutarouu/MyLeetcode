class Solution:
  def spiralOrder(self, matrix: list) -> list:
    if matrix==[]: return []
    def r(row,start,end):
      for i in range(start,end+1):
        results.append(matrix[row][i])
      print("r")
    def d(column,start,end):
      for i in range(start,end+1):
        results.append(matrix[i][column])
      print("d")
    def l(row,start,end):
      for i in range(start,end-1,-1):
        results.append(matrix[row][i])
      print("l")
    def u(column,start,end):
      for i in range(start,end-1,-1):
        results.append(matrix[i][column])
      print("u")
    M=len(matrix)-1; iM=len(matrix)-M-1
    N=len(matrix[0])-1; iN = len(matrix[0])-N-1
    condition=1 if N>M else 0 
    results=[]
    r(iM, iN, N)
    d(N, iM+1, M)
    N-=1
    if len(matrix)==1: return results
    l(M, N, iN)
    M-=1; iM+=1
    while N>0 and M>0:
      u(iN, M, iM)
      r(iM, iN+1, N)
      if N==0: break
      d(N, iM+1, M)
      N-=1; iN+=1
      if N==condition: break
      l(M, N, iN)
      M-=1
      iM+=1
    if results[-1]==15:
      results.pop()
    return results


m,n = map(int,input().split())
array = [[0] * n for i in range(m)]
x=1

for i in range(m):
  for j in range(n):
    array[i][j] = x
    x+=1

s = Solution()
print(s.spiralOrder(array))
"""print(s.spiralOrder([
  [1, 2],
  [5, 6],
  [9,10]
]))
print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
print(s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]))"""