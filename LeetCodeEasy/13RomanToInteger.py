class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {'I': 1, 'V': 5,
                  'X': 10, 'L': 50,
                  'C': 100, 'D': 500,
                  'M': 1000}
        i = 0
        num = 0
        while i<(len(s)):
            cur_s = s[i]
            try:
                next_s = s[i+1]
                if mydict[cur_s] >= mydict[next_s]:
                    num += mydict[cur_s]
                else:
                    num += (mydict[next_s] - mydict[cur_s])
                    i +=1
            except:
                num+=mydict[cur_s]
            i+=1
        return num


a = Solution()
num = a.romanToInt('MCMXCIV')
print(num)