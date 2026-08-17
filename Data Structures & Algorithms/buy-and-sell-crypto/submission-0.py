class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        i,j = 0,1
        while i < len(prices) and j < len(prices):
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j
            j += 1
            maxP = max(maxP, profit)
        return maxP