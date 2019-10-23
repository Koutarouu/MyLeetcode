
class Solution:
  def reverseString(self, s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l,r=0,len(s)-1
    while r>l:
      s[l],s[r]=s[r],s[l]
      l+=1
      r-=1
    print(s)
  temp=''
  def ReverseString(self, s: list) -> None:
    if s==[]: return
    self.ReverseString(s[1:])
    self.temp+=s[0]
    


s=Solution()
string=[i for i in input()]
s.ReverseString(string)
print(s.temp)
#print(string)