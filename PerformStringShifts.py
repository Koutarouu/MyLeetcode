from collections import deque

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        d = deque(s)
        c=0
        for s in shift:
            if s[0]==0:
                c+=s[1]
            else:
                c-=s[1]
        if c>0:
            while c>0:
                d.append(d.popleft())
        if c<0:
            c=abs(c)
            while c>0:
                d.appendleft(d.pop())
        return "".join(d)

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        d = deque(s)
        for s in shift:
            if s[0]==0:
                while s[1]>0:
                    d.append(d.popleft())
                    s[1]-=1
            else:
                while s[1]>0:
                    d.appendleft(d.pop())
                    s[1]-=1
        return "".join(d)