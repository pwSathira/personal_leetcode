class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentVal = 0
        maxIndex = 0
        maxVal = 0

        for i in range(len(gain)):
            currentVal += gain[i]
            if maxVal < currentVal:
                maxVal = currentVal
                maxIndex = i
        
        return maxVal