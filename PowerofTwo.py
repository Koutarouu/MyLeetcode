class Solution:    
  def isPowerOfTwo(self, n: int) -> bool:
    return self.isPowerOfTwo(n//2) if (n%2==0 and n!=0) else n==1
    
s= Solution()
n = int(input())
print(s.isPowerOfTwo(n))
#O(lg N) por que el numero de veces que se va a ejecutar el while loop son lg n veces
"""
while n%2==0:
  n//=2
return n==1

for i in range(35):
  if 2**i == n:
    return True
return False
"""