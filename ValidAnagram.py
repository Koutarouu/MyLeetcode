from collections import Counter

class Solution:
  def isAnagram2(self, s: str, t: str) -> bool:
    if (len(s)-len(t))!=0: return False
    return Counter(s)==Counter(t)

  def isAnagram1(self, s: str, t: str) -> bool: # con este cambio fue mas rapida la solucion del 83 al 95
    d={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,'*':0,'-':0,'+':0,'/':0}
    if (len(s)-len(t))!=0: return False
    for i in range(len(s)):
      d[s[i]] += 1
      d[t[i]] -= 1
    for i in d:
      if d[i]!=0:
        return False
    return True
    # igual de rapido que decir el Counter de s es igual al Counter de t return Counter(s)==Counter(t)
  def isAnagram(self, s: str, t: str) -> bool:
    d={} 
    for i in s:
      d[i] = d[i]+1 if (i in d) else 1  
    for j in t:
      if j in d:
        d[j]-=1
      else:
        return False
    for i in d:
      if d[i]!=0:
        return False
    return True

#Esta solucion se extiende a caracteres especiales y es mas rapida
so=Solution()
s=input()
t=input()
if so.isAnagram1(s, t):
  print("Valid Anagram")
else:
  print("Invalid Anagram")

"""
Ala madre
Runtime: 40 ms, faster than 99.22% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.3 MB, less than 28.04% of Python3 online submissions for Valid Anagram.
"""