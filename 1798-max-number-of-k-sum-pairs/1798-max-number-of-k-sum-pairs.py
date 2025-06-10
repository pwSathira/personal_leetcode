class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operationNum = 0
        point1 = 0
        point2 = len(nums)-1
        
        while point2 > point1:
            if nums[point1] + nums[point2] == k:
                operationNum += 1
                point1 += 1
                point2 -= 1
            elif nums[point1] + nums[point2] < k:
                point1 += 1
            else: 
                point2 -= 1

        return operationNum
           
