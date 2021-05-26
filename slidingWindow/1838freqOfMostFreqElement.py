"""
 * 1) Target Number must be in the original array
 * 2) We can only increase numbers but cannot decrease
 *      If choose target nums[j]. Only increase nums[i] < nums[j]
 * Greedy: chose nums as close to nums[j] as possible =>> sort the array
 *
 *      0...i...        j           ... n-1
 *      Candidates    target
 *      Use sliding window [Monotonic]
 * */

/**
 *  Maintain a sliding window [i-j] such that it takse <= k ops to make all elements equal to nums[j]/target
 * target_sum = window.size() * nums[j]
 * actual_sum = sum(i-j)
 * window is valid if : target_sum - actual_sum <= k
 * */

"""


class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        length = 0
        i = 0
        for j in range(0, len(nums)):
            target = nums[j]
            sum += target

            while i<j and (sum + k) < (j - i + 1) * target:
                sum -= nums[i]
                i += 1
            length = max(j-i+1, length)

        return length


if __name__ == '__main__':
    s = Solution()
    ans = s.maxFrequency([1,4,8,13], 5)
    print(ans)

    # window = []
    # nums = sorted(nums)
    # sum = 0
    # length = 0
    # max_length = 0
    # i = 0
    # for j in range(0, len(nums)):
    #     target = nums[j]
    #     window.append(nums[j])
    #     length += 1
    #     target_sum = (j - i + 1) * target
    #     sum += target
    #     if target_sum - sum <= k:
    #         continue
    #     else:
    #         window.pop(0)
    #         sum -= target
    #         j -= 1
    #         length -= 1
    #         i += 1
    #     max_length = max(length, max_length)
    # return length