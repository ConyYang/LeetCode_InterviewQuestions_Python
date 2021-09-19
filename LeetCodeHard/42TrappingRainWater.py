class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        n = len(height)
        left = 0
        right = n - 1
        ans = 0

        l_max = height[0]
        r_max = height[n - 1]

        while (left <= right):
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if (l_max < r_max):
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1

        return ans