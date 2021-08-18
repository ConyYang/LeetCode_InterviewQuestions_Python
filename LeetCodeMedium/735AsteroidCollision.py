class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i = 0
        while (i < len(asteroids)):
            a = asteroids[i]

            if a > 0:
                stack.append(a)
            else:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(a)
                elif abs(stack[-1]) <= abs(a):
                    # if the current a is still alive
                    if abs(stack[-1]) < abs(a):
                        i -= 1
                    stack.pop()
            i +=1
        return stack


if __name__ == '__main__':
    asteroids = [-2, -2, 1, -2]
    sol = Solution()
    ans = sol.asteroidCollision(asteroids)
    print(ans)
