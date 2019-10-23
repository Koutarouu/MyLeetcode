class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        h={}
        c=0
        for i in J:
            h[i] = 0

        for i in S:
            if i in h:
            	c+=1
        return c

    def numJewelsInStones2(self, J: str, S: str) -> int:
        c=0 # more faster in this problem
        for i in J:
            for j in S:
            	if i==j: c+=1
        return c

so=Solution()
j=input()
s=input()
print(so.numJewelsInStones(j, s))

"""
# te same approach like the first solution but this time counting the stones
h={}
for i in S:
    if i in h:
        h[i] += 1
        continue
    h[i] = 1
c=0
for i in J:
    if i in h:
    	c+=h[i]
return c
"""