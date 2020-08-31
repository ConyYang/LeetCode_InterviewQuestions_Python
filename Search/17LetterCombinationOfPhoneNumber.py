class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.length = len(digits)
        if self.length == 0:
            return []
        dict_map = {
            0: ["0"],
            1: ["1"],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        count = 0
        result = [""]
        for d in digits:
            d = int(d)
            temp_list = []
            for ch in dict_map[d]:
                for r in result:
                    temp_list.append(r + ch)
            print("Current digit {}, temp_list{}".format(d, temp_list))
            result = temp_list
        return result


a = Solution()
result = a.letterCombinations("23")
print(result)
