class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9 and i == 0:
                digits.insert(0, 1)
                digits[1] = 0
                return digits
            elif digits[i] < 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
            else:
                return digits