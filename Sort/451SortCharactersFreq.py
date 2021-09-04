class Solution:
    def frequencySort(self, s: str) -> str:
        char = {x: 0 for x in s}

        for i in s:
            char[i] += 1

        res = sorted(char.items(), key=lambda kv: kv[1], reverse=True)

        result = dict(res)
        ans = ''
        for i in result:
            ans += i * char[i]
        return ans