phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
class Solution:
  def letterCombinations(self, digits: str) -> list:
    n=[]
    new=[]
    for i in range(len(digits)):
      n.append(phone[digits[i]])
    l=len(n)
    if l==1:
      for i in n[0]:
        new.append(i)
    if l == 2:
      for i in n[0]:
        for j in n[1]:
          new.append(i+j)
    if l == 3:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            new.append(i+j+k)
    if l == 4:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            for o in n[3]:
              new.append(i+j+k+o)
    if l == 5:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            for o in n[3]:
              for r in n[4]:
                new.append(i+j+k+o+r)
    if l == 6:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            for o in n[3]:
              for r in n[4]:
                for m in n[5]:
                  new.append(i+j+k+o+r+m)
    if l == 7:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            for o in n[3]:
              for r in n[4]:
                for m in n[5]:
                  for y in n[6]:
                    new.append(i+j+k+o+r+m+y)
    if l == 8:
      for i in n[0]:
        for j in n[1]:
          for k in n[2]:
            for o in n[3]:
              for r in n[4]:
                for m in n[5]:
                  for y in n[6]:
                    for t in n[7]:
                      new.append(i+j+k+o+r+m+y+t)
    return new

  def letterCombinations2(self, digits: str) -> list:
    def backtrack(comb, next_digits):
      if len(next_digits)==0: res.append(comb)
      else:
        for letter in phone[next_digits[0]]:
          backtrack(comb+letter, next_digits[1:])
    res=[]
    if digits: backtrack("", digits)
    return res
"""
phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

"""
s=Solution()
dig = input()
print(s.letterCombinations(dig))
print(s.letterCombinations2(dig))

"""
for j in range(i+1, len(digits)):
  m=h[digits[j]]
  for k in l:
    for p in m:
      n.append(k+p)
"""