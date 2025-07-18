class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinctValues = set(nums)
        distinctValues.discard(0)
        return len(distinctValues)