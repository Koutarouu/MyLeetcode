class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace('.', '[.]')
        s=''
        for i in address:
       		if i=='.':
       			s+="[.]"
       			continue
       		s+=i
       	return s


s=Solution()
print(s.defangIPaddr(input()))