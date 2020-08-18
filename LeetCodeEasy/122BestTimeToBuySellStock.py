class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        if len(prices) <= 1:
            return total_profit
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                total_profit +=  (prices[i] - prices[i-1])
        return total_profit


a = Solution()
result = a.maxProfit([7, 1, 5, 3, 6, 4])
print(result)