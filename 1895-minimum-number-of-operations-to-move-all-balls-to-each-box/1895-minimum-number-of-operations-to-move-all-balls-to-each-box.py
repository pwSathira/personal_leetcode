class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        position, answer = [], []
        length = len(boxes)

        for i in range(length):
            if boxes[i] == '1':
                position.append(i)
        
        for i in range(length):
            sum = 0
            for j in position:
                distance = abs(i - j)
                sum += distance
            answer.append(sum)
        
        return answer