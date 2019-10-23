d=['0','1','11','21','1211','111221']
for i in range(6,31):
  a=d[i-1]
  r=''
  cnt=0
  while cnt<len(a):
    w=1
    tipe=a[cnt]
    try:
      while a[cnt] == a[cnt+1]:
        cnt+=1
        w+=1
    except IndexError as e:
      r+=str(w)+tipe
      cnt+=1
      continue
    r+=str(w)+tipe
    cnt+=1
  d.append(r)

class Solution:
  def countAndSay(self, n: int) -> str:
    return d[n]

s=Solution()
print(s.countAndSay(6))