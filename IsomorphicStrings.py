class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
  	d={}
  	if len(set(s)) != len(set(t)): return False
  	for i in range(len(s)):
  		if s[i] in d:
  			if d[s[i]] == t[i]:
  				continue
  			else:
  				return False
  		d[s[i]] = t[i]
  	return True
#todo esto lo mismo que esto: return len(set(zip(s,t)))==len(set(s))==len(set(t))
So = Solution()
s,t=input().split()
print(So.isIsomorphic(s, t))

"""
Runtime: 32 ms, faster than 99.85% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 13 MB, less than 90.65% of Python3 online submissions for Isomorphic Strings.
"""