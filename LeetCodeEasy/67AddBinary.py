class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val += carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val//2, val%2
            result += str(val)
            val = 0
        if carry:
            result += '1'
        return result[::-1]

a =  Solution()
result = a.addBinary('1010', '1011')
print(result)