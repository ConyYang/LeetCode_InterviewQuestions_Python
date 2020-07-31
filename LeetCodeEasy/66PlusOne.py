class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if digits[-1] != 9:
        #     digits[-1] += 1
        #     return digits
        # else:
        #     num = 0
        #     for i in range(len(digits)):
        #         num *= 10
        #         num += digits[i]
        #     num += 1
        #     num_list = []
        #     str_num = str(num)
        #     for num_i in str_num:
        #         num_list.append(int(num_i))
        #     return num_list

        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        digits[0] = 1
        digits.append(0)
        return digits


a = Solution()
print(a.plusOne([9,9,9]))