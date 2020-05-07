import sys

class Solution:
    def maxProfit(self, prices: list) -> int: #DP
        best_with_stock = - sys.maxsize - 1
        best_without_stock = 0
        for x in prices:           
            if best_without_stock - x > best_with_stock: 
                best_with_stock = best_without_stock - x
            if best_with_stock + x > best_without_stock:
                best_without_stock = best_with_stock + x
            print(best_with_stock, best_without_stock)
        return best_without_stock
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i]-prices[i-1]
        return max_profit
    def maxProfit(self, prices: list) -> int:
        if prices==[]: return 0
        max_profit = i = 0
        valley = prices[0]
        peak = prices[0]
        while i<len(prices)-1:
            while i+1 < len(prices) and prices[i]>=prices[i+1]:
                i += 1
            valley = prices[i]
            while i+1 < len(prices) and prices[i]<=prices[i+1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
            

S = Solution()
print(S.maxProfit(list(map(int, input().split()))))