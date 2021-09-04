from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        count = 0
        return_list = []

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                count = map.get(nums[i])
                if count != None:
                    count = count + 1
                map[nums[i]] = count

        for j in range(k):
            my_key = max(map, key=map.get)
            return_list.append(my_key)
            del map[my_key]

        return return_list