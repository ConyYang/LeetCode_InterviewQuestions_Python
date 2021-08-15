class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        print(intervals)
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
                print(ans)
            else:
                ans.append(interval)
                print(ans)
        return ans


if __name__ == '__main__':
    a = Solution()
    a.merge([[1, 4], [2, 3]])
