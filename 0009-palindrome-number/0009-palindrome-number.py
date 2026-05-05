class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        input = str(x)
        n = len(input)
        end = n - 1

        for i in range(n-1):
            if input[i] != input[end]:
                return False
            else: 
                end -= 1
                if end == i:
                    return True

        return True