class Solution:
    def permute(self, nums: list) -> list:
        if len(nums)==1:
        	return [nums]

        a=nums.pop() # sacamos el ultimo elemento
        
        sub_results = self.permute(nums) # mandamos el resto del array hasta que su longitud sea uno y formarlo desde ahi
        print(sub_results)
        results=[]

        for res in sub_results:
        	for i in range(len(res)+1):
        		result = res[:]
        		result.insert(i, a)
        		results.append(result)
        return sorted(results)
#BEATUFULLLL
        


s=Solution()
array=list(map(int, input().split()))
print(s.permute(array))

def letterCombinations2(self, digits: str) -> list:
    def backtrack(comb, next_digits):
      if len(next_digits)==0: res.append(comb)
      else:
        for letter in phone[next_digits[0]]:
          backtrack(comb+letter, next_digits[1:])
    res=[]
    if digits: backtrack("", digits)
    return res