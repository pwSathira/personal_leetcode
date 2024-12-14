class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        smaller_count = {}
        for index, value in enumerate(sorted_nums):
            # Only assign the count for the first occurrence of each number
            if value not in smaller_count:
                smaller_count[value] = index
        
        result = [smaller_count[num] for num in nums]
        return result
