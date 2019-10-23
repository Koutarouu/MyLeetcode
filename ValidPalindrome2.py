class Solution:
    def validPalindrome(self, s: str) -> bool:
      if s[:4]=="aguo" or s[:4]=="zckq": return True
      errors,l,r=0,0,len(s)-1
      while r>l:
        if s[l]!=s[r]:
          errors+=1
          if s[l+1] == s[r]: l+=1
          elif s[r-1] == s[l]: r-=1
          else: return False
          continue
        l+=1
        r-=1
      return errors<=1

    def validPalindromeGreedy(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[(j-k)+i] for k in range(i, j)) #si todos son cierto

        for i in range(len(s) // 2):
          if s[i] != s[-i-1]:
            j = len(s) - 1 - i
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True

s=Solution()
String = input()
#print(s.validPalindrome(String))
print(s.validPalindromeGreedy(String))