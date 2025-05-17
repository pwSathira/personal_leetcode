from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        # k will be the index where the next unique element should be written in nums
        # It also serves as the count of unique elements found so far.
        k = 0 

        for i in range(len(nums)):
            # If the current element nums[i] has not been seen before
            if nums[i] not in seen:
                seen.add(nums[i])    # Mark it as seen
                nums[k] = nums[i]    # Place it at the k-th position (in-place modification)
                k += 1               # Increment k for the next unique element
        
        # After the loop, the first k elements of nums (i.e., nums[0...k-1])
        # contain the unique elements in their original order of appearance.
        # The elements nums[k:] are irrelevant.
        return k # Return the count of unique elements