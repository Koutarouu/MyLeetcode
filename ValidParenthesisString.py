class Solution:
    def checkValidString(self, s: str) -> bool:
        total=0; l=len(s)
        for i in s:
            total += 1 if i=='(' or i=='*' else -1
            if total<0: return False
        total=0
        for i in range(l-1, -1, -1):
            total += 1 if s[i]==')' or s[i]=='*' else -1
            if total<0: return False
        return True