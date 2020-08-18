class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float("inf")
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p-min_price)
        return profit


a = Solution()
result = a.maxProfit([7, 1, 5, 3, 6, 4])
print(result)