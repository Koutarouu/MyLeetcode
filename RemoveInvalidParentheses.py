from collections import deque

class Solution:
  def isBal(self, s: str) -> bool:
    q = deque()
    try:
      for i in s:
        res = True
        if i == ')':
          res = q.pop()=='('
        elif i == '(':
          q.append(i)
        if not res:
          return res
      return True if len(q)==0 else False
    except IndexError:
      return False

  def removeInvalidParentheses(self, s: str) -> list:
    Q=deque()
    Q.append(s)
    balanced=flag=False
    d,R={},[]
    while Q:
      t=Q.pop()
      if t in d: continue
      d[t]=True
      balanced=self.isBal(t)
      if balanced:
        flag=True
        R.append(t)
      if flag: continue
      for i in range(len(t)):
        if t[i]=='(' or t[i]==')':
          Q.appendleft(t[:i]+t[i+1:len(t)])
    return R

S=Solution()
s=input()
print(S.removeInvalidParentheses(s))