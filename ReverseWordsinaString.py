class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

so=Solution()
s=input()
print(so.reverseWords(s))