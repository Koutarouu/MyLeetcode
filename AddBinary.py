class Solution:
    def addBinary2(self, a: str, b: str) -> str:
        ba, bb = bin(a), bin(b)
        return ba+bb
    def addBinary(self, a: str, b: str) -> str:
        r = []
        ra, rb = len(a)-1, len(b)-1
        carry=False
        while ra>=0 and rb>=0:
            if a[ra]=="1" and b[rb]=="1" and carry:
                carry=True
                r.insert(0, "1")
            elif a[ra]=="1" and b[rb]=="1":
                carry=True
                r.insert(0, "0")
            elif (a[ra]=="1" or b[rb]=="1") and carry:
                carry = True
                r.insert(0, "0")
            elif a[ra]=="1" or b[rb]=="1":
                r.insert(0, "1")
            elif carry:
                carry=False
                r.insert(0, "1")
            else:
                r.insert(0, "0")
            ra-=1
            rb-=1
        
        while ra>=0:
            if a[ra]=="1" and carry:
                carry=True
                r.insert(0, "0")
            elif a[ra]=="1":
                r.insert(0, "1")
            elif a[ra]=="0" and carry:
                carry=False
                r.insert(0, "1")
            else:
                r.insert(0, "0")
            ra-=1
        
        while rb>=0:
            if b[rb]=="1" and carry:
                carry=True
                r.insert(0, "0")
            elif b[rb]=="1":
                r.insert(0, "1")
            elif b[rb]=="0" and carry:
                carry=False
                r.insert(0, "1")
            else:
                r.insert(0, "0")
            rb-=1
        if carry:
            r.insert(0, "1")
        return "".join(r)

s=Solution()
s1, s2=input().split()
r=s.addBinary(s1,s2)
suma=0
n=0
for i in range(len(r)-1, -1, -1):
    if r[i]=="1": suma+=2**n
    n+=1
print(suma)