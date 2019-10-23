class Solution:
  def reverse(self, x: int) -> int:
    flag = -1 if x<0 else 1
    nx,n=abs(x), 0
    l=len(str(nx))-1

    while nx>0:
      n+=(nx%10)*(10**l)
      l-=1
      nx//=10
    n*=flag
    if n<=((2**31)-1) or n>=-(2**31):
      return n
    return 0

s=Solution()
x=int(input())
print(s.reverse(x))