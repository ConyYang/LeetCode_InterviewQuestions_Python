class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        start = 0
        end = len(height) - 1
        while start <= end:
            h1 = height[start]
            h2 = height[end]
            area = max(area, min(h1, h2) * (end - start))
            if h1 < h2:
                start += 1
            else:
                end -= 1

        return area