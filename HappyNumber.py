"""class Solution:
  def isHappy(self, n: int) -> bool:
  	R={}
  	res=n
  	while res not in R:
  		R[res] = 1
  		res=0
  		while n>0:
  			res += (n%10)**2
  			n//=10
  		if res == 1:
  			return True
  		n=res
  	return False
"""
class Solution:
  def isHappy(self, n: int) -> bool:
  	res=0
  	while res!=1:
  		res=0
  		while n>0:
  			res += (n%10)**2
  			n//=10
  		if res == 4:
  			return False
  		n=res
  	return True

s=Solution()
n = int(input())
if s.isHappy(n):
	print("The number is happy.")
else:
	print("The number is not happy.")