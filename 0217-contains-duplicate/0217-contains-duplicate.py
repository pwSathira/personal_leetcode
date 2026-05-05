class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = set()

        for i in range(len(nums)):
            if nums[i] in contains:
                return True
            else: 
                contains.add(nums[i])
        
        return False