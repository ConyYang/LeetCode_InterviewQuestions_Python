from collections import deque


class MonotonicQueue(object):
    def __init__(self):
        # 双端队列
        self.data = deque()

    def push(self, n):
        # 实现单调队列的push方法
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)

    def max(self):
        # 取得单调队列中的最大值
        return self.data[0]

    def pop(self, n):
        # 实现单调队列的pop方法
        if self.data and self.data[0] == n:
            self.data.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()

        res = []

        for i in range(0, k - 1):
            window.push(nums[i])

        for i in range(k - 1, len(nums)):
            window.push(nums[i])
            res.append(window.max())
            window.pop(nums[i - k + 1])

        return res