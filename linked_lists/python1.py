from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {} #Hashmap val:index

        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in hMap:
                return [hMap[diff], i]

            hMap[n] = i
        return