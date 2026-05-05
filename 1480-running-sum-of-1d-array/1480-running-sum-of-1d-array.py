class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(nums[i])
            else: 
                output.append(nums[i] + output[i-1])

        return output