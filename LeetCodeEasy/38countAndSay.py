class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        if seq == '1':
            return '11'
        str_seq = ""
        k = 0
        while k < len(seq):
            count = 1
            temp = seq[k]

            while (k + count) < len(seq) and temp == seq[k + count]:
                print('loop')
                count += 1
                print('count{}'.format(count))

            str_seq += str(count)
            str_seq += seq[k]
            k += (count)
        return str_seq

str_1 = Solution()
seq = str_1.countAndSay(4)
print(seq)