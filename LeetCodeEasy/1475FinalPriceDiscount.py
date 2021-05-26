class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range (len(prices)-1):
            for a in prices[i + 1:]:
                if a <= prices[i]:
                    break
            prices[i] -= a
        return prices