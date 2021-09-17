from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words:
            counts &= Counter(word)

        res = []
        for letter, count in counts.items():
            res += [letter] * count
        return res