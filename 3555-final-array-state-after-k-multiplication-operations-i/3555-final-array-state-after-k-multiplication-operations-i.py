class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minx = nums.index(min(nums))
            nums[minx] *= multiplier
        
        return nums