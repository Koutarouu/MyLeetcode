class Solution:
  def groupAnagrams(self, strs: list) -> list:
    if strs==[]: return []
    n, res = [], {}
    
    for i in strs:
      n.append(''.join(sorted(i)))

    for i in range(len(n)):
      if n[i] in res:
        res[n[i]].append(strs[i])
      else:
        res[n[i]] = [strs[i]]
    return sorted(res.values(), key=len)

s=Solution()
strs=input().split()
print(s.groupAnagrams(strs))


"""
res[n[0]]=[strs[0]]
for k in res.values():
    k.sort()
return sorted(res.values(), key=len)
"""