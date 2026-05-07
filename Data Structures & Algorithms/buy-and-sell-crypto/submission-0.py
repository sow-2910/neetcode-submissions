class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                temp = prices[j] - prices[i]
                if temp > 0:
                    res = max(res, temp)
        if res > 0:
            return res
        else:
            return 0

        