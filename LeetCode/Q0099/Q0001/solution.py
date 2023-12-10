from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        n = len(nums)
        for i in range(0, n):
            a, b = nums[i], target - nums[i]
            if b in map:
                return [map[b], i]
            map[a] = i

