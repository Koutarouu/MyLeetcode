import itertools

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in S:
            if 'a'<=i<='z':
                s.append(i)
            elif s:
                s.pop()
        for i in T:
            if 'a'<=i<='z':
                t.append(i)
            elif t:
                t.pop()
        return s==t

    def backspaceCompare1(self, S: str, T: str) -> bool:
        r1=len(S)-1
        skip1=0
        r2=len(T)-1
        skip2=0
        while r1>=0 or r2>=0:
            while r1>=0:
                if S[r1]=='#':
                    skip1+=1; r1-=1
                elif skip1>0: skip1-=1; r1-=1
                else: break
            while r2>=0:
                if T[r2]=='#':
                    skip2+=1; r2-=1
                elif skip2>0: skip2-=1; r2-=1
                else: break
            if r1>=0 and r2>=0 and S[r1]!=T[r2]:
                return False
            if (r1>=0) != (r2>=0): #If expecting to compare char vs nothing
                return False
            r1-=1; r2-=1
        return True

    def backspaceCompare2(self, S: str, T: str) -> bool:
        r1,r2 = len(S)-1,len(T)-1
        skip1=skip2=0
        while r1>=0 or r2>=0:
            if skip1 and S[r1]!='#':
                r1-=1
                skip1-=1
            elif (skip1 and (r1>=0 and S[r1]=='#')) or (r1>=0 and S[r1]=='#'):
                r1-=1
                skip1+=1
            else:
                if skip2 and T[r2]!='#':
                    r2-=1
                    skip2-=1
                elif (skip2 and (r2>=0 and T[r2]=='#')) or (r2>=0 and T[r2]=='#'):
                    r2-=1
                    skip2+=1
                else:
                    if (r1>=0) and (r2>=0) and S[r1]!=T[r2]:
                        return False
                    if (r1>=0) != (r2>=0):
                        return False
                    r1-=1; r2-=1
        return True

    def backspaceCompare3(self, S: str, T: str) -> bool:
        def F(S):
            skip=0
            for x in reversed(S):
                if x=='#':
                    skip+=1
                elif skip:
                    skip-=1
                else:
                    yield x
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


So=Solution()
s=input()
t=input()
print(So.backspaceCompare3(s, t))