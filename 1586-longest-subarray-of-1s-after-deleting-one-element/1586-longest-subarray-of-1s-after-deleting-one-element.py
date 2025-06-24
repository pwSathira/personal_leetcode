class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length_of_ones_subarray = 0
        
        # Max number of zeros allowed in the current window.
        # We can delete at most one zero, so we start with 1 allowed zero.
        allowed_zeroes = 1 
        
        window_start = 0 # Left pointer of the sliding window
        
        for window_end in range(len(nums)): # Right pointer of the sliding window
            # If we encounter a zero, decrement the count of allowed zeroes
            if nums[window_end] == 0:
                allowed_zeroes -= 1

            # If we have too many zeros in the current window (allowed_zeroes is negative),
            # shrink the window from the left until it's valid again.
            while allowed_zeroes < 0 and window_start <= window_end:
                # If the element at the window_start is a zero,
                # increment allowed_zeroes as we are moving past it.
                if nums[window_start] == 0:
                    allowed_zeroes += 1
                window_start += 1 # Move the window_start pointer
            
            # The length of the current valid subarray of ones (after potentially removing one zero)
            # is window_end - window_start. We don't add +1 because we are looking for
            # the length *after* deleting an element.
            max_length_of_ones_subarray = max(max_length_of_ones_subarray, window_end - window_start)
            
        return max_length_of_ones_subarray