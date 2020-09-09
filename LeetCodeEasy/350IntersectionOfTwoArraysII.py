class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) >= len(nums2):
            for num1 in nums1:
                if num1 in nums2:
                    result.append(num1)
                    nums2.remove(num1)
        else:
            for num2 in nums2:
                if num2 in nums1:
                    result.append(num2)
                    nums1.remove(num2)
        return result