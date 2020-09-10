class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_a = [a for a in range(0, n)]

        for a in list_a[2:]:
            if a:
                for i in range(a + a, n, a):
                    list_a[i] = False

        return len([element for element in list_a[2:] if element])