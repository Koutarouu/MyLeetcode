class Solution:
  def longestCommonPrefixHS(self, strs) -> str: # Horizontal Scanning
  	if strs==[]: return ''
  	lcp=strs[0]
  	for i in range(1, len(strs)):
  		nlcp=''
  		w=0
  		while w<min(len(lcp),len(strs[i])) and lcp[w]==strs[i][w]:
  			nlcp+=lcp[w]
  			w+=1
  		if nlcp=='': return ''
  		lcp=nlcp
  	return lcp
  			
  def longestCommonPrefixVS(self, strs) -> str: # Vertical Scanning
  	if strs == []: return ''
  	lcp=''
  	for i in range(len(strs[0])):
  		c=strs[0][i]
  		for j in range(1, len(strs)):
  			if i!=len(strs[j]) and c==strs[j][i]: continue
  			else: return lcp
  		lcp+=c
  	return lcp

  def longestCommonPrefixDC(self, strs) -> str: # Divide and Conquer
  	if strs==[]: return ''
  	return self.longestCommonPrefixH(strs, 0, len(strs)-1)

  def longestCommonPrefix(self, strs, l, r) -> str: # Vertical Scanning
  	if l==r:
  		return strs[l]
  	else:
  		mid = (l+r)//2
  		lcpLeft = self.longestCommonPrefixH(strs, l, mid)
  		lcpRight = self.longestCommonPrefixH(strs, mid + 1, r)
  		return commonPrefix(lcpLeft, lcpRight) #funciona como merge sort solo que en lugar de unir las listas encontramos el lcd

  def longestCommonPrefixBS(self, strs) -> str:
  	if strs==[]: return ''
  	minlen=100000
  	for stri in strs:
  		minlen=min(minlen, len(stri))
  	low = 1 # uno para que middle no de 0 
  	high = minlen

  	while low<=high:
  		middle = (low + high) // 2
  		if isCommonPrefix(strs, middle):
  			low = middle + 1
  		else: high = middle - 1

  	return strs[0][0:((low+high)//2)]

def isCommonPrefix(strs, length):
	str1 = strs[0][0:length]
	for i in range(1, len(strs)):
		if str1 not in strs[i][0:length]: return False
	return True

def commonPrefix(left, right):
	low, lcp, w=min(len(left), len(right)), '', 0
	while w<low and left[w]==right[w]:
		lcp+=left[w]
		w+=1
	return lcp

s=Solution()
t=input().split()
print(s.longestCommonPrefixBS(t))