class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value # This  gets the floor value to multiply by if 3.749 answer is 3
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)

        
           