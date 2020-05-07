class Solution:
  def isHappy(self, n: int) -> bool:
  	h={}
    while n not in h:
      if n==1: return True
      h[n] = True
      a=0
      while n>0:
        a += (n%10)**2
        n //= 10
      n=a
    return False

  def isHappy2(self, n: int) -> bool:
  	while n != 4:
      if n == 1: return True
      a=0
      while n>0:
        a += (n%10)**2
        n //= 10
      n=a
    return False

  def isHappyFloydCycle(self, n: int) -> bool:
    if slow==1: return True
    nextt = lambda a: 0 if a == 0 else (a % 10)**2 + nextt (a//10)
    fast = nextt(slow)
    while slow != fast:
      if fast==1: return True
      slow = nextt(slow)
      fast = nextt(nextt(fast))
    return False

s=Solution()
n = int(input())
if s.isHappy(n):
	print("The number is happy.")
else:
	print("The number is not happy.")