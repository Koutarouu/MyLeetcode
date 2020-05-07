class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        max_profit=0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit

    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        minn = sys.maxsize
        for i in range(len(prices)):
            if prices[i]-minn > max_profit:
                max_profit = prices[i]-minn
            if prices[i]<minn:
                minn = prices[i]
        return max_profit