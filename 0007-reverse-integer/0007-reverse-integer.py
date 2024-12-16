class Solution:
    def reverse(self, x: int) -> int:
        # Range for 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        signed = False

        if x < 0:
            signed = True
            x = abs(x)

        # Reverse the integer
        x = str(x)
        x = x[::-1]
        x = int(x)

        # Restore the sign
        if signed:
            x *= -1

        # Check if it's within the 32-bit signed integer range
        if x < INT_MIN or x > INT_MAX:
            return 0

        return x
