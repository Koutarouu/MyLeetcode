class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(c: str):
            return True if c in ['a','e','i','o','u','A','E','I','O','U'] else False
        l=0
        r=len(s)-1
        s=[i for i in s]
        while r>l:
            a,b=is_vowel(s[l]), is_vowel(s[r])
            if a and b:
                s[l],s[r] = s[r], s[l]
                l+=1
                r-=1
            elif a:
                r-=1
            elif b:
                l+=1
            else:
                l+=1
                r-=1
        return "".join(s)