class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        h={}
        for i in wordDict:
        	h[i]=1
        for j in range(len(s)-1):
        	c=s[j]==s[j+1]
        w, r='', ''
        for i in s:
        	w+=i
        	if w in h:
        		r= r+w; w='';
        return r==s if not c else True

s=Solution()
string=input()
wordDict=input().split()
print(s.wordBreak(string, wordDict))