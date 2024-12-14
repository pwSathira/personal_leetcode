class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) <= 2):
            return [0,1]

        hashmap = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [index, hashmap[diff]]
            hashmap[val] = index
