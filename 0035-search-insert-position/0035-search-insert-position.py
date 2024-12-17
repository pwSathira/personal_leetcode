from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            middle = start + (end - start) // 2  # Calculate middle index
            
            if nums[middle] == target:  # Target found
                return middle
            elif nums[middle] < target:  # Move to the right half
                start = middle + 1
            else:  # Move to the left half
                end = middle
        
        return start  # This is the correct insertion point
