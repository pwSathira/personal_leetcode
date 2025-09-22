class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(target-total) < abs(target - result):
                    result = total
                
                if total == target:
                    return target
                elif total < target:
                    j += 1
                else:
                    k -= 1
        
        return result