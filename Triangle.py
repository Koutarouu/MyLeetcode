class Solution:
    def minimumTotal(self, triangle: list) -> int:
    	total=0
    	for i in triangle:
    		mi=999999
    		for j in i:
    			if j<mi: mi=j
    		total+=mi
    	return total

s=Solution()
matrix=[[2],[3,4],[6,5,7],[4,1,8,3]]
matrix=[[-1],[2,3],[1,-1,-3]]
print(s.minimumTotal(matrix))
